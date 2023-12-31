from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pyperclip
import keyboard as kb
import time

# This whole code block is dedicated to getting the Latin and English forms of the words in the story.
driver = webdriver.Chrome()
driver.get(pyperclip.paste())
button = driver.find_element(By.XPATH, '/html/body/div[8]')
button.click()
time.sleep(0.1)
vtrev_div = driver.find_element(By.ID, "vtrev")
vtrev_html = vtrev_div.get_attribute("innerHTML")
html = vtrev_html
driver.quit()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', id='tab')
lat_texts = []
eng_texts = []

for row in table.find_all('tr'):
    lat_cell = row.find('td', class_='lat')
    eng_cell = row.find('td', class_='eng')

    if lat_cell and eng_cell:
        lat_texts.append(lat_cell.get_text(strip=True))
        eng_texts.append(eng_cell.get_text(strip=True))

# Set up our category lists
know = []
recog = []
unknown = []
discard = []

# Fill the specified column
def selectFill(target: list):
    for x in range(len(target)):
        kb.write(target[x])
        time.sleep(1)
        kb.press("down")
        time.sleep(1)
    kb.press("tab")
    time.sleep(1)
    for y in range(len(target)):
        kb.press("up")
        time.sleep(1)

# Makes sure that there are enough rows in the table to fit all vocab terms
def makeSpace():
    neededRows = max(len(know), len(recog), len(unknown))
    for i in range(neededRows-1):
        for i in range(3):
            kb.press("tab")
            time.sleep(0.01)
    time.sleep(0.1)
    for i in range(neededRows-1):
        kb.press("up")
        time.sleep(0.01)

# Fill all the columns
def fillAll():
    makeSpace()
    selectFill(know)
    selectFill(recog)
    selectFill(unknown)

# Take user input on their knowledge of the vocab word
def setCategory():
    time.sleep(0.1)
    while True:
        if kb.is_pressed("1"):
            return know
        if kb.is_pressed("2"):
            return recog
        if kb.is_pressed("3"):
            return unknown
        if kb.is_pressed("4"):
            return discard


# This is the main code block that runs through all the vocab words and places them in their respective categories
print("1 for know, 2 for recognize, 3 for don't know, 4 for discard")
print("")
for i in range(len(lat_texts)):
    print("")
    print("(" + str(i+1) + "/" + str(len(lat_texts)) + ")")
    print(lat_texts[i])
    currentEntry = lat_texts[i] + " - " + eng_texts[i]
    setCategory().append(currentEntry)
    kb.press("backspace")
    time.sleep(0.1)

fillAll()
