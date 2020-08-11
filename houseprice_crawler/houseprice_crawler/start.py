from scrapy import cmdline

cmdline.execute("scrapy crawl location".split())
cmdline.execute("scrapy crawl info".split())
cmdline.execute("scrapy crawl price".split())
