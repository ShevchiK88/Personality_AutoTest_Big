from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time



# Cоздаем директорию для сохранения
# При успешном создании возвращает путь dir
# location- где будет располагаться папка ["/Users/Vitalii/Desktop"]
# directory_name- название самой папки    ["ScreenShots"]
# test_devise- имя папки с именем девайса куда будем сохранять ["Iphone 5"]
def MakeDirectory(location,directory_name, test_device):
    try:
        direct = "way"
        direct = location+"/"+directory_name+"/" + test_device
        os.makedirs(direct)
        return str(direct)
    except OSError:
        print("Создать директорию %s не удалось или она уже существует" %direct)
        return str(direct)

# Создание скриншотов
# directory- путь, можно получить из функции MakeDirectory в виде переменой
# или прописать путь самому к РЕАЛЬНО существующей директории
# devise- имя устройства, записываеться в название файла скриншота
# page- имя страницы, записываеться в название файла скриншота
def MakeScreenshot(directory ,devise, page):
    try:
        driver.save_screenshot(directory+"/" + devise+ "_" + page + "_screenshot.png")
    except Exception:
        print("Не удалось зоздать скриншот"+directory+"/" + devise+ "_" + page + "_screenshot.png")

# Поиск и взаимодействие с элементом через selector
def FindAndClick_selector(selector):
    try:
        element = driver.find_element_by_css_selector(str(selector))
        element.click()
        time.sleep(2)
    except Exception:
        print("Элемент не найден")

# Поиск и взаимодействие с элементом через xpath
def FindAndClick_xpath(xpath):
    try:
        element = driver.find_element_by_xpath(str(xpath))
        element.click()
        time.sleep(0.2)
    except Exception:
        print("Элемент не найден ", xpath)
        return False

# Поиск элемента через xpath и получение его полных координат
# Возвращает словарь с перечнем всех координат
#
#    x,y------------x1,y
#      |             |
#      |             |
#   x,y1------------x1,y1
#
# для получение значений координат  x/y_up/low_left/right_angle
def ElementCoordinatesAndDimensionsXpath(xpath):
    try:
        element = driver.find_element_by_xpath(str(xpath))
        element_location = element.location
        element_size = element.size

        x = element_location.get('x')
        y = element_location.get('y')
        h = element_size.get('height')
        w = element_size.get('width')
        x1 = x + w
        y1 = y + h

        element_value = {'x_up_left_angle': x, "y_up_left_angle": y,
                         'x_low_left_angle': x, "y_low_left_angle": y1,
                         'x_up_right_angle': x1, "y_up_right_angle": y,
                         'x_low_right_angle': x1, "y_low_right_angle": y1}

        return element_value
    except Exception:
        print("Не удалось получить координаты и размеры элемента ", xpath)
        return False

# В функцию передаються словари координат верхнего и нижнего элемента веб страницы,
# Проверяеться их пересечения
# При пересичении возвращает True
def ColisionTopBottom (coordinates_top, coordinates_bottom ):
    try:
        if coordinates_top.get('y_low_left_angle') > coordinates_bottom.get('y_up_left_angle'):
            return True
        else:
            return False

    except Exception:
        print("Colision Top Bottom Dont work")

# В функцию передаються словари координат левого и правого элемента веб страницы,
# Проверяеться их пересечения
# При пересичении возвращает True
def ColisionLeftRight (coordinates_left, coordinates_right ):
    try:
        if coordinates_left.get('x_up_right_angle') > coordinates_right.get('x_up_left_angle'):
            return True
        else:
            return False
    except Exception:
        print("Colision Left Right don't work")

# Cоздаем эмуляцию устройства в Хроме
test_device = "iPhone 5"
mobile_emulation = {"deviceName": test_device}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

#необходимо вставить путь к драйверу
driver = webdriver.Chrome('/Users/Vitalii/Desktop/chromedriver', desired_capabilities=chrome_options.to_capabilities())

# Cоздание директории
local="/Users/Vitalii/Desktop"
dir = MakeDirectory(local, 'ScreenShots', test_device)

# Открытие страницы в браузере
driver.get('https://mbti-web-50ca5.web.app')
time.sleep(2)

# Start_page
print("\nStart Page-------------------------------------------------------------------------------------")
header = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[1]')
img = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/span/img')
title = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/h2')
text = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/p')
letsgo = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/button')

# check colision
if ColisionTopBottom(header, img): MakeScreenshot(dir,test_device,"Start_Page")
if ColisionTopBottom(img, title): MakeScreenshot(dir,test_device,"Start_Page")
if ColisionTopBottom(title, text): MakeScreenshot(dir,test_device,"Start_Page")
if ColisionTopBottom(text, letsgo): MakeScreenshot(dir,test_device,"Start_Page")

