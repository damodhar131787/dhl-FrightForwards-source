# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from .items import DhlItem
from datetime import datetime
import MySQLdb
class DhlPipeline(object):
    def __init__(self):
                self.con=MySQLdb.connect(host='localhost',user='root',db='task',use_unicode=True,charset="utf8",passwd='dbms')
                self.cur=self.con.cursor()
                self.table='dhl2'
    def process_item(self, item, spider):
        result=item['data']
        doc='#<>#'.join([str(result.get('ref_no_1', '')),str(result.get('container','')),str(result.get('carrier_name','')),result.get('source',''),str(datetime.now()),str(datetime.now())])
        with open('dhl3.jl','a+') as f:
            f.write(str(doc))
            f.write('\n')
        self.cur.execute("LOAD DATA LOCAL INFILE '/home/headrun/dhl/dhl/spiders/dhl3.jl' IGNORE INTO TABLE %s FIELDS TERMINATED BY'#<>#'(reference_no,container_no,standardized_carrier_name,source,created_at,modified_at)"%(self.table))
        self.con.commit()


        return item
