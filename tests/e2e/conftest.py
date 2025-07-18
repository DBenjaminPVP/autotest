import pytest_asyncio
from playwright.async_api import async_playwright, Browser, Page
from src.utils.config_reader import ConfigReader

@pytest_asyncio.fixture
async def page():
    config:ConfigReader = ConfigReader()
    base_url:str = config.get_website_url()
    
    async with async_playwright() as p:
        browser:Browser = await p.chromium.launch()
        page:Page = await browser.new_page()
        await page.goto(base_url)
        
        yield page 
        
        print("Test over, closing browser")
        await browser.close() 