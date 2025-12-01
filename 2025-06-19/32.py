from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from random import randint
o = Options()
o.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=o)
# browser.get('https://www.qa-practice.com/elements/button/simple')
# browser.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')


browser.get('https://app.onlinetestpad.com')

# click_button = browser.find_element(By.ID,'submit-id-submit')
# click_button = browser.find_element(By.ID,'txtEmail').click()
click_button = browser.find_element(By.XPATH,'//input[@id="txtEmail"]')
sleep(2)
click_button.click()
click_button.send_keys("airfox@mail.ru")

click_button = browser.find_element(By.XPATH,'//input[@id="txtPassword"]')
sleep(2)
click_button.click()
click_button.send_keys("!QAZ2wsx")


click_button = browser.find_element(By.XPATH,'//button[@type="submit"]')
sleep(3)
click_button.click()



def qz(q1,a1,a2,a3,a4,a5,url,id):
    # открыть тест
    click_button=browser.get(url)

    sleep(1)
    # click_button.click()
    sleep(1)
    # id="qid_70218675"
    qid1=f'//*[@id="{id}"]/div/div[2]/test-question-view/div/div/div[2]/test-question-view-rbchk/div/div/div/div[1]/label/i'
    qid2=f'//*[@id="{id}"]/div/div[1]/button[2]/span'
    click_button = browser.find_element(By.XPATH,qid1)
    sleep(1)
    click_button.click()
    sleep(1)

    # скопировали шаблон во второй
    click_button = browser.find_element(By.XPATH,qid2).click()


    sleep(1)
    click_button = browser.find_element(By.XPATH,'/html/body/popover-confirm-window/div/div[2]/div/div[1]/select')
    click_button.click()
    sleep(1)
    click_button.send_keys(Keys.NUMPAD2)
    click_button.send_keys(Keys.RETURN)


    click_button = browser.find_element(By.XPATH,'/html/body/popover-confirm-window/div/div[2]/div/div[2]/button')
    click_button.click()
    #конец копировани яшаблона во второй

    sleep(1)
    # tox-edit-area__iframe


    # iframe1 = browser.find_element(By.XPATH,'//iframe[@class="tox-edit-area__iframe"]')
    iframe1 = browser.find_element(By.XPATH,'//iframe[@id="mce_0_ifr"]')
    # browser.switch_to.frame(iframe1)

    iframe2 = browser.find_element(By.XPATH,'//iframe[@id="mce_2_ifr"]')
    iframe3 = browser.find_element(By.XPATH,'//iframe[@id="mce_3_ifr"]')
    iframe4 = browser.find_element(By.XPATH,'//iframe[@id="mce_4_ifr"]')
    iframe5 = browser.find_element(By.XPATH,'//iframe[@id="mce_5_ifr"]')
    iframe6 = browser.find_element(By.XPATH,'//iframe[@id="mce_6_ifr"]')
    save1 = browser.find_element(By.XPATH,'//*[@id="qid_0"]/div/test-question-edit/div/div/div[2]/button[2]')


    # browser.switch_to.frame(iframe2)

    browser.switch_to.frame(iframe1)


    # задание
    click_button = browser.find_element(By.XPATH,'//*[@id="tinymce" and @data-id="mce_0"]/child::p')
    click_button.click()

    click_button.send_keys(q1)

    # переход в главное
    browser.switch_to.default_content()

    browser.switch_to.frame(iframe2)
    click_button = browser.find_element(By.XPATH,'//*[@id="tinymce" and @data-id="mce_2"]/child::p')
    click_button.click()

    click_button.send_keys(a1)

    # переход в главное
    browser.switch_to.default_content()

    browser.switch_to.frame(iframe3)
    click_button = browser.find_element(By.XPATH,'//*[@id="tinymce" and @data-id="mce_3"]/child::p')
    click_button.click()

    click_button.send_keys(a2)


    # переход в главное
    browser.switch_to.default_content()

    browser.switch_to.frame(iframe4)
    click_button = browser.find_element(By.XPATH,'//*[@id="tinymce" and @data-id="mce_4"]/child::p')
    click_button.click()

    click_button.send_keys(a3)

    # переход в главное
    browser.switch_to.default_content()

    browser.switch_to.frame(iframe5)
    click_button = browser.find_element(By.XPATH,'//*[@id="tinymce" and @data-id="mce_5"]/child::p')
    click_button.click()

    click_button.send_keys(a4)


    # переход в главное
    browser.switch_to.default_content()

    browser.switch_to.frame(iframe6)
    click_button = browser.find_element(By.XPATH,'//*[@id="tinymce" and @data-id="mce_6"]/child::p')
    click_button.click()

    click_button.send_keys(a5)

    browser.switch_to.default_content()
    save1.click()

