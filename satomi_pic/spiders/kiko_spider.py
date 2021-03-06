from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from satomi_pic.items import SatomiPicItem

class SatomiSpider(CrawlSpider):
	name="kiko_pic_spider"

#	download_delay=1

	allowed_domains=[]

	start_urls=[
		'http://movie.douban.com/celebrity/1275762/photo/1133260362/'
	]

	rules=(
		Rule(LinkExtractor(allow=(r'http://movie.douban.com/celebrity/1275762/photo/\d+')),callback='parse_item',follow=True),

	)

	def parse_item(self,response):
		print response

		sel=Selector(response)

		item=SatomiPicItem()

		item['image_urls']=sel.xpath('//div[@class="photo-show"]/div[@class="photo-wp"]/a/img/@src').extract()

		yield item