print("header", header,
      "\n img  ", img,
      "\ntitle ", title,
      "\n text ", text,
      "\n  go  ", letsgo,)

FindAndClick_xpath('//*[@id="root"]/div/button')

# CheckBox
print("\nCheck box---------------------------------------------------------------------------------------")

header = ElementCoordinatesAndDimensionsXpath('/html/body/div[3]/div/div/div[1]')
body = ElementCoordinatesAndDimensionsXpath('/html/body/div[3]/div/div/div[2]')
footer = ElementCoordinatesAndDimensionsXpath('/html/body/div[3]/div/div/div[3]')

# check colision
if ColisionTopBottom(header, body): MakeScreenshot(dir,test_device,"Start_Page_Check_Box")
if ColisionTopBottom(body, footer): MakeScreenshot(dir,test_device,"Start_Page_Check_Box")

print("header", header,
      "\n body ", body,
      "\nfooter", footer,)

# Okay
FindAndClick_xpath('/html/body/div[3]/div/div/div[2]/input')
FindAndClick_xpath('/html/body/div[3]/div/div/div[3]/a')

# Question 30
for i in range(1, 31, 1):

    print("\nQuestion",i,"------------------------------------------------------------------------------------")

    if i == 1 or i == 29:
        header = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[1]')
        text = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/p')
        v1 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/div[1]')
        v2 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/div[2]')
        v3 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/div[3]')
        next = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/a')

        #colision
        if ColisionTopBottom(header, text): MakeScreenshot(dir,test_device,"Q_"+str(i))
        if ColisionTopBottom(text, v1): MakeScreenshot(dir,test_device,"Q_"+str(i))
        if ColisionTopBottom(v1, v2): MakeScreenshot(dir,test_device,"Q_"+str(i))
        if ColisionTopBottom(v2, v3): MakeScreenshot(dir,test_device,"Q_"+str(i))
        if ColisionTopBottom(v3, next): MakeScreenshot(dir,test_device,"Q_"+str(i))

        print("header",header,
              "\n text ",text,
              "\n  v1  ",v1,
              "\n  v2  ",v2,
              "\n  v3  ",v3,
              "\n next ",next)

        FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[1]')
        FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[2]')
        FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[3]')
        FindAndClick_xpath('//*[@id="root"]/div/a')
    elif i == 2:
        time.sleep(1)

        header = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[1]')
        text = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/p')
        b1 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/p[1]')
        b2 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/p[2]')
        b3 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/p[3]')
        b4 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/p[4]')
        b5 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/p[5]')
        b6 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/p[6]')
        next = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/a')

        # Colision
        if ColisionTopBottom(header, text): print("col")

        if ColisionTopBottom(text, b1): print("col")
        if ColisionTopBottom(text, b2): print("col")
        if ColisionTopBottom(text, b3): print("col")

        if ColisionTopBottom(b1, b5): print("col")
        if ColisionTopBottom(b2, b4): print("col")
        if ColisionTopBottom(b3, b6): print("col")
        if ColisionTopBottom(b4, b6): print("col")
        if ColisionTopBottom(b5, next): print("col")
        if ColisionTopBottom(b6, next): print("col")

        if ColisionLeftRight(b1, b2): print("col")
        if ColisionLeftRight(b1, b4): print("col")
        if ColisionLeftRight(b5, b2): print("col")
        if ColisionLeftRight(b5, b4): print("col")
        if ColisionLeftRight(b2, b3): print("col")
        if ColisionLeftRight(b4, b3): print("col")

        print("header", header,
              "\n text ", text,
              "\n  b1  ", b1,
              "\n  b2  ", b2,
              "\n  b3  ", b3,
              "\n  b4  ", b4,
              "\n  b5  ", b5,
              "\n  b6  ", b6,
              "\n next ", next)

        FindAndClick_xpath('//*[@id="root"]/div/div[3]/p[1]')
        FindAndClick_xpath('//*[@id="root"]/div/div[3]/p[2]')
        FindAndClick_xpath('//*[@id="root"]/div/div[3]/p[3]')
        FindAndClick_xpath('//*[@id="root"]/div/div[3]/p[4]')
        FindAndClick_xpath('//*[@id="root"]/div/div[3]/p[5]')
        FindAndClick_xpath('//*[@id="root"]/div/div[3]/p[6]')
        FindAndClick_xpath('//*[@id="root"]/div/a')
    elif i == 3 or i == 4 or i == 30:
        header = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[1]')
        text = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/p')
        v1 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/div[1]')
        v2 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/div[2]')
        v3 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/div[3]')
        v4 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/div[4]')
        next = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/a')

        # Colision
        if i == 4:
            if ColisionTopBottom(header, text): print("col")
            if ColisionTopBottom(text, v1): print("col")
            if ColisionTopBottom(text, v2): print("col")
            if ColisionTopBottom(v1, v3): print("col")
            if ColisionTopBottom(v2, v4): print("col")
            if ColisionTopBottom(v2, next): print("col")
            if ColisionTopBottom(v4, next): print("col")
            if ColisionLeftRight(v1, v2): print("col")
            if ColisionLeftRight(v3, v4): print("col")
        else:
            if ColisionTopBottom(header, text): print("col")
            if ColisionTopBottom(text, v1): print("col")
            if ColisionTopBottom(v1, v2): print("col")
            if ColisionTopBottom(v2, v3): print("col")
            if ColisionTopBottom(v3, v4): print("col")
            if ColisionTopBottom(v4, next): print("col")

        print("header", header,
              "\n text ", text,
              "\n  v1  ", v1,
              "\n  v2  ", v2,
              "\n  v3  ", v3,
              "\n  v4  ", v4,
              "\n next ", next)

        FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[1]')
        FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[2]')
        FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[3]')
        FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[4]')
        FindAndClick_xpath('//*[@id="root"]/div/a')
    elif i == 10 or i == 16 or i == 23:

        header = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[1]')
        board_img = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/img')
        board_desc = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/p[1]')
        board_writer = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/p[2]')
        next = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/a')

        # Colision
        if ColisionTopBottom(header, board_img): MakeScreenshot(dir,test_device,"Q_"+str(i))
        if ColisionTopBottom(board_img, board_desc): MakeScreenshot(dir,test_device,"Q_"+str(i))
        if ColisionTopBottom(board_desc, board_writer): MakeScreenshot(dir,test_device,"Q_"+str(i))
        if ColisionTopBottom(board_writer, next): MakeScreenshot(dir,test_device,"Q_"+str(i))

        print("header", header,
               "\n bimg ",board_img,
               "\n bdes ",board_desc,
               "\n bwri ",board_writer,
               "\n next ", next)

        FindAndClick_xpath('//*[@id="root"]/div/a')
    elif i == 28:
        header = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[1]')
        del_img = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/img[1]')
        del_text = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/p')
        next = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/a')

        # Colision
        if ColisionTopBottom(header, del_img): MakeScreenshot(dir,test_device,"Q_"+str(i))
        if ColisionTopBottom(del_img, del_text): MakeScreenshot(dir,test_device,"Q_"+str(i))
        if ColisionTopBottom(del_text, next): MakeScreenshot(dir,test_device,"Q_"+str(i))

        print("header", header,
              "\n dimg ",del_img,
              "\n dtex ",del_text,
              "\n next ", next)

        FindAndClick_xpath('//*[@id="root"]/div/a')
    else:
        header = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[1]')
        text = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/p')
        v1 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/div[1]')
        v2 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]/div[2]')
        next = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/a')

        # Colision
        if ColisionTopBottom(header, text): MakeScreenshot(dir,test_device,"Q_"+str(i))
        if ColisionTopBottom(text, v1): MakeScreenshot(dir,test_device,"Q_"+str(i))
        if ColisionTopBottom(v1, v2): MakeScreenshot(dir,test_device,"Q_"+str(i))
        if ColisionTopBottom(v2, next): MakeScreenshot(dir,test_device,"Q_"+str(i))

        print("header", header,
              "\n text ", text,
              "\n  v1  ", v1,
              "\n  v2  ", v2,
              "\n next ", next)

        FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[1]')
        FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[2]')
        FindAndClick_xpath('//*[@id="root"]/div/a')

