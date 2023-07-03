Property Data Scraper

This Python script scrapes property data from the Dentoc CAD website for a range of property IDs and years, and saves the data to a CSV file.

Requirements

To run this script, you need:

Python 3.x
The requests library
The beautifulsoup4 library
A range of property IDs to search

Usage

Clone this repository to your local machine.
Install the required libraries using pip install -r requirements.txt.
Open scraper.py in a text editor.
Modify the prop_id range in the for loop to match the range of property IDs you want to search.
Run the script using python scraper.py.
The script will create a CSV file named property_data.csv in the same directory as the script, and write the scraped data to the file.

Output

The CSV file contains the following columns:

  Property ID: The ID of the property searched.
  Year: The year of the property data searched.
  Address: The address of the property searched.
  Market Value: The market value of the property searched for the given year.
  If the market value is not found for a given year, the value in the Market Value column will be "Not found".

Limitations
This script assumes that the property search page has the same structure, and that the property data is formatted in the same way. If the structure or formatting of the page changes, this script may need to be updated accordingly.

License
This script is released under the MIT License.
