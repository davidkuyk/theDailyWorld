# theDailyWorld

[![GitHub version](https://img.shields.io/badge/version-v1.0.0-blue.svg)](https://github.com/davidkuyk/theDailyWorld)
[![License](https://img.shields.io/github/license/davidkuyk/theDailyWorld.svg)](https://github.com/davidkuyk/theDailyWorld/blob/main/LICENSE)

A minimalistic Javascript world news app.

## Table of Contents

- [theDailyWorld](#thedailyworld)
  - [Table of Contents](#table-of-contents)
  - [Background](#background)
  - [Future Feature Ideas](#future-feature-ideas)
  - [Installation](#installation)
  - [Scaffolding](#scaffolding)
  - [Bugs](#bugs)
  - [Author](#author)
  - [License](#license)

## Background

> Feb 17, 2021: I've converted the app from a simple Python web scraping file to a fullstack Javascript webpage.

The inspiration behind The Daily World was my frustration with the clutter on every news site. I've always wanted a news site that simply shows you the headlines, one per topic.

I'm also fascinated by the idea of a news site that gives you news from every country in one glance. So that's my eventual goal.

As of now, I've added large, influential organizations in a section at the top of the page, and then the top 50 countries in order of largest to smallest population. On each page load, the server checks to see when each headline was last updated. If it has been over 24 hours since the last update, the server will fetch a new headline from the source and save it to the database. The new headlines will appear on page reload.

You can hover over each entity name to see the full name (if abbreviated). Clicking on each entity name will take you to the source page so you can read more stories about the entity. Clicking on the headline will open the story in a new tab.

## Future Feature Ideas

- Finish adding all countries
- Add section for the world's largest, most influential corporations
- Add "our philosophy" tooltip at top on page
- Add map picture in country tooltip
- Add "new version available" button
- Diversify news sources
- Generate another article with button click

## Installation

[Click here](http://theDailyWorld.herokuapp.com/) to go to the site. Or, if you want to clone this repository, open your terminal and type:

```sh
git clone https://github.com/davidkuyk/theDailyWorld.git
cd theDailyWorld
```

## Scaffolding

```text
theDailyWorld
├── public
│   └── style.css
├── views
    └── index.ejs
├── server.js
├── package.json
├── package-lock.json
├── Procfile
├── LICENSE
└── README.md
```

## Bugs

If you have questions, feature requests or a bug you want to report, please click [here](https://github.com/davidkuyk/theDailyWorld/issues) to open an issue.

## Author

- [**David Kuyk**](https://davidkuyk.github.io/)

## License

Copyright (c) 2021 David Kuyk.

Usage is provided under the MIT License. See [LICENSE](https://github.com/davidkuyk/theDailyWorld/blob/main/LICENSE) for the full details.
