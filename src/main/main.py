from SecAdvScraper import SecAdvScraper as SAP
import argparse
import csv
import requests

if __name__ == "__main__":

    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, required=True, help="URL to fetch data from")
    parser.add_argument("--output", type=str, required=True, help="Output file path")
    args = parser.parse_args()

    # Extract data and save to Excel file
    URL = args.url
    OUTPUT_PATH = args.output
    ScrapedData = SAP(URL)
    ScrapedData.WriteToExcel(OUTPUT_PATH)