import requests, bs4
import os
from selenium import webdriver
import time
from random import randint
    
driver = webdriver.Chrome()
path = os.path.dirname(os.path.realpath(__file__)) + '/thedailyworld.html'

entities = {
    'United Nations': {'abbr': 'UN','source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'World Trade Organization': {'abbr': 'WTO', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '}, 
    'International Monetary Fund': {'abbr': 'IMF', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'World Bank': {'abbr': 'World Bank', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'European Union': {'abbr': 'EU', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'World Health Organization': {'abbr': 'WHO', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'National Endowment for Democracy': {'abbr': 'NED', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'USAID': {'abbr': 'USAID', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'NATO': {'abbr': 'NATO', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'China': {'abbr': 'China', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'India': {'abbr': 'India', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'United States': {'abbr': 'U.S.', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Indonesia': {'abbr': 'Indonesia', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Pakistan': {'abbr': 'Pakistan', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Brazil': {'abbr': 'Brazil', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Nigeria': {'abbr': 'Nigeria', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Bangladesh': {'abbr': 'Bangladesh', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Russia': {'abbr': 'Russia', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Mexico': {'abbr': 'Mexico', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Japan': {'abbr': 'Japan', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Ethiopia': {'abbr': 'Ethiopia', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Philippines': {'abbr': 'Philippines', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Egypt': {'abbr': 'Egypt', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Vietnam': {'abbr': 'Vietnam', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Democratic Republic of Congo': {'abbr': 'DR Congo', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Germany': {'abbr': 'Germany', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Turkey': {'abbr': 'Turkey', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Iran': {'abbr': 'Iran', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Thailand': {'abbr': 'Thailand', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'United Kingdom': {'abbr': 'UK', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'France': {'abbr': 'France', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Italy': {'abbr': 'Italy', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'South Africa': {'abbr': 'South Africa', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Tanzania': {'abbr': 'Tanzania', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Myanmar': {'abbr': 'Myanmar', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Kenya': {'abbr': 'Kenya', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'South Korea': {'abbr': 'South Korea', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Colombia': {'abbr': 'Colombia', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
    'Spain': {'abbr': 'Spain', 'source': 'https://news.google.com/search?q=', 'location': 'article > h3 > a '},
}

playFile = open(path, 'w')

playFile.write('''<style>
html {
    background-color: #b5b5b5
}

h1 {
    margin: 10px;
    font-size: 27px;
}

a {
    color: #333333;
    text-decoration: none;
}

.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted black;
}

.tooltip .tooltiptext {
  font-size: 16px;
  visibility: hidden;
  width: 200px;
  background-color: black;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 5px 0;

  /* Position the tooltip */
  position: absolute;
  z-index: 1;
  top: -5px;
  left: 105%;
}

.tooltip:hover .tooltiptext {
  visibility: visible;
}

.entityName{
    color: #020a77
}

</style>''')

playFile.flush()

print('Gathering headlines...')

# loop through entities
try:
    i = 0
    for key, values in entities.items():
        time.sleep(randint(0, 2))
        if i == 3:
            driver.get('file://' + path)
        searchTerm = values['source'] + key
        res = requests.get(searchTerm)
        res.raise_for_status()
        noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
        headline = noStarchSoup.select(values['location'])
        title = headline[0].text
        link = 'https://news.google.com' + (headline[0].attrs['href']).lstrip('.')

        # filter articles with "opinion" in the title
        if "opinion" in title or "Opinion" in title:
            title = headline[1].text
            link = 'https://news.google.com' + (headline[1].attrs['href']).lstrip('.')

        # if title is missing, manually get article title from link
        if len(title) == 0:
            try:
                res = requests.get(link)
                res.raise_for_status()
                noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
                headline = noStarchSoup.select('body h1')
                title = headline[0].text.strip()
            except:
                title = "No Title"
        entityName = "<span class='entityName'>" + values['abbr'] + "</span>: "
        entityLink = values['source'] + key.replace(' ', '%20')
        # if no link
        if len(link) == 0:
            link = 'No Link'
        # add divider below organizations
        if i < 8:
            playFile.write(("<h1><a href={4} target='_blank'><div class='tooltip'><span class='tooltiptext'>{3}</span>{0}</a></div> <a href={2} target='_blank'>{1}</a></h1>").format(entityName, title, link, countries[i], entityLink))
        elif i == 8:
            playFile.write(("<h1><a href={4} target='_blank'><div class='tooltip'><span class='tooltiptext'>{3}</span>{0}</a></div> <a href={2} target='_blank'>{1}</a></h1><hr>").format(entityName, title, link, countries[i], entityLink))
        else:
            playFile.write(("<h1><a href={3} target='_blank'>{0}</a><a href={2} target='_blank'>{1}</a></h1>").format(entityName, title, link, entityLink))
        # clear and print progress
        os.system('clear')
        if i == 0 or i % 3 == 0:
            playFile.flush()
            driver.refresh()
        print(f"{i+1}/{len(countries)}")
        i += 1
except Exception as err:
    print('An exception happened: ' + str(err))
playFile.close()
os.system('clear')
print('Done.')