import pytest
from playwright.sync_api import Page, expect, Locator

@pytest.mark.browserstack
def test_item_purchase(page:Page):
    page.goto('https://bstackdemo.com/')
    item: Locator = page.locator("//div[@class='shelf-item']").filter(has_text='iPhone 11', has_not_text='iPhone 11 Pro')
    #priceTag: Locator = item.locator("//div[@class='shelf-item__price']").locator("//div[@class='val']")
    #price : str = f"{await priceTag.locator("//small").inner_text()}{ await priceTag.locator("//span").text_content()}{await priceTag.locator("//b").text_content()}"
    #print(price)
    item.locator('//div[@class="shelf-item__buy-btn"]').click()
    assert page.get_by_text('bag').is_visible()
    cart: Locator  = page.locator("//div[@class='float-cart__shelf-container']")
    cart.locator('//div[@class="shelf-item"]').first.wait_for()
    count: int = cart.locator('//div[@class="shelf-item"]').count()
    assert count == 1
    page.get_by_text('Checkout').click()
    page.get_by_text("Select Username").click()
    page.locator("#react-select-2-option-0-0").click()
    page.get_by_text("Select Password").click()
    page.locator("#react-select-3-option-0-0").click()
    page.get_by_role(role='button',name='Log In').click()
    page.locator('//input[@id="firstNameInput"]').fill("benjamin")
    page.locator('//input[@id="lastNameInput"]').fill("defays")
    page.locator('//input[@id="addressLine1Input"]').fill("9 impasse du petit bois")
    page.locator('//input[@id="provinceInput"]').fill("Saint Georges es Allier")
    page.locator('//input[@id="postCodeInput"]').fill("63800")
    page.get_by_role(role='button',name='Submit').click()
    assert page.locator("#confirmation-message").is_visible()
    
    
