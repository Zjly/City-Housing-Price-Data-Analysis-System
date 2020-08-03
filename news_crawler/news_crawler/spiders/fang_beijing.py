import scrapy

from news_crawler.items import NewsCrawlerItem


class FangSpider(scrapy.Spider):
	name = "fang_beijing"
	# 前面不用加http://
	allowed_domains = ["search.fang.com"]
	start_urls = [
		"http://search.fang.com/news/search.jsp?q=%B1%B1%BE%A9+%C2%A5%CA%D0&sl=title&fld=&sort=date&sc=&city=&starttime=&endtime=&forms=both"
	]

	def parse(self, response):
		# 找到其中每条新闻的标题
		for news in response.xpath('//div[@class="postTitle"]'):
			item = NewsCrawlerItem()
			# 获取文章标题
			item["title"] = news.xpath('.//a[@target="_blank"]/span').extract()
			# 获取文章链接
			item["link"] = news.xpath('.//a[@target="_blank"]/@href').extract()
			yield item

		# 爬取下一页
		next_page = response.xpath('//a[text()="下一页"]/@href').extract_first()
		next_url = "http://search.fang.com/news/search.jsp" + next_page
		if next_page is not None:
			next_page_url = response.urljoin(next_url)
			yield scrapy.Request(next_page_url, callback=self.parse)