# Email
time.sleep(15)
print("\nEmail page----------------------------------------------------------------------------------------")
header = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[1]')
img = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/img[1]')
title = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/h1')
text = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/p')
input_box = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/input')
button = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/a')

# colision
if ColisionTopBottom(header, img): MakeScreenshot(dir,test_device,"Email")
if ColisionTopBottom(img, title): MakeScreenshot(dir,test_device,"Email")
if ColisionTopBottom(title, text): MakeScreenshot(dir,test_device,"Email")
if ColisionTopBottom(text, input_box): MakeScreenshot(dir,test_device,"Email")
if ColisionTopBottom(input_box, button): MakeScreenshot(dir,test_device,"Email")

print("header", header,
      "\n img  ", img,
      "\ntitle ", title,
      "\n text ", text,
      "\n in   ", input_box,
      "\nbutton", button)

element = driver.find_element_by_css_selector("#root > div > input").send_keys("example@gmail.com")
FindAndClick_selector("#root > div > a")

#Get My Plan
print("\nGet my plan---------------------------------------------------------------------------------------")
header = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[1]')
personality = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[2]')
progress = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[3]')
img_l = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/img[1]')
text_l = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/p')
img_pr1 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/img[2]')
text_love = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/h2[1]')
img_cust = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[4]/div/img[1]')
lr_cust = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[5]')
title_cust = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/h2[2]')
img_pr2 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/img[3]')
text_bfit = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/h2[3]')
img_bfit = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/img[4]')
text_persona = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/h2[4]')
img_persona = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[6]/div/img[2]')
lr_persona = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[7]')
career_tab = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[8]')
text_faq = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/h2[5]')
faq_1 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[9]/div[1]/div[1]')
faq_2 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[9]/div[2]/div[1]')
faq_3 = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[9]/div[3]/div[1]')
img_money = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/img[5]')
img_report = ElementCoordinatesAndDimensionsXpath('//*[@id="getplan"]')
b_report = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/div[10]/a')
img_sec_pay = ElementCoordinatesAndDimensionsXpath('//*[@id="root"]/div/img[6]')

