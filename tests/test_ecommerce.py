import pytest
import time
import pages.home_page
import pages.product_select_page
import pages.checkout_page
import pages.shipping_page
import pages.payment_page
import pytest_check as check

#AC1 Add 2 Socks to Shopping Cart
def test_add_2_products_to_cart(login):
    driver = login
    home_page = pages.home_page.HomePage(driver)
    product_select_page = pages.product_select_page.ProductSelectPage(driver)
    checkout_page = pages.checkout_page.CheckoutPage(driver)

    assert home_page.is_loaded(), "Home page not loaded"

    home_page.click_cart_icon()
    time.sleep(5)
    checkout_page.clear_all_existing_products()
    checkout_page.click_close_button()
    
    home_page.click_search_icon()
    home_page.enter_search_input("socks")
    home_page.click_size_button()
    home_page.click_size_36_40()
    home_page.click_size_apply_button()
    time.sleep(5)
    home_page.click_first_socks()

    product_select_page.select_size_36_40()
    time.sleep(2)
    product1_original_price = product_select_page.get_original_price()
    product1_discount_price = product_select_page.get_discount_price()
    product_select_page.click_add_to_cart()
    product_select_page.click_pop_out_close()
    product_select_page.click_back_button()
    time.sleep(5)
    home_page.click_second_socks()

    product_select_page.select_size_7_9()
    time.sleep(2)
    product2_original_price = product_select_page.get_original_price()
    product2_discount_price = product_select_page.get_discount_price()
    product_select_page.click_add_to_cart()
    product_select_page.click_view_shopping_cart()

    assert checkout_page.is_loaded(), "Checkout page not loaded"
    time.sleep(5)
    product1_name = checkout_page.get_product1_name()
    product2_name = checkout_page.get_product2_name()
    product1_size = checkout_page.get_product1_size()
    product2_size = checkout_page.get_product2_size()
    product1_price = checkout_page.get_product1_price()
    product2_price = checkout_page.get_product2_price()
    check.is_in("Anna Socks", product1_name, "Product 1 name does not match")
    check.is_in("Tamara Socks", product2_name, "Product 2 name does not match")
    
    check.is_in("36 to 40", product1_size, "Product 1 size does not match")
    check.is_in("7 to 9", product2_size, "Product 2 size does not match")
    
    check.equal(product1_price, product1_discount_price, "Product 1 price does not match")
    check.equal(product2_price, product2_discount_price, "Product 2 price does not match")


#AC2 Fill Shipping Form and Reveal Details on Payment Page
def test_add_2_products_to_cart(login):
    driver = login
    home_page = pages.home_page.HomePage(driver)
    product_select_page = pages.product_select_page.ProductSelectPage(driver)
    checkout_page = pages.checkout_page.CheckoutPage(driver)
    shipping_page = pages.shipping_page.ShippingPage(driver)
    payment_page = pages.payment_page.PaymentPage(driver)

    assert home_page.is_loaded(), "Home page not loaded"

    home_page.click_cart_icon()
    time.sleep(5)
    checkout_page.clear_all_existing_products()
    checkout_page.click_close_button()
    
    home_page.click_search_icon()
    home_page.enter_search_input("socks")
    home_page.click_size_button()
    home_page.click_size_36_40()
    home_page.click_size_apply_button()
    time.sleep(5)
    home_page.click_first_socks()

    product_select_page.select_size_36_40()
    time.sleep(2)
    product_select_page.click_add_to_cart()
    product_select_page.click_pop_out_close()
    product_select_page.click_back_button()
    time.sleep(5)
    home_page.click_second_socks()

    product_select_page.select_size_7_9()
    time.sleep(2)
    product_select_page.click_add_to_cart()
    product_select_page.click_view_shopping_cart()

    assert checkout_page.is_loaded(), "Checkout page not loaded"
    time.sleep(5)
    checkout_page.click_checkout_button()
    time.sleep(5)
    shipping_page.enter_street("123")
    shipping_page.enter_house_number("1234")
    shipping_page.enter_post_code("12345")
    shipping_page.enter_city("New York")
    # shipping_page.select_region()
    shipping_page.click_first_shipping_method()
    shipping_page.click_next()
    
    assert payment_page.is_loaded(), "Payment page not loaded"
    time.sleep(5)
    shipping_username = payment_page.get_shipping_username()
    shipping_street_housenumber = payment_page.get_shipping_street_housenumber()
    shipping_post_code_city = payment_page.get_shipping_post_code_city()
    shipping_region_country = payment_page.get_shipping_region_country()
    check.equal(shipping_username, "Tester One", "Shipping username does not match")
    check.equal(shipping_street_housenumber, "123 1234", "Shipping street and house number does not match")
    check.equal(shipping_post_code_city, "12345 New York", "Shipping postal code and city does not match")
    check.equal(shipping_region_country, "Alaska, United States", "Shipping region and country does not match")

    billing_username = payment_page.get_billing_username()
    billing_street_housenumber = payment_page.get_billing_street_housenumber()
    billing_post_code_city = payment_page.get_billing_post_code_city()
    billing_region_country = payment_page.get_billing_region_country()
    check.equal(billing_username, "Tester One", "Billing username does not match")
    check.equal(billing_street_housenumber, "123 1234", "Billing street and house number does not match")
    check.equal(billing_post_code_city, "12345 New York", "Billing postal code and city does not match")
    check.equal(billing_region_country, "Alaska, United States", "Billing region and country does not match")