import pytest_asyncio
import asyncio
from playwright.async_api import async_playwright, BrowserContext, Page
from src.utils.config_reader import ConfigReader

@pytest_asyncio.fixture
async def page():
    config:ConfigReader = ConfigReader()
    base_url:str = config.get_website_url()
    
    async with async_playwright() as p:
        """this is the base that will be executed before and after (from yield) each tests"""
        browser:BrowserContext = await p.chromium.launch_persistent_context(
            user_data_dir="user_data",
            headless=False,  # Run in headed mode to see what's happening
        )
        page:Page = await browser.new_page()
        await page.goto(base_url)
        
        yield page 
        
        print("Closing browser.")
        #give a bit of time to check the browser before the end of the test
        await asyncio.sleep(2)
        await browser.close()