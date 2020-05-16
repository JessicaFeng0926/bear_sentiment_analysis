import os

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.font_manager import FontManager
import pandas as pd
import seaborn as sns

# 获取两份用于绘制数据的文件的路径
basedir = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(basedir,'data')
pos_path = os.path.join(data_path,'正面情感结果_improved_manual.csv')
neg_path = os.path.join(data_path,'负面情感结果_improved_manual.csv') 

# 这是绘制的图片存放的路径
image_path = os.path.join(basedir,'image')

# 这是字体的存放路径
font_path = os.path.join(basedir,'font')

# 加载数据，得到两个DataFrame对象
dfp = pd.read_csv(pos_path)
dfn = pd.read_csv(neg_path)

# 自定义字体对象，用微软雅黑字体，这样可以很好地支持中文显示
myfont = FontProperties(fname=os.path.join(font_path,'msyh.ttf'))

def pos_neg_score()->None:
    '''绘制正面结果总分和负面结果总分对比的直方图
    

    Returns
    -------
    None

    '''

    # 正面结果总分和负面结果总分
    pos_score = dfp.score.sum()
    neg_score = dfn.score.sum()
    
    # 绘制直方图
    plt.bar([1,2],[pos_score,neg_score],color=['#5CB85C','#D9534F'])
    plt.xticks([1,2],['正面','负面'],fontproperties=myfont)
    plt.title('正面总分vs负面总分',fontproperties=myfont)
    plt.savefig(os.path.join(image_path,'正负总权重对比.png'),dpi=200)
    
def frequency(data:pd.DataFrame,pos:bool=True)->None:
    '''绘制正面/负面词语频率分布直方图
    

    Parameters
    ----------
    data : pd.DataFrame
        只接受dfp和dfn两种
    pos : bool, optional
        告知程序此时画的是正面还是负面，默认是正面.注意要和第一个参数保持一致.

    Returns
    -------
    None
        

    '''
    # 改变默认的宽高比，让图片细长
    if data.word.unique().size>=10:
        fig,ax = plt.subplots(figsize=(20,2))
        # 词语比较多，需要紧缩布局
        plt.tight_layout()
        # 避免词语重叠，让词语旋转一个角度
        ax.xaxis.set_tick_params(rotation=60)
    else:
        fig,ax = plt.subplots()
    
    # 这里的font参数只接受字符串
    # 所以我们要从字体的FontProperties对象获取匹配的字体名称
    sns.set(style='ticks',font=myfont.get_name())
    sns.countplot('word',data=data,ax=ax)
    
    name = '正面' if pos else '负面'
    ax.set_xlabel('%s词语'%name)
    ax.set_ylabel('频次')
    ax.set_title('%s词语频次统计图'%name)
    
    # 设置了较高的分辨率
    # bbox_inches参数保证所有内容都会显示在图片上,否则词语会被切掉
    fig.savefig(os.path.join(image_path,'%s统计.png'%name),
                dpi=200,bbox_inches='tight')
   
   
    
    
    
    

if __name__ == '__main__':
    # 绘制正面结果总分和负面结果总分对比的直方图
    pos_neg_score()
    # 画正面词语频次统计图
    frequency(dfp)
    # 画负面词语频次统计图
    frequency(dfn,pos=False)
    
  
    
    
    
    