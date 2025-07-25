from playwright.async_api import expect, Page
from src.pages.login_page import LoginPage
from src.utils.config_reader import ConfigReader
import pytest

@pytest.mark.training
@pytest.mark.asyncio
class TestLogin:
    
    async def test_successful_login(self, page:Page):
        """Test the login flow of a user that is not blocked or suspended"""
        config: ConfigReader = ConfigReader()
        loginPage:LoginPage = LoginPage(page=page)
        
        username:str = config.get_standard_user()
        password:str = config.get_password()
        
        await loginPage.login(username=username, password=password)
        
        #checks if the user arrives on the inventory page
        await expect(actual=page).to_have_url(url_or_reg_exp=config.get_inventory_url()) 
        
    async def test_locked_user(self, page:Page):
        """Tests the login flow of a suspended user"""
        config: ConfigReader = ConfigReader()
        loginPage:LoginPage = LoginPage(page=page)
        
        username:str = config.get_locked_user()
        password:str = config.get_password()
        
        await loginPage.login(username=username, password=password)
        
        #checks that the error message appears when the user logs in 
        await expect(actual=page).to_have_url(url_or_reg_exp=config.get_website_url())
        await expect(actual=page.locator(loginPage.ERROR_MESSAGE)).to_have_text(loginPage.LOCKED_OUT_MSG)
        #Closes the error message and check that the message disappeared
        await loginPage.close_error()
        await expect(actual=page.locator(loginPage.ERROR_MESSAGE)).to_have_count(0)
    
        
                
        