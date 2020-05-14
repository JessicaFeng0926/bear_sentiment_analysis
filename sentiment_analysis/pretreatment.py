import os

import pandas as pd
import numpy as np
from numpy import NaN
import jieba

# 获取当前文件夹的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))

def drop_duplicates(filepath:str)->str:
    '''文本去重

    Parameters
    ----------
    filepath : str
        要去重的文本的路径，文件类型需要是csv,并且只处理单列文件.

    Returns
    -------
    str
        返回新文件的路径.

    '''
    # 判断文件类型是否正确
    filename = os.path.basename(filepath)
    if filename[-3:]!='csv':
        print('只处理csv文件！')
        return 
    
    # 读入文件，生成DataFrame对象
    df = pd.read_csv(filepath)
    if df.shape[1] != 1:
        print('只处理单列文件！')
        return
    # 在控制台打印出当前文件的行数
    print('原始文件行数为：%s'%df.shape[0])
    # 去重
    column = df.iloc[:,0]
    column = column.drop_duplicates()
    new_df = column.to_frame()
    # 组合出新文件的文件名
    new_filename = filename[:-4]+'_unique.csv'
   
    # 组合出新文件的完整路径
    new_filepath = os.path.join(basedir,'data')
    new_filepath = os.path.join(new_filepath,new_filename)
    # 写入文件
    new_df.to_csv(new_filepath,index=False)
    # 在控制台打印去重后的文件的行数和路径
    print('去重后的文件行数为：%s,\n存放路径为：%s.'%(new_df.shape[0],new_filepath))
    print('*'*30)
    return new_filepath

def compress(sentence:str,tail:bool=False)->str:
    '''机械压缩去词
    

    Parameters
    ----------
    sentence : str
        需要压缩的字符串.
    tail : bool, optional
        原本压缩句子的头部，如果设为True，就压缩尾部. 

    Returns
    -------
    str
        返回压缩后的字符串.

    '''
    # 新建两个列表用作临时存储容器
    list1 = []
    list2 = []
    # 这是用于存储压缩后的内容的容器
    ans = []
    # 如果用户需要从尾部压缩，就反转原始字符串
    if tail:
        sentence = sentence[::-1]
    # 先把第0个字符放进列表1
    list1.append(sentence[0])
    for letter in sentence[1:]:
        # 如果当前字符和列表1的开头相同
        if letter == list1[0]:
            # 规则1，如果此时列表2为空，直接填充列表2
            if not list2:
                list2.append(letter)
            # 规则2，列表2不为空，且列表1和列表2内容一样，清空列表2
            elif list1 == list2:
                list2 = [letter]
            # 规则3，列表2不为空，但是列表2和列表2内容不一样，清空两个列表
            else:
                ans = ans + list1 + list2
                list1 = [letter]
                list2 = []
        # 如果当前字符和列表1的开头不同
        else:
            # 规则4，此时列表1和列表2重复，也重复长度大于等于2，清空两个列表
            if list1 == list2:
                if len(list2)>=2:
                    ans += list1
                    list1 = [letter]
                    list2 = []
                else:
                    list1 += list2
                    list1.append(letter)
                    list2 = []
            else:
                # 规则5，此时列表1和列表2内容不一样，并且列表2是空的，继续填充列表1
                if not list2:
                    list1.append(letter)
                # 规则6，此时列表2和列表2内容不一样，列表2已经有了字符，继续填充列表2
                else:
                    list2.append(letter)
    # 遍历结束后，最后检查一次两个列表
    # 规则7，如果此时的列表1和列表2一样，去掉列表2
    if list1 == list2:
        ans = ans + list1
    else:
        ans = ans + list1 + list2
    # 如果是尾部压缩，还要记得转回来
    if tail:
        ans.reverse()
    return ''.join(ans)
                    
                    
def compress_for_file(filepath:str)->NaN:
    '''这是应用到文件级别的机械压缩去词
    

    Parameters
    ----------
    filepath : str
        文件路径，只接受单列csv文件

    Returns
    -------
    str
        压缩去词后的新文件路径.

    '''
    # 判断文件类型是否正确
    filename = os.path.basename(filepath)
    if filename[-3:]!='csv':
        print('只处理csv文件！')
        return 
    
    # 读取给定的文件，生成DataFrame对象
    df = pd.read_csv(filepath)
    # 判断是否是单列文件
    if df.shape[1] != 1:
        print('只处理单列文件！')
        return 
    
    # 取出要进行机械压缩去词的列
    column = df.iloc[:,0]
    # 头压缩
    head = column.apply(compress)
    # 尾压缩
    tail = head.apply(compress,args=(True,))
    # 转成新的DataFrame对象
    new_df = tail.to_frame()
    
    # 组合出新文件的文件名
    new_filename = filename[:-4]+'_compressed.csv'
   
    # 组合出新文件的完整路径
    new_filepath = os.path.join(basedir,'data')
    new_filepath = os.path.join(new_filepath,new_filename)
    
    # 写入文件
    new_df.to_csv(new_filepath,index=False)
    
    # 在控制台打印出提示信息
    print('被压缩的行数为：%s\n存储路径为：%s'%\
          (np.count_nonzero(tail!=column),new_filepath))
    print('*'*30)
    return new_filepath
    

