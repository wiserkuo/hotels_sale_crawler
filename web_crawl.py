# This Python file uses the following encoding: utf-8
import os, sys,time
import urllib.request
from optparse import OptionParser
from bs4 import BeautifulSoup
from selenium import webdriver
def usage():
	print (''' \033[92m	crawl from to get something. \n
	usage : python3 web_crawl.py [-g] [gameId]
 
	-h : help
	-g : gameId
     
	By Maras. \033[0m''')
	sys.exit()
     
#取得參數輸入
def get_parameters():
	global gameId
	gameId = None
	optp = OptionParser(add_help_option=False,epilog="web_crawl")
	optp.add_option("-g","--gameId",dest="gameId",help="-g Steam App Game ID")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	if opts.help:
		usage()
     
	if opts.gameId is not None:
		gameId = opts.gameId
     
    #開始
if __name__ == '__main__':
    if len(sys.argv) < 1:
        usage()
    get_parameters()
    url = None
    print("\njalan 1/26-29 x4 persons yuzawa")
    #if gameId is not None:
    url = "https://www.jalan.net/160000/LRG_160500/?screenId=UWW1402&distCd=01&idx=0&rootCd=04&stayYear=2019&stayMonth=1&stayDay=26&stayCount=3&roomCount=1&adultNum=4&roomCrack=400000&kenCd=160000&lrgCd=160500&mvTabFlg=1&vosFlg=2&activeSort=1"
    #else: 
    #print ('Please input -g or -h')
     
    if url is not None:
        #設置假的瀏覽器資訊
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
        req = urllib.request.Request(url = url,headers=headers)
        page = urllib.request.urlopen(req)
        contentBytes = page.read().decode('shift-jis', 'ignore')
        soup = BeautifulSoup(str(contentBytes), "html.parser")
    #    print(str(contentBytes))
        #soup = BeautifulSoup( str(contentBytes).encode('shift-jis'), fromEncoding="shift-jis"
        #soup = BeautifulSoup(contentBytes)
        matches = soup.find_all("a", { "class" : "s16_00 fb" })
        matches2 = soup.find_all("span", { "class" : "s11_66" })
        matches3 = soup.find_all("span", { "class" : "s16_F60b" })
        print(matches[2].string)
        #matches[0].string=matches[0].string.decode('utf-8')
        print(matches2[0].string);

        for i in range(len(matches)):
            print(matches[i].string)

        #for match in matches:
        #    print(match.string);
            #print(match2.string);

        #for match in matches2:
        #    print(match.string);    

    print("\njalan 2/6 yuzawa")
    #if gameId is not None:
    url = "https://www.jalan.net/170000/LRG_171400/SML_171408/?stayYear=2019&stayMonth=2&stayDay=6&stayCount=1&roomCount=1&adultNum=2&minPrice=0&maxPrice=999999&mealType=1&activeSort=1&contHideFlg=1&kenCd=170000&lrgCd=171400&smlCd=171408&distCd=01&roomCrack=200000&reShFlg=1"
    #else: 
    #print ('Please input -g or -h')
     
    if url is not None:
        #設置假的瀏覽器資訊
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
        req = urllib.request.Request(url = url,headers=headers)
        page = urllib.request.urlopen(req)
        contentBytes = page.read().decode('shift-jis', 'ignore')
        soup = BeautifulSoup(str(contentBytes), "html.parser")
    #    print(str(contentBytes))
        #soup = BeautifulSoup( str(contentBytes).encode('shift-jis'), fromEncoding="shift-jis"
        #soup = BeautifulSoup(contentBytes)
        matches = soup.find_all("a", { "class" : "s16_00 fb" })
        matches2 = soup.find_all("span", { "class" : "s11_66" })
        matches3 = soup.find_all("span", { "class" : "s16_F60b" })

        #matches[0].string=matches[0].string.decode('utf-8')
        print(matches3[0].string);
        for match in matches:
            print(match.string);
            #print(match2.string);

        #for match in matches2:
        #    print(match.string);    
    print("\njalan 2/7 yuzawa")
    url = "https://www.jalan.net/170000/LRG_171400/SML_171408/?stayYear=2019&stayMonth=2&stayDay=7&stayCount=1&roomCount=1&adultNum=2&minPrice=0&maxPrice=999999&mealType=1&activeSort=1&contHideFlg=1&kenCd=170000&lrgCd=171400&smlCd=171408&distCd=01&roomCrack=200000&reShFlg=1"
    #else: 
    #print ('Please input -g or -h')
     
    if url is not None:
    	#設置假的瀏覽器資訊
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
        req = urllib.request.Request(url = url,headers=headers)
        page = urllib.request.urlopen(req)
        contentBytes = page.read().decode('shift-jis', 'ignore')
        soup = BeautifulSoup(str(contentBytes), "html.parser")
    #    print(str(contentBytes))
        #soup = BeautifulSoup( str(contentBytes).encode('shift-jis'), fromEncoding="shift-jis"
        #soup = BeautifulSoup(contentBytes)
        matches = soup.find_all("a", { "class" : "s16_00 fb" })
        matches2 = soup.find_all("span", { "class" : "s11_66" })
        matches3 = soup.find_all("span", { "class" : "s16_F60b" })

        #matches[0].string=matches[0].string.decode('utf-8')
        print(matches3[0].string);
        for match in matches:
            print(match.string);
            #print(match2.string);

        #for match in matches2:
        #    print(match.string);    
    print("\njalan 2/7 fuji lake")
    url = " https://www.jalan.net/150000/LRG_150600/SML_150602/?stayYear=2019&stayMonth=2&stayDay=7&stayCount=1&roomCount=1&adultNum=2&minPrice=0&maxPrice=999999&mealType=1&activeSort=1&contHideFlg=1&kenCd=150000&lrgCd=150600&smlCd=150602&distCd=01&roomCrack=200000&reShFlg=1&mvTabFlg=0&listId=4&screenId=UWW1402"
    if url is not None:
        #設置假的瀏覽器資訊
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
        req = urllib.request.Request(url = url,headers=headers)
        page = urllib.request.urlopen(req)
        contentBytes = page.read().decode('shift-jis', 'ignore')
        soup = BeautifulSoup(str(contentBytes), "html.parser")
    #    print(str(contentBytes))
        #soup = BeautifulSoup( str(contentBytes).encode('shift-jis'), fromEncoding="shift-jis"
        #soup = BeautifulSoup(contentBytes)
        matches = soup.find_all("a", { "class" : "s16_00 fb" })
        matches2 = soup.find_all("span", { "class" : "s11_66" })
        matches3 = soup.find_all("span", { "class" : "s16_F60b" })
        #matches[0].string=matches[0].string.decode('utf-8')
        print(matches3[0].string);
        for match in matches:
            print(match.string);
            #print(match.string);
    print("\njalan 2/8 fuji lake") 
    url = " https://www.jalan.net/150000/LRG_150600/SML_150602/?stayYear=2019&stayMonth=2&stayDay=8&stayCount=1&roomCount=1&adultNum=2&minPrice=0&maxPrice=999999&mealType=1&activeSort=1&contHideFlg=1&kenCd=150000&lrgCd=150600&smlCd=150602&distCd=01&roomCrack=200000&reShFlg=1&mvTabFlg=0&listId=4&screenId=UWW1402"
    if url is not None:
        #設置假的瀏覽器資訊
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
        req = urllib.request.Request(url = url,headers=headers)
        page = urllib.request.urlopen(req)
        contentBytes = page.read().decode('shift-jis', 'ignore')
        soup = BeautifulSoup(str(contentBytes), "html.parser")
    #    print(str(contentBytes))
        #soup = BeautifulSoup( str(contentBytes).encode('shift-jis'), fromEncoding="shift-jis"
        #soup = BeautifulSoup(contentBytes)
        matches = soup.find_all("a", { "class" : "s16_00 fb" })
        matches2 = soup.find_all("span", { "class" : "s11_66" })
        matches3 = soup.find_all("span", { "class" : "s16_F60b" })
        #matches[0].string=matches[0].string.decode('utf-8')
        print(matches3[0].string);
        for match in matches:
            print(match.string);
            #print(match.string);
    print("\nagoda 2/8 fuji lake")

    url = "https://www.agoda.com/zh-tw/pages/agoda/default/DestinationSearchResult.aspx?city=247771&languageId=20&userId=4b0b5e8a-7f50-4b6e-9790-b3b16a0b0d06&pageTypeId=103&origin=TW&locale=zh-TW&cid=1618670&tag=323699e6-7c3a-c519-85e3-8ac1c1f1eb8f&gclid=CjwKCAjwyrvaBRACEiwAcyuzRBGTZ6W851NUUbDD2VNmM30AaJV55KhLa_iy7PQmEiaXJTQvPh1SLhoCOW8QAvD_BwE&aid=82361&currencyCode=JPY&htmlLanguage=zh-tw&cultureInfoName=zh-TW&ckuid=4b0b5e8a-7f50-4b6e-9790-b3b16a0b0d06&prid=0&checkIn=2019-02-08&checkOut=2019-02-09&rooms=1&adults=2&children=0&priceCur=JPY&los=1&textToSearch=%E5%AF%8C%E5%A3%AB%E6%B2%B3%E5%8F%A3%E6%B9%96&hotelArea=242206&productType=-1&roomOffers=78322&sort=priceLowToHigh"
   
    driver = webdriver.Firefox()
    driver.get(url)
    print(driver.title)
    #time.sleep(3)
    #elem_searchboxbackdrop = driver.find_element_by_css_selector(".SearchboxBackdrop")
    time.sleep(1)
    elem_calendaralert =driver.find_element_by_css_selector(".AlertMessage__close")
    elem_calendaralert.click()
    #driver.execute_script("window.scrollTo(0, Y)") 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, (document.body.scrollHeight*2)/4);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, (document.body.scrollHeight*3)/4);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    contentBytes=driver.page_source
    driver.quit()
    if url is not None:
        #設置假的瀏覽器資訊
        #headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
        #req = urllib.request.Request(url = url,headers=headers)
        #time.sleep(3)
        #page = urllib.request.urlopen(req)
        #contentBytes = page.read().decode('utf-8', 'ignore')
        soup = BeautifulSoup(str(contentBytes), "html.parser")
        #print(str(contentBytes))
        #soup = BeautifulSoup( str(contentBytes).encode('shift-jis'), fromEncoding="shift-jis"
        #soup = BeautifulSoup(contentBytes)
        matches = soup.find_all("h3", { "class" : "hotel-name" })
        #matches2 = soup.find_all("span", { "class" : "price soft-red" })
        #matches[0].string=matches[0].string.decode('utf-8')
        for match in matches:
            print(match.string);

    print("\nagoda 2/7 yuzawa")
    url = "https://www.agoda.com/zh-tw/pages/agoda/default/DestinationSearchResult.aspx?asq=u2qcKLxwzRU5NDuxJ0kOF462uCg8qYNhnPhCTwnX%2BMZgr6w414KUo9Wt0ERI57djncbzTLOPBjT84OgAAKXmu4x92HCpRxs78zavyKc31gwv636%2BnKnEMgaiNgNdVgIh88061MyBFl2V0zy389SldIWVvnXUD7orlEK%2FusG2VlltLd3PNpyf6ftBl5MCuYUPtV3isswlap%2BgP3Wk4ekrZA%3D%3D&city=106278&tick=636692413341&languageId=20&userId=aa53ca34-0193-4227-bb50-09b62f7bc3f4&pageTypeId=103&origin=TW&locale=zh-TW&cid=-1&aid=130243&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&ckuid=aa53ca34-0193-4227-bb50-09b62f7bc3f4&prid=0&checkIn=2019-02-07&checkOut=2019-02-08&rooms=1&adults=2&children=0&priceCur=TWD&los=1&textToSearch=%E6%B9%AF%E6%BE%A4&productType=-1&sort=priceLowToHigh"
    driver = webdriver.Firefox()
    driver.get(url)
    print(driver.title)
    #time.sleep(3)
    #elem_searchboxbackdrop = driver.find_element_by_css_selector(".SearchboxBackdrop")
    time.sleep(1)
    #elem_calendaralert =driver.find_element_by_css_selector(".AlertMessage__close")
    #elem_calendaralert.click()
    #driver.execute_script("window.scrollTo(0, Y)") 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, (document.body.scrollHeight*2)/4);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, (document.body.scrollHeight*3)/4);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    contentBytes=driver.page_source
    driver.quit()
    if url is not None:
        #設置假的瀏覽器資訊
        #headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
        #req = urllib.request.Request(url = url,headers=headers)
        #time.sleep(3)
        #page = urllib.request.urlopen(req)
        #contentBytes = page.read().decode('utf-8', 'ignore')
        soup = BeautifulSoup(str(contentBytes), "html.parser")
        #print(str(contentBytes))
        #soup = BeautifulSoup( str(contentBytes).encode('shift-jis'), fromEncoding="shift-jis"
        #soup = BeautifulSoup(contentBytes)
        matches = soup.find_all("h3", { "class" : "hotel-name" })
        #matches2 = soup.find_all("span", { "class" : "price soft-red" })
        #matches[0].string=matches[0].string.decode('utf-8')
        for match in matches:
            print(match.string);