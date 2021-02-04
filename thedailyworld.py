import requests, bs4
import os
from selenium import webdriver
import time
from random import randint
    
driver = webdriver.Chrome()
path = os.path.dirname(os.path.realpath(__file__)) + '/thedailyworld.html'

countries = ['United Nations', 'World Trade Organization', 'International Monetary Fund', 'World Bank', 'European Union', 'World Health Organization', 'National Endowment for Democracy', 'USAID', 'NATO', 'China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam', 'Democratic Republic of Congo', 'Germany', 'Turkey', 'Iran', 'Thailand', 'United Kingdom', 'France', 'Italy', 'South Africa', 'Tanzania', 'Myanmar', 'Kenya', 'South Korea', 'Colombia', 'Spain']

abbreviations = ['UN', 'WTO', 'IMF', 'World Bank', 'EU', 'WHO', 'NED', 'USAID', 'NATO', 'China', 'India', 'U.S.', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam', 'DR Congo', 'Germany', 'Turkey', 'Iran', 'Thailand', 'U.K.', 'France', 'Italy', 'South Africa', 'Tanzania', 'Myanmar', 'Kenya', 'South Korea', 'Colombia', 'Spain']

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

# loop through countries
try:
    for i in range(len(countries)):
        time.sleep(randint(0, 2))
        if i == 3:
            driver.get('file://' + path)
        searchTerm = 'https://news.google.com/search?q=' + countries[i]
        res = requests.get(searchTerm)
        res.raise_for_status()
        noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
        headline = noStarchSoup.select('article > h3 > a')
        title = headline[0].getText()
        link = 'https://news.google.com' + (headline[0].attrs['href']).lstrip('.')

        # filter articles with "opinion" in the title
        if "opinion" in title or "Opinion" in title:
            title = headline[1].getText()
            link = 'https://news.google.com' + (headline[1].attrs['href']).lstrip('.')

        # if title is missing, manually get article title from link
        if len(title) == 0:
            try:
                res = requests.get(link)
                res.raise_for_status()
                noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
                headline = noStarchSoup.select('body h1')
                title = headline[0].getText().strip()
            except:
                title = "No Title"
        entityName = "<span class='entityName'>" + abbreviations[i] + "</span>: "
        entityLink = "https://news.google.com/search?q=" + countries[i].replace(' ', '%20')
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
        googlenews.clear()
        os.system('clear')
        if i % 3 == 0:
            playFile.flush()
            driver.refresh()
        print(f"{i+1}/{len(countries)}")
except Exception as err:
    print('An exception happened: ' + str(err))
playFile.close()
os.system('clear')
print('Done.')