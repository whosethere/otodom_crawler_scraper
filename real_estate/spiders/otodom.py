import scrapy
from scrapy.linkextractors import LinkExtractor
import json
from pymongo import MongoClient
import base64
import io
from real_estate.items import Otodom
from scrapy.loader import ItemLoader
import datetime
import time
import re



class OtodomSpider(scrapy.Spider):
    name = 'otodom'
    allowed_domains = ['otodom.pl']
    start_urls = ['https://www.otodom.pl/wynajem/mieszkanie/?nrAdsPerPage=72']

    def parse(self, response):
        
        ogloszenie = response.xpath('//article/@data-url').extract()

        for url_ogloszenia in ogloszenie:
            yield scrapy.Request(url_ogloszenia,
                                callback=self.parse_ogloszenie,
                                meta={'url_ogloszenia':url_ogloszenia})
                            
        next_page =  response.xpath('//li[@class="pager-next"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback = self.parse)

    

    def parse_ogloszenie(self, response):
        
        link_ogloszenia = response.meta['url_ogloszenia']
        typ_oferty  = response.xpath('//div[@class="css-1gjwmw9"]/text()').extract()
        tytul_ogloszeia  = response.xpath('//div[@class="css-1ld8fwi"]/text()').extract()
        lokalizacja = response.xpath('//a[@class="css-12hd9gg"]/text()').extract() # to do przetwarzanie tekstu
        cena  = response.xpath('//div[@class="css-1vr19r7"]/text()').extract()


        
        # odds_away = match.xpath('normalize-space(./div/div[2]/market-selections/rate-button[2]/button)').extract_first()
    
        czynsz_dodatkowo = ""
        liczba_pokoi =""
        licza_pieter =""
        ogrzewanie =""
        kaucja =""
        rodzaj_zabudowy =""
        material_budynku =""
        stan_wykonczenia =""
        powierzchnia =""
        pietro =""
        okna =""
        dostepne_od =""
        
        szczegoly_ogloszenia = response.xpath('normalize-space(//div[@class="css-1ci0qpi"]/ul/li)')
        for szczegol in response.xpath('(//div[@class="css-1ci0qpi"]/ul/li)'): 
            szczegol = szczegol.extract() 
            szczegol = szczegol.replace("<li>", "").replace("<strong>", "").replace("</li>", "").replace("</strong>", "") 
            co,jakie = szczegol.split(":")

            if co == "Czynsz - dodatkowo":
                czynsz = jakie
            if co == "Kaucja":
                kaucja = jakie
            if co == "Powierzchnia":
                powierzchnia = jakie
            if co == "Liczba pokoi":
                liczba_pokoi = jakie
            if co == "Rodzaj zabudowy":
                rodzaj_zabudowy = jakie
            if co == "Piętro":
                pietro = jakie
            if co == "Liczba pięter":
                liczba_pieter = jakie
            if co == "Materiał budynku":
                material_budynku = jakie
            if co == "Okna":
                okna = jakie
            if co == "Ogrzewanie":
                ogrzewanie = jakie
            if co == "Stan wykończenia":
                stan_wykonczenia = jakie
            if co == "Dostępne od":
                dostepne_od = jakie
        
        numer_oferty = response.xpath('//div[@class="css-kos6vh"]/text()').extract_first() 
        numer_oferty = numer_oferty.split(":")[1]
        kiedy_dodano = response.xpath('//div[@class="css-lh1bxu"]/text()')[0].extract()
        kiedy_aktualizowano = response.xpath('//div[@class="css-lh1bxu"]/text()')[1].extract()

        # tytul_ogloszeia  = response.xpath('//div[@class="css-1ld8fwi"]/text()').extract()
        # lokalizacja = response.xpaht('//a[@class="css-12hd9gg"]/text()').extract() # to do przetwarzanie tekstu
        # cena  = response.xpath('//div[@class="css-1vr19r7"]/text()').extract()
        # czynsz_dodatkowo = ""
        # liczba_pokoi =""
        # licza_pieter =""
        # ogrzewanie =""
        # kaucja =""
        # rodzaj_zabudowy =""
        # material_budynku =""
        # stan_wykonczenia =""
        # powierzchnia =""
        # pietro =""
        # okna =""
        # dostepne_od =""

        loader = ItemLoader(item=Otodom(), response=response)
        loader.add_value('numer_oferty', numer_oferty)
        loader.add_value('kiedy_dodano', kiedy_dodano)
        loader.add_value('kiedy_aktualizowano', kiedy_aktualizowano)
        loader.add_value('typ_oferty', typ_oferty)
        loader.add_value('okna', okna)
        loader.add_value('tytul_ogloszeia', tytul_ogloszeia)
        loader.add_value('lokalizacja', lokalizacja)
        loader.add_value('cena', cena)
        loader.add_value('czynsz_dodatkowo', czynsz_dodatkowo)
        loader.add_value('liczba_pokoi', liczba_pokoi)
        loader.add_value('licza_pieter', licza_pieter)
        loader.add_value('pietro', pietro)
        loader.add_value('ogrzewanie', ogrzewanie)
        loader.add_value('kaucja', kaucja)
        loader.add_value('rodzaj_zabudowy', rodzaj_zabudowy)
        loader.add_value('material_budynku', material_budynku)
        loader.add_value('stan_wykonczenia', stan_wykonczenia)
        loader.add_value('powierzchnia', powierzchnia)
        loader.add_value('dostepne_od', dostepne_od)
        loader.add_value('link_ogloszenia', link_ogloszenia)
        yield loader.load_item()