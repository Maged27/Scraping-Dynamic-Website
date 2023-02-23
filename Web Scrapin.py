import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd 


Website = "https://www.adamchoi.co.uk/goalsbyhalf/detailed"
driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get(Website)
driver.maximize_window()

all_matches_button = driver.find_element("xpath", '//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]').click()



dropdown = Select(driver.find_element(By.ID,"country"))
dropdown.select_by_visible_text("Spain")
time.sleep(4)

matches = driver.find_elements(By.TAG_NAME,'tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    home_team.append(match.find_element(By.XPATH,'./td[2]').text)
    score.append(match.find_element(By.XPATH,'./td[3]').text)
    away_team.append(match.find_element(By.XPATH,'./td[4]').text)
driver.quit()

df = pd.DataFrame({"date" : date, "home_team" : home_team, "score" : score , "away_team": away_team})
df.to_csv("football.csv", index= False) 
print(df)