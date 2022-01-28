import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    # never put the http protocol here
    allowed_domains = ['www.worldometers.info/']
    start_urls = [
        'https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        title = response.xpath("//h1/text()").get()
        countries = response.xpath("//td/a/text()").getall()

        # always return the data as a dict
        yield {
            'title': title,
            'countries': countries
        }
