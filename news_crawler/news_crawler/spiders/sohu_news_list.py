import scrapy

from news_crawler.items.sohu_news_list_items import SohuNewsListCrawlerItem


class FangSpider(scrapy.Spider):
	name = "sohu_news_list"
	# 前面不用加http://
	allowed_domains = ["house.focus.cn"]
	start_urls = [
		"https://house.focus.cn/zixun/zhengce/1/"
	]

	def parse(self, response):
		# 找到其中每条新闻的标题
		for news in response.xpath('//li[@class="news-list-item global-clearfix"]'):
			item = SohuNewsListCrawlerItem()
			# 获取文章标题
			item["title"] = news.xpath('.//div[@class="news-list-detail"]/a/@title').extract_first()
			# 获取文章链接
			item["link"] = news.xpath('.//div[@class="news-list-detail"]/a/@href').extract_first()
			yield item

		# 爬取下一页
		next_page_url = response.xpath('//a[text()="下一页"]/@href').extract_first()
		if next_page_url is not None:
			next_page_url = response.urljoin(next_page_url)
			yield scrapy.Request(next_page_url, callback=self.parse)
