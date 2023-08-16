import csv

class PokemonInfo():
    def __init__(self, _name, _usage, _players, _wins, _losses):
        self.name    = _name
        self.usage   = int(_usage)
        self.players = int(_players)
        self.wins    = int(_wins)
        self.losses  = int(_losses)

class PokemonAccumulatedData():
    def __init__(self):
        self.data = {}
    
    def is_in_accumulated_data(self, _name):
        if _name in self.data:
            return True
        else:
            return False
    
    def add_new_pokemon(self, poke_info):
        self.data[poke_info.name] = poke_info

    def update_pokemon_info(self, poke_info):
        poke_name = poke_info.name
        self.data[poke_name].usage   += poke_info.usage
        self.data[poke_name].players += poke_info.players
        self.data[poke_name].wins    += poke_info.wins
        self.data[poke_name].losses  += poke_info.losses

    def data_handler(self, poke_info):
        if self.is_in_accumulated_data(poke_info.name):
            self.update_pokemon_info(poke_info)
        else:
            self.add_new_pokemon(poke_info)

accumulated_data = PokemonAccumulatedData()

with open("poketeste.csv", "r") as file:
    csvreader = csv.reader(file)
    next(csvreader) #skip header
    for row in csvreader:
        _poke_info = PokemonInfo(row[1], row[3], row[2], row[4], row[0]) # name, usage, players, wins & losses
        accumulated_data.data_handler(_poke_info)
    #for i in accumulated_data.data: 
    #    print(accumulated_data.data[i].name + " " + str(accumulated_data.data[i].usage) + " " + str(accumulated_data.data[i].players) + " " + str(accumulated_data.data[i].wins) + " " + str(accumulated_data.data[i].losses))

with open("VGCdata.csv", 'w', newline="") as file:
    csvwriter = csv.writer(file)
    header = ['Name', 'Usage', 'Shared', 'Wins', "Losses", "Win Rate"]
    csvwriter.writerow(header)
    for pokemon in accumulated_data.data:
        _wins   = accumulated_data.data[pokemon].wins
        _losses = accumulated_data.data[pokemon].losses

        line = [accumulated_data.data[pokemon].name,
                accumulated_data.data[pokemon].usage,
                "{:.2f}".format(100*(accumulated_data.data[pokemon].usage/accumulated_data.data[pokemon].players)),
                _wins,
                _losses,
                "{:.2f}".format(_wins/(_wins + _losses))]
                
        csvwriter.writerow(line)