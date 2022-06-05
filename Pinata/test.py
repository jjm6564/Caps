from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import text as text
import createJson as createJson
#gvrlab05
#Graphics405!
#chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)
pinataUrl = "https://app.pinata.cloud/signin"


def movePage_Pinata():

    driver.get(pinataUrl)


    logIn_Pinata()
    upLoad()

    copyPath()
    
    
def logIn_Pinata():
    driver.implicitly_wait(3)
    driver.find_element_by_name('email').send_keys(text.email)
    driver.implicitly_wait(3)
    driver.find_element_by_name('password').send_keys(text.password)
    driver.find_element_by_class_name('mt-4').click()
    print("complete")

def upLoad():
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/button').click()
    print("+")

    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/a[2]').click()
    print("file")

    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("input[type='file']").send_keys(r"C:/Users/mvr/Desktop/image/"+text.file_name)
    print("upLoad")

    driver.implicitly_wait(10)
    driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/button").click()
    
    print("upload complete")
    
    driver.implicitly_wait(30)
   
def copyPath():
    global ipfs 
    ipfs = driver.find_element_by_link_text(text.file_name).get_attribute('href')
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    ipfs_split= ipfs.split('/')
    ipfs = ipfs_split[4]
    ipfs = 'ipfs://'+ipfs
    text.ipfs = ipfs
    createJson.main()
    


movePage_Pinata()
#upLoad()
#copyPath()
#createJson.createJson()