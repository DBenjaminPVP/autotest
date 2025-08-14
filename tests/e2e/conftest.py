import pytest_asyncio
from playwright.async_api import async_playwright, BrowserContext, Page
from src.utils.config_reader import ConfigReader
import shutil
import tempfile

@pytest_asyncio.fixture
async def page():
    config:ConfigReader = ConfigReader()
    base_url:str = config.get_website_url()
     # Create a temporary directory for the user profile
    profile_dir = tempfile.mkdtemp()
    async with async_playwright() as p:
        """this is the base that will be executed before and after (from yield) each tests"""
        browser:BrowserContext = await p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=True,  # Recommended for Docker/CI environments
            args=["--disable-features=ProcessSingleton"] # A good safety measure
        )
        page:Page = await browser.new_page()
        await page.goto(base_url)
        
        yield page 
        
        print("Closing browser.")
        await browser.close()
        shutil.rmtree(profile_dir)