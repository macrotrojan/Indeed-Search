from typing import Container
import requests
from bs4 import BeautifulSoup
from requests.api import get
from termcolor import colored,cprint


def Ascii_Art():
    cprint("""
     ▄▄▄██▀▀▀▒█████   ▄▄▄▄        ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ 
   ▒██  ▒██▒  ██▒▓█████▄    ▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒
   ░██  ▒██░  ██▒▒██▒ ▄██   ░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░
▓██▄██▓ ▒██   ██░▒██░█▀       ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ 
 ▓███▒  ░ ████▓▒░░▓█  ▀█▓   ▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓
 ▒▓▒▒░  ░ ▒░▒░▒░ ░▒▓███▀▒   ▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒
 ▒ ░▒░    ░ ▒ ▒░ ▒░▒   ░    ░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░
 ░ ░ ░  ░ ░ ░ ▒   ░    ░    ░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░
 ░   ░      ░ ░   ░               ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░
                       ░                                      ░                

                       --Made By @MalwareBum On instagram
    
    """, "green")





Query = input("What Job Do You Want To Search For:")
location = input("Location:")

URL = "https://www.indeed.com/jobs?q="+Query+"&l="+location+""
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("td", id="resultsCol")

job_elements = results.find_all("div" , class_="slider_item")
a =+ 0


Ascii_Art()
for job_element in job_elements:
    titles = job_element.find("span")
    title = job_element.find("div", class_="new topLeft holisticNewBlue desktop")
    location = job_element.find("div", class_="companyLocation")
    payment = job_element.find("span", class_="salary-snippet")
    link = job_element.find()
    print("█"*21, "Results", "█"*21, "\n")
    cprint(titles.text, "green")
    cprint(location.text, "blue")
    if payment == None:
        cprint("No Payment Shown", "red")
    if payment != None:
        cprint(payment.text, "yellow")
    print("="*50, "\n")