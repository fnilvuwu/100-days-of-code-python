from bs4 import BeautifulSoup
import requests
# with open("index.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())

# all_anchor_tag = soup.find_all(name="a")

# for tag in all_anchor_tag:
#     print(tag.get("href"))

response = requests.get("https://news.ycombinator.com/")
yc_web_site = response.text

soup = BeautifulSoup(yc_web_site, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


highest_upvote_index = article_upvotes.index(max(article_upvotes))

print(article_texts[highest_upvote_index])
print(article_links[highest_upvote_index])
print(max(article_upvotes))
