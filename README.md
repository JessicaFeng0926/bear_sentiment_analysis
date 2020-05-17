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
│      └─data\
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
