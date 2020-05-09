# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join, Identity



class Otodom(scrapy.Item):

    okna = scrapy.Field(output_processor = TakeFirst())
    numer_oferty =scrapy.Field(output_processor = TakeFirst())
    kiedy_dodano =scrapy.Field(output_processor = TakeFirst())
    kiedy_aktualizowano=scrapy.Field(output_processor = TakeFirst())
    typ_oferty =scrapy.Field(output_processor = TakeFirst())
    tytul_ogloszeia =scrapy.Field(output_processor = TakeFirst())
    lokalizacja=scrapy.Field(output_processor = TakeFirst())
    cena=scrapy.Field(output_processor = TakeFirst())
    czynsz_dodatkowo=scrapy.Field(output_processor = TakeFirst())
    liczba_pokoi=scrapy.Field(output_processor = TakeFirst())
    licza_pieter=scrapy.Field(output_processor = TakeFirst())
    ogrzewanie=scrapy.Field(output_processor = TakeFirst())
    kaucja=scrapy.Field(output_processor = TakeFirst())
    rodzaj_zabudowy=scrapy.Field(output_processor = TakeFirst())
    material_budynku=scrapy.Field(output_processor = TakeFirst())
    stan_wykonczenia=scrapy.Field(output_processor = TakeFirst())
    powierzchnia=scrapy.Field(output_processor = TakeFirst())
    dostepne_od=scrapy.Field(output_processor = TakeFirst())
    link_ogloszenia=scrapy.Field(output_processor = TakeFirst())
    pietro = scrapy.Field(output_processor = TakeFirst())