def get_id(url):
    # открыть тест
    print (url)
    # if url=="":
    #     url='https://app.onlinetestpad.com/tests/gcyoftlygy2so/questions'
    #     # url='https://app.onlinetestpad.com/tests/qlw7rhgfd6clo/questions'
    click_button = browser.get(url)
    sleep(3)
    click_button = browser.find_element(By.XPATH, '//div[starts-with(@id, "qid_")]')
    id=click_button.get_attribute("id")
    if len(id)>0:
        return id
    else:
        return 0


    #

    # sleep(1)
    # # click_button.click()
    # sleep(1)
    # id = "qid_70218675"
    # qid1 = f'//*[@id="{id}"]/div/div[2]/test-question-view/div/div/div[2]/test-question-view-rbchk/div/div/div/div[1]/label/i'
    # qid2 = f'//*[@id="{id}"]/div/div[1]/button[2]/span'
    # click_button = browser.find_element(By.XPATH, qid1)
    # sleep(1)
    # click_button.click()
    # sleep(1)
    #
    # # скопировали шаблон во второй
    # click_button = browser.find_element(By.XPATH, qid2).click()
    #
    # sleep(1)
    # click_button = browser.find_element(By.XPATH, '/html/body/popover-confirm-window/div/div[2]/div/div[1]/select')
    # click_button.click()
    # sleep(1)
    # click_button.send_keys(Keys.NUMPAD2)
    # click_button.send_keys(Keys.RETURN)
    #
    # click_button = browser.find_element(By.XPATH, '/html/body/popover-confirm-window/div/div[2]/div/div[2]/button')
    # click_button.click()
    # # конец копировани яшаблона во второй
    #
    # sleep(1)
    # # tox-edit-area__iframe
    #
    # # iframe1 = browser.find_element(By.XPATH,'//iframe[@class="tox-edit-area__iframe"]')
    # iframe1 = browser.find_element(By.XPATH, '//iframe[@id="mce_0_ifr"]')
    # # browser.switch_to.frame(iframe1)
    #
    # iframe2 = browser.find_element(By.XPATH, '//iframe[@id="mce_2_ifr"]')
    # iframe3 = browser.find_element(By.XPATH, '//iframe[@id="mce_3_ifr"]')
    # iframe4 = browser.find_element(By.XPATH, '//iframe[@id="mce_4_ifr"]')
    # iframe5 = browser.find_element(By.XPATH, '//iframe[@id="mce_5_ifr"]')
    # iframe6 = browser.find_element(By.XPATH, '//iframe[@id="mce_6_ifr"]')
    # save1 = browser.find_element(By.XPATH, '//*[@id="qid_0"]/div/test-question-edit/div/div/div[2]/button[2]')
    #
    # # browser.switch_to.frame(iframe2)
    #
    # browser.switch_to.frame(iframe1)
    #
    # # задание
    # click_button = browser.find_element(By.XPATH, '//*[@id="tinymce" and @data-id="mce_0"]/child::p')
    # click_button.click()
    #
    # click_button.send_keys(q1)
    #
    # # переход в главное
    # browser.switch_to.default_content()
    #
    # browser.switch_to.frame(iframe2)
    # click_button = browser.find_element(By.XPATH, '//*[@id="tinymce" and @data-id="mce_2"]/child::p')
    # click_button.click()
    #
    # click_button.send_keys(a1)
    #
    # # переход в главное
    # browser.switch_to.default_content()
    #
    # browser.switch_to.frame(iframe3)
    # click_button = browser.find_element(By.XPATH, '//*[@id="tinymce" and @data-id="mce_3"]/child::p')
    # click_button.click()
    #
    # click_button.send_keys(a2)
    #
    # # переход в главное
    # browser.switch_to.default_content()
    #
    # browser.switch_to.frame(iframe4)
    # click_button = browser.find_element(By.XPATH, '//*[@id="tinymce" and @data-id="mce_4"]/child::p')
    # click_button.click()
    #
    # click_button.send_keys(a3)
    #
    # # переход в главное
    # browser.switch_to.default_content()
    #
    # browser.switch_to.frame(iframe5)
    # click_button = browser.find_element(By.XPATH, '//*[@id="tinymce" and @data-id="mce_5"]/child::p')
    # click_button.click()
    #
    # click_button.send_keys(a4)
    #
    # # переход в главное
    # browser.switch_to.default_content()
    #
    # browser.switch_to.frame(iframe6)
    # click_button = browser.find_element(By.XPATH, '//*[@id="tinymce" and @data-id="mce_6"]/child::p')
    # click_button.click()
    #
    # click_button.send_keys(a5)
    #
    # browser.switch_to.default_content()
    # save1.click()

    # click_button = browser.find_element(By.XPATH,'/html/body/popover-confirm-window/div/div[2]/div/div[2]/button').click()
    # sleep(3)
    # click_button = browser.find_element(By.XPATH,'/html/body/popover-confirm-window/div/div[2]/div/div[1]/select')
    # click_button.click()


    # click_button.send_keys("!QAZ2wsx")

    # click_button = browser.find_element(By.XPATH,'//a[@class="nav-link" and contains(text(),"Тесты")]')
    # sleep(5)
    #

    # click_button = browser.find_element(By.CLASS_NAME,'p-4')
    # sleep(5)
    # link=browser.find_element(By.PARTIAL_LINK_TEXT,'/contact/')
    #
    # click_button = browser.find_element(By.CSS_SELECTOR,'input[class="btn btn-primary"]')
    # click_button = browser.find_element(By.CSS_SELECTOR,'input[href="/contact/"]')
    #
    # # <a href="/contact/">Contact</a>
    # click_button = browser.find_element(By.XPATH,'//input[@class="btn btn-primary"]')
    # //a[@href="/contact/"]
    # click_button = browser.find_element(By.XPATH,'//a[@href="/contact/"]')



    # ищет по классу и по тексту
    # click_button = browser.find_element(By.XPATH,'//label[@class="form-check-label" and contains(text(),"Select")]')

    # //label[@class="form-check-label" and contains(text(),"Select")]
    # //*[text()="Contact"]

    # sleep(5)
    # click_button.click()
    # # sleep(5)
    # # link.click()ё
    # sleep(5)

    # ищем тен footer после label class==
    # //label[@class=" form-label"]/following::footer




    # ищем див в родителском уровня 1
    # //label[@class=" form-label"]/ancestor::div[1]

    # ищем див в родителском уровня
    # //label[@class=" form-label"]/parent::div

    # ищем  всех родителей *
    # //label[@class=" form-label"]/parent::*

    # ищем всё выше
    # //label[@class=" form-label"]/preceding::*
    # содержащий content=
    # //label[@class=" form-label"]/preceding::*[@content]


