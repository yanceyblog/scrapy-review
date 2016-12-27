# coding:utf-8


from scrapy import cmdline

cmdline.execute("scrapy crawl review -o review.json".split())
