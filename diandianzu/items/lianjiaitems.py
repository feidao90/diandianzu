import scrapy


class LianJiaItem(scrapy.Item):
    city = scrapy.Field()  # 城市
    region = scrapy.Field()  # 区域

    tradingArea = scrapy.Field()  # 商圈
    realName = scrapy.Field()  # 楼盘名称

    averagePrice = scrapy.Field()  # 均价
    propertyType = scrapy.Field() #物业类型

    saleStatus = scrapy.Field() #售卖状态
    projectAddress = scrapy.Field() #项目地址

    developer = scrapy.Field() #开发商
    propertyCompany = scrapy.Field() #物业公司

    latestSalingTime = scrapy.Field() #开盘时间
    volumeRate = scrapy.Field() #容积率

    propertyYears = scrapy.Field() #产权年限
    greeningRate = scrapy.Field() #绿化率

    plannedHouseholds = scrapy.Field() #规划户数
    propertyCosts = scrapy.Field()  # 物业费

    parkingSpace = scrapy.Field()  # 车位
    heatingWays = scrapy.Field()  #供暖方式

    waterSupply = scrapy.Field()  #供水方式
    PowerSupply = scrapy.Field()  #供电方式

    buildingType = scrapy.Field()  #建筑类型
    area = scrapy.Field()  # 占地面积

    buildingArea = scrapy.Field()  #建筑面积
    pass