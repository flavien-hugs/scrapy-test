'''
    Extraction des personnages d'animation
    via Wikipe
'''

import scrapy


class CharactersSpider(scrapy.Spider):
    name = "character"
    start_urls = [
        'https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Personnage_d%27animation',
    ]

    def parse(self, response):
        for link in response.css('div#mw-pages div.mw-content-ltr li'):
            yield {
                'character': link.css('a::text').extract_first(),
            }
