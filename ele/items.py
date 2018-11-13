# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CategoryItem(Item):
    collection = table = 'Category'

    count = Field()
    id = Field()
    image_url = Field()
    level = Field()
    name = Field()


class ShopItem(Item):
    collection = table = 'Shop'

    address = Field()
    description = Field()
    distance = Field()
    flavors = Field()
    delivery_fee = Field()
    minimum_order_amount = Field()
    id = Field()
    image_path = Field()
    latitude = Field()
    longitude = Field()
    name = Field()
    opening_hours = Field()
    order_need_time = Field()
    phone = Field()
    promotion_info = Field()
    rating = Field()
    rating_count = Field()
    recent_order_num = Field()


class GoodsItem(Item):
    collection = table = 'Goods'

    restaurant_id = Field()
    restaurant_name = Field()
    classification = Field()
    classification_id = Field()
    id = Field()
    name = Field()
    price = Field()
    description = Field()
    image_path = Field()
    rating = Field()
    tips = Field()
    rating_count = Field()
    month_sales = Field()
    food_id = Field()
    stock = Field()


