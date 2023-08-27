# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
# import settings
from scrapy.exceptions import DropItem


class DemoPipeline:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='icc_team_ranking',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def close_spider(self , spider):
        self.connection.close()

    def process_item(self, item, spider):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO men_ranking (ranking, team, matches, points, rating) VALUES (%s, %s , %s , %s , %s)"
                cursor.execute(sql, (item['ranking'], item['team'], item['matches'], item['points'], item['rating']))
                self.connection.commit()
        except Exception as e:
            # Handle exceptions and log errors
            raise DropItem(f"Error processing item: {e}")
        return item
