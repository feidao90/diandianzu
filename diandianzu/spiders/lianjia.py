import scrapy
from ..items.lianjiaitems import LianJiaItem
import time
import pymysql
import re

class DianDianZuSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['sz.fang.lianjia.com']

    # 设置下载延时
    download_delay = 5
    start_urls = 'https://sz.fang.lianjia.com/loupan/futianqu-nanshanqu-longgangqu-baoanqu-luohuqu-longhuaqu-yantianqu-guangmingxinqu-pingshanqu-dapengxinqu/pg'

    db = pymysql.connect('rm-wz970j84167q2388a.mysql.rds.aliyuncs.com','voffice_sz','******','ziguan_local',charset = 'utf8')
    cursor = db.cursor()

    # 抓取深圳所有区域数据
    def start_requests(self):
        for i in range(1, 42):
            url = self.start_urls + '%s' % i + '/'
            page = scrapy.Request(url)
            yield page

    # # 抓取首页数据
    # def start_requests(self):
    #     url = self.start_urls + '%s' % 1 + '/'
    #     page = scrapy.Request(url)
    #     yield page

    def parse(self, response):
        for sel in response.xpath('/html/body/div[4]/ul[2]/li[1]/div'):
            item = dict()

            item['city'] = '深圳'
            item['region'] = sel.xpath('string(./div[2]/span[1])').extract()
            item['region'] = item['region'][0] if len(item['region']) > 0 else ''

            item['tradingArea'] = sel.xpath('string(./div[2]/span[2])').extract()
            item['tradingArea'] = item['tradingArea'][0] if len(item['tradingArea']) > 0 else ''
            item['realName'] = sel.xpath('string(./div[1]/a)').extract()
            item['realName'] = item['realName'][0] if len(item['realName']) > 0 else ''
            item['realName'] = item['realName'] + item['city'] + item['region'] + item['tradingArea']

            url = sel.xpath('string(./div[1]/a/@href)').extract()
            url = url[0] if len(url) > 0 else ''
            # 设置时间间隔
            url = 'https://sz.fang.lianjia.com/' + url
            time.sleep(5)
            yield response.follow(url,
                                  meta={'item': item},
                                  method='GET',
                                  dont_filter=True,
                                  callback=self.parse_detail)

    def parse_detail(self, response):
        item = LianJiaItem()
        tempItem = response.meta['item']

        item['city'] = tempItem['city']
        item['region'] = tempItem['region']

        item['tradingArea'] = tempItem['tradingArea']
        item['realName'] = tempItem['realName']

        for sel in response.xpath('/html/body/div[2]/div[2]/div[4]/div[2]'):

            priceNum = sel.xpath('string(./div[1]/p[1]/span[2])').extract()
            priceNum = priceNum[0] if len(priceNum) > 0 else ''
            priceUnit = sel.xpath('string(./div[1]/p[1]/span[3])').extract()
            priceUnit = priceUnit[0] if len(priceUnit) > 0 else ''
            item['averagePrice'] = priceNum + priceUnit
            item['averagePrice'] = re.sub("\D", "", item['averagePrice'])
            item['averagePrice'] = item['averagePrice'] if len(item['averagePrice']) > 0 else '0'

            item['propertyType'] = sel.xpath('string(./div[2]/div/p[2]/span[2])').extract()
            item['propertyType'] = item['propertyType'][0] if len(item['propertyType']) > 0 else ''
            item['saleStatus'] = sel.xpath('string(./div[1]/div/div/span)').extract()
            item['saleStatus'] = item['saleStatus'][0] if len(item['saleStatus']) > 0 else ''

        item['projectAddress'] = response.xpath('string(//*[@id="house-details"]/div/p[2]/span[2])').extract()
        item['projectAddress'] = item['projectAddress'][0] if len(item['projectAddress']) > 0 else ''
        item['developer'] = response.xpath('string(//*[@id="house-details"]/div/p[4]/span[2])').extract()
        item['developer'] = item['developer'][0] if len(item['developer']) > 0 else ''

        item['propertyCompany'] = response.xpath('string(//*[@id="house-details"]/div/p[4]/span[2])').extract()
        item['propertyCompany'] = item['propertyCompany'][0] if len(item['propertyCompany']) > 0 else ''
        item['latestSalingTime'] = response.xpath('string(//*[@id="house-details"]/div/ul/li[1]/p/span[2])').extract()
        item['latestSalingTime'] = item['latestSalingTime'][0] if len(item['latestSalingTime']) > 0 else ''

        item['volumeRate'] = response.xpath('string(//*[@id="house-details"]/div/ul/li[4]/p/span[2])').extract()
        item['volumeRate'] = item['volumeRate'][0] if len(item['volumeRate']) > 0 else ''
        item['propertyYears'] = response.xpath('string(//*[@id="house-details"]/div/ul/li[5]/p/span[2])').extract()
        item['propertyYears'] = item['propertyYears'][0] if len(item['propertyYears']) > 0 else ''

        item['greeningRate'] = response.xpath('string(//*[@id="house-details"]/div/ul/li[6]/p/span[2])').extract()
        item['greeningRate'] = item['greeningRate'][0] if len(item['greeningRate']) > 0 else ''
        item['plannedHouseholds'] = response.xpath('string(//*[@id="house-details"]/div/ul/li[7]/p/span[2])').extract()
        item['plannedHouseholds'] = item['plannedHouseholds'][0] if len(item['plannedHouseholds']) > 0 else ''

        item['propertyCosts'] = response.xpath('string(//*[@id="house-details"]/div/ul/li[8]/p/span[2])').extract()
        item['propertyCosts'] = item['propertyCosts'][0] if len(item['propertyCosts']) > 0 else ''
        item['propertyCosts'] = re.sub("\D", "", item['propertyCosts'])
        item['propertyCosts'] = item['propertyCosts'] if len(item['propertyCosts']) > 0 else '0'

        item['parkingSpace'] = response.xpath('string(//*[@id="house-details"]/div/ul/div/li[1]/p/span[2])').extract()
        item['parkingSpace'] = item['parkingSpace'][0] if len(item['parkingSpace']) > 0 else ''
        # 去除'\n'、'\t'、'\r'
        item['parkingSpace'] = item['parkingSpace'].replace('\n', '').replace('\t', '').replace(' ', '')

        item['heatingWays'] = response.xpath('string(//*[@id="house-details"]/div/ul/div/li[2]/p/span[2])').extract()
        item['heatingWays'] = item['heatingWays'][0] if len(item['heatingWays']) > 0 else ''
        item['waterSupply'] = response.xpath('string(//*[@id="house-details"]/div/ul/li[9]/p/span[2])').extract()
        item['waterSupply'] = item['waterSupply'][0] if len(item['waterSupply']) > 0 else ''

        item['PowerSupply'] = response.xpath('string(//*[@id="house-details"]/div/ul/li[10]/p/span[2])').extract()
        item['PowerSupply'] = item['PowerSupply'][0] if len(item['PowerSupply']) > 0 else ''
        item['buildingType'] = response.xpath('string(//*[@id="house-details"]/div/ul/li[11]/p/span[2])').extract()
        item['buildingType'] = item['buildingType'][0] if len(item['buildingType']) > 0 else ''

        item['area'] = response.xpath('string(//*[@id="house-details"]/div/ul/li[13]/p/span[2])').extract()
        item['area'] = item['area'][0] if len(item['area']) > 0 else ''
        # 去除'\n'、'\t'、'\r'
        item['area'] = item['area'].replace('\n', '').replace('\t', '').replace(' ', '')
        item['area'] = re.sub("\D", "", item['area'])
        item['area'] = item['area'] if len(item['area']) > 0 else '0'

        item['buildingArea'] = response.xpath('string(//*[@id="house-details"]/div/ul/li[14]/p/span[2])').extract()
        item['buildingArea'] = item['buildingArea'][0] if len(item['buildingArea']) > 0 else ''
        # 去除'\n'、'\t'、'\r'
        item['buildingArea'] = item['buildingArea'].replace('\n', '').replace('\t', '').replace(' ', '')
        item['buildingArea'] = re.sub("\D", "", item['buildingArea'])
        item['buildingArea'] = item['buildingArea'] if len(item['buildingArea']) > 0 else '0'


        sql = 'INSERT INTO lianjia_spider(city, region,tradingArea,averagePrice,buildingName,propertyType,saleStatus,projectAddress,developer,propertyCompany,latestSalingTime,volumeRate,propertyYears,greeningRate,plannedHouseholds,propertyCosts,parkingSpace,heatingWays,waterSupply,PowerSupply,buildingType,area,buildingArea)' \
              ' VALUES (\'%s\', \'%s\',\'%s\',%f,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%f,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%f,%f)' \
              % (item['city'], item['region'], item['tradingArea'], float(item['averagePrice']), item['realName'],
                 item['propertyType'], item['saleStatus'], item['projectAddress'], item['developer'],
                 item['propertyCompany'],
                 item['latestSalingTime'], item['volumeRate'], item['propertyYears'], item['greeningRate'],
                 item['plannedHouseholds'], float(item['propertyCosts']), item['parkingSpace'], item['heatingWays'],
                 item['waterSupply'],
                 item['PowerSupply'], item['buildingType'], float(item['area']), float(item['buildingArea']))
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # Rollback in case there is any error
            self.db.rollback()
        pass



