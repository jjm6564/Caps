
#------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import text
import createJson
import time
import pinataAuto
#------------------------------------
#gvrlab05
#Graphics405!
#chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
driver = webdriver.Chrome('chromedriver.exe', options=options)

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
# driver = webdriver.Chrome(chrome_driver, options= chrome_options)
pinataUrl = "https://app.pinata.cloud/signin"


def movePage_Pinata():

    driver.get(pinataUrl)

    logIn_Pinata()
    upLoad()
   
    uploadFolder()
    
    
def logIn_Pinata():
    driver.implicitly_wait(3)
    driver.find_element_by_name('email').send_keys(text.email)
    driver.implicitly_wait(3)
    driver.find_element_by_name('password').send_keys(text.password)
    driver.find_element_by_class_name('mt-4').click()
    print("complete")
    

def upLoad():
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/button').click()
    print("+")

    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div/a[2]').click()
    print("file")

    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("input[type='file']").send_keys(r"C:/Users/mvr/Desktop/image/"+text.file_name) # 상대경로로 변경하기 사진 경로
    print("upLoad")

    driver.implicitly_wait(10)
    driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/button").click()
    
    print("upload complete")
    
    driver.implicitly_wait(30)
    while(1):
        try:
            copyPath()
            break
        except:
            print('로딩중..')
            time.sleep(1)
   
def copyPath():
    '''
    global ipfs 
    ipfs = driver.find_element_by_link_text(text.file_name).get_attribute('href')
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    ipfs_split= ipfs.split('/')
    ipfs = ipfs_split[4]
    ipfs = 'ipfs://'+ipfs

    text.ipfs = ipfs
    createJson.main()
    '''
    global ipfs 
    if(text.ipfs==""):
        ipfs = driver.find_element_by_link_text(text.file_name).get_attribute('href')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        ipfs_split= ipfs.split('/')
        ipfs = ipfs_split[4]
        ipfs = 'ipfs://'+ipfs
        text.ipfs = ipfs
        print(text.ipfs)
        createJson.main()
    else:
        ipfs = driver.find_element_by_link_text(text.NFTname).get_attribute('href')
        ipfs_split= ipfs.split('/')
        ipfs = ipfs_split[4]
        ipfs = 'ipfs://'+ipfs
        text.json_ipfs += ipfs+'/'
        print(text.json_ipfs)

def uploadFolder():
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/button').click()
    print("+")

    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div/a[1]').click()
    print('folder')

    driver.implicitly_wait(5)
    driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/button').click()
    print('select')

    pinataAuto.uploadPinataAutogui()
    #--upload

    driver.find_element_by_xpath('//*[@id="thresholdconfig"]').send_keys(text.NFTname)
    driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/button').click()
    while(1):
        try:
            copyPath()
            break
        except:
            print('cid추출중')
            time.sleep(3)
    #driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/button/text()').click()
    #driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/button/i').click()
    #여기서 json ipfs 추출하기


movePage_Pinata()
#uploadFolder()
#QmWj3vMLQg43Dp6nzSgMbRdVLE36euT57ro7RDAR2eGYZD