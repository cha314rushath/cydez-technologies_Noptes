# page.getByRole() to locate by explicit and implicit accessibility attributes.
# page.getByText() to locate by text content.
# page.getByLabel() to locate a form control by associated label's text.
# page.getByPlaceholder() to locate an input by placeholder.
# page.getByAltText() to locate an element, usually image, by its text alternative.
# page.getByTitle() to locate an element by its title attribute.
# page.getByTestId() to locate an element based on its data-testid attribute (other attributes can be configured).
from playwright.sync_api import expect
# def test_locators_get_by_role(page):
#     page.goto("https://demowebshop.tricentis.com/")
#     page.get_by_role("link",name="Log in").click()
#     page.get_by_role("textbox",name="Email").fill("abc@gmail.com")
#     page.get_by_role("textbox",name="password").fill("abc123")
#     page.get_by_role("button",name="Log in").click()
    
# def test_get_by_text(page):
#     page.goto("https://www.facebook.com/")
#     login_to_facebook_text = page.get_by_text("Log in to Facebook")
#     expect(login_to_facebook_text).to_be_visible()
#     forgot_password_button = page.get_by_text("Forgotten password?")
#     forgot_password_button.click()
    
#page.getByLabel() to locate a form control by associated label's text.
# def test_get_by_label(page):
#     page.goto("https://demowebshop.tricentis.com/")
#     register_link = page.get_by_text("Register")
#     register_link.click()
#     page.get_by_label("Male").nth(0).check()
#     page.get_by_label("First name:").fill("abc")
#     page.get_by_label("Last name:").fill("xyz")
#     page.get_by_label("Email:").fill("abc@gmail.com")
#     page.get_by_label("Password:").nth(0).fill("abc123")
#     #[password , confirm password] are two fields with same label, so we need to use nth() to select the first one.
#     # index 0 / index 1
#     # eles = page.get_by_label("Password:")
#     # eles[0].fill("abc123")
#     # eles[1].fill("abc123")
#     page.get_by_label("Confirm password:").fill("abc123")
#     page.get_by_role("button",name="Register").click()
    
# # page.getByPlaceholder() to locate an input by placeholder.
# def test_get_by_placeholder(page):
#     page.goto("https://www.amazon.in/")
#     page.get_by_placeholder("Search Amazon.in").fill("books")
#     page.keyboard.press("Enter")
#     page.wait_for_timeout(5000)
    
# # only img's 
# # def test_get_by_alt_text(page):
# #     page.goto("https://demowebshop.tricentis.com/")
# #     logo = page.get_by_alt_text("Tricentis Demo Web Shop")
#     expect(logo).to_be_visible()
# # page.getByTitle() to locate an element by its title attribute.
# # title = "values"

def test_get_by_title(page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(5000)
    logo = page.get_by_title("Speed | Tricentis")
    logo.click()
    # expect(logo).to_be_visible()

# def test_get_by_test_id(page):
#     page.goto("https://demowebshop.tricentis.com/")
#     page.wait_for_timeout(5000)
#     logo = page.get_by_test_id("Tricentis Demo Web Shop")
#     logo.click()
#     # expect(logo).to_be_visible()
    