# bear_sentiment_analysis
京东小熊吐司机用户评论数据情感分析

## 目录结构
├─bearspider\
│  │  main.py\
│  │  scrapy.cfg\
│  │\
│  ├─bearspider\
│  │  │  items.py\
│  │  │  middlewares.py\
│  │  │  pipelines.py\
│  │  │  settings.py\
│  │  │  __init__.py\
│  │  │\
│  │  ├─spiders\
│  │  │  │  bearcomments.py\
│  │  │  │  __init__.py\
│  │  │  │\
│  │  │  └─__pycache__\
│  │  │          &emsp;&emsp;&emsp;bearcomments.cpython-37.pyc\
│  │  │          &emsp;&emsp;&emsp;bearscomment.cpython-37.pyc\
│  │  │          &emsp;&emsp;&emsp;__init__.cpython-37.pyc\
│  │  │\
│  │  └─__pycache__\
│  │          &emsp;&emsp;&emsp;items.cpython-37.pyc\
│  │          &emsp;&emsp;&emsp;middlewares.cpython-37.pyc\
│  │          &emsp;&emsp;&emsp;settings.cpython-37.pyc\
│  │          &emsp;&emsp;&emsp;__init__.cpython-37.pyc\
│  │\
│  └─storage\
│      &emsp;└─data\
│              &emsp;&emsp;&emsp;all_comments.csv\
│              &emsp;&emsp;&emsp;utf8_comments1.csv\
│              &emsp;&emsp;&emsp;utf8_comments2.csv\
│\
└─sentiment_analysis\
    │  &emsp;&emsp;&emsp;improvement.py\
    │  &emsp;&emsp;&emsp;pretreatment.py\
    │  &emsp;&emsp;&emsp;visuslization.py\
    │  &emsp;&emsp;&emsp;京东小熊吐司机用户评论数据情感分析.pdf\
    │\
    ├─data\
    │      &emsp;&emsp;&emsp;all_comments_unique.csv\
    │      &emsp;&emsp;&emsp;all_comments_unique_compressed.csv\
    │      &emsp;&emsp;&emsp;all_comments_unique_compressed_shortdropped.csv\
    │      &emsp;&emsp;&emsp;neg_improvement.csv\
    │      &emsp;&emsp;&emsp;pos_improvement.csv\
    │      &emsp;&emsp;&emsp;words_for_analysis.txt\
    │      &emsp;&emsp;&emsp;words_for_analysis_中性情感结果.txt\
    │      &emsp;&emsp;&emsp;words_for_analysis_情感分布统计结果.txt\
    │      &emsp;&emsp;&emsp;words_for_analysis_情感分布视图.txt\
    │      &emsp;&emsp;&emsp;words_for_analysis_情感分析详细结果.txt\
    │      &emsp;&emsp;&emsp;words_for_analysis_正面情感结果.txt\
    │      &emsp;&emsp;&emsp;words_for_analysis_负面情感结果.txt\
    │      &emsp;&emsp;&emsp;中性情感结果.txt\
    │      &emsp;&emsp;&emsp;中性情感结果_improved.csv\
    │      &emsp;&emsp;&emsp;正面情感结果.txt\
    │      &emsp;&emsp;&emsp;正面情感结果_improved.csv\
    │      &emsp;&emsp;&emsp;正面情感结果_improved_manual.csv\
    │      &emsp;&emsp;&emsp;负面情感结果.txt\
    │      &emsp;&emsp;&emsp;负面情感结果_improved.csv\
    │      &emsp;&emsp;&emsp;负面情感结果_improved_manual.csv\
    │\
    ├─font\
    │      &emsp;&emsp;&emsp;msyh.ttf\
    │\
    ├─image\
    │      &emsp;&emsp;&emsp;正负总权重对比.png\
    │      &emsp;&emsp;&emsp;正面统计.png\
    │      &emsp;&emsp;&emsp;负面统计.png\
    │\
    ├─pos_neg\
    │      &emsp;&emsp;&emsp;neg_comment.txt\
    │      &emsp;&emsp;&emsp;neg_sentiment.txt\
    │      &emsp;&emsp;&emsp;pos_comment.txt\
    │      &emsp;&emsp;&emsp;pos_sentiment.txt\
    │\
    └─stopwords\
            &emsp;&emsp;&emsp;baidu_stopwords.txt\
            &emsp;&emsp;&emsp;cn_stopwords.txt\
            &emsp;&emsp;&emsp;hit_stopwords.txt\
            &emsp;&emsp;&emsp;scu_stopwords.txt\
## 目录说明
- bearspider : scrapy爬虫项目
- sentiment_analysis : 存放数据清洗、分析、优化和可视化相关文件\
&emsp; - pretreatment.py : 数据预处理\
&emsp; - improvement.py : 对ROSTCM6生成的分析结果进行优化\
&emsp; - visualization.py : 对分析结果进行可视化处理\
&emsp; - data : 存放数据预处理和结果优化过程中生成的全部.txt和.csv文件\
&emsp; - font : 存放数据可视化过程中需要使用的中文字体文件\
&emsp; - image : 存放可视化过程中生成的图片\
&emsp; - pos_neg : 存放用于分析结果优化的正负面词语字典\
&emsp; - stopwords : 存放停用词字典
## 项目流程介绍
### 数据采集
- 使用scrapy从京东采集了小熊DSL-A02Z1多士炉(吐司机)的1200条评论数据。
### 数据预处理
- 对采集的原始评论数据进行去重
- 对去重后的评论数据进行机械压缩去词
- 对机械压缩去词后的评论数据进行短句删除
- 对上一步得到的结果进行分词和去除停用词的处理
### 词语情感极性标注
- 利用ROSTCM6的情感分析功能对从评论中抽取的有效词语进行情感极性标注，生成正面、中性和负面三个类别的词语集合
### 分析结果优化
- 机械优化：以知网情感极性词典为依据，对ROSTCM6的分析结果进行优化。对于被错误标注为正面的负面词语和被错误标注为负面的正面词语，进行重新标注，权重取相反数;对于被错误标注为中性的正面和负面词语，进行重新标注 ，权重取1或-1;其他正确标注的词语和情感极性词典未收录的词语，保持不变。
- 手动优化：检查正面和负面词语集合，如果依然存在明显的标注错误，手动修改;如果存在因语境缺失而语义不详的词语，从原始评论数据中找出上下文再做判断。
### 数据可视化
- 绘制正负权重对比直方图
- 绘制正面词语频次分布直方图
- 绘制负面词语频次分布直方图
### 结论展示
- 撰写《京东小熊吐司机用户评论数据情感分析》一文
## 开发环境及依赖库介绍
- python3.7.6
- pandas1.0.1
- numpy1.18.1
- seaborn0.10.0
- matplotlib3.1.3

#### -*-有问题欢迎交流讨论-*-
