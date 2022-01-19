
import requests
import time
import os
import winsound
import webbrowser
from twilio.rest import Client
from bs4 import BeautifulSoup

status = '"Instock":true'
account_sid = ""            #Twilio account sid
auth_token = ""             #Twilio auth token
client = Client(account_sid, auth_token)
duration = 2000     #Beep duration in milliseconds
freq = 440      #Hz


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

def message(url):
    client.api.account.messages.create(
            to="",                  #Phone Number
            from_="",               #Twilio number
            body="The item is instock at " + url)



# Newegg product urls
page1Url = "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-gaming-x-trio-10g/p/N82E16814137597?nm_mc=AFC-RAN-COM&cm_mmc=AFC-RAN-COM&utm_medium=affiliates&utm_source=afc-NowInStock&AFFID=1709054&AFFNAME=NowInStock&ACRID=1&ASUBID=nismain&ASID=&ranMID=44583&ranEAID=1709054&ranSiteID=AKGBlS8SPlM-Y3G17C6Ch2Y8enBJ48lhUg&Item=N82E16814137597"
page2Url = "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g-oc/p/N82E16814137598?Description=msi%203080&cm_re=msi_3080-_-14-137-598-_-Product&quicklink=true"
page3Url = "https://www.newegg.com/asus-geforce-rtx-3080-tuf-rtx3080-o10g-gaming/p/N82E16814126452?Description=3080&cm_re=3080-_-14-126-452-_-Product&quicklink=true"
page4Url = "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g/p/N82E16814137600?Description=3080&cm_re=3080-_-14-137-600-_-Product"
page5Url = "https://www.newegg.com/asus-geforce-rtx-3080-tuf-rtx3080-10g-gaming/p/N82E16814126453?Description=3080&cm_re=3080-_-14-126-453-_-Product"
page6Url = "https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3895-kr/p/N82E16814487519?Description=3080&cm_re=3080-_-14-487-519-_-Product"
page7Url = "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-10gd/p/N82E16814932329?Description=3080&cm_re=3080-_-14-932-329-_-Product"
page8Url = "https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3883-kr/p/N82E16814487521?Description=3080&cm_re=3080-_-14-487-521-_-Product"
productUrls = [page1Url, page2Url, page3Url, page4Url, page5Url, page6Url, page7Url, page8Url]

while True:
    for productUrl in productUrls:
        source = requests.get(productUrl, headers=headers).text
        if status not in source:
            print('Item is sold out')
        else:
            print(productUrl)
            webbrowser.open(productUrl)
            winsound.Beep(freq, duration)
            message(productUrl)
        

    time.sleep(15)
    os.system('cls')



