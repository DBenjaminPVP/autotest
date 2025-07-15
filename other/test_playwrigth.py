import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # ** Start intercepting requests **
        # We're watching for any URL that ends with .png or .jpg
        await page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())

        # Now, go to a page with images
        await page.goto("https://en.wikipedia.org/wiki/Cat")
        
        # The page will load, but all the cat pictures will be blocked!
        await page.screenshot(path="no_cat_pics.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
    
    
    
# to compare element pixel by pixel 
# await expect(page).toHaveScreenshot('buy-now-button.png');

# This will take a screenshot of the entire visible viewport
#await expect(page).to_have_screenshot("main-screen.png")

# How to handle dynamic content with a mask
#await expect(page).to_have_screenshot(
#    "main-screen-with-mask.png",
    # Mask the ad banner and the clock so they don't cause failures
#    mask=[
#        page.locator("#ad-banner"),
#        page.locator("#live-clock")
#    ]
#)