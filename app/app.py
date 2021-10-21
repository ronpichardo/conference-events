#!/usr/bin/env python3
from flask import Flask, render_template, request
from bs4 import BeautifulSoup as soup
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    try:
        link_results = djangocon()
        return render_template('index.html', results=link_results)
    except Exception as e:
        return render_template('index.html',results=f'<h3>Exception: {e}</h3>')

sites = []
def djangocon():
    req = requests.get('https://2021.djangocon.us')
    bs = soup(req.text, 'lxml')
    desc = bs.header
    
    title = "Djangocon"
    date = desc.strong.text
    link = desc.a['href']
    target = desc.a.text

    sites.append({ 'title': title, 'target': target, 'link': link, 'date': date })

    return sites


def atlantacode():
    req = requests.get('https://www.atlantacodecamp.com/2021')
    bs = soup(req.text, 'lxml')
    container = bs.find_all('div','description')
    desc = container[0].find_all('a')

    title = 'Atlanta CodeCamp 2021'
    for item in desc:
        href = item['href']
        if href.startswith('http'):
            pass
        else:
            href = 'https://www.atlantacodecamp.com' + href
        target = item.text
        sites.append({ 'title': title, 'target': target, 'link': href, 'date': 'tbd' })

    return 

def grab_links():
    get_res = []
    get_res.append(atlantacode())
    get_res.append(djangocon())

    return sites

if __name__ == '__main__':
    app.run()