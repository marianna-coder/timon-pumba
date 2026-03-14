import datetime

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input [@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")
password = driver.find_element(By.XPATH, "//input [@id='password']")
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH, "//input [@id='login-button']")
button_login.click()
print("Click Login Button")

print(" Приветствуем вас в нашем интернет магазине!")
print( " Выбери один из следующих товаров и укажите его номер: 1-Sauce Labs Backpack ,  2- Sauce Labs Bike Light, 3-Sauce Labs Bolt T-Shirt, 4-Sauce Labs Fleece Jacket, 5-Sauce Labs Onesie, 6- Test.allTheThings() T-Shirt (Red)")
product= input()

try:
    product = int(input("Введите число от 1 до 6: "))
    if product < 1 or product > 6:
        print("Пожалуйста, введите число от 1 до 6.")
        print("До свидания. Будем рады увидеть вас в нашем магазине в следующий раз!")
        exit()
except ValueError:
    print("Это не число. Пожалуйста, введите цифру от 1 до 6.")
    print("До свидания. Будем рады увидеть вас в нашем магазине в следующий раз!")
    exit()
def cart_to_end(driver, value_product, value_price_product):
    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart.click()
    print("Enter Cart")

    """INFO CART PRODUCT """
    cart_product = driver.find_element(By.XPATH, "//*[@data-test= 'inventory-item-name']")
    value_cart_product = cart_product.text
    print(value_cart_product)

    assert value_product == value_cart_product
    print("INFO Cart Product 1 good")

    price_cart_product = driver.find_element(By.XPATH, "//*[@data-test= 'inventory-item-price']")
    value_price_cart_product = price_cart_product.text
    print(value_price_cart_product)

    assert value_price_product == value_price_cart_product
    print("INFO Cart price Product 1 good")

    button_checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
    button_checkout.click()
    print("Click checkout")

    """Select user info"""
    wait = WebDriverWait(driver, 10)
    first_name_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='first-name']")))
    first_name_input.send_keys("Marianna")
    print("Input first name")

    last_name_input = driver.find_element(By.XPATH, "//input[@id= 'last-name']")
    last_name_input.send_keys("Vaganova")
    print("Input last name")

    postal_code_input = driver.find_element(By.XPATH, "//input[@id= 'postal-code']")
    postal_code_input.send_keys(23748)
    print("Input postal code")

    button_continue = driver.find_element(By.XPATH, "//input[@id= 'continue']")
    button_continue.click()
    print("Click continue")

    """INFO finish PRODUCT """
    finish_product = driver.find_element(By.XPATH, "//*[@data-test= 'inventory-item-name']")
    value_finish_product= finish_product.text
    print(value_finish_product)

    assert value_product == value_finish_product
    print("INFO finish Product 1 good")

    price_finish_product = driver.find_element(By.XPATH, "//*[@data-test= 'inventory-item-price']")
    value_price_finish_product = price_finish_product.text
    print(value_price_finish_product)

    assert value_price_product == value_price_finish_product
    print("INFO finish price Product 1 good")

    summary_price = driver.find_element(By.XPATH, "//*[@data-test= 'subtotal-label']")
    value_summary_price = summary_price.text
    print(value_summary_price)

    item_total = "Item total: " + value_price_finish_product
    print(item_total)

    assert value_summary_price == item_total
    print("Total summary price good")

    """ Reset the cart"""
    button_finish = driver.find_element(By.XPATH, "//button[@id= 'finish']")
    button_finish.click()
    print("Click Finish")

    button_back_home = driver.find_element(By.XPATH, "//button[@id= 'back-to-products']")
    button_back_home.click()
    print("Click back home")

def product_choice(product):
    if int(product) == 1:
        print("Хочу купить Sauce Labs Backpack")
        product = driver.find_element(By.XPATH, "//a[@id= 'item_4_title_link']")
        value_product = product.text
        print("Confirm" + " " + value_product)

        price_product = driver.find_element(By.XPATH, "//*[@data-test= 'inventory-item-price'][1]")
        value_price_product = price_product.text
        print(value_price_product)

        select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        select_product.click()
        print("Select product")

        cart_to_end(driver, value_product, value_price_product)


    elif int(product) == 2:
        print("Хочу купить Sauce Labs Bike Light")

        product = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")
        value_product = product.text
        print("Confirm" + " " + value_product)

        price_product = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[2]")
        value_price_product = price_product.text
        print(value_price_product)

        select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
        select_product.click()
        print("Select product")

        cart_to_end(driver, value_product, value_price_product)

    elif int(product) == 3:
        print("Хочу купить Sauce Labs Bolt T-Shirt")
        product = driver.find_element(By.XPATH, "//a[@id= 'item_1_title_link']")
        value_product = product.text
        print("Confirm" + " " + value_product)

        price_product = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[3]")
        value_price_product = price_product.text
        print(value_price_product)

        select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        select_product.click()
        print("Select product_3")

        cart_to_end(driver, value_product, value_price_product)

    elif int(product) == 4:
        print("Хочу купить Sauce Labs Fleece Jacket")
        product = driver.find_element(By.XPATH, "//a[@id= 'item_5_title_link']")
        value_product = product.text
        print("Confirm" + " " + value_product)

        price_product = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[4]")
        value_price_product = price_product.text
        print(value_price_product)

        select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
        select_product.click()
        print("Select product")

        cart_to_end(driver, value_product, value_price_product)

    elif int(product) == 5:
        print("Хочу купить Sauce Labs Onesie")
        product = driver.find_element(By.XPATH, "//a[@id= 'item_2_title_link']")
        value_product = product.text
        print("Confirm" + " " + value_product)

        price_product = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[5]")
        value_price_product = price_product.text
        print(value_price_product)

        select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
        select_product.click()
        print("Select product")

        cart_to_end(driver, value_product, value_price_product)

    elif int(product) == 6:
        print("Хочу купить Test.allTheThings() T-Shirt (Red)")
        product = driver.find_element(By.XPATH, "//a[@id= 'item_3_title_link']")
        value_product = product.text
        print("Confirm" + " " + value_product)

        price_product = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[6]")
        value_price_product = price_product.text
        print(value_price_product)

        select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
        select_product.click()
        print("Select product")

        cart_to_end(driver, value_product, value_price_product)

product_choice(product)

while True:
    print("Хотите купить еще один товар? Да/Нет")
    answer = input()
    if answer.lower().strip() == "да":
        product = input()
        try:
            product = int(input("Введите число от 1 до 6: "))
            if product < 1 or product > 6:
                print("Пожалуйста, введите число от 1 до 6.")
                print("До свидания. Будем рады увидеть вас в нашем магазине в следующий раз!")
                exit()
        except ValueError:
            print("Это не число. Пожалуйста, введите цифру от 1 до 6.")
            print("До свидания. Будем рады увидеть вас в нашем магазине в следующий раз!")
            exit()
        product_choice(product)
    else:
        print("Будем рады увидеть вас в нашем магазине в следующий раз!")
        break



