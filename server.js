// find all documents and save to array: http://mongodb.github.io/node-mongodb-native/2.2/quick-start/quick-start/

require('dotenv').config();
const express = require('express');
const fs = require('fs');
const PORT = process.env.PORT || '8080'
const app = express();
const puppeteer = require('puppeteer');
const MongoClient = require('mongodb').MongoClient;
const URI = process.env.MONGO_URI;
const ejs = require('ejs');

let client;
let name;
let source;
let loc;
let parent;
let abbr;

async function mongoConnect (option, name = '', title = '', link = '', res = '') {
  const client = await MongoClient.connect(URI, { useUnifiedTopology: true });
  const db = client.db('theDailyWorld');
  const collection = db.collection('headlines');

  if (option == 'find') {
    console.log('Collecting database...')
    let result = await collection.find({}).toArray();
    return result;
  }
  if (option == 'save') {
    collection.findOneAndUpdate({name: name}, {$set: {title: title, link: link}}, {new: true}, function(updatedDoc) {
      console.log('Updated the ' + name + ' headline')
      });
  }
  if (option == 'render') {
    let resultToRender = await collection.find({}).toArray();
    return resultToRender;
  }

  if (option == 'close') {
    client.close();
    console.log('Done updating.')
    console.log('Database connection closed.')
  }
}

async function scrape () {
  try {
    console.log("Scraping...");
    let browser = await puppeteer.launch({headless: true, args: ['--no-sandbox'] });
    let results = await mongoConnect('find');
    for(let i=0; i < results.length; i++) {
      try {
        let page = await browser.newPage();
        await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36');
        name = results[i]['name'] // from db
        abbr = results[i]['abbr'] // from db
        parent = results[i]['parent'] // from db
        source = results[i]['source'] // from db
        loc = results[i]['location'] // from db
        await page.goto(source);
        await page.waitForSelector(loc);
        await page.exposeFunction('mongoConnect', mongoConnect);
        await page.evaluate(async (name, abbr, parent, source, loc) => {
          let headline = document.querySelector(loc);
          let title = headline.innerText.replace(/^\s+|\s+$/g, '');
          let link = parent + headline.getAttribute('href').replace(/^\., ''/);
          await mongoConnect('save', name, title, link)
        }, name, abbr, parent, source, loc);
        await page.waitForTimeout(Math.floor(Math.random() * 4000 + 1000));
      } catch (err) {
        console.log(err.stack);
    };
  }
  //mongoConnect('close')
} catch (e) {
  console.log(e.stack);
}
};

// Make our db accessible to our router
app.use(function(req,res,next){
  req.db = URI;
  next();
});

app.use(express.static(__dirname + "/public"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set("view engine", "ejs");

// https://closebrace.com/tutorials/2017-03-02/the-dead-simple-step-by-step-guide-for-front-end-developers-to-getting-up-and-running-with-nodejs-express-and-mongodb
app.get("/", async (req, res) => {
  const headlinelist = await mongoConnect('render');
  res.render("index", {headlinelist: headlinelist});
});

app.set("port", PORT);

app.listen(PORT, () => {
  console.log('Listening on port ' + PORT);
});

scrape();