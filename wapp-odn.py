import time
import sys
from selenium import webdriver
from plyer import notification

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
time.sleep(5)
confirm = input("Done? (Y/N) : ")

if confirm == "Y" or confirm == "y":
    print("Program is starting...")
    txt = "Unknown"
    newtxt = txt

    while True:
        time.sleep(1)
        state = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/header')
        stateString = state.text
        
        if 'online' in stateString:
            txtcon = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span')
            newtxt = txtcon.text
            if txt != newtxt:
                txt = newtxt
                notification.notify(
                    title = f"{txt} is ONLINE",
                    message = f"Start a conversation with {txt}. Best of Luck!",
                    app_icon = "icon_online.ico",
                    timeout = 72000
                )
                ctime = time.strftime("%H:%M:%S", time.localtime())
                print(f"{ctime} - {txt} is Online")

        else:
            txt = "Unknown"

else:
    sys.exit()