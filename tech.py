import re
import requests
from bs4 import BeautifulSoup

# Define a list of technologies along with their regex patterns
technologies = [
    ("jQuery", r'jquery.*\.js'),
    ("React.js", r'react.*\.js'),
    ("WooCommerce", r'woocommerce'),
    ("Bootstrap", r'bootstrap.*\.css'),
    ("Shopify", r'shopify'),
    ("Next.js", r'./_next/[^>]*' ),
    ("MaterializeCSS", r'materialize.*\.css'),
    ("PHP", r'\.php'),
    ("Python", r'python'),
    ("Google Maps", r'./maps')
]
def detect_technology(url, regex_pattern):
    if re.search(regex_pattern, str(soup)):
        return True
#web =['https://goldsgym.in/','https://www.flipkart.com','https://dropsuite.com/','https://www.bang-olufsen.com/en/us','https://www.macrumors.com/','https://venturebeat.com/','https://mashable.com','https://thenextweb.com','https://wired.com','https://facebook.com','https://ecommercefastlane.com','https://instagram.com','https://x.com','https://spotify.com','https://cuvette.tech','https://leden.dansstudiopetitplie.com','https://pythonanywhere.com','https://aircare.acer.com','https://spiritanimal.info','https://kaspersky.com','https://shop.singletracks.com/','https://studio.jane.com','https://woocommerce.com/','https://www.amc.edu.in/','https://materializecss.com/showcase.html','http://srkrec.ac.in','https://asana.com/','https://www.awwwards.com/sites/undersight-co','https://flo.io','https://graphically.io','https://www.airbnb.co.in/?locale=en&_set_bev_on_new_domain=1692797282_ZmU4Yzg3OGE4ZTE3']

'''
for maunal input replace web=input()

if you want more no of sites to be checked use web=list[map(input().split())]
'''
website=input('enter the website:')
response = requests.get(website)
soup = BeautifulSoup(response.text, 'html.parser')
for tech_name, pattern in technologies:
    if detect_technology(website,pattern):
        print(f"Technology: {tech_name}")
        print(f"-Regex pattern: {pattern}")
