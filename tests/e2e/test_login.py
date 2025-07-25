from playwright.async_api import expect, Page
from src.pages.login_page import LoginPage
from src.utils.config_reader import ConfigReader
import pytest

@pytest.mark.training
@pytest.mark.asyncio
class TestLogin:
    
    async def test_successful_login(self, page:Page) -> None:
        """Test the login flow of a user that is not blocked or suspended"""
        config: ConfigReader = ConfigReader()
        loginPage:LoginPage = LoginPage(page=page)
        
        username:str = config.get_standard_user()
        password:str = config.get_password()
        
        await loginPage.login(username=username, password=password)
        
        #checks if the user arrives on the inventory page
        await expect(actual=page).to_have_url(url_or_reg_exp=config.get_inventory_url()) 
        
    async def test_locked_user(self, page:Page) -> None:
        """Tests the login flow of a suspended user"""
        config: ConfigReader = ConfigReader()
        loginPage:LoginPage = LoginPage(page=page)
        
        username:str = config.get_locked_user()
        password:str = config.get_password()
        
        await loginPage.login(username=username, password=password)
        
        #checks that the error message appears when the user logs in 
        await expect(actual=page).to_have_url(url_or_reg_exp=config.get_website_url())
        await expect(actual=page.locator(loginPage.ERROR_MESSAGE)).to_have_text(loginPage.ERR_MSG_LOCK)
        #Closes the error message and check that the message disappeared
        await loginPage.close_error()
        await expect(actual=page.locator(loginPage.ERROR_MESSAGE)).to_have_count(0)
    
    async def test_error_wrong_password_wrong_username(self, page:Page) -> None:
        """Tests the error when a user tries to login with a wrong password and username"""
        config: ConfigReader = ConfigReader()
        loginPage:LoginPage = LoginPage(page=page)
        emptyStr:str = " "
        
        await loginPage.login(username=emptyStr, password=emptyStr)
        await expect(actual=page).to_have_url(url_or_reg_exp=config.get_website_url())
        await expect(actual=page.locator(loginPage.ERROR_MESSAGE)).to_have_text(loginPage.ERR_MSG_WRNG)
        
    async def test_error_no_password(self, page:Page) -> None:
        """Tests the error when a user tries to login without providing a password"""
        config: ConfigReader = ConfigReader()
        loginPage:LoginPage = LoginPage(page=page)
        
        await loginPage.login(username=config.get_standard_user())
        await expect(actual=page).to_have_url(url_or_reg_exp=config.get_website_url())
        await expect(actual=page.locator(loginPage.ERROR_MESSAGE)).to_have_text(loginPage.ERR_MSG_PSWD)
    
    async def test_error_no_username(self, page:Page) -> None:
        """Tests the error when a user tries to login without providing a username"""
        config: ConfigReader = ConfigReader()
        loginPage:LoginPage = LoginPage(page=page)    
        await loginPage.login(password=config.get_password())
        await expect(actual=page).to_have_url(url_or_reg_exp=config.get_website_url())
        await expect(actual=page.locator(loginPage.ERROR_MESSAGE)).to_have_text(loginPage.ERR_MSG_USRN)
        
                
        