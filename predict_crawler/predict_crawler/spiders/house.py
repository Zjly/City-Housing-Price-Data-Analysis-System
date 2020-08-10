import scrapy

from predict_crawler.items import PredictCrawlerItem


class House(scrapy.Spider):
	name = "house"
	allowed_domains = ["wuhan.esf.fang.com"]

	# 设置爬取的网页地址
	urls = []
	base_url = "https://wuhan.esf.fang.com/house/i3"
	for i in range(1, 101):
		urls.append(base_url + str(i) + "/")

	start_urls = urls

	def parse(self, response):
		for page in response.xpath('//dl[@dataflag="bg"]'):
			item = PredictCrawlerItem()
			item["name"] = page.xpath('.//p[@class="add_shop"]/a/@title').extract_first()
			item["unit_price"] = page.xpath('.//dd[@class="price_right"]/span[2]/text()').extract_first().replace("元/㎡",
																												  "")
			item["total_price"] = page.xpath('.//dd[@class="price_right"]/span[1]/b/text()').extract_first()
			item["unit_type"] = page.xpath('.//p[@class="tel_shop"]/text()').extract_first().replace("\n", "").replace(
				"\t", "")
			item["area"] = page.xpath('.//p[@class="tel_shop"]/text()').extract()[1].replace("\n", "").replace("\t",
																											   "").replace(
				"㎡", "")
			item["towards"] = page.xpath('.//p[@class="tel_shop"]/text()').extract()[3].replace("\n", "").replace("\t",
																												  "")
			item["floor"] = page.xpath('.//p[@class="tel_shop"]/text()').extract()[2].replace("\n", "").replace("\t",
																												"")
			item["address"] = page.xpath('.//p[@class="add_shop"]/span/text()').extract_first()
			item["year"] = page.xpath('.//p[@class="tel_shop"]/text()').extract()[4].replace("\n", "").replace("\t", "")

			# 跳过错误数据
			if not (item["area"].replace(".", "").isdigit() and item["unit_price"].replace(".", "").isdigit() and item[
				"total_price"].replace(".", "").isdigit()):
				continue

			yield item
