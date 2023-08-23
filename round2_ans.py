import re
import requests
from bs4 import BeautifulSoup

# Define a list of technologies along with their regex patterns
technologies = [
    ("jQuery", r'\/jquery.*\.js'),
    ("React.js", r'react.*\.js'),
    ("WooCommerce", r'woocommerce'),
    ("Bootstrap", r'bootstrap.*\.css'),
    ("Shopify", r'shopify'),
    ("Next.js", r'next.*\.js'),
    ("MaterializeCSS", r'materialize.*\.css'),
    ("PHP", r'\.php'),
    ("Python", r'python'),
    ("Google Maps", r'googleapis\.com\/maps')
]

def detect_technology(url, regex_pattern):
    if re.search(regex_pattern, str(soup)):
        return True

website =input("enter the website:")
response = requests.get(website)
soup = BeautifulSoup(response.text, 'html.parser')
for tech_name, pattern in technologies:
     if detect_technology(website,pattern):
        print(f"{ct}.Technology: {tech_name}")
        print(f"-Regex pattern: {pattern}")
        print(f"sample website:{website}")
