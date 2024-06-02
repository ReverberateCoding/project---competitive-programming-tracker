from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from models import question, problem_set

def atcoder_propagate(problem_sets):
    #Accesing the URL
    url = "https://kenkoooo.com/atcoder/#/table/Reverberate"


    driver = webdriver.Chrome()

    driver.get(url)

    wait = WebDriverWait(driver, 10)
    #wait.until(EC.presence_of_element_located((By.CLASS_NAME, "table-problem")))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "table-success")))
    html = driver.page_source

    driver.quit()

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
