# This is a template for a Python scraper on Morph (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.
import scraperwiki
import lxml.html
import datetime
import time
import re

from threading import Thread
url = ['http://www.indiegogo.com/projects?filter_category=Technology&filter_country=CTRY_US&filter_quick=popular_all&pg_num=']
for x in url:
    def indiegogo():
        for i in range(1,4):
            try:
                url = x+str(i)
                root = scraperwiki.scrape(url)
                content = lxml.html.etree.HTML(root)
                categorie = content.xpath('//div[contains(@class,"project-category")]')
                nom = content.xpath('//div[contains(@class,"project-details")]/a')
                #porteur_projet = content.xpath('//p[contains(@class,"creator")]/a')
                porteur_projet = content.xpath('//p[contains(@class,"creator")]/span/a')
                details = content.xpath('//p[contains(@class,"description")]')
                stats = content.xpath('//span[contains(@id,"project-stats-funding-pct")]')
                montant = content.xpath('//span[contains(@class,"currency currency-medium")]/span')
                lien = content.xpath('//div[contains(@class,"project-details")]/a[@href]')
                for karazana,projet,olona,deta,marika,vola,rohy in zip(categorie,nom,porteur_projet,details,stats,montant,lien):
            #print olona.text,asa.text,deta.text,marika.text,vola.text
                    data = {
                                'Categorie': karazana.text,
                                'Projet' : projet.text,
                                'Nom du porteur': olona.text,
                                'details': deta.text,
                                'statistique': marika.text,
                                'montant obtenu': vola.text,
                                'lien':  "http://www.indiegogo.com"+rohy.attrib.get('href'),
                                'date' : datetime.datetime.now()
                            }
                    scraperwiki.sqlite.save(unique_keys=['Projet'], data=data)


            except:
                print "None"
    t = Thread(target=indiegogo)
    t.start()
