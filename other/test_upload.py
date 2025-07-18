import pytest
import asyncio
from playwright.async_api import  async_playwright, expect, Browser,BrowserContext, Page

@pytest.mark.fanappform
async def test_upload():
    # Create a new browser context with the saved authentication state
    # This loads the cookies and local storage from the 'auth.json' file
    async with async_playwright() as p:
        browser:Browser = await p.chromium.launch(headless=False)
        context:BrowserContext = await browser.new_context(storage_state="auth.json")
        try:
                page:Page = await context.new_page()
                await page.goto('', timeout=60000)
                async with page.expect_popup():
                        await page.get_by_role("button", name='Sign in with Google').click()
                await expect(page.locator("//article[@class='show-unauth']").get_by_text("Video Upload Dashboard",exact=True)).to_be_visible()
                await page.locator("//input[@id='fileInput']").set_input_files(files='/Users/benjamindefays/Downloads/test.mp4')
                await expect(page.locator('//select[@id="videoTypeSelect"]')).to_be_visible()
                await page.locator('//select[@id="videoTypeSelect"]').select_option(value='free', timeout=5000)
                await expect(page.locator('//select[@id="videoTypeSelect"]')).to_contain_text('Free')
                await page.locator("//input[@id='isFreeCheckbox']").check(timeout=5000)
                await expect(page.locator("//input[@id='isFreeCheckbox']")).to_be_checked()
        except Exception as e:
                print(f"An error occurred: {e}")
        finally:
                print("Closing browser.")
                await context.close()
    
if __name__ == "__main__":
    asyncio.run(test_upload())
    
