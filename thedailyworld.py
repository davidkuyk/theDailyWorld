from GoogleNews import GoogleNews
import requests, bs4
import os
from selenium import webdriver
    
driver = webdriver.Chrome()
path = os.path.dirname(os.path.realpath(__file__)) + '/thedailyworld.html'
googlenews = GoogleNews('en')

countries = ['United Nations', 'World Trade Organization', 'International Monetary Fund', 'World Bank', 'European Union', 'World Health Organization', 'National Endowment for Democracy', 'USAID', 'NATO', 'China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam', 'Democratic Republic of Congo', 'Germany', 'Turkey', 'Iran', 'Thailand', 'United Kingdom', 'France', 'Italy', 'South Africa', 'Tanzania', 'Myanmar', 'Kenya', 'South Korea', 'Colombia', 'Spain']

abbreviations = ['UN, WTO, IMF, World Bank, EU, WHO, NED, USAID, NATO', 'China', 'India', 'U.S.', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam', 'DR Congo', 'Germany', 'Turkey', 'Iran', 'Thailand', 'U.K.', 'France', 'Italy', 'South Africa', 'Tanzania', 'Myanmar', 'Kenya', 'South Korea', 'Colombia', 'Spain']

playFile = open(path, 'w')

playFile.write('''<style>
html {
    background-color: #383838
}

h1 {
    margin: 10px;
    font-size: 27px;
}

a {
    color: #dadada;
    text-decoration: none;
}

</style>''')

playFile.flush()

print('Gathering headlines...')

# loop through countries
for country in countries:
    googlenews.search(country)
    title, link = googlenews.result()[0]['title'], googlenews.result()[0]['link']
    # filter articles with "opinion" in the title
    if "opinion" in title or "Opinion" in title:
        title, link = googlenews.result()[1]['title'], googlenews.result()[1]['link']
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
    title = "<span style='color: #E7E375'>" + country + "</span>: " + title
    # if no link
    if len(link) == 0:
        link = 'No Link'
    # add divider below organizations
    if countries.index(country) == 8:
        playFile.write(("<h1><a href={1} target='_blank'>{0}</a></h1><br><hr>").format(title, link))
    else:
        playFile.write(("<h1><a href={1} target='_blank'>{0}</a></h1>").format(title, link))
    # clear and print progress
    googlenews.clear()
    os.system('clear')
    if countries.index(country) % 5 == 0: 
        playFile.flush()
        driver.refresh()
    print(f"{countries.index(country)}/{len(countries)}")
playFile.close()
print('Done.')