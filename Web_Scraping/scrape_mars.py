#!/usr/bin/env python
# coding: utf-8

# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd
from selenium import webdriver


def scrape():

        # ## NASA Mars News

        mars_news_url = "https://mars.nasa.gov/news"

        # Use Panda's `read_html` to parse the url
        mars_news_request = requests.get(mars_news_url)
        mars_news_request

        # Create BeautifulSoup object; parse with 'html.parser'
        news_soup = BeautifulSoup(mars_news_request.text, 'html.parser')

        news_title = news_soup.find('div', 'a', class_="content_title").text
        news_p = news_soup.find('div', class_="rollover_description_inner").text


        # ## JPL Mars Space Images - Featured Image

        executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
        browser = Browser('chrome', **executable_path)

        url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url_img)

        html = browser.html
        img_soup = BeautifulSoup(html, 'html.parser')

        base_img_url = "https://www.jpl.nasa.gov"
        img_url = img_soup.find("a", class_="button fancybox")["data-fancybox-href"]
        featured_img = (base_img_url + img_url)
        print (featured_img)


        # ## Mars Weather

        mars_weather_url = "https://twitter.com/marswxreport?lang=en)"

        # Use Panda's `read_html` to parse the url
        weather_request = requests.get(mars_weather_url)

        # Create BeautifulSoup object; parse with 'html.parser'
        weather_soup = BeautifulSoup(weather_request.text, 'html.parser')

        mars_weather= weather_soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text


        # ## Mars Facts

        mars_facts_url = "https://space-facts.com/mars/"

        facts_table = pd.read_html(mars_facts_url)
        facts_df = facts_table[0]
        facts_df.columns = ["Key", "Value"]
        mars_facts_df = facts_df.set_index(["Key"])
        mars_facts_df

        mars_html_table = mars_facts_df.to_html()
        mars_html_table = mars_html_table.replace("\n", "")
        mars_html_table


        # ## Mars Hemispheres

        mars_hemisp_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(mars_hemisp_url)

        html = browser.html
        hemispheres_soup = BeautifulSoup(html, 'html.parser')

        hemispheres = hemisphere_soup.find_all("div", class_="item")

        base_hem_img_url = "https://astrogeology.usgs.gov"

        hemisphere_image_urls = []

        for hemisphere in hemispheres:
            title = hemisphere.find("h3").text
            img_url = hemisphere.find("a")["href"]
            thumble_img_link = base_hem_img_url + img_url 

            browser.visit(thumble_img_link)
            html = browser.html
            full_img_soup=BeautifulSoup(html, "html.parser")
            downloads = full_img_soup.find("div", class_="downloads")
            image_url = downloads.find("a")["href"]
            hemisphere_image_urls.append({"title": title, "img_url": image_url})

        mars_data = {
            "News_Title": news_title,
            "News Paragraph": news_p,
            "Featured Image": featured_img,
            "Weather": mars_weather,
            "Hemisphere Images": hemisphere_image_urls
            }
            #print(mars_data)

        return mars_data