# f=open("test_1.csv", encoding="utf8")
# s = f.readline()
# cnt = 0
#
#
# a=[]
# for s in f:
#     s = s.strip().replace('\xa0', ' ')
#     cnt += 1
#     m = s.split(';')
#     # print (cnt,len(m),m)
#     a.append(m)
# for i in range(450,500):
#     m=a[i]
#     q1 = f"{m[2]}\n{m[3]}"
#     a1 = m[4]
#     a2 = m[5]
#     a3 = m[6]
#     a4 = m[7]
#     a5 = m[8]
#     print(f"{i}\t{q1}\n,{a1},{a2},{a3},{a4},{a5}")
#     qz(q1,a1,a2,a3,a4,a5)
# url='https://app.onlinetestpad.com/tests/qlw7rhgfd6clo/questions'
# url='https://app.onlinetestpad.com/tests/gcyoftlygy2so/questions'
# url='https://app.onlinetestpad.com/tests/5au2ynt4of2hm/questions'
# print (url)
# print (get_id(url))

# urls="https://app.onlinetestpad.com/tests/tlgrp4gweay4k/questions,https://app.onlinetestpad.com/tests/crtt75ce3n5dk/questions,https://app.onlinetestpad.com/tests/iii54z3ivgc2o/questions,https://app.onlinetestpad.com/tests/2az6vqf3hzyia/questions,https://app.onlinetestpad.com/tests/hq35crdonbcyu/questions,https://app.onlinetestpad.com/tests/5edzanen5rggw/questions,https://app.onlinetestpad.com/tests/gec4fadcthtsi/questions,https://app.onlinetestpad.com/tests/ywlrwrl4wdjtk/questions"
urls="https://app.onlinetestpad.com/tests/anq63qdhseuic/questions,https://app.onlinetestpad.com/tests/ooprc262ey7oa/questions,https://app.onlinetestpad.com/tests/n6h43gphuvczs/questions,https://app.onlinetestpad.com/tests/6tdckq6zdufna/questions,https://app.onlinetestpad.com/tests/75fl3sa3crw3g/questions,https://app.onlinetestpad.com/tests/uk7yw4fjvvx5a/questions"
urls=list(urls.split(','))
urls=urls[::-1]
print (urls)

f=open("test_1.csv", encoding="utf8")
s = f.readline()
cnt = 0


a=[]
for s in f:
    s = s.strip().replace('\xa0', ' ')
    cnt += 1
    m = s.split(';')
    # print (cnt,len(m),m)
    a.append(m)

for u,url in enumerate(urls):
    id=get_id(url)

    for i in range(1000+u*50,1050+u*50):
        m=a[i]
        q1 = f"{m[2]}\n{m[3]}"
        a1 = m[4]
        a2 = m[5]
        a3 = m[6]
        a4 = m[7]
        a5 = m[8]
        print(f"{i}\t{id}\n{url}\n{q1},{a1},{a2},{a3},{a4},{a5}")
        qz(q1,a1,a2,a3,a4,a5,url,id)