import requests
import pandas as pd
from bs4 import BeautifulSoup
import io

#Define the URL
url = "https://en.wikipedia.org/wiki/Comma-separated_value"
# Get the url content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract all tables from the url
tables = pd.read_html(io.StringIO(str(soup)))

# Extract cars table
cars = tables[1]
print(cars)

# Export cars to csv
cars.to_csv("/Users/rukhshandaashraf/Desktop/st_2195/st2195_assignment_2/python_csv/cars_python.csv",index=False)
