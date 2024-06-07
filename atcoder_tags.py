import requests
from bs4 import BeautifulSoup
import json

links = [
    #DP
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Simple-DP",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Restore-DP",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/String-DP",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Section-DP",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Digit-DP",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Tree-DP",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Every-Direction-DP",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Bit-DP",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Probability-DP",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Expected-Value-DP",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Insert-DP",
    #"https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Link-DP",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Inline-DP",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Matrix-Power",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/CHT",
    #"https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Monge-DP",
    #"https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Alien-DP",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Kitamasa",
    "https://atcoder-tags.herokuapp.com/tags/Dynamic-Programming/Other",

    #GRAPH
    "https://atcoder-tags.herokuapp.com/tags/Graph/Shortest-Path",
    "https://atcoder-tags.herokuapp.com/tags/Graph/Minimum-Spanning-Tree",
    "https://atcoder-tags.herokuapp.com/tags/Graph/LCA",
    "https://atcoder-tags.herokuapp.com/tags/Graph/Strongly-Connected-Components",
    "https://atcoder-tags.herokuapp.com/tags/Graph/Topological-Sort",
    "https://atcoder-tags.herokuapp.com/tags/Graph/Euler-Tour",
    "https://atcoder-tags.herokuapp.com/tags/Graph/Euler-Path-and-Hamilton-Path",
    "https://atcoder-tags.herokuapp.com/tags/Graph/HL-Decomposition",
    "https://atcoder-tags.herokuapp.com/tags/Graph/Centroid-Decomposition",
    "https://atcoder-tags.herokuapp.com/tags/Graph/Check-Tree",
    "https://atcoder-tags.herokuapp.com/tags/Graph/Kirchhoff",
    "https://atcoder-tags.herokuapp.com/tags/Graph/Two-Edge-Connected-Components",
    "https://atcoder-tags.herokuapp.com/tags/Graph/Bi-Connected-Components",
    #"https://atcoder-tags.herokuapp.com/tags/Graph/Cycle-Basis",
    "https://atcoder-tags.herokuapp.com/tags/Graph/dfs-tree",
    #"https://atcoder-tags.herokuapp.com/tags/Graph/Erdesh",
    "https://atcoder-tags.herokuapp.com/tags/Graph/Other",

    #DATA STRUCTURES
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/stack",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/queue",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/set",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/map",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/deque",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/multiset",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/priority_queue",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/Union-Find-Tree",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/BIT",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/Segment-Tree",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/Lazy-Segment-Tree",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/Sparse-Table",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/WaveletMatrix",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/Persistent-Data-Structures",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/Balanced-Tree",
    "https://atcoder-tags.herokuapp.com/tags/Data-Structure/Other"
]

atcoder_problem_categories = dict()

#Categories
for link in links:
    path_components = link.split('/')[::-1][0:2][::-1]
    category = path_components[0]
    sub_category = path_components[1]
    print(path_components)
    if category in atcoder_problem_categories.keys():
        atcoder_problem_categories[category][sub_category] = list()
    else:
        atcoder_problem_categories[category] = dict()
        atcoder_problem_categories[category][sub_category] = list()
#Sub Categories
for link in links:

    path_components = link.split('/')[::-1][0:2][::-1]
    category = path_components[0]
    sub_category = path_components[1]

    response = requests.get(url=link)

    soup = BeautifulSoup(response.text, "html.parser")

    elements = soup.find_all("strong")
    elements.pop(0)
    for element in elements:
        print(element)
        atcoder_problem_categories[category][sub_category].append(str(element.text))
#print(atcoder_problem_categories)

with open("atcoder_tags.json", "w") as file:
    json.dump(atcoder_problem_categories, file)
