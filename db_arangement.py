#db_arangement.py
#-*- coding:utf-8 -*-
import re

#正規表現を適用する文
t = """
ここにいじくりたい文章をいれる
"""

#2単位の科目のsql
matches2 = re.findall(u'<option value="2">(.+)</option>',t)
print "----------------ここから２単位-----------------------------------"
for m in matches2:
	sql = "INSERT INTO テーブル名 SET name="+ "'" +m + "'," + " credit=2;"
	print sql

print "----------------ここから４単位-----------------------------------"
#4単位の科目のsql
matches4 = re.findall(u'<option value="4">(.+)</option>',t)
for m in matches4:
	sql = "INSERT INTO テーブル名 SET name="+ "'" +m + "'," + " credit=4;"
	print sql

