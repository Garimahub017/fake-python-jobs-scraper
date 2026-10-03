# Fake Python Jobs Web Scraper

A beginner-friendly Python web scraper that extracts job listings from the Fake Python Jobs website and saves the data into a CSV file.

## Project Overview

This project uses Python, Requests, and BeautifulSoup to scrape job listings from:


https://realpython.github.io/fake-jobs/

The scraper collects:

- Job title
- Company name
- Location
- Job detail page URL

The collected data is then stored in a CSV file for easy use and analysis.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- CSV module

## Features

- Scrapes job listings from a webpage
- Extracts structured job information
- Handles missing fields using `N/A`
- Saves the results into a CSV file
- Displays the total number of jobs scraped

## Project Structure

```text
fake_job_scrapper/
│
├── scraper.py
├── jobs.csv
├── requirements.txt
└── README.md

## Installation

Make sure Python is installed on your system.

Install the required libraries using:

```bash
python -m pip install -r requirements.txt


## Project Page

Project URL:

https://github.com/Garimahub017/fake-python-jobs-scraper