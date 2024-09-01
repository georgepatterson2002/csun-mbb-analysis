import requests
from bs4 import BeautifulSoup
import urllib.parse
import pandas as pd

starting_year = year = 2023
years_searched = 9

data = []

scoring_data = {year: [] for year in range(starting_year, starting_year - years_searched, -1)}

urls = []

for i in range(years_searched):
    urls.append("https://gomatadors.com/sports/mens-basketball/stats/" + str(starting_year-i) + "-" + str(starting_year+1-i))

# Iterate through each URL for each year
for url in urls:

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate points element
    pts_elements = soup.select('#category-leaders-scoring td[data-label="Points"]')
    
    pts_list = [int(pts_element.text.strip()) for pts_element in pts_elements]

    # Locate name element
    name_elements = soup.find('section', id='category-leaders-scoring').find_all('td', {'data-label': 'Name'})

    # Strip name and append to scoring_data
    for i, name_element in enumerate(name_elements):

        full_name = name_element.text.strip().split("#")[-1].strip()
        full_name = full_name.split(" ", 1)[-1].strip()
        last_name, *last_name_parts = full_name.split(",")
        first_name = ' '.join(last_name_parts).strip()

        scoring_data[year].append((last_name, first_name, pts_list[i]))

    year -= 1


urls = []

position_data = {year: [] for year in range(starting_year, starting_year - years_searched, -1)}

for i in range(years_searched):
    urls.append("https://gomatadors.com/sports/mens-basketball/roster/" + str(starting_year-i) + "-" + str(starting_year+1-i)[2:])

year = starting_year

# Iterate through URLs
for url in urls:


    last_name_list = []
    first_name_list = []
    position_list = []
    

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find position element
    position_elements = soup.find_all("span", class_="sidearm-roster-player-position-long-short hide-on-small-down")
    
    # Strip points from element
    for element in position_elements:
        position = element.text.strip()
        position_list.append(position)

    # Find name element
    name_elements = soup.find_all("a", attrs={"data-bind": "click: function() { return true; }, clickBubble: false"})

    # Strip name and append to position_data
    for element in name_elements:
        name = element.text.strip()
        #Do not include elements where name is "Full Bio"... Resolves bug
        if name != "Full Bio" and name != '':
            parts = name.split(maxsplit=1)
            first_name = parts[0]
            last_name = parts[1] if len(parts) > 1 else ""
            first_name_list.append(first_name)
            last_name_list.append(last_name)

    for item in zip(last_name_list, first_name_list, position_list):
        position_data[year].append(item)

    year -= 1


# Match identical names is position_data and scoring_data to consolidate information
for year in position_data:

    for last_name, first_name, position in position_data[year]:

        points = 0
       
        for score_last_name, score_first_name, score_points in scoring_data[year]:
            if last_name == score_last_name and first_name == score_first_name:
                points = score_points
                break

        data.append([year, last_name, first_name, position, points])
    

# Create DataFrame
df = pd.DataFrame(data, columns=['Year', 'Last Name', 'First Name', 'Position', 'Points'])

# Export to Excel
df.to_excel('consolidated_data.xlsx', index=False)