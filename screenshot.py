from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from textToSpeech import count_comments
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 20)


df = pd.read_csv('database.csv')
post_url = df.iloc[-1, 2]
post_id = df.iloc[-1, 0]

driver.get(post_url)
time.sleep(10)


def takeScreenshot(xpath_name, post_id, filename):
    elementByID = driver.find_element(By.XPATH, xpath_name)
    screenshotPath = f'assets/{post_id}/{filename}.png'
    elementByID.screenshot(screenshotPath)


XPathBodyTitle = f"//*[@id='t3_{post_id}']"
image = takeScreenshot(XPathBodyTitle, post_id, 0)

comment_df = pd.read_csv(f'assets/{post_id}/comments.csv')
count = 1

for i in (comment_df.loc[:count_comments-2, 'ID']):
    XPathComment = f'//*[@id="comment-tree"]/shreddit-comment[{count}]'
    image = takeScreenshot(XPathComment, post_id, count)
    count += 1
