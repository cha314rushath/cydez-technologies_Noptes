from playwright.sync_api import sync_playwright, expect
def test_demo(page,browser_name):
    page.goto("https://www.google.com")
    print(page.title())
    print(browser_name)
    expect(page).to_have_title("Google")
    




#Why context :--> Context is used to manage the lifecycle of the browser and page instances in Playwright. It allows you to create multiple pages within the same browser instance and ensures proper cleanup after the tests are completed.
# 2 browser one for user sec admin 
# from playwright.sync_api import sync_playwright,expect
# def test_application():
#     with sync_playwright() as p:
#        browser = p.chromium.launch(headless=False)
#        # user 
#        end_user_context = browser.new_context()  # Create a new browser context  
#        end_user_page = end_user_context.new_page()  # Create a new page in the end user context      
#        end_user_page.goto("http://localhost:3000/")  # Navigate to Google in the end user context 
#        # expect(act).to_have_title(exp)  # Assert the title of the page in the end user contextxt
#        expect(end_user_page).to_have_title("ShopEase")  # Assert the title of the page in the end user context  
       
#        # admin
#        admin_context = browser.new_context()  # Create a new browser context for the admin user
#        admin_page = admin_context.new_page()  # Create a new page in the admin context
#        admin_page.goto("http://localhost:3000")  # Navigate to Google in the admin context
#        expect(admin_page).to_have_title("ShopEase")  # Assert the title of the page in the admin context
       









# from dotenv import load_dotenv
# import os

# load_dotenv()

# base_url = os.getenv("BASE_URL")

# print(base_url)

# from playwright.sync_api import sync_playwright,expect
# def test_demo(page):
#     page.goto("https://www.google.com")
#     print(page.title())
#     expect(page).to_have_title("Google")

# def test_google():
#     with sync_playwright() as p:

#         browser = p.chromium.launch(headless=False)

#         page = browser.new_page()

#         page.goto("https://www.google.com")

#         print("Title:", page.title())

#         browser.close()
# test_google()
