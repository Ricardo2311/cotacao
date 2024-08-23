import scrapy

class EconomiaUolSpider(scrapy.Spider):
    name = "economiauol"
    
    def start_requests(self):
        urls = ["https://economia.uol.com.br/cotacoes/"]

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

            

    def parse(self, response):

        for elemento in response.xpath("//div[@class='hidden-xs']"):
            yield{
                'nome': elemento.xpath(".//a[1]/text()").get(),
                'preco': elemento.xpath(".//a[3]/text()").get()
            }
                
