from playwright.async_api import Page


class LoginPage:
    #xpath locators for the login page's fields
    USERNAME_FIELD = '//input[@id="user-name"]'
    PASSWORD_FIELD = '//input[@id="password"]'
    LOGIN_BUTTON = '//input[@id="login-button"]'
    ERROR_MESSAGE = '//h3[@data-test="error"]'
    CLOSE_ERROR_BUTTON = '//button[@class="error-button"]'
    
    #error messages used by this page
    ERR_MSG_LOCK = 'Epic sadface: Sorry, this user has been locked out.'
    ERR_MSG_WRNG = 'Epic sadface: Username and password do not match any user in this service'
    ERR_MSG_PSWD = 'Epic sadface: Password is required'
    ERR_MSG_USRN = 'Epic sadface: Username is required'
    
    
    def __init__(self, page: Page):
        self.page = page
        
    async def login(self, username:str | None = None, password:str | None = None)->None:
        """Perform a complete login."""
        if username:
            await self.page.locator(selector=self.USERNAME_FIELD).fill(value=username)
        if password:
            await self.page.locator(selector=self.PASSWORD_FIELD).fill(value=password)
        await self.page.locator(selector=self.LOGIN_BUTTON).click()
        
    async def close_error(self)->None:
        """Close the error pop up """
        await self.page.locator(selector=self.CLOSE_ERROR_BUTTON).click()    
        
    async def clear_login_fields(self)->None:
        """clear the username and password fields on the login page"""
        await self.page.locator(selector=self.USERNAME_FIELD).clear()
        await self.page.locator(selector=self.PASSWORD_FIELD).clear()