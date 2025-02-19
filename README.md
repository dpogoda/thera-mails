# Installation

# Therapist Email Scraper

This Python script scrapes email addresses from therapist profiles on therapie.de. It's designed to collect contact information for therapists in specified locations with specific specializations.

## Prerequisites

- Python 3.x
- Chrome WebDriver
  - [Download here](https://sites.google.com/chromium.org/driver/downloads?authuser=0)
- Required Python packages:
  ```bash
  pip install selenium requests
  ```

## Usage Tips

### Sending Mass Emails Efficiently

The collected email addresses can be used effectively for reaching multiple therapists at once:

1. **Use BCC for Mass Mailing**
   - Put all collected email addresses in the BCC (Blind Carbon Copy) field
   - Benefits:
     - Send one email to reach many therapists simultaneously
     - Increases chances of finding available therapy spots
     - Protects therapists' privacy (recipients can't see other addresses)
     - More professional approach than individual emails
     - Saves time compared to sending individual emails

2. **Email Etiquette**
   - Write a professional and clear subject line
   - Include your key requirements (location, insurance, specialization)
   - Keep the message concise but informative
   - Consider mentioning that you're contacting multiple therapists due to the known difficulty in finding available spots

## Files

### main.py

The main script that handles the web scraping functionality:

- Loads configuration from `config.json`
- Fetches therapist profile URLs from search results
- Extracts email addresses from individual profiles using Selenium
- Handles pagination automatically
- Removes duplicate email addresses
- Prints results to file

### config.json

Configuration file that contains:

- `base_url`: The search URL with your desired filters (location, specialization, etc.)
- `path_to_chromedriver`: Path to your Chrome WebDriver executable
- `num_pages`: Number of pages to scrape

## Setup

1. Install the required Python packages:

   ```bash
   pip install selenium requests
   ```
2. Download Chrome WebDriver:

   - Visit [Chrome WebDriver Downloads](https://sites.google.com/chromium.org/driver/downloads?authuser=0)
   - Download the version matching your Chrome browser
   - Update the `path_to_chromedriver` in `config.json` with your local path
3. Configure `config.json`:

   - Modify the `base_url` if you want to change search parameters
   - Set the correct `path_to_chromedriver` for your system
   - Adjust `num_pages` based on how many pages you want to scrape

## Usage

Run the script using:

`python main.py`

The script will:

1. Process each page in the search results
2. Visit each therapist's profile
3. Extract email addresses
4. Save emails to a dated file (format: collected_emails_YYYY-MM-DD.txt)
5. Display unique email addresses found
6. Show the total count of unique emails

**Note**: Currently, the script may trigger your default email program to open multiple times when collecting email addresses. This is a known issue that will be addressed in future updates.

## Roadmap

### Planned Features

1. Rate Limiting & Error Handling

   - Implement proper handling of 429 (Too Many Requests) responses
   - Add exponential backoff for retry attempts
   - Implement request rate limiting to prevent server overload
   - Automatic detection of total available pages
2. Bug Fixes & Improvements

   - Prevent external mail program from opening during scraping
   - Optimize email extraction process
   - Reduce system resource usage
   - Remove manual page number configuration
3. Data Management

   - Save results to CSV/Excel files
   - Database integration for storing historical data
   - Export options in multiple formats
4. Advanced Features

   - Proxy support for distributed scraping
   - Configurable scraping parameters through UI
   - Detailed logging system
   - Email validation and verification

## Notes

- The script includes delays to respect the website's loading times
- Uses Selenium to handle dynamic content
- Automatically removes duplicate email addresses
- Handles errors gracefully and continues processing
- Saves all collected emails to a date-stamped file
- May trigger your default email client multiple times (temporary limitation)

## Legal Notice

Ensure you comply with therapie.de's terms of service and local data protection laws when using this scraper.
