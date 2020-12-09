import reply_voice as reply
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from speech_rec import rec_voice
import playsound

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

def wiki():
    global driver
    if (driver == 0):
        driver = webdriver.Chrome(PATH,options=chrome_options)
    else:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
    
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    
    playsound.playsound("sounds/wiki.mp3")
    search = driver.find_element_by_id("searchInput")
    search.send_keys(rec_voice())
    search.send_keys(Keys.ENTER)
    driver.find_element_by_class_name('searchmatch').click()


def youtubeplay():
    global driver
    
    if (driver == 0):
        driver = webdriver.Chrome(PATH,options=chrome_options)
    else:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        
    playsound.playsound('sounds/play.mp3')
    searchstr = rec_voice()
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
        print('already logged in')

def msg():
    global driver
    
    if (driver == 0):
        driver = webdriver.Chrome(PATH,options=chrome_options)
    else:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
    

    driver.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
    time.sleep(5)
    playsound.playsound("sounds/who.mp3")
    temp_rec = input('To? :   ')

    driver.find_element_by_name('to').send_keys(temp_rec)
    
    # set subject
    playsound.playsound("sounds/subject.mp3")
    subject = driver.find_element_by_name('subjectbox')
    sub = rec_voice()
    subject.send_keys(sub)
    # message 
    playsound.playsound("sounds/message.mp3")
    message = driver.find_element_by_id(':9g')
    voice_message = rec_voice()
    message.send_keys(voice_message)
    driver.find_element_by_id(':81').click()
    time.sleep(10)
    #driver.quit()
    
def whichfun():
    while True:
        rec = rec_voice()

        if rec=='play':
            youtubeplay()
            
        elif rec=='what day':
            whatday()
            
        elif rec=='date':
            whatdate()
            
        elif rec == 'wikipedia' or rec == 'Wikipedia':
            wiki()
            
        elif rec=='quit':
            playsound.playsound("sounds/bye.mp3")
            break
        else:
            print("sleeping")
            time.sleep(10)
        
whichfun()
#youtubeplay('toxicity')
#print(URL)
#youtubenext()




