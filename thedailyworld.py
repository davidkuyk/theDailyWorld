import requests, bs4
import os
from selenium import webdriver
import time
from random import randint
    
driver = webdriver.Chrome()
path = os.path.dirname(os.path.realpath(__file__)) + '/thedailyworld.html'

entities = {
    'United Nations': {'abbr': 'UN','parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=united%20nations', 'location': 'article > h3 > a'},
    'World Trade Organization': {'abbr': 'WTO', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=world%20trade%20organization', 'location': 'article > h3 > a'}, 
    'International Monetary Fund': {'abbr': 'IMF', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=International%20Monetary%20Fund', 'location': 'article > h3 > a'},
    'World Bank': {'abbr': 'World Bank', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=World%20Bank', 'location': 'article > h3 > a'},
    'European Union': {'abbr': 'EU', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=European%20Union', 'location': 'article > h3 > a'},
    'World Health Organization': {'abbr': 'WHO', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=World%20Health%20Organization', 'location': 'article > h3 > a'},
    'National Endowment for Democracy': {'abbr': 'NED', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=National%20Endowment%20for%20Democracy', 'location': 'article > h3 > a'},
    'USAID': {'abbr': 'USAID', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=USAID', 'location': 'article > h3 > a'},
    'NATO': {'abbr': 'NATO', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=NATO', 'location': 'article > h3 > a'},
    'China': {'abbr': 'China', 'parent': 'https://www.scmp.com', 'source': 'https://www.scmp.com/news/china', 'location': '.article-title__article-link'},
    'India': {'abbr': 'India', 'parent': 'https://timesofindia.indiatimes.com/india', 'source': 'https://timesofindia.indiatimes.com/india', 'location': '.top-newslist > li > .w_tle > a'},
    'United States': {'abbr': 'U.S.', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=U.S.', 'location': 'article > h3 > a'},
    'Indonesia': {'abbr': 'Indonesia', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Indonesia', 'location': 'article > h3 > a'},
    'Pakistan': {'abbr': 'Pakistan', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Pakistan', 'location': 'article > h3 > a'},
    'Brazil': {'abbr': 'Brazil', 'parent': '', 'source': 'https://www1.folha.uol.com.br/internacional/en/', 'location': '.c-main-headline__url'},
    'Nigeria': {'abbr': 'Nigeria', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Nigeria', 'location': 'article > h3 > a'},
    'Bangladesh': {'abbr': 'Bangladesh', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Bangladesh', 'location': 'article > h3 > a'},
    'Russia': {'abbr': 'Russia', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Russia', 'location': 'article > h3 > a'},
    'Mexico': {'abbr': 'Mexico', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Mexico', 'location': 'article > h3 > a'},
    'Japan': {'abbr': 'Japan', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Japan', 'location': 'article > h3 > a'},
    'Ethiopia': {'abbr': 'Ethiopia', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Ethiopia', 'location': 'article > h3 > a'},
    'Philippines': {'abbr': 'Philippines', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Philippines', 'location': 'article > h3 > a'},
    'Egypt': {'abbr': 'Egypt', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Egypt', 'location': 'article > h3 > a'},
    'Vietnam': {'abbr': 'Vietnam', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Vietnam', 'location': 'article > h3 > a'},
    'Democratic Republic of Congo': {'abbr': 'DR Congo', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=DR%20Congo', 'location': 'article > h3 > a'},
    'Germany': {'abbr': 'Germany', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Germany', 'location': 'article > h3 > a'},
    'Turkey': {'abbr': 'Turkey', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Turkey', 'location': 'article > h3 > a'},
    'Iran': {'abbr': 'Iran', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Iran', 'location': 'article > h3 > a'},
    'Thailand': {'abbr': 'Thailand', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Thailand', 'location': 'article > h3 > a'},
    'United Kingdom': {'abbr': 'UK', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=U.K.', 'location': 'article > h3 > a'},
    'France': {'abbr': 'France', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=France', 'location': 'article > h3 > a'},
    'Italy': {'abbr': 'Italy', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Italy', 'location': 'article > h3 > a'},
    'South Africa': {'abbr': 'South Africa', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=South%20Africa', 'location': 'article > h3 > a'},
    'Tanzania': {'abbr': 'Tanzania', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Tanzania', 'location': 'article > h3 > a'},
    'Myanmar': {'abbr': 'Myanmar', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Myanmar', 'location': 'article > h3 > a'},
    'Kenya': {'abbr': 'Kenya', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Kenya', 'location': 'article > h3 > a'},
    'South Korea': {'abbr': 'South Korea', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=South%20Korea', 'location': 'article > h3 > a'},
    'Colombia': {'abbr': 'Colombia', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Colombia', 'location': 'article > h3 > a'},
    'Spain': {'abbr': 'Spain', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Spain', 'location': 'article > h3 > a'},
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
# try:
i = 0
for key, values in entities.items():
    time.sleep(randint(0, 2))
    if i == 3:
        driver.get('file://' + path)
    searchTerm = values['source']
    res = requests.get(searchTerm)
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    headline = noStarchSoup.select(values['location'])
    title = headline[0].text
    link = values['parent'] + (headline[0].attrs['href']).lstrip('.')

    # filter articles with "opinion" in the title
    if "opinion" in title or "Opinion" in title:
        title = headline[1].text
        link = values['parent'] + (headline[1].attrs['href']).lstrip('.')

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
    entityLink = values['source']
    # if no link
    if len(link) == 0:
        link = 'No Link'
    # add divider below organizations
    if i < 8:
        playFile.write(("<h1><a href={4} target='_blank'><div class='tooltip'><span class='tooltiptext'>{3}</span>{0}</a></div> <a href={2} target='_blank'>{1}</a></h1>").format(entityName, title, link, key, entityLink))
    elif i == 8:
        playFile.write(("<h1><a href={4} target='_blank'><div class='tooltip'><span class='tooltiptext'>{3}</span>{0}</a></div> <a href={2} target='_blank'>{1}</a></h1><hr>").format(entityName, title, link, key, entityLink))
    else:
        playFile.write(("<h1><a href={3} target='_blank'>{0}</a><a href={2} target='_blank'>{1}</a></h1>").format(entityName, title, link, entityLink))
    # clear and print progress
    os.system('clear')
    if i == 0 or i % 3 == 0:
        playFile.flush()
        driver.refresh()
    print(f"{i+1}/{len(entities)}")
    i += 1
# except Exception as err:
    # print('An exception happened: ' + str(err))
playFile.close()
# os.system('clear')
print('Done.')