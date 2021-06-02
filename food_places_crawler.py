import requests as req
from bs4 import BeautifulSoup

#use requests to retrieve a website based on user search query e.g. input 'sg food places'
user_search=input("Search here...")
search_query_list=(user_search.strip()).split(' ')
search_link="https://www.google.com/search?q="+'+'.join(search_query_list)
search_page=req.get(search_link)
#use beautifulsoup to crawl through the web elements 
search_soup = BeautifulSoup(search_page.text, 'html.parser')
search_results = search_soup.find('div', id='search')

# and go to 'View all' button
for view_all in search_results.find('div', class_='ndElDd'): 
# ! AttributeError: 'NoneType' object has no attribute 'find', to resolve


    # request the URL of 'View all'
    for link in view_all.find('a'):
        food_places_page=req.get(link.get('href')) 
        # parse the page
        food_soup = BeautifulSoup(food_places_page.text, 'html.parser')
        # for all food places, retrieve the info like name, ratings, address
        for food_place in food_soup.find('div', id='search'):
            for food_info in food_place.find_all('div', class_='cXedhc uQ4NLd'): # filter text
                print(food_info.find('ellip').text)
                print(food_info.find('rllt__details').text)