if ColisionTopBottom(header, personality): MakeScreenshot(dir,test_device,"Header_Octagon")
if ColisionTopBottom(personality, progress): MakeScreenshot(dir,test_device,"Octagon_Potential")
if ColisionTopBottom(progress, img_l): MakeScreenshot(dir,test_device,"Potential_Lightbulb_img")
if ColisionTopBottom(img_l, text_l): MakeScreenshot(dir,test_device,"Lightbulb_img_Lightbulb_text")
if ColisionTopBottom(text_l, img_pr1): MakeScreenshot(dir,test_device,"Lightbulb_text_WhatsInYouPerRepo")
if ColisionTopBottom(img_pr1, text_love): MakeScreenshot(dir,test_device,"WhatsInYouPerRepo_OurCustLoveUs")
if ColisionTopBottom(text_love, img_cust): MakeScreenshot(dir,test_device,"OurCustLoveUs_CustScrollPhoto")
if ColisionTopBottom(img_cust, lr_cust): MakeScreenshot(dir,test_device,"CustScrollPhoto_LeftRightCust")
if ColisionTopBottom(lr_cust, title_cust): MakeScreenshot(dir,test_device,"LeftRightCust_GetTheBusiness")
if ColisionTopBottom(title_cust, img_pr2): MakeScreenshot(dir,test_device,"GetTheBusiness_GTBimg")
if ColisionTopBottom(img_pr2, text_bfit): MakeScreenshot(dir,test_device,"GTBimg_BenefitsYouGet")
if ColisionTopBottom(text_bfit, img_bfit): MakeScreenshot(dir,test_device,"BenefitsYouGet_BYGimg")
if ColisionTopBottom(img_bfit, text_persona): MakeScreenshot(dir,test_device,"BYGimg_RockStarsText")
if ColisionTopBottom(text_persona, img_persona): MakeScreenshot(dir,test_device,"RockStarsText_RockStarsImg")
if ColisionTopBottom(img_persona, lr_persona): MakeScreenshot(dir,test_device,"RockStarsImg_LeftRightRS")
if ColisionTopBottom(lr_persona, career_tab): MakeScreenshot(dir,test_device,"LeftRightRS_CareerTab")
if ColisionTopBottom(career_tab, text_faq): MakeScreenshot(dir,test_device,"CareerTab_FAQtitle")
if ColisionTopBottom(text_faq, faq_1): MakeScreenshot(dir,test_device,"FAQtitile_FAQ1")
if ColisionTopBottom(faq_1, faq_2): MakeScreenshot(dir,test_device,"FAQ1_FAQ2")
if ColisionTopBottom(faq_2, faq_3): MakeScreenshot(dir,test_device,"FAQ2_FAQ3")
if ColisionTopBottom(faq_3, img_money): MakeScreenshot(dir,test_device,"FAQ3_MoneyBack")
if ColisionTopBottom(img_money, img_report): MakeScreenshot(dir,test_device,"MoneyBack_BuyRepo")
if ColisionTopBottom(img_report, b_report): MakeScreenshot(dir,test_device,"BuyRepo_BuyRepoButton")
if ColisionTopBottom(b_report, img_sec_pay): MakeScreenshot(dir,test_device,"BuyRepoButton_SecurityPayments")

