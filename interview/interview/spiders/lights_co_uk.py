from ..items import InterviewItemFile, InterviewItemImage

from selenium import webdriver
from selenium.webdriver import FirefoxOptions

import scrapy
import requests
import json


class LightsCoUkSpider(scrapy.Spider):
    name = 'lights_co_uk'
    start_urls = ['https://www.lights.co.uk/philips-hue-white-color-impress-led-pillar-light.html']

    def __init__(self):

        self.path = "."
        self.driver_options = FirefoxOptions()
        self.driver_options.headless = True
        self.driver = webdriver.Firefox(self.path, options=self.driver_options)

    def _get_images(self, response):

        pre_focus = 39
        after_focus = 4

        raw_image_urls = response.css('div.swiper-slide picture').getall()
        clean_image_urls = []

        for item in raw_image_urls:
            clean_image_urls.append(response.urljoin(
                item[(item.find('<source type="image/jpeg"') + pre_focus):(item.find('.jpg">') + after_focus)]))

        clean_image_urls.pop(0)

        image_item = InterviewItemImage()
        image_item['image_urls'] = clean_image_urls
        return image_item

    def _get_datasheet(self, response):

        self.driver.get(response.url)
        datasheet_element = self.driver.find_element_by_css_selector('a.download-file__link')
        try:
            datasheet_element.click()
            datasheet_relative_url = self.driver.find_element_by_css_selector('a.download-file__link').get_attribute(
                'href')
        except Exception as e:
            print(e)
        finally:
            self.driver.close()

        datasheet_absolute_url = response.urljoin(datasheet_relative_url)

        file_item = InterviewItemFile()
        file_item['file_urls'] = [datasheet_absolute_url]
        return file_item

    def _get_video(self):

        v_request = requests.get(
            'https://mycliplister.com/jplist/87003/11288bee564ee813a1d3b024327c32753637593bb7687741251aac1a3f2e5e387542f'
            '4b245d8376b29ebbfb4da4b9e02ce2ce1436d4b4474c07dce950673b6cc09b1bf1d3d45e851bb6c4477e7a6415e3_x4c002731b13c1'
            'f45b3e232a7d57a46cb136ae0d8048003374d7a135d765a8c63d6ffaa4f54aa5e818aad9c6892b2be28ef03d0d1baf356eb0ab63cb3'
            'd3f42637')

        v_response = json.loads(v_request.content)
        video_url = v_response['cliplist']['clip']['clipurl']

        video_item = InterviewItemFile()
        video_item['file_urls'] = [video_url]
        return video_item

    def parse(self, response):

        yield self._get_images(response)
        yield self._get_datasheet(response)
        yield self._get_video()





