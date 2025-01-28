import time

from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By

response=requests.get(url="https://appbrewery.github.io/Zillow-Clone/")

soup=BeautifulSoup(response.text,"html.parser")
lista=soup.select(selector="ul li a")
anchors=[i.get("href") for i in lista]
print(anchors)

listp=soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")
prices=[i.getText().strip("+/mo") for i in listp]
print(prices)

listd=soup.find_all(name="address")
addresses=[i.getText().replace("\n", "").replace("|", "").strip() for i in listd]
print(addresses)



from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/17vpbKBn3PoUzT_061TpX2L67A-v5wCA1Gofyv771HoE/viewform?edit_requested=true")

a=driver.find_element(By.XPATH,"//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
p=driver.find_element(By.XPATH,"//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
l=driver.find_element(By.XPATH,"//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
s=driver.find_element(By.XPATH,"//*[@id=\"mG61Hd\"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span")


for i in range(len(addresses)):
    a = driver.find_element(By.XPATH,
                            "//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    p = driver.find_element(By.XPATH,
                            "//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    l = driver.find_element(By.XPATH,
                            "//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    s = driver.find_element(By.XPATH, "//*[@id=\"mG61Hd\"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    a.send_keys(addresses[i])
    p.send_keys(prices[i])
    l.send_keys(anchors[i])
    s.click()
    print(f"Submitted: {addresses[i]}, {prices[i]}, {anchors[i]}")
    time.sleep(3)
    driver.get(
        "https://docs.google.com/forms/d/17vpbKBn3PoUzT_061TpX2L67A-v5wCA1Gofyv771HoE/viewform?edit_requested=true")

    #a2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    #a2.click()
    time.sleep(3)



print("finished")
driver.close()