print(         "header", header,
              "\nPerso  ", personality,
              "\nProgr  ", progress,
              "\nLampa  ", img_l,
              "\nL_tex  ", text_l,
              "\nPR_im  ", img_pr1,
              "\nlovet  ", text_love,
              "\nC_img ", img_cust,
              "\nC_L/r  ", lr_cust,
              "\ntit_c  ", title_cust,
              "\nper_i  ", img_pr2,
              "\nbenif  ", text_bfit,
              "\nimgbe  ", img_bfit,
              "\nP_text ", text_persona,
              "\nP_img  ", img_persona,
              "\nP_L/R  ", lr_persona,
              "\nC_tab  ", career_tab,
              "\n  FAQ  ", text_faq,
              "\n faq1  ", faq_1,
              "\n faq2  ", faq_2,
              "\n faq3  ", faq_3,
              "\nQarnt  ", img_money,
              "\nRep_i  ", img_report,
              "\nRep_b  ", b_report,
              "\nVisa   ", img_sec_pay,)


#now potential
FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[1]/p[2]')
FindAndClick_xpath('//*[@id="root"]/div/div[3]/div[1]/p[1]')

#left right customers
scroll = driver.find_element_by_xpath('//*[@id="root"]/div/h2[1]').location_once_scrolled_into_view
time.sleep(2)
FindAndClick_xpath('//*[@id="root"]/div/div[5]/img[2]')
FindAndClick_xpath('//*[@id="root"]/div/div[5]/img[2]')
FindAndClick_xpath('//*[@id="root"]/div/div[5]/img[2]')
FindAndClick_xpath('//*[@id="root"]/div/div[5]/img[2]')
FindAndClick_xpath('//*[@id="root"]/div/div[5]/img[1]')
FindAndClick_xpath('//*[@id="root"]/div/div[5]/img[1]')
FindAndClick_xpath('//*[@id="root"]/div/div[5]/img[1]')
FindAndClick_xpath('//*[@id="root"]/div/div[5]/img[1]')

#left right persona
scroll = driver.find_element_by_xpath('//*[@id="root"]/div/h2[4]').location_once_scrolled_into_view
time.sleep(2)
scroll = driver.find_element_by_xpath('//*[@id="root"]/div/h2[4]').location_once_scrolled_into_view
time.sleep(2)
FindAndClick_xpath('//*[@id="root"]/div/div[7]/img[2]')
FindAndClick_xpath('//*[@id="root"]/div/div[7]/img[2]')
FindAndClick_xpath('//*[@id="root"]/div/div[7]/img[2]')
FindAndClick_xpath('//*[@id="root"]/div/div[7]/img[2]')
FindAndClick_xpath('//*[@id="root"]/div/div[7]/img[1]')
FindAndClick_xpath('//*[@id="root"]/div/div[7]/img[1]')
FindAndClick_xpath('//*[@id="root"]/div/div[7]/img[1]')
FindAndClick_xpath('//*[@id="root"]/div/div[7]/img[1]')

#career tab Carreer Relationship Strength Read_More
scroll = driver.find_element_by_xpath('//*[@id="root"]/div/div[7]').location_once_scrolled_into_view
time.sleep(2)
FindAndClick_xpath('//*[@id="uncontrolled-tab-example-tab-profile"]')
FindAndClick_xpath('//*[@id="uncontrolled-tab-example-tab-contact"]')
FindAndClick_xpath('//*[@id="uncontrolled-tab-example-tab-home"]')

#FAQ
scroll = driver.find_element_by_xpath('//*[@id="root"]/div/h2[5]').location_once_scrolled_into_view
time.sleep(2)
FindAndClick_xpath('//*[@id="root"]/div/div[9]/div[1]/div[1]')
FindAndClick_xpath('//*[@id="root"]/div/div[9]/div[2]/div[1]')
FindAndClick_xpath('//*[@id="root"]/div/div[9]/div[3]/div[1]')

#Get my report
driver.find_element_by_tag_name('body').send_keys(Keys.END)
scroll = driver.find_element_by_xpath('//*[@id="root"]/div/img[6]').location_once_scrolled_into_view
driver.find_element_by_tag_name('body').send_keys(Keys.END)
MakeScreenshot(dir,test_device,"Taimer")
FindAndClick_xpath('//*[@id="root"]/div/div[10]/a')

#Pay Data
time.sleep(1)
MakeScreenshot(dir,test_device,"CreditCardPage_checkout")

#Закрытие браузера
time.sleep(3)
driver.quit()
