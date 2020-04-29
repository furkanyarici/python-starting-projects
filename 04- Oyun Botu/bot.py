from selenium import webdriver
import time
import threading
browser = webdriver.Firefox()
browser.get("https://tr.rivalregions.com/")


girisyap = browser.find_element_by_xpath("//*[@id='sa_add2']/div[2]/a[2]/div")

girisyap.click()

email = browser.find_element_by_xpath("//*[@id='identifierId']")
email.send_keys("furkanbeydegil@gmail.com")

ileri = browser.find_element_by_xpath("//*[@id='identifierNext']/span/span")

ileri.click()

time.sleep(10)
sifre = browser.find_element_by_name("password")

sifre.send_keys("furkan869")

sifre_next = browser.find_element_by_xpath("//*[@id='passwordNext']/span")

sifre_next.click()

time.sleep(10)

browser.execute_script("window.open('https://tr.rivalregions.com/#auction/all/' , 'new window')")

ihalepara = browser.find_element_by_xpath("//*[@id='auction_price_t']")
ihalebahis = browser.find_element_by_xpath("//*[@id='list_tbody']/tr/td[4]/div")
ihaleinput = browser.find_element_by_xpath("//*[@id='auction_input']/div[1]/input)
ihalebahis2 = browser.find_element_by_xpath("//*[@id='auction_make_bet']")

ihalebahis.click()
                                           
ihalepara.text = int(ihalepara.text)
if ( ihalepara.text < 1000000000 ) :
    ihalepara.text += 1000
    
    
    
    
