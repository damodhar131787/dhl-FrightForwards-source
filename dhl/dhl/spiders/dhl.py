import scrapy 
import requests
import json
import urllib
from urllib.parse import urlencode
from scrapy.http import Request, FormRequest
from collections import OrderedDict
from ..items import DhlItem
class Dhl(scrapy.Spider):
    name='dhl'
    # def start_requests(self):
    start_urls=['https://dhli.dhl.com/dhli-client/publicTracking?']
        
            #response.xpath('//form/@action').extract()
            #Out[10]: ['./publicTracking;jsessionid=BbAa6Zq7APl9f0oZ0wuz6UOQw0zq7_7IqXQxFJez-OukR2r-SMqJ!-2095115767?0-1.IFormSubmitListener-form']
            #url='https://dhli.dhl.com/dhli-client/publicTracking?33-3.IFormSubmitListener-form'
            # url='https://dhli.dhl.com/dhli-client/publicTracking?'
            #url='https://dhli.dhl.com/dhli-client/publicTracking?'
            # yield FormRequest(url,callback=self.parse)
    def parse(self,response):
    	ids=['BTSA02163', '1ME008336', 'NYPA02185', 'PRGA03190','FLR-XF-0586523']
    	for key in ids:
            cookies={
                     '$Cookie: JSESSIONID': 'bY0aZQjPnsapFGmTM-VofFxgnIZVJE1xec5xZugS4elJAHsGxL1B\\u00211734992326',
                    'BIGipServerpl_dhli.dhl.com_8003': '1785284773.17183.0000',
                    'TS01440ae2': '012d4839b3bbced9f6eda3e0652a6f9d9f6786e8be2c5129968ddafa87d809d47deff6165b89db75beccb3dc2beff5daa129eb481c6f323856ab59d1181eb50a36a70c398ceacdea358c277a7ab06767d2793b5d2c',
                    }
            headers={
                    'Connection': 'keep-alive',
                    'Cache-Control': 'max-age=0',
                    'Origin': 'https://dhli.dhl.com',
                    'Upgrade-Insecure-Requests': '1',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-User': '?1',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                    'dnt': '1',
                    'Sec-Fetch-Site': 'same-origin',
                    'Referer': 'https://dhli.dhl.com/dhli-client/publicTracking?',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9,te;q=0.8',
                    }
            #import pdb;pdb.set_trace()
            #par=''.join(response.xpath('//form/@action').extract())
            par=''.join(response.xpath('//form/@action').get()).replace('./publicTracking;jsessionid=BbAa6Zq7APl9f0oZ0wuz6UOQw0zq7_7IqXQxFJez-OukR2r-SMqJ!-2095115767?','')
           # params=(
            #        ('%s'%(par),''),
             #       )
            #params=(('0-1.IFormSubmitListener-form'),'')
            data={
                    'id3_hf_0': '',
                    'searchType': 'HBN',
                    'searchValue': '%s'%(key),
                    'searchButton': ''
                    }
            #url='https://dhli.dhl.com/dhli-client/publicTracking?'+urlencode(params)
            url='https://dhli.dhl.com/dhli-client/publicTracking?0-1.IFormSubmitListener-form'
            #import pdb;pdb.set_trace()
            meta={'key':key}
            yield FormRequest(url,method="POST",headers=headers,formdata=data,callback=self.parse1,meta={'meta_data':meta})
    def parse1(self,response):
        key1=response.meta.get('meta_data','').get('key','')
        #print(response.body)
        #import pdb;pdb.set_trace()
        count=[]
        if 'NYPA02185' in key1 or 'BTSA02163' in key1:
            container=response.xpath('//div[@class="border-body"]/div//span/text()').extract()[5]
            count.append(container)
        else:
            multiple=''.join(response.xpath('//select//text()').extract()).strip('\n')
            count.append(multiple)

        print("************************************************************")
        #print(container)
        print("keyvalue",key1)
        print("************************************************************")
        source='DHL'
        data=OrderedDict([
        ('ref_no_1',key1),
        ('container',count),
        ('carrier_name',''),
        ('source',source),])

        yield {'data':data,}












































# class Dhl(scrapy.Spider):
#     name='dhl'
#     def start_requests(self):
#         ids=['BTSA02163', '1ME008336', 'NYPA02185', 'PRGA03190','FLR-XF-0586523']
#         for key in ids:
#             #params = (('5-2.IFormSubmitListener-form', ''),)
#             params = (('1-1.IFormSubmitListener-form', ''),)
#             data={
#                 'id3_hf_0': '',
#                 'searchType': 'HBN',
#                 'searchValue': '%s'%(key),
#                 'searchButton': ''
#                 }
