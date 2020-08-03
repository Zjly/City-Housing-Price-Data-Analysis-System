from scrapy import cmdline

# 执行爬虫
cmdline.execute("scrapy crawl fang_beijing -o links_beijing.json".split())
