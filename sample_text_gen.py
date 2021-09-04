from bs4 import BeautifulSoup
import requests

URL = "https://lists.wordreference.com/show/top-2000-english-words.1/"
r = requests.get(url=URL).text

soup = BeautifulSoup(r, 'html.parser')
# print(soup.prettify())

# Scrape 2000 English Words for our sample text
word_list = [word.text.lower() for word in soup.find_all(class_="termEditable")]
# print(word_list)

# Use the range of word_list to add a string to each word
for i in range(0, len(word_list)):
    word_list[i] += " \n"

header = ['word']

with open('sample_text.txt', 'w', encoding='UTF-8', newline='') as f:
    f.writelines(word_list)

