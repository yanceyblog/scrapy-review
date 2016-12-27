# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


# 音乐
class MusicItem(Item):
    music_name = Field()
    music_alias = Field()
    music_singer = Field()
    music_time = Field()
    music_rating = Field()
    music_votes = Field()
    music_tags = Field()
    music_url = Field()


# 乐评
class MusicReviewItem(Item):
    review_title = Field()
    review_content = Field()
    review_author = Field()
    review_music = Field()
    review_time = Field()
    review_url = Field()
