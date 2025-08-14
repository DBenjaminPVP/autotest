from playwright.async_api import Page


class InventoryPage:
    #xpath locators for the inventory page's fields
    
    def __init__(self, page: Page):
        self.page = page
        
    #async def login(self)->None:
    #    """Perform a complete login."""
    #    await self.page.locator(selector=self.USERNAME_FIELD).fill(value=username)
    #    await self.page.locator(selector=self.PASSWORD_FIELD).fill(value=password)
    #    await self.page.locator(selector=self.LOGIN_BUTTON).click()