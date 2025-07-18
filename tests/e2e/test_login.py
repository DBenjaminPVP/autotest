from playwright.async_api import expect, Page
from src.pages.login_page import LoginPage
from src.utils.config_reader import ConfigReader
import pytest

@pytest.mark.training
@pytest.mark.asyncio
class TestLogin:
    
    async def test_successful_login(self, page:Page):
        config: ConfigReader = ConfigReader()
        loginPage:LoginPage = LoginPage(page=page)
        
        username:str = config.get_standard_user()
        password:str = config.get_password()
        
        await loginPage.login(username=username, password=password)
        
        await expect(actual=page).to_have_url(url_or_reg_exp=config.get_inventory_url()) 
        
    async def test_locked_users(self, page:Page):
        config: ConfigReader = ConfigReader()
        loginPage:LoginPage = LoginPage(page=page)
        
        username:str = config.get_locked_user()
        password:str = config.get_password()
        
        await loginPage.login(username=username, password=password)
        
        await expect(actual=page).to_have_url(url_or_reg_exp=config.get_website_url())        
        