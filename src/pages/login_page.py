from playwright.async_api import Page


class LoginPage:
    #xpath locator for the login page field
    USERNAME_FIELD = '//input[@id="user-name"]'
    PASSWORD_FIELD = '//input[@id="password"]'
    LOGIN_BUTTON = '//input[@id="login-button"]'
    ERROR_MESSAGE = '//h3[@data-test="error"]'
    CLOSE_ERROR_BUTTON = '//button[@class="error-button"]'
    LOCKED_OUT_MSG = 'Epic sadface: Sorry, this user has been locked out.'
    
    
    def __init__(self, page: Page):
        self.page = page
        
    async def login(self, username:str, password:str)->None:
        """Perform a complete login."""
        await self.page.locator(selector=self.USERNAME_FIELD).fill(value=username)
        await self.page.locator(selector=self.PASSWORD_FIELD).fill(value=password)
        await self.page.locator(selector=self.LOGIN_BUTTON).click()
        
    async def close_error(self)->None:
        """Close the error pop up """
        await self.page.locator(selector=self.CLOSE_ERROR_BUTTON).click()