def replace_short_with_nan(sentence:str)-> NaN:
    '''把短句子替换为NaN
    

    Parameters
    ----------
    sentence : str
        要判断的句子.

    Returns
    -------
    NaN
        遇到短句子会返回NaN
        长句子就返回本身

    '''
    if len(sentence) <= 4:
        return NaN
    return sentence


def drop_short_comments(filepath:str)->str:
    '''删除csv文件中的短句子
    

    Parameters
    ----------
    filepath : str
        文件路径，只接受单列csv文件.

    Returns
    -------
    str
        删除短句后的新文件路径.

    '''
    # 判断文件类型是否正确
    filename = os.path.basename(filepath)
    if filename[-3:]!='csv':
        print('只处理csv文件！')
        return 
    
    # 读取给定的文件，生成DataFrame对象
    df = pd.read_csv(filepath)
    # 判断是否是单列文件
    if df.shape[1] != 1:
        print('只处理单列文件！')
        return 
    
    # 在控制台打印出原文件的函数
    print("原始文件的行数为：%s"%df.shape[0])
    print("*"*30)
    
    # 取出要进行短句删除的列
    column = df.iloc[:,0]
    # 短句删除
    column_with_nan = column.apply(replace_short_with_nan)
    column_without_nan = column_with_nan.dropna()
    # 转化为DataFrame对象
    new_df = column_without_nan.to_frame()
    
    # 组合出新文件的文件名
    new_filename = filename[:-4]+'_shortdropped.csv'
   
    # 组合出新文件的完整路径
    new_filepath = os.path.join(basedir,'data')
    new_filepath = os.path.join(new_filepath,new_filename)
    
    # 写入文件
    new_df.to_csv(new_filepath,index=False)
    
    # 在控制台打印信息
    print("删除短句后的行数为：%s\n存储路劲是：%s"%(new_df.shape[0],new_filepath))
    print('*'*30)
    return new_filepath


def cut_words(filepath:str)->str:
    '''这是把csv文件里的评论内容切成词，保存为txt文件的函数
    

    Parameters
    ----------
    filepath : str
        文件路径，只接受单列csv文件.

    Returns
    -------
    str
        切词后生成的txt文件路径.

    '''
    # 判断文件类型是否正确
    filename = os.path.basename(filepath)
    if filename[-3:]!='csv':
        print('只处理csv文件！')
        return 
    
    # 读取给定的文件，生成DataFrame对象
    df = pd.read_csv(filepath)
    # 判断是否是单列文件
    if df.shape[1] != 1:
        print('只处理单列文件！')
        return 
    
    # 抽出要分词的列
    column = df.iloc[:,0]
    
    # 载入停用词
    # 使用百度停用词，中文停用词，哈工大停用词，四川大学机器智能实验室停用词的结合
    stopwords = set()
    # 这是这四个停用词文件放置的文件夹路径
    stopwords_path = os.path.join(basedir,'stopwords')
    # 四个停用词文件的名字列表
    stopwords_names = ['baidu_stopwords.txt',
                       'hit_stopwords.txt',
                       'cn_stopwords.txt',
                       'scu_stopwords.txt']
    # 把四个停用词文件里的词都添加到集合里
    for name in stopwords_names:
        with open(os.path.join(stopwords_path,name),encoding='utf-8') as f:
            while True:
                word = f.readline()[:-1]
                if not word:
                    break
                stopwords.add(word)
                
    # 构造出新文件的路径
    new_filepath = os.path.join(basedir,'data')
    new_filepath = os.path.join(new_filepath,'words_for_analysis.txt')
    
    # 统计停用词和有效词的个数
    count_stopwords = 0
    count_validwords = 0
    
    # 对每个句子都用jieba分词，过滤掉停用词，有效的词写入新文件
    with open(new_filepath,'a',encoding='utf-8') as f:
        for index,sentence in column.iteritems():
            words = jieba.cut(sentence)
            for word in words:
                if word not in stopwords:
                    f.write(word+'\n')
                    count_validwords += 1
                else:
                    count_stopwords += 1
                    
    print('有效词个数：%s\n停用词个数：%s'%(count_validwords,count_stopwords))
    return new_filepath
        
    
if __name__ == '__main__':
    # 去重
    unique_path = drop_duplicates(r'D:\Python学习\bear_sentiment_analysis\bearspider\storage\data\all_comments.csv')
    # 机械压缩去词
    compressed_path = compress_for_file(unique_path)
    # 短句删除
    shortdropped_path = drop_short_comments(compressed_path)
    # 过滤停用词+分词
    words_path = cut_words(shortdropped_path)
    
    
    