<h1 align="center">Project Ariados</h1>

<p align="center">
<img align="center" src="https://archives.bulbagarden.net/media/upload/thumb/f/fc/Menu_HOME_0168.png/60px-Menu_HOME_0168.png">
</p>

Project Ariados is a Python application focus on WebScraping, it utilizes the scrapy framework to more easily get numerous information across the https://play.limitlesstcg.com web page and generate a compilation of data that helps competitive Pokémon players to better understand the current state of the metagame.

---

<h3 align="center">Technologies</h3>

<p align="center">
<img align="center" src="https://archives.bulbagarden.net/media/upload/thumb/c/cf/Menu_HOME_0167.png/60px-Menu_HOME_0167.png">
</p>

* Python's framework Scrapy
* Csv files

---

<h3 align="center">Code Summary</h3>

<p align="center">
<img align="center" src="https://archives.bulbagarden.net/media/upload/thumb/c/cf/Menu_HOME_0167.png/60px-Menu_HOME_0167.png">
</p>

The main code is the spider named <i>ariados</i> on th following path.
```
LimitlessScraper\limitless_vgc_scraper\limitless_vgc_scraper\spiders\aridos.py
```
The class AriadosSpider inherit from the Spider class in scrapy framework and have two functions. The parse function access the tournaments pages and iterate throughout each tournament in each page, calling the parse_tour_page function.

On parse_tour_page function, the data from each Pokémon is extracted and associated to a Spider Item who will be returned.

---

<h3 align="center">Configurations and References</h3>

<p align="center">
<img align="center" src="https://archives.bulbagarden.net/media/upload/thumb/c/cf/Menu_HOME_0167.png/60px-Menu_HOME_0167.png">
</p>

Mainly I followed this video tutorial: https://www.youtube.com/watch?v=mBoX_JCKZTE&t=6569s

---

<h3 align="center">How to Run</h3>

<p align="center">
<img align="center" src="https://archives.bulbagarden.net/media/upload/thumb/c/cf/Menu_HOME_0167.png/60px-Menu_HOME_0167.png">
</p>

On the root page, runs the following command to activate the environment.
```
venv\Scripts\activate
```
Next open the <i>limitless_vgc_scraper</i> folder.
```
cd limitless_vgc_scraper
```
To test any hypothetical code combination use the following command to create a shell where you can access the web page data without compromise the code structure.
```
scrapy shell
```
Once created, start by using the <b>fetch</b> command to acess the page, and only than some use the <b>response</b> command to recieve the data.
```
fetch("YOUR_URL")
css.response.("YOUR_FILTER")
```
To run the main application and gets the result on terminal, use the following command.
```
scrapy crawl ariados
```
And to run the main application while saving the results in a csv file, use the following command.
```
scrapy crawl ariados -O csvfilename.csv
```

---

<h3 align="center">Further Features</h3>

<p align="center">
<img align="center" src="https://archives.bulbagarden.net/media/upload/thumb/c/cf/Menu_HOME_0167.png/60px-Menu_HOME_0167.png">
</p>

* Create a loop only for the topcut results in order to save the data about the best resulting teams of each tournament.
* Create an option to look in others periods of time instead of only 4 weeks.

---

<h3 align="center">Authors</h3>

<p align="center">
<img align="center" src="https://archives.bulbagarden.net/media/upload/thumb/c/cf/Menu_HOME_0167.png/60px-Menu_HOME_0167.png">
</p>

* Myself
* Luciano Begot - @lucianobegot on Twitter

