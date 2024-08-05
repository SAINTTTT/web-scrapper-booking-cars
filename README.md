# Car Price Alert Bot

This project helps you receive alerts on Telegram for cars that have a price lower than your desired threshold. Currently, it is set up to notify you for prices below $700.

## How It Works

The script scrapes car prices from a specified URL and sends a Telegram message when it finds a car priced below the threshold.

## Setup Instructions

### 1. Configure Your Telegram Bot

Follow the [Telegram Bot Tutorial](https://core.telegram.org/bots/tutorial) to create your bot and obtain the necessary credentials (Telegram token and chat ID).

### 2. Set Up Secrets in GitHub Actions

1. Go to your GitHub repository.
2. Navigate to `Settings` > `Secrets and variables` > `Actions`.
3. Click on `New repository secret`.
4. Add the following secrets:
   - `TELEGRAM_TOKEN`: Your Telegram bot token.
   - `CHAT_ID`: Your Telegram chat ID.
   - `SEARCH_URL`: The URL of the search you want to monitor (e.g., `https://bookingcars.com/ar/list/destination/US/destination-city/NYC/dropoff/JFK/09-06-2024-11:00/T/Aeropuerto_Internacional_John_F._Kennedy/pickup/JFK/09-01-2024-11:00/T/Aeropuerto_Internacional_John_F._Kennedy/point-of-sale/United%20States/Aeropuerto_Internacional_John_F._Kennedy`).

### 3. Workflow Configuration

The GitHub Actions workflow is configured to run the scraper script periodically. Make sure the `requirements.txt` file includes all necessary dependencies.

### Example Workflow

```yaml
name: Run Selenium Web Scraper

on:
  schedule:
    - cron: '0 * * * *' # Runs every hour
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Check out repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x' # Choose the Python version you need

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        sudo apt-get update
        sudo apt-get install -y wget unzip
        wget -N https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
        unzip chromedriver_linux64.zip
        sudo mv chromedriver /usr/local/bin/chromedriver
        sudo chown root:root /usr/local/bin/chromedriver
        sudo chmod +x /usr/local/bin/chromedriver
        sudo apt-get install -y xvfb

    - name: Run scraper
      env:
        TELEGRAM_TOKEN: ${{ secrets.TELEGRAM_TOKEN }}
        CHAT_ID: ${{ secrets.CHAT_ID }}
        SEARCH_URL: ${{ secrets.SEARCH_URL }}
      run: |
        xvfb-run --auto-servernum --server-args='-screen 0 1920x1080x24' python your-script.py
