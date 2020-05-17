# bear_sentiment_analysis
京东小熊吐司机用户评论数据情感分析
## 目录结构
├─bearspider
│  │  main.py
│  │  scrapy.cfg
│  │
│  ├─bearspider
│  │  │  items.py
│  │  │  middlewares.py
│  │  │  pipelines.py
│  │  │  settings.py
│  │  │  __init__.py
│  │  │
│  │  ├─spiders
│  │  │  │  bearcomments.py
│  │  │  │  __init__.py
│  │  │  │
│  │  │  └─__pycache__
│  │  │          bearcomments.cpython-37.pyc
│  │  │          bearscomment.cpython-37.pyc
│  │  │          __init__.cpython-37.pyc
│  │  │
│  │  └─__pycache__
│  │          items.cpython-37.pyc
│  │          middlewares.cpython-37.pyc
│  │          settings.cpython-37.pyc
│  │          __init__.cpython-37.pyc
│  │
│  └─storage
│      └─data
│              all_comments.csv
│              utf8_comments1.csv
│              utf8_comments2.csv
│
└─sentiment_analysis
    │  improvement.py
    │  pretreatment.py
    │  visuslization.py
    │  京东小熊吐司机用户评论数据情感分析.pdf
    │
    ├─data
    │      all_comments_unique.csv
    │      all_comments_unique_compressed.csv
    │      all_comments_unique_compressed_shortdropped.csv
    │      neg_improvement.csv
    │      pos_improvement.csv
    │      words_for_analysis.txt
    │      words_for_analysis_中性情感结果.txt
    │      words_for_analysis_情感分布统计结果.txt
    │      words_for_analysis_情感分布视图.txt
    │      words_for_analysis_情感分析详细结果.txt
    │      words_for_analysis_正面情感结果.txt
    │      words_for_analysis_负面情感结果.txt
    │      中性情感结果.txt
    │      中性情感结果_improved.csv
    │      正面情感结果.txt
    │      正面情感结果_improved.csv
    │      正面情感结果_improved_manual.csv
    │      负面情感结果.txt
    │      负面情感结果_improved.csv
    │      负面情感结果_improved_manual.csv
    │
    ├─font
    │      msyh.ttf
    │
    ├─image
    │      正负总权重对比.png
    │      正面统计.png
    │      负面统计.png
    │
    ├─pos_neg
    │      neg_comment.txt
    │      neg_sentiment.txt
    │      pos_comment.txt
    │      pos_sentiment.txt
    │
    └─stopwords
            baidu_stopwords.txt
            cn_stopwords.txt
            hit_stopwords.txt
            scu_stopwords.txt
