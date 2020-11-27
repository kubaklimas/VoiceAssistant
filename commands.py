import speech_recognition as sr
import reply_voice as reply
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


PATH = "C:\Program Files (x86)\chromedriver.exe"
CUR_URL = ""
TITLE = ""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless-false')
chrome_options.add_argument("--user-data-dir=chrome-data")  
driver = 0




def whatday():
    x = datetime.datetime.now()
    dayname = x.strftime("%A")
    wholereply = "Today is"+dayname
    reply.speak(wholereply)


def whatdate():
    today = datetime.date.today()
    d = today.strftime("%d %B %Y")
    wholereply = "Today is"+d
    reply.speak(wholereply)

def wiki(arg):
    global driver
    if (driver == 0):
        driver = webdriver.Chrome(PATH,options=chrome_options)
    else:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
    
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    search = driver.find_element_by_id("searchInput")
    search.send_keys(arg)
    search.send_keys(Keys.ENTER)


def youtubeplay(title):
    global driver
    
    if (driver == 0):
        driver = webdriver.Chrome(PATH,options=chrome_options)
    else:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])

    searchstr = str(title)
    driver.get("https://www.youtube.com/results?search_query="+searchstr)
    driver.find_element_by_id("video-title").click()


def mail():
    global driver
    
    MAIL = 'engproVoiceAssistant@gmail.com'
    #password = getpass("Your google password for user {} : ".format(MAIL))
    password = '1234voice'
    
    
    if (driver == 0):
        driver = webdriver.Chrome(PATH,options=chrome_options)
    else:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])

    try:
        #driver = webdriver.Chrome(PATH,options=chrome_options)
        driver.get("https://gmail.com")
        driver.find_element_by_link_text('Zaloguj się').click()
        driver.switch_to_window(driver.window_handles[0])
        #close first window with google info
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        #login page
        log = driver.find_element_by_id("identifierId")
        log.send_keys(MAIL)
        driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
        #wait for password screen
        time.sleep(3)
        driver.find_element_by_css_selector("input[type=password]").send_keys(password)
        driver.find_element_by_id('passwordNext').click()
    except:
        print('aready logged in')


    
def whichfun():
    while True:
        txt = int(input("Co robimy towarzyszu: "))
        if txt==1:
            youtubeplay('Fuck you bloody bastard bitch')
        elif txt==2:
            wiki('python') 
        else:
            break
        
whichfun()
#youtubeplay('toxicity')
#print(URL)
#youtubenext()




