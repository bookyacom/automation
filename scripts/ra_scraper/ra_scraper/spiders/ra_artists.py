import scrapy


class RaArtists(scrapy.Spider):
    name = "RA_Artists"
    start_urls = [
        'https://www.residentadvisor.net/dj.aspx?area=%s' % (x,) for x in range(3, 501)
    ]

    def __init__(self):
        self.base_url= "https://www.residentadvisor.net"

    def parse(self, response):

        country = response.xpath("//li[@id='liCountry']/span/text()").extract_first()

        if country.lower() == 'select a country': return None

        region = response.xpath("//li[@id='liArea']/span/text()").extract_first()
        artist_list = response.xpath("//div[@class='fl pr8']/span/a/text()").extract()
        artist_link = response.xpath("//div[@class='fl pr8']/span/a/@href").extract()

        # unable to get the contact information of djs, idea cfscrape
        # (https://stackoverflow.com/questions/33247662/how-to-bypass-cloudflare-bot-ddos-protection-in-scrapy)
        for artist, link in zip(artist_list, artist_link):
            url = self.base_url + link
            yield scrapy.Request(url, callback=self.parse_artist,
                                 meta={'country': country, 'region': region,
                                        'type': 'artist', 'artist': artist, 'url': url})

        yield {'type': 'meta_artist', 'country': country, 'region': region, 'url': response.url}

    def parse_artist(self, response):

        data = dict()
        personal_info = response.xpath("//section[@class='contentDetail clearfix']//ul[@class='clearfix']/li")
        for info in personal_info:
            info_type = info.xpath("div/text()").extract_first().replace("/", "").strip().lower()
            if info_type == "on the internet":
                social_media = info.xpath("a/text()").extract()
                social_links = info.xpath("a/@href").extract()
                info_entry = dict(zip(social_media, social_links))
            else:
                info_entry = "-".join(info.xpath("text()").extract())
            data[info_type] = info_entry

        data['contact_emails'] = response.xpath("//div[@class='pt8 breakword']/a").extract()
        data.update(response.meta)

        yield data
