from GoogleNews import GoogleNews
import requests, bs4
import os, sys

googlenews = GoogleNews('en')

countries = ['United Nations', 'World Trade Organization', 'International Monetary Fund', 'World Bank', 'European Union', 'World Health Organization', 'National Endowment for Democracy', 'USAID', 'NATO', 'China', 'India', 'U.S.', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam', 'DR Congo', 'Germany', 'Turkey', 'Iran', 'Thailand', 'U.K.', 'France', 'Italy', 'South Africa', 'Tanzania']

playFile = open('thedailyworld.html', 'w')

playFile.write('''<style>
html {
    background-color: #383838
}

h1 {
    margin: 10px;
}

a {
    color: #dadada;
    text-decoration: none;
}

</style>''')

print('Gathering headlines...')

fontSize = 40
for country in countries:
    fontSize = fontSize - .5
    googlenews.search(country)
    title, link = googlenews.result()[0]['title'], googlenews.result()[0]['link']
    if len(title) == 0:
        try:
            res = requests.get(link)
            res.raise_for_status()
            noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
            headline = noStarchSoup.select('body h1')
            title = country + ": " + headline[0].getText().strip()
        except:
            title = country + ": No Title"
    title = title.split()
    newTitle = ''
    for word in title:
        if word == country:
            word = f"<span style='color: #E7E375'>{word}</span> "
            newTitle += word
        else:
            newTitle += word + ' '
    title = newTitle
    if len(link) == 0:
        link = 'No Link'
    if countries.index(country) == 8:
        playFile.write(("<h1 style='font-size: {2}px;'><a href={1}>{0}</a></h1><br><hr>").format(title, link, fontSize))
    else:
        playFile.write(("<h1 style='font-size: {2}px;'><a href={1}>{0}</a></h1>").format(title, link, fontSize))
    googlenews.clear()
    os.system('clear')
    print(f"{countries.index(country)}/{len(countries)}")

playFile.close()
print('Done.')
os.system("open -a 'Google Chrome' thedailyworld.html")