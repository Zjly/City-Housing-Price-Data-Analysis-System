import json
import re
import scrapy

from news_crawler.items.sohu_news_details_items import SohuNewsDetailsCrawlerItem


class NewsDetailsSpider(scrapy.Spider):
	name = "sohu_news_details"
	allowed_domains = ["house.focus.cn"]

	# 读取json文件中的文章地址进行爬取
	links = []
	with open("links_sohu_news_list.json", "r") as f:
		json_data = json.load(f)

		for data in json_data:
			links.append(data["link"])

	start_urls = links

	def parse(self, response):
		for news in response.xpath('//div[@class="main-content"]'):
			item = SohuNewsDetailsCrawlerItem()
			# 获取文章标题
			item["title"] = news.xpath('.//h1/text()').extract_first()
			# 获取文章时间
			item["time"] = news.xpath('.//div[@class="info-source"]/span[2]/text()').extract_first()
			# 获取文章内容并清除其中的标签
			content = news.xpath('.//div[@class="info-content"]').extract_first()
			content = re.compile(r'<[^>]+>', re.S).sub('', content)
			item["content"] = content
			yield item
