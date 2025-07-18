from playwright.async_api import Page


class LoginPage:
    #xpath locator for the login page field
    USERNAME_FIELD = '//input[@id="user-name"]'
    PASSWORD_FIELD = '//input[@id="password"]'
    LOGIN_BUTTON = '//input[@id="login-button"]'
    
    def __init__(self, page: Page):
        self.page = page
        
    async def login(self, username:str, password:str)->None:
        """A single high-level async method to perform a complete login."""
        await self.page.locator(selector=self.USERNAME_FIELD).fill(value=username)
        await self.page.locator(selector=self.PASSWORD_FIELD).fill(value=password)
        await self.page.locator(selector=self.LOGIN_BUTTON).click()