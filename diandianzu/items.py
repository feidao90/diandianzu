# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DiandianzuItem(scrapy.Item):

    city = scrapy.Field()  # 城市
    region = scrapy.Field()  # 区域

    tradingArea = scrapy.Field()  # 商圈
    averagePrice = scrapy.Field()  # 均价

    realName = scrapy.Field()  # 楼盘名称
    profile = scrapy.Field()  # 简介

    completionTime = scrapy.Field()  # 竣工时间
    location = scrapy.Field()  # 地理位置

    layerHeight = scrapy.Field()  # 层高
    layerNum = scrapy.Field()  # 层数

    property = scrapy.Field()  # 物业
    propertyCosts = scrapy.Field()  # 物业费

    parkingSpace = scrapy.Field()  # 车位
    parkingRent = scrapy.Field()  # 车位月租

    airConditioning = scrapy.Field()  # 空调
    airfee = scrapy.Field()  # 空调费

    airhours = scrapy.Field()  # 空调开放时长
    elevator = scrapy.Field()  # 电梯

    network = scrapy.Field()  # 网络
    checkBusiness = scrapy.Field()  # 入住企业

    priceRange = scrapy.Field()  # 价格区间
    buildingAveragePrice = scrapy.Field()  # 大厦均价

    houseType = scrapy.Field()  # 户型划分
    area = scrapy.Field()  # 面积

    price = scrapy.Field()  # 价格
    floorNum = scrapy.Field()  # 楼层

    decoration = scrapy.Field()  # 装修
    updateTime = scrapy.Field()  # 更新时间

    shortestLease = scrapy.Field()  # 最短租期
    freeRentPeriod = scrapy.Field()  # 免租期
    pass
