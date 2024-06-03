#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from models import question, problem_set
from playwright.sync_api import sync_playwright

def fetch_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        # Wait for the content to load
        page.wait_for_load_state('networkidle')
        content = page.content()
        browser.close()
        return content

def atcoder_propagate(problem_sets, username):
    #Accesing the URL
    url = f"https://kenkoooo.com/atcoder/#/table/{username}"
    html = fetch_html(url=url)
    soup = BeautifulSoup(html,'html.parser')

    niggas = soup.find_all(class_="table-success")

    contests = soup.find_all("tr")
    #Adding all problems to problemset
    for j, contest in enumerate(contests):
        if j == 0:
            continue
        children = contest.children
        contest_element = None
        question_elements = list()
        for i, child in enumerate(children):
            if i == 0:
                contest_element = child
            else:
                question_elements.append(child)
        problem_sets.append(problem_set(contest_element=contest_element,question_elements=question_elements, judge="AtCoder"))
