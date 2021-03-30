from bs4 import BeautifulSoup
import requests
import re

inputStr = str(input("Enter string to find in URLs: "))
def web1(input):
    url = "https://www.nytimes.com/section/technology"

    page = BeautifulSoup(requests.get(url).text, "lxml")
    matchingArray=[]
    for headlines in page.find_all(re.compile('^h[1-6]$')):
        matchingArray.append(headlines.text.strip())

    i=0
    while(i<len(matchingArray)):
        if input in matchingArray[i]:
            print("Thread-1: ",matchingArray[i])
        i=i+1


def web2(input):
    url = "https://www.theguardian.com/us/technology"

    page = BeautifulSoup(requests.get(url).text, "lxml")
    matchingArray=[]

    for headlines in page.find_all(re.compile('^h[1-6]$')):
       matchingArray.append(headlines.text.strip())

    i=0
    while(i<len(matchingArray)):
        if input in matchingArray[i]:
            print("Thread-2: ",matchingArray[i])
        i=i+1

def web3(input):
    url = "https://news.ycombinator.com/"

    page = BeautifulSoup(requests.get(url).text, "lxml")
    matchingArray=[]

    for headlines in page.find_all(class_="title"):
        for loop in headlines.find_all(class_="storylink"):
            matchingArray.append(loop.text.strip())
     #       print(loop.text.strip())

    i=0
    while(i<len(matchingArray)):
        if input in matchingArray[i]:
            print("Thread-3: ",matchingArray[i])
        i=i+1


from threading import  Thread

t1= Thread(target=web1, args=(inputStr,))
t2= Thread(target=web2, args=(inputStr,))
t3= Thread(target=web3, args=(inputStr,))

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()