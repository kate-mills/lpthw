from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
# set tree equal to ( from html get the fromstring function and call it with the content from page )
tree = html.fromstring(page.content) # html.fromstring implicity expects bytes as input so we have to use page.content rather than page.text


# This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
prices = tree.xpath('//span[@class="item-price"]/text()')

print 'Buyers: ', buyers
print 'Prices: ', prices

for person in buyers:
    print person
