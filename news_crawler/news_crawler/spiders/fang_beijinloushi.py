import scrapy

from news_crawler.items import NewsCrawlerItem


class FangSpider(scrapy.Spider):
	name = "fang_beijinloushi"
	allowed_domains = ["http://search.fang.com"]
	start_urls = [
		"http://search.fang.com/news/search.jsp?q=%B1%B1%BE%A9+%C2%A5%CA%D0&sl=title&fld=&sort=date&sc=&city=&starttime=&endtime=&forms=both",
	]

	def parse(self, response):
		f = open('a.txt', 'wb')
		f.write(response.body)
		f.close()
		# for news in response.xpath('//div[@class="postTitle"]'):
		# 	item = NewsCrawlerItem()
		# 	item["title"] = news.xpath('//a[@target="_blank"]/span').extract_first()
		# 	yield item

