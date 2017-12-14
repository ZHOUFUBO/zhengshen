import scrapy
import json
from scrap_zhengshen.items import ScrapZhengshenItem
import csv


class scrap_zhengshen(scrapy.Spider):
    name = 'zhengshen'
    start_urls = ['http://tingshen.court.gov.cn/search/a/revmor/full?keywords=&provinceCod' \
                  'e=0&cityCode=0&label=&courtCode=&catalogId=&dataType=2&pageSize=200&addre' \
                  'ss=&timeFlag=0&caseType=&courtType=&pageNumber=%s&extType=' % str(page) for page in range(1, 11)]
    def parse(self, response):
        infos=json.loads(response.body_as_unicode())
        # write = csv.writer(open('zhengshen.csv', 'w', encoding='gb18030', newline=''))
        for index,info in enumerate(infos['resultList']):
            item=ScrapZhengshenItem()
            item['case_id']=info['caseId']
            item['case_no']=info['caseNo']
            item['url']='http://tingshen.court.gov.cn/live/{}'.format(str(info['caseId']))
            # if index==0:
            #     write.writerow(item.keys())
            # write.writerow(item.values())
            yield item
