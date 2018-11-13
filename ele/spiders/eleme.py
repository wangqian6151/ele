# -*- coding: utf-8 -*-
import json

import scrapy
import geohash
from scrapy import Request
from ele.items import CategoryItem, ShopItem, GoodsItem


class ElemeSpider(scrapy.Spider):
    name = 'eleme'

    allowed_domains = ['www.ele.me']

    base_url = 'https://www.ele.me/restapi/shopping/v2/restaurant/category?latitude={lat}&longitude={lng}'

    category_url = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash={geohashcode}&latitude={lat}&limit=24&longitude={lng}&offset={offset}&restaurant_category_ids%5B%5D={category_id}&terminal=android'

    shop_url = 'https://www.ele.me/restapi/shopping/v2/menu?restaurant_id={restaurant_id}&terminal=android'

    latlng_list = [
        # (22.536263, 114.057237),
        # (22.533013, 113.930476),
        # (22.545892, 114.127442),
        # (22.525736, 114.025985),
        # (22.570995, 113.870155),
        # (22.590042, 113.846465),
        # (22.547055, 114.121209),
        # (22.541437, 114.120249),
        # (22.611609, 114.030151),
        # (22.692586, 114.043121),
        # (22.7696, 113.852077),
        # (22.765657, 113.905472),
        # (22.604249, 114.118397),
        # (22.724456, 114.271555),
        # (22.578183, 114.111643),
        # (22.540909, 114.060895),
        (22.720507, 113.833226),
        (22.672108, 113.826256),
        (22.776335, 113.891308),
        (22.67952, 113.93875),
        (22.689297, 114.132421),
        (22.642928, 114.198236),
        (22.766667, 114.301872),
        (22.73674, 114.375258),
        (22.631664, 114.42404),
        (22.596137, 114.475708),
        (22.550019, 114.482506),
        (22.503635, 113.923993),
        (22.563576, 113.902609),
        (22.51928, 114.042319),
        (22.538961, 114.071974),
        (22.568257, 114.114961),
        (22.542001, 114.114366),

    ]

    def start_requests(self):
        for lat, lng in self.latlng_list:
            yield Request(self.base_url.format(lat=lat, lng=lng), callback=self.parse_category,
                          meta={'lat': lat, 'lng': lng})

    def parse_category(self, response):
        result = json.loads(response.text)
        category_id_list = list()
        for i in range(1, len(result)):
            detail = result[i]
            sub_categories = detail.get('sub_categories')
            for sub in sub_categories:
                category_item = CategoryItem()
                category_item['count'] = sub.get('count')
                category_item['id'] = sub.get('id')
                image = sub.get('image_url')
                if image.endswith('png'):
                    category_item['image_url'] = '/'.join(
                        ['http://fuss10.elemecdn.com', image[0], image[1:3], image[3:]]) + '.' + image[-3:]
                elif image.endswith('jpeg'):
                    category_item['image_url'] = '/'.join(
                        ['http://fuss10.elemecdn.com', image[0], image[1:3], image[3:]]) + '.' + image[-4:]
                else:
                    category_item['image_url'] = '/'.join(
                        ['http://fuss10.elemecdn.com', image[0], image[1:3], image[3:]]) + '.' + image[32:]
                category_item['level'] = sub.get('level')
                category_item['name'] = sub.get('name') + detail.get('name') if category_item['id'] == \
                                                                                detail.get('ids')[0] else sub.get(
                    'name')
                yield category_item
                category_id_list.append(sub.get('id'))

        self.logger.debug('category_id_list: {}'.format(category_id_list))
        lat = response.meta.get('lat')
        lng = response.meta.get('lng')
        geohashcode = geohash.encode(lat, lng)
        # for category_id in category_id_list[:]:
        for category_id in [252, 254, 271, 273]:
            yield Request(
                self.category_url.format(lat=lat, lng=lng, category_id=category_id, geohashcode=geohashcode, offset=0),
                callback=self.parse_shops,
                meta={'lat': lat, 'lng': lng, 'category_id': category_id, 'geohashcode': geohashcode, 'offset': 0})

    def parse_shops(self, response):
        result = json.loads(response.text)
        if result:
            for shop in result:
                shop_item = ShopItem()
                shop_item['address'] = shop.get('address')
                shop_item['description'] = shop.get('description')
                shop_item['distance'] = shop.get('distance')
                # for f in shop.get('flavors'):
                #     shop_item['flavors'] += '/'.join([str(f.get('id')), f.get('name')]) + ' '
                shop_item['flavors'] = str(shop.get('flavors'))
                shop_item['delivery_fee'] = shop.get('float_delivery_fee')
                shop_item['minimum_order_amount'] = shop.get('float_minimum_order_amount')
                shop_item['id'] = shop.get('id')
                image = shop.get('image_path')
                if image.endswith('png'):
                    shop_item['image_path'] = '/'.join(
                        ['http://fuss10.elemecdn.com', image[0], image[1:3], image[3:]]) + '.' + image[-3:]
                elif image.endswith('jpeg'):
                    shop_item['image_path'] = '/'.join(
                        ['http://fuss10.elemecdn.com', image[0], image[1:3], image[3:]]) + '.' + image[-4:]
                else:
                    shop_item['image_path'] = '/'.join(
                        ['http://fuss10.elemecdn.com', image[0], image[1:3], image[3:]]) + '.' + image[32:]
                shop_item['latitude'] = shop.get('latitude')
                shop_item['longitude'] = shop.get('longitude')
                shop_item['name'] = shop.get('name')
                shop_item['opening_hours'] = str(shop.get('opening_hours'))
                shop_item['order_need_time'] = shop.get('order_lead_time')
                shop_item['phone'] = shop.get('phone')
                shop_item['promotion_info'] = shop.get('promotion_info')
                shop_item['rating'] = shop.get('rating')
                shop_item['rating_count'] = shop.get('rating_count')
                shop_item['recent_order_num'] = shop.get('recent_order_num')
                yield shop_item

                restaurant_id = shop.get('id')
                restaurant_name = shop.get('name')

                yield Request(self.shop_url.format(restaurant_id=restaurant_id), callback=self.parse_goods,
                              meta={'restaurant_name': restaurant_name})

            lat = response.meta.get('lat')
            lng = response.meta.get('lng')
            category_id = response.meta.get('category_id')
            geohashcode = response.meta.get('geohashcode')
            offset = response.meta.get('offset') + 24
            self.logger.debug('parse_shops offset: {}'.format(offset))
            yield Request(
                self.category_url.format(lat=lat, lng=lng, category_id=category_id, geohashcode=geohashcode,
                                         offset=offset),
                callback=self.parse_shops,
                meta={'lat': lat, 'lng': lng, 'category_id': category_id, 'geohashcode': geohashcode,
                      'offset': offset})

    def parse_goods(self, response):
        result = json.loads(response.text)
        restaurant_name = response.meta.get('restaurant_name')
        for goods in result:
            classification = goods.get('name')
            classification_id = goods.get('id')
            for foods in goods.get('foods'):
                food_item = GoodsItem()
                food_item['restaurant_name'] = restaurant_name
                food_item['classification'] = classification
                food_item['classification_id'] = classification_id
                food_item['id'] = foods.get('item_id')
                food_item['name'] = foods.get('name')
                food_item['description'] = foods.get('description')
                image = foods.get('image_path')
                if image.endswith('png'):
                    food_item['image_path'] = '/'.join(
                        ['http://fuss10.elemecdn.com', image[0], image[1:3], image[3:]]) + '.' + image[-3:]
                elif image.endswith('jpeg'):
                    food_item['image_path'] = '/'.join(
                        ['http://fuss10.elemecdn.com', image[0], image[1:3], image[3:]]) + '.' + image[-4:]
                else:
                    food_item['image_path'] = '/'.join(
                        ['http://fuss10.elemecdn.com', image[0], image[1:3], image[3:]]) + '.' + image[32:]
                food_item['rating'] = foods.get('rating')
                food_item['tips'] = foods.get('tips')
                food_item['rating_count'] = foods.get('rating_count')
                food_item['month_sales'] = foods.get('month_sales')
                food_item['restaurant_id'] = foods.get('restaurant_id')
                food_item['food_id'] = foods.get('specfoods')[0].get('food_id')
                food_item['stock'] = foods.get('specfoods')[0].get('stock')
                food_item['price'] = foods.get('specfoods')[0].get('price')
                yield food_item
