import os

# 获取当前文件夹的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))
# 获取词典所在目录的路径
dict_path = os.path.join(basedir,'pos_neg')
# 获取优化前后的文件存储的目录
data_path = os.path.join(basedir,'data')

def load_words(filenames:list,drop:list=None,extra:list=None)->set:
    '''载入正向/负向词典
    

    Parameters
    ----------
    filenames : list
        只接受文件名
        所以所有要载入的正向词语文件都必须放到.\pos_neg目录下
    drop : list, optional
        如果提供了，会把这几个词语从集合里去掉. The default is None.
    extra : list, optional
        如果提供了，会把这几个词语添加到集合里. The default is None.

    Returns
    -------
    set
        返回词语集合.

    '''

    
    filepaths = [os.path.join(dict_path,name) for name in filenames]
    # 存放词语的集合
    words = set()
    for path in filepaths:
        with open(path,encoding='utf-8') as f:
            while True:
                word = f.readline()
                if not word:
                    break
                words.add(word[:-1])
    # 微调正向词语
    if drop:
        words -= set(drop)
    if extra:
        words |= set(extra)
    return words


def to_utf8(pos_rost_name:str,neu_rost_name:str,neg_rost_name:str)->list:
    '''把ROST生成的utf-16-le格式的文件转化为utf-8格式
    

    Parameters
    ----------
    pos_rost_name : str
        正面文件名.必须存储在.\data目录下
    neu_rost_name : str
        中性文件名.必须存储在.\data目录下
    neg_rost_name : str
        负面文件名.必须存储在.\data目录下

    Returns
    -------
    list
        转化好的文件【路径】列表.

    '''
    # 下面是三个ROSTCM6生成的文件的路径
    filepaths =[os.path.join(data_path,pos_rost_name),
                os.path.join(data_path,neu_rost_name),
                os.path.join(data_path,neg_rost_name)]
                
    # 存储转化好的文件路径的列表
    ans = []
    for path in filepaths:
        with open(path,encoding='utf-16-le') as f:
            content = f.read()[1:]
            new_filename = os.path.basename(path)[-10:]
            new_filepath = os.path.join(data_path,new_filename)
            ans.append(new_filepath)
            with open(new_filepath,'w',encoding='utf-8') as newf:
                newf.write(content)
                
    return ans
    
    


def improve(filepaths:list)->list:
    '''优化正面，中性，还有负面的结果
    

    Parameters
    ----------
    filepaths : list
        utf-8编码的正面，中性以及负面结果路径.

    Returns
    -------
    list
        优化后的三个文件路径.

    '''
    # 新旧文件路径
    pos_rost_path,neu_rost_path,neg_rost_path = filepaths
    pos_file_path = os.path.join(data_path,'正面情感结果_improved.csv')
    neu_file_path = os.path.join(data_path,'中性情感结果_improved.csv')
    neg_file_path = os.path.join(data_path,'负面情感结果_improved.csv')
    
    #  优化正面
    with open(pos_rost_path,encoding='utf-8') as pos_rost,\
    open(pos_file_path,'a',encoding='utf-8') as pos_file,\
    open(neg_file_path,'a',encoding='utf-8') as neg_file:
        pos_file.write('score,word\n')
        neg_file.write('score,word\n')
        while True:
            line = pos_rost.readline()
            if not line:
                break
            if len(line)==3:
                continue
            score,word = line.split()
            # 如果正负完全错了，写到对立的文件里，否则就留在原地
            if word in neg_words:
                neg_file.write('%s,%s\n'%(str(-int(score)),word))
                print('负面误判为正面：%s'%line)
            else:
                pos_file.write('%s,%s\n'%(score,word))
        
    # 优化负面
    with open(neg_rost_path,encoding='utf-8') as neg_rost,\
    open(pos_file_path,'a',encoding='utf-8') as pos_file,\
    open(neg_file_path,'a',encoding='utf-8') as neg_file:
        while True:
            line = neg_rost.readline()
            if not line:
                break
            if len(line) == 3:
                continue
            score,word = line.split()
            # 如果正负完全反了，写到对立的文件里，否则就留在原地
            if word in pos_words:
                pos_file.write('%s,%s\n'%(str(-int(score)),word))
                print('正面误判为负面：%s'%line)
                
            else:
                neg_file.write('%s,%s\n'%(score,word))
        
    # 优化中立
    with open(neu_rost_path,encoding='utf-8') as neu_rost,\
    open(pos_file_path,'a',encoding='utf-8') as pos_file,\
    open(neg_file_path,'a',encoding='utf-8') as neg_file,\
    open(neu_file_path,'a',encoding='utf-8') as neu_file:
        neu_file.write('score,word\n')
        while True:
            line = neu_rost.readline()
            if not line:
                break
            if len(line)==3:
                continue
            score,word = line.split()
            # 如果是正向的，给它的权重是1
            if word in pos_words:
                pos_file.write('%s,%s\n'%(1,word))
                print('正面误判为中立：%s'%line)
            # 负向的就给它-1的权重
            elif word in neg_words:
                neg_file.write('%s,%s\n'%(-1,word))
                print('负面误判为中立：%s'%line)
            else:
                neu_file.write('%s,%s\n'%(score,word))
    return [pos_file_path,neu_file_path,neg_file_path]
if __name__ == '__main__':
    # 载入正向词典
    pos_words = load_words(
        ['pos_comment.txt','pos_sentiment.txt'],
        drop=['超级'],extra=['不可多得'])
    # 载入负向词典
    neg_words = load_words(
        ['neg_comment.txt','neg_sentiment.txt'],
        drop=['黄色','嫩'],extra=['慢'])
    # 获取重新编码的utf-8文档
    pos_rost_path,neu_rost_path,neg_rost_path = to_utf8(
        'words_for_analysis_正面情感结果.txt',
        'words_for_analysis_中性情感结果.txt',
        'words_for_analysis_负面情感结果.txt')
    # 优化
    pos_file_path,neu_file_path,neg_file_path = improve(
        [pos_rost_path,neu_rost_path,neg_rost_path])
    
    # 优化后还要手动调整一下,主要关注正面和负面
    
    
    
    
        
            
    

            