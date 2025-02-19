import json
import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from datetime import datetime

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

# Function to fetch therapist profile URLs from a page
def fetch_profile_urls(page_number, base_url):
    url = base_url.format(page_number)
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        profile_urls = re.findall(r'<a href="/profil/[a-z\.]+/"', html_content)
        profile_urls = [x.split("<a href=")[1].split('"')[1] for x in profile_urls]
        full_urls = [f"https://www.therapie.de{url}" for url in profile_urls]
        return full_urls
    return []

# Function to fetch email addresses by simulating a click on the contact button
def fetch_emails_from_profile(profile_url, driver):
    emails = []
    try:
        driver.get(profile_url)
        time.sleep(2)  # Wait for the page to load
        contact_button = driver.find_element(By.ID, "contact-button")
        contact_button.click()
        time.sleep(2)  # Wait for the email to load/display

        html_content = driver.page_source
        emails = re.findall(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", html_content
        )
    except Exception as e:
        print(f"Error fetching emails from {profile_url}: {e}")
    return emails

# Main function to loop through pages and fetch emails from profile pages
def main():
    config = load_config()
    all_emails = set()  # Using a set instead of list to avoid duplicates

    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--disable-gpu')  # Required for some systems
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # Prevent opening of mail program by disabling mailto links
    options.add_experimental_option("prefs", {
        "protocol_handler.excluded_schemes": {
            "mailto": True
        }
    })
    service = Service(config['path_to_chromedriver'])
    driver = webdriver.Chrome(service=service, options=options)

    current_date = datetime.now().strftime('%Y-%m-%d')
    filename = f'collected_emails_{current_date}.txt'
    # Open file in append mode
    with open(filename, 'a') as email_file:
        try:
            for page in range(1, config['num_pages']):  
                print(f"Processing page {page}...")
                profile_urls = fetch_profile_urls(page, config['base_url']+f"&page={page}")
                for profile_url in profile_urls:
                    print(f"Fetching emails from: {profile_url}")
                    emails = fetch_emails_from_profile(profile_url, driver)
                    
                    # Write new emails to file
                    for email in emails:
                        if email not in all_emails:  # Only write if it's a new email
                            all_emails.add(email)
                            email_file.write(f"{email}\n")
                            email_file.flush()  # Ensure immediate write to disk
                            print(f"New email found and saved: {email}")
        finally:
            driver.quit()

    print(f"\nTotal unique email addresses found: {len(all_emails)}")
    print(f"All emails have been saved to '{filename}'")

if __name__ == "__main__":
    main()