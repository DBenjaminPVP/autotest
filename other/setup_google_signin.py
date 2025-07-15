import os
import pytest
from playwright.async_api import async_playwright
import asyncio

@pytest.mark.signin
async def test_setup():
    """
    Main function to run the Playwright script for Google login using the SYNC API.
    This script will:
    1. Launch a browser.
    2. Navigate to the Google login page.
    3. Fill in the email and password from environment variables.
    4. Handle the 2FA TOTP code.
    5. Save the authentication state to 'auth.json'.
    """
    with async_playwright() as p:
        # Launch a persistent context to save the state
        context = await p.chromium.launch_persistent_context(
            user_data_dir="user_data",
            headless=False,  # Run in headed mode to see what's happening
            args=["--disable-blink-features=AutomationControlled"] # Helps to avoid detection by Google
        )
        page = await context.new_page()

        try:
            # Go to your target page that requires login
            await page.goto('https://fan-project-staging.firebaseapp.com/cloudflare/', timeout=60000)

            # --- Google Login Flow ---
            # Click the 'Sign in with Google' button
            # A new popup window for Google login should appear
            async with page.expect_popup() as popup_info:
                await page.get_by_role("button", name='Sign in with Google').click()
            popup_page = popup_info.value

            # Fill in the email
            await popup_page.get_by_label('Email or phone').fill(os.environ['GOOGLE_USER'])
            await popup_page.get_by_role('button', name='Next').click()

            # Fill in the password
            # It's good practice to wait for the element to be visible
            await popup_page.wait_for_selector('input[type="password"]', timeout=5000)
            await popup_page.get_by_label('Enter your password').fill(os.environ['GOOGLE_PWD'])
            await popup_page.get_by_role('button', name='Next').click()

            
            # Wait for navigation after login to ensure it's successful
            await page.wait_for_url("**/cloudflare/**", timeout=60000)
            print("Login successful! ✅")

            # --- Save storage state ---
            await context.storage_state(path="auth.json")
            print("Authentication state saved to auth.json")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Closing browser.")
            await asyncio.sleep(5)
            await context.close()

if __name__ == "__main__":
    asyncio.run(test_setup())