from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

url = 'https://www.microcenter.com/search/search_results.aspx?N=&cat=&Ntt=3070+graphics+card&searchButton=search'

uClient = urlopen(url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

card_names = page_soup.findAll("div",{"class":"pDescription compressedNormal2"})

for company in card_names:
	company = card_names[0].a["data-brand"]

	graphics_cards = page_soup.findAll("div",{"class":"pDescription compressedNormal2"})
	gpuname = graphics_cards[0].a["data-name"]

	card_price = page_soup.findAll("div",{"class":"price"})
	item_price = card_price[0].text.strip()

	card_location = page_soup.findAll("div",{"class":"instore"})
	location = card_location[0].text.strip()

	card_stock = page_soup.findAll("div",{"class":"stock"})
	stock = card_stock[0].text.strip('" ",\n,\r')

	print("company: " + company)
	print("gpu_name: " + gpuname)
	print("item_price: " + item_price)
	print("location: " + location)
	print("stock: " + stock)
