from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time


# Поиск и взаимодействие с элементом через xpath
def FindAndClick_xpath(xpath):
    try:
        element = driver.find_element_by_xpath(str(xpath))
        element.click()
        time.sleep(0.2)
    except Exception:
        print("Элемент не найден ", xpath)
        return False

def FindAndClick_selector(selector):
    try:
        element = driver.find_element_by_css_selector(str(selector))
        element.click()
        time.sleep(0.2)
    except Exception:
        print("Элемент не найден")


Type_list_abbreviation = [
    "INFP" ,
    "INFJ" ,
    "ENFJ" ,
    "ENFP" ,
    "INTJ" ,
    "ENTJ" ,
    "ENTP" ,
    "INTP" ,
    "ESFJ" ,
    "ESFP" ,
    "ISFJ" ,
    "ISFP" ,
    "ESTJ" ,
    "ESTP" ,
    "ISTJ" ,
    "ISTP" ]

Type_list_transcript = [
    "Mediator",
    "Advocate",
    "Protagonist",
    "Campaigner",
    "Architect",
    "Commander",
    "Debater",
    "Logician",
    "Consul",
    "Entertainer",
    "Defender",
    "Adventurer",
    "Executive",
    "Entrepreneur",
    "Logistician",
    "Virtuoso"]

for i in range(0,len(Type_list_abbreviation),1):



    type_A = Type_list_abbreviation[i]
    type_T = Type_list_transcript[i]

    driver = webdriver.Chrome('/Users/Vitalii/Desktop/chromedriver')
    # Открытие страницы в браузере
    driver.get('https://mbti-web-50ca5--test-humjvp8v.web.app/')
    time.sleep(1)

    # print("\nStart Page-------------------------------------------------------------------------------------")
    FindAndClick_xpath('//*[@id="root"]/div/button')
    # print("\nCheck box---------------------------------------------------------------------------------------")
    time.sleep(1)
    FindAndClick_xpath('/html/body/div[3]/div/div/div[2]/input')
    FindAndClick_xpath('/html/body/div[3]/div/div/div[3]/a')

    # Question 30
    # E/I 7 12 17 21 26 Зеленый
    # S/N 5 9 14 19 24 Желтый
    # F/T 6 11 15 20 25 Синий
    # J/P 8 13 18 22 27 Красный

    # INFP	Mediator
    # INFJ	Advocate
    # ENFJ	Protagonist
    # ENFP	Campaigner
    # INTJ	Architect
    # ENTJ	Commander
    # ENTP	Debater
    # INTP	Logician
    # ESFJ	Consul
    # ESFP	Entertainer
    # ISFJ	Defender
    # ISFP	Adventurer
    # ESTJ	Executive
    # ESTP	Entrepreneur
    # ISTJ	Logistician
    # ISTP	Virtuoso

    for i in range(1, 31, 1):

        # print("\nQuestion",i,"------------------------------------------------------------------------------------")

        if i == 1 or i == 29:

            FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[3]')
            FindAndClick_xpath('//*[@id="root"]/div/a')

        elif i == 2:

            time.sleep(1)
            FindAndClick_xpath('//*[@id="root"]/div/div[3]/p[1]')
            FindAndClick_xpath('//*[@id="root"]/div/a')

        elif i == 3 or i == 4 or i == 30:

            FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[4]')
            FindAndClick_xpath('//*[@id="root"]/div/a')

        # Info_page
        elif i == 10 or i == 16 or i == 23 or i == 28:
            FindAndClick_xpath('//*[@id="root"]/div/a')

        else:

            if i == 7 or i == 12 or i == 17 or i == 21 or i == 26:

                if type_A[0] == "E":
                    FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[1]')
                    # print("E")
                    FindAndClick_xpath('//*[@id="root"]/div/a')

                if type_A[0] == "I":
                    FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[2]')
                    # print("I")
                    FindAndClick_xpath('//*[@id="root"]/div/a')

            if i == 5 or i == 9 or i == 14 or i == 19 or i == 24:
                if type_A[1] == "S":
                    FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[1]')
                    # print("S")
                    FindAndClick_xpath('//*[@id="root"]/div/a')

                if type_A[1] == "N":
                    FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[2]')
                    # print("N")
                    FindAndClick_xpath('//*[@id="root"]/div/a')

            if i == 6 or i == 20:
                if type_A[2] == "F":
                    FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[1]')
                    # print("F")
                    FindAndClick_xpath('//*[@id="root"]/div/a')

                if type_A[2] == "T":
                    FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[2]')
                    # print("T")
                    FindAndClick_xpath('//*[@id="root"]/div/a')

            if i == 11 or i == 15 or i == 25:
                if type_A[2] == "T":
                    FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[1]')
                    # print("F")
                    FindAndClick_xpath('//*[@id="root"]/div/a')

                if type_A[2] == "F":
                    FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[2]')
                    # print("T")
                    FindAndClick_xpath('//*[@id="root"]/div/a')

            if i == 8 or i == 18 or i == 22 or i == 27:
                if type_A[3] == "J":
                    FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[1]')
                    # print("J")
                    FindAndClick_xpath('//*[@id="root"]/div/a')

                if type_A[3] == "P":
                    FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[2]')
                    # print("P")
                    FindAndClick_xpath('//*[@id="root"]/div/a')

            if i == 13:
                if type_A[3] == "P":
                    FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[1]')
                    # print("J")
                    FindAndClick_xpath('//*[@id="root"]/div/a')

                if type_A[3] == "J":
                    FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[2]')
                    # print("P")
                    FindAndClick_xpath('//*[@id="root"]/div/a')

    # Email
    time.sleep(15)
    # print("\nEmail page----------------------------------------------------------------------------------------")

    element = driver.find_element_by_css_selector("#root > div > input").send_keys("shevchik769@gmail.com")
    FindAndClick_selector("#root > div > a")

    # Получение типа
    type_site = driver.find_element_by_css_selector('#root > div > div.personality > span > span > span').text

    if type_T != type_site:
        print("\tTest data: [",type_A,':',type_T,"]","\tSite data: [",type_site,"]", "\tStatus: FAILED!")
    else:
        print("\tTest data: [",type_A,':',type_T,"]","\tSite data: [",type_site,"]", "\tStatus: Pass!")



    # Закрытие браузера
    time.sleep(10)
    driver.quit()







