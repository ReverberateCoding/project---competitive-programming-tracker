import requests
from bs4 import BeautifulSoup
import json

categories = [
    "Dynamic-Programming"
]

atcoder_problem_categories = dict()

for category in categories:
    url = f"https://atcoder-tags.herokuapp.com/tag_search/{category}"
    response = requests.get(url=url)

    soup = BeautifulSoup(response.text, "html.parser")

    elements = soup.find_all("strong")
    elements.pop(0)
    atcoder_problem_categories[category] = list()
    for element in elements:
        print(element)
        atcoder_problem_categories[category].append(str(element.text))
print(atcoder_problem_categories)

with open("atcoder_tags.json", "w") as file:
    json.dump(atcoder_problem_categories, file)