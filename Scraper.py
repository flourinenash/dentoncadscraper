import csv
import re
import requests
from bs4 import BeautifulSoup

# Define the base URL for the property search
base_url = 'https://propaccess.trueautomation.com/clientdb/Property.aspx?cid=19&prop_id={}&year={}'

# Define the range of property IDs to search
prop_id_start = 180440
prop_id_end = 180460

# Define the range of years to search
year_start = 2010
year_end = 2023

# Open a CSV file for writing and write the header row
with open('property_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Property ID', 'Year', 'Address', 'Market Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Loop over the property IDs to search
    for prop_id in range(prop_id_start, prop_id_end):
        # Send a GET request to the property search URL for the latest year (2023)
        response = requests.get(base_url.format(prop_id, 2023))
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()

        # Extract the property address from the text using a regular expression
        address_match = re.search(r'Address:(.*?)Mapsco:', text, re.DOTALL)
        if address_match:
            address = address_match.group(1).strip()

        # Loop over the years to search for property data
        for year in range(year_start, year_end):
            # Format the property search URL with the current property ID and year
            url = base_url.format(prop_id, year)

            # Send a GET request to the property search URL
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()

            # Extract the property market value from the text using a regular expression
            market_value_match = re.search(r'Market Value:=\s*\$?([\d,]+)', text)
            if market_value_match:
                market_value = market_value_match.group(1).replace(',', '')
                # Write a row to the CSV file with the property data
                writer.writerow({'Property ID': prop_id, 'Year': year, 'Address': address, 'Market Value': market_value})
            else:
                # Write a row to the CSV file with a "Not found" market value
                writer.writerow({'Property ID': prop_id, 'Year': year, 'Address': address, 'Market Value': 'Not found'})