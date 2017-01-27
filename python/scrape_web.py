import requests
from bs4 import BeautifulSoup

url = "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Napa%2C+CA"
url_page_2 = url + '&page=' + str(2) + '&s=relevance'
r = requests.get(url)

def get_data_from_url(url, pages):
    r = requests.get(url)
    if pages > 1:
        url_page_2 = url + '&page=' + str(pages) + '&s=relevance'
    


soup = BeautifulSoup(r.content)
# print soup.prettify()

links = soup.find_all("a")

for link in links:
    h=link.get("href")
    # print  "<a href='%s'> %s </a>"  %(h, link.text )

div_class_info = soup.find_all("div", {"class": "info"})
# print div_class_info

for item in div_class_info:
        # print item.contents[0].text
        # print item.contents[1].text
        # print item.contents[1].text# 22:24 https://www.youtube.com/watch?v=3xQTJi2tqgk
        # print item.text, type(item.text) #type unicode
        # print len(item.contents)
        business_name = item.contents[0].find_all("a", {"class": "business-name"})[0].text
        # business_address = item.contents[1].find_all("p", {"class": "adr"})[0].text

        print "-" * 10
        print "\n", business_name
        # print business_address
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
