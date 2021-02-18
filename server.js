
require('dotenv').config();
const express = require('express');
const fs = require('fs');
const app = express();
const http = require('http').createServer(app);
const puppeteer = require('puppeteer');

function theBigOne () {
  console.log('Running...')
  fs.writeFileSync(__dirname + "/views/index.html", '')

  const entities = {
    'United Nations': {'abbr': 'UN','parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=united%20nations', 'location': 'article > h3 > a'},
    'World Trade Organization': {'abbr': 'WTO', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=world%20trade%20organization', 'location': 'article > h3 > a'}, 
    'International Monetary Fund': {'abbr': 'IMF', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=International%20Monetary%20Fund', 'location': 'article > h3 > a'},
    'World Bank': {'abbr': 'World Bank', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=World%20Bank', 'location': 'article > h3 > a'},
    'European Union': {'abbr': 'EU', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=European%20Union', 'location': 'article > h3 > a'},
    'NATO': {'abbr': 'NATO', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=NATO', 'location': 'article > h3 > a'},
    'World Health Organization': {'abbr': 'WHO', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=World%20Health%20Organization', 'location': 'article > h3 > a'},
    'USAID': {'abbr': 'USAID', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=USAID', 'location': 'article > h3 > a'},
    'National Endowment for Democracy': {'abbr': 'NED', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=National%20Endowment%20for%20Democracy', 'location': 'article > h3 > a'},
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
    'United Kingdom': {'abbr': 'UK', 'parent': '', 'source': 'https://www.theguardian.com/uk?INTCMP=CE_UK', 'location': 'a.js-headline-text'},
    'France': {'abbr': 'France', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=France', 'location': 'article > h3 > a'},
    'Italy': {'abbr': 'Italy', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Italy', 'location': 'article > h3 > a'},
    'South Africa': {'abbr': 'South Africa', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=South%20Africa', 'location': 'article > h3 > a'},
    'Tanzania': {'abbr': 'Tanzania', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Tanzania', 'location': 'article > h3 > a'},
    'Myanmar': {'abbr': 'Myanmar', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Myanmar', 'location': 'article > h3 > a'},
    'Kenya': {'abbr': 'Kenya', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Kenya', 'location': 'article > h3 > a'},
    'South Korea': {'abbr': 'South Korea', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=South%20Korea', 'location': 'article > h3 > a'},
    'Colombia': {'abbr': 'Colombia', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Colombia', 'location': 'article > h3 > a'},
    'Spain': {'abbr': 'Spain', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Spain', 'location': 'article > h3 > a'},
    'Uganda': {'abbr': 'Uganda', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Uganda', 'location': 'article > h3 > a'},
    'Argentina': {'abbr': 'Argentina', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Argentina', 'location': 'article > h3 > a'},
    'Algeria': {'abbr': 'Algeria', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Algeria', 'location': 'article > h3 > a'},
    'Sudan': {'abbr': 'Sudan', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Sudan', 'location': 'article > h3 > a'},
    'Ukraine': {'abbr': 'Ukraine', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Ukraine', 'location': 'article > h3 > a'},
    'Iraq': {'abbr': 'Iraq', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Iraq', 'location': 'article > h3 > a'},
    'Afghanistan': {'abbr': 'Afghanistan', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Afghanistan', 'location': 'article > h3 > a'},
    'Poland': {'abbr': 'Poland', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Poland', 'location': 'article > h3 > a'},
    'Canada': {'abbr': 'Canada', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Canada', 'location': 'article > h3 > a'},
    'Morocco': {'abbr': 'Morocco', 'parent': 'https://news.google.com', 'source': 'https://news.google.com/search?q=Morocco', 'location': 'article > h3 > a'}
  }

  let header = `
  <head>
    <link type="text/css" rel="stylesheet" href="style.css" />
  </head>
  
  <h1 class='title'>The Daily World</h1>
  <h3 id="todaysDate"></h3>
  
  <script type="text/javascript">
    var months = ['January','February','March','April','May','June','July','August','September','October','November','December'];       
    var today = new Date();    
    document.getElementById("todaysDate").innerHTML = months[today.getMonth()] + " " + today.getDate()+ ", " + today.getFullYear();

    function timedRefresh(timeoutPeriod) {
      setTimeout("location.reload(true);",timeoutPeriod);
    }
    
    window.onload = timedRefresh(10000);
  </script>
  `

  let source;
  let loc;
  let parent;
  let abbr;
  let finalHeadline;

  async function run () {
    try {
      var stream = fs.createWriteStream(__dirname + "/views/index.html", {flags:'a'});
      stream.write(header);
      console.log('Opening browser...')
      const browser = await puppeteer.launch({headless: true, args: ['--no-sandbox'] });
      const page = await browser.newPage();
      await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36');
      
      for (const [key, value] of Object.entries(entities)) {
        try {
        console.log('Gathering headline...')
        source = value['source']
        loc = value['location']
        parent = value['parent']
        abbr = value['abbr']
        await page.goto(source);
        await page.waitForSelector(loc);
        const titles = await page.evaluate((key, source, loc, parent, abbr) => {
          let headline = document.querySelector(loc);
          let title = headline.innerText.replace(/^\s+|\s+$/g, '');
          let link = parent + headline.getAttribute('href').replace(/^\., ''/);
          let entityName = "<span class='entityName'>" + abbr + "</span>: "
          let finalHeadlines = `<h1><a href=${source} target='_blank'><div class='tooltip'><span class='tooltiptext'>${key}</span>${entityName}</a></div> <a href=${link} target='_blank'>${title}</a></h1>`;
          return finalHeadlines;
        }, key, source, loc, parent, abbr);
        stream.write(titles)
        await page.waitForTimeout(Math.floor(Math.random() * 4000 + 1000));
      } catch (e) {
        console.log(e);
      }
      }

      await browser.close();
      return titles;
    } catch (e) {
        return e;
    }
  }
  
  
  
  // MAIN HEADLINE LOOP
  
    run().then((res) => {
      stream.write(res)
    })
  };

app.use(express.static(__dirname + "/public"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/views/index.html");
});

http.listen(process.env.PORT || 3000, () => {
  console.log('Listening on port ' + process.env.PORT);
});

theBigOne();