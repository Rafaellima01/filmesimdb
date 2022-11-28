import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top']

    def parse(self, response):

        for filmes in response.css('.titleColumn'):
            yield {
                'titulos': filmes.css('.titleColumn a::text').get(),
                'ano': filmes.css('.secondaryInfo ::text').get()[1:-1],
                'nota': response.css('strong ::text').get(),
            }
        pass
