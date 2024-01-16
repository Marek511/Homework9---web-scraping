import requests
from bs4 import BeautifulSoup
import json

base_url = "http://quotes.toscrape.com"
quotes = []
authors = []


def get_quotes(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	quotes_div = soup.find_all('div', class_='quote')
	for quote_div in quotes_div:
		quote_text = quote_div.find('span', class_='text').text
		author_name = quote_div.find('small', class_='author').text
		tags = [tag.text for tag in quote_div.find_all('a', class_='tag')]

		quotes.append({
			'quote': quote_text,
			'author': author_name,
			'tags': tags
		})

		if author_name not in [author['name'] for author in authors]:
			authors.append({
				'name': author_name,
				'quotes': [quote_text]
			})
		else:
			authors_index = [author['name'] for author in authors].index(author_name)
			authors[authors_index]['quotes'].append(quote_text)

	next_page = soup.find('li', class_='next')
	if next_page:
		next_page_url = base_url + next_page.find('a')['href']
		get_quotes(next_page_url)


get_quotes(base_url)

with open('quotes.json', 'w') as quotes_file:
	json.dump(quotes, quotes_file, indent=4)

with open('authors.json', 'w') as authors_file:
	json.dump(authors, authors_file, indent=4)
