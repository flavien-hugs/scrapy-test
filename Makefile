SHELL := /bin/bash

# SCRAPER
personnage:
	cd data/ && rm -rf characters.json && cd .. && scrapy runspider scraper_pers_animation.py -o data/characters.json

# 
pers_animation_fr:
	cd data/ && rm -rf pers_animation_fr.json && cd .. && scrapy runspider scraper_pers_animation_fr.py -o data/pers_animation_fr.json

#
quotes:
	cd data/ && rm -rf quotes.json && cd .. && scrapy runspider scraper_quotes.py -o data/quotes.json