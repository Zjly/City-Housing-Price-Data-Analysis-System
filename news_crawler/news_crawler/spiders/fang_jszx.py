import scrapy

from news_crawler.items import NewsCrawlerItem


class FangSpider(scrapy.Spider):
	name = "fang_jszx"
	allowed_domains = ["http://search.fang.com"]
	start_urls = [
		"https://news.fang.com/s/zx_%2525E6%2525A5%2525BC%2525E5%2525B8%252582_%2525E6%2525A5%2525BC%2525E5%2525B8%252582%2525E6%252596%2525B0%2525E9%252597%2525BB_%2525E9%2525A2%252598%2525E7%25259B%2525AE%2525E6%252590%25259C%2525E7%2525B4%2525A2_%2525E4%2525B8%25258D%2525E9%252599%252590%252520_%2525E5%25258F%252591%2525E5%2525B8%252583%2525E6%252597%2525B6%2525E9%252597%2525B4_%25E5%258C%2597%25E4%25BA%25AC_1.html",
	]

	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
	}

	def parse(self, response):
		for news in response.xpath('//ul[@class="list_sou"]'):
			item = NewsCrawlerItem()
			item["title"] = news.xpath('//h3[@class="f20 mt05"]/a/text()').extract_first()
			yield item

