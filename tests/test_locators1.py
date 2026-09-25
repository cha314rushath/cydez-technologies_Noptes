def test_collecting_all_links(page):
    page.goto("https://www.flipkart.com/",wait_until="domcontentloaded")
    links = page.locator("//a")
    for i in links.all():
        print("link" , i.get_attribute("href"),flush=True)
    
    links.last.click()
    links.first.click()
    links.nth(0).click()
# html tables collect the all num of rows and col's
# html tables collect items in rows and cols



# def test_get_options(page):
#     page.goto("https://demowebshop.tricentis.com/",wait_until="domcontentloaded")
#     page.locator("(//li[@class='inactive'])[1]/a").click()
#     products_locators =  page.locator("//h2[@class='product-title']")
#     # ================================================
#     #    num of products
#     # ====================================================
#     print("num of books =" , products_locators.count())
#     #   ======================== first book ==========
#     print("first book is", products_locators.nth(0).all_text_contents())   
#     # =======================================
#     #  all product text 
    # print("products list",products_locators.all_inner_texts())
#  ===================================================================
    #  products in the list with product name we selected
    # ==================================================
    # product_list = ["Computing and Internet","Fiction","Health Book"]
    # for i in product_list:
    #     product = page.locator(f"//a[text()='{i}']/../..//input[@value='Add to cart']")
    #     product.click()
    # =========================================
    


# def test_count_the_link(page):
#     page.goto("https://demowebshop.tricentis.com/",wait_until="domcontentloaded")
#     links_locator = page.locator("//a")
#     # Wait until at least one link is attached
#     links_locator.first.wait_for(state="attached")
#     links = links_locator.all() 
#     print(len(links)) # how many links are present in the page
#     print(type(links))
#     for i in links:
#         print(i.text_content(),flush=True) # text of the link
#     print("*" * 50)
#     for i in links:
#         print(i.get_attribute("href"),flush=True) # href of the link
        

# # def test_table(page):
# #     page.goto("https://www.w3schools.com/html/html_tables.asp")
# #     count_tables =  page.locator("//table").count() # how many tables are present in the page
# #     print(count_tables,flush=True)
#     # "
#     #                 Welcome to our store"
#     # find single ele  :-->signle ele
#     # find multiple ele :-->multiple ele in the list 
    
    
#     # link Tag_name a / link is present in the href attribute of the anchor tag
#     # <a href="https://www.amazon.in/gp/help/customer/display.html?nodeId=200507590">Help</a>
#     # finding the ele (//a) :a tag
#     # get the links :-->arrtibute href
#     # get the link of the text :-->text methods
#     # link :-->//a
#     # img :-->//img
#     # table :-->//table
#     # rows :-->//tr
#     # columns :-->//td
#     # list :-- //ol or //ul
#     # list items :-->//li
    
