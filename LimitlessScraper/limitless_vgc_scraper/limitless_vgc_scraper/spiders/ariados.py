import scrapy
from limitless_vgc_scraper.items import PokemonItem

page_counter = 1

class AriadosSpider(scrapy.Spider):
    name = "ariados"
    allowed_domains = ["play.limitlesstcg.com"]
    start_urls = ["https://play.limitlesstcg.com/tournaments/completed?game=VGC&format=all&platform=all&type=online&time=4weeks"]

    def parse(self, response):
        tours = response.css('table tr') #get all lines from table

        for tour in tours[1:]: # loop nas linhas da tabela
            number_of_players = tour.css('td ::text')[2].get()
            relative_url      = tour.css('td a ::attr(href)')[0].get()
            tour_url          = 'https://play.limitlesstcg.com' + relative_url[0:-9] + 'metagame' # retirar a palavra standings e adicionar a palavra metagame
            yield response.follow(tour_url, callback=self.parse_tour_page, meta={'pl_num': number_of_players}) # chama o metodo que vai lidar com a url a ser acessada
        
        global page_counter
        if page_counter < int(response.css('div.page-options ul.pagination li ::text')[-2].get()):
            page_counter += 1
            next_page_url = self.start_urls[0] + '&page=' + str(page_counter)
            yield response.follow(next_page_url, callback=self.parse) #recursividade

    def parse_tour_page(self, response):
        tour_players_number   = response.meta.get('pl_num')
        table_rows            = response.css('table.meta tr')

        for row in table_rows[1:]: #[1:] to skip the header

            win_loss_ties_str       = row.css('td ::text')[3].get()
            [wins, losses, ties]    = win_loss_ties_str.split(" - ")
            pokemon_name            = row.css('td a ::text').get()
            
            pokemon_item = PokemonItem()

            pokemon_item['name']    = pokemon_name
            pokemon_item['usage']   = row.css('td ::text')[0].get()
            pokemon_item['players'] = tour_players_number
            pokemon_item['wins']    = wins
            pokemon_item['losses']  = losses

            yield(pokemon_item)