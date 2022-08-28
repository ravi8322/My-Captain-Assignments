# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 11:16:36 2022

@author: RAVI TEJ
"""




import requests
from bs4 import BeautifulSoup
import pandas



oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_MAX=3
scraped_info_list=[]


for page_num in range(1, page_num_MAX):
    url = oyo_url + str(page_num_MAX)
    print("GET Request for: " + url)
    req = requests.get(url)
    content = req.content
    
    soup = BeautifulSoup(content, "html.parser")
    all_hotels = soup.find_all("div", {"class": "hotelCardListing"})
    print(all_hotels)
    
    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription__hotelName d-textEllipsis"}).text
        hotel_dict["address"] = hotel.find("span", {"class": "u-line--clamp-2"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "ListingPrice__finalPrice"}).text
        try:
            hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating__ratingSummary"}).text
        except AttributeError:
            hotel_dict["rating"] = None
            
        parent_amenities_element = hotel.find("div", {"class": "amenityWrapper"})
        
        amenities_list = []
        for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())
            
        hotel_dict["amenities"] = ', '.join(amenities_list[:-1])
        
        scraped_info_list.append(hotel_dict)
        

dataFrame = pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("Oyo.csv")