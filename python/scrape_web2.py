import requests
from bs4 import BeautifulSoup

url = "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Napa%2C+CA"
next_url = url + '&page=' + str(2) + '&s=relevance'


r = requests.get(url)
r2 = requests.get(next_url)



soup = BeautifulSoup(r.content)
soup2 = BeautifulSoup(r2.content)
# print soup2.prettify()


info = soup.find_all("div", {"class": "info"})
info2 = soup2.find_all("div", {"class", "info"})

for item in info and info2:

    print "-" * 10
    business_name = item.contents[0].find_all("a", {"class": "business-name"})[0].text
    print business_name

    try:
        business_address = item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text
        business_city = item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text.replace(',', ' ')
        business_state = item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text
        business_zip = item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text
        print business_address
        print business_city, business_state, business_zip
    except:
        pass

    try:
        print item.contents[1].find_all("div", {"class": "primary"})[0].text
    except:
        pass
