'''
    Extraction des catégorie de personnage d'animation française
    via Wikipedia
'''

import scrapy


class CompanySpider(scrapy.Spider):
    name = "personnageAnimationFrancais"
    start_urls = [
        'https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Personnage_d%27animation_fran%C3%A7ais',
    ]

    def parse(self, response):
        for link in response.css('div#mw-pages div.mw-content-ltr li'):
            yield {
                'person': link.css('a::text').extract_first(),
            }
