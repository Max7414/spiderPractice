from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException, MoveTargetOutOfBoundsException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import streamlit
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://querycourse.ntust.edu.tw/querycourse/#/ClassSchedule')

actions = ActionChains(driver)
actions.move_by_offset(300, 300).click().perform()

wait = WebDriverWait(driver, 10)
elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "v-select__selections")))


def rm(x):
    return list(dict.fromkeys(x))


def d_show():
    element = elements[2]
    element.click()
    department_list = []
    for i in range(1, 12):
        try:
            D = driver.find_element(By.XPATH, '//*[@id="app"]/div[5]/div/div/div[{i}]/a/div/div'.format(i=i))
            time.sleep(1)
            department_list.append(D.text)
        except Exception as e:
            break
    for text in department_list:
        print(text)
    # actions.move_by_offset(300, 300).click().perform()


def FoS(sSel):
    if sSel:
        return
    element = elements[0]
    time.sleep(4)
    element.click()
    foS = driver.find_element(By.XPATH, '//*[@id="app"]/div[7]/div/div/div[2]/a/div/div')
    foS.click()


def College():
    element = elements[1]
    college = driver.find_element(By.XPATH, '//*[@id="app"]/div[6]/div/div/div[3]/a/div/div')
    element.click()

    College_list = []
    for i in range(1, 8):
        C = driver.find_element(By.XPATH, '//*[@id="app"]/div[6]/div/div/div[{i}]/a/div/div'.format(i=i))
        time.sleep(1)
        College_list.append(C.text)
    for text in College_list:
        print(text)

    college.click()


def Department(s):
    # element = elements[2]
    department = driver.find_element(By.XPATH, '//*[@id="app"]/div[5]/div/div/div[{s}]/a/div/div'.format(s=s))
    # element.click()
    department.click()


def selYears():
    element = elements[3]
    selYears = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div/div[2]/a/div/div')
    element.click()
    selYears.click()


def Years(sel):
    element = elements[4]
    Years = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div[{sel}]/a/div/div'.format(sel=sel))
    search = driver.find_element(By.XPATH, '//*[@id="app"]/div[8]/main/div/div/div[1]/div[6]/button/div')
    element.click()
    Years.click()
    search.click()


def showCourse():
    Courses = driver.find_element(By.TAG_NAME, 'tbody')
    time.sleep(1)
    Courses2 = Courses.find_elements(By.TAG_NAME, 'tr')
    print(Courses2)
    prefixes = ['M', 'T', 'W', 'R', 'F']
    number_range = range(1, 11)
    C_List = {}
    ForcedCourse = []
    NotForced = []
    for prefix in prefixes:
        for number in number_range:
            key = f'{prefix}{number}'
            C_List[key] = []

    for i in Courses2:
        print(i.text)
        if len(i.text.split()) > 3:
            if i.text.split()[3] == "必":
                ForcedCourse.append(i.text.split())
        else:
            NotForced.append(i.text.split())

    seen = set()

    unique_courses = []

    for course in ForcedCourse:
        if course[1] not in seen:
            unique_courses.append(course)
            seen.add(course[1])

    for course in unique_courses:
        print(course)
        if len(course)>6:
            print(course[6].split(','))
            for x in course[6].split(','):
                C_List[x].append(course[1])


    print(C_List)



    #for i in ForcedCourse:
        #if len(i) > 6:
            #print(i[6])
            #ttime.append(i[6])


FoS(1)
College()
d_show()
Department(1)
selYears()
Years(1)

showCourse()

time.sleep(100)

driver.quit()
