# CSUN_MBB_Analysis
A deeper look into the CSUN Men's Basketball team performance (2015-2023). Analyzing the impact of specific positions and how CSUN has ranked within the conference.

## Tableau Dashboard
You can view the interactive Tableau dashboard for this project [here](https://public.tableau.com/app/profile/george.patterson4334/viz/CSUNAnalysis/TeamHistoryDashboard).

## Project Overview

This project is a comprehensive data analysis of individual player statistics for the California State University, Northridge (CSUN) men's basketball team. The analysis focuses on player positions and points scored over the past nine seasons (Excluding covid year 2020). The data was collected using a Python web scraper I developed, processed in Excel, and visualized with Tableau to uncover insights about team performance, specifically regarding the contribution of forwards.

## Project Goals

- Scrape and consolidate individual player statistics (such as positions and points scored) from the CSUN men's basketball website.
- Combine the scraped data with additional data from a separate team database (https://www.kaggle.com/datasets/andrewsundberg/college-basketball-dataset).
- Create dynamic data visualizations using Excel pivot tables and Tableau dashboards to identify performance trends and insights.

## Key Tools and Technologies Used

- **Python**: Utilized for web scraping to collect player statistics.
  - **Requests**: To send HTTP requests and retrieve web pages.
  - **BeautifulSoup**: To parse HTML and extract specific elements containing player data.
  - **Pandas**: To organize the scraped data into a structured format and export it to Excel.
- **Excel**: Used for data cleaning, transformation, and analysis with pivot tables and slicers for interactive exploration. Conditional formatting is used to highlight successful (50% plus win/loss ratio) and unsuccessful (25% and below) years.
- **Tableau**: For creating a visual dashboard that highlights key insights, such as the performance of non-primary scoring positions over time.

## Data Collection and Methodology

1. **Web Scraping**:
   - A Python script was developed to scrape player data from CSUN's basketball team website.
   - Data collected includes player names, positions, and points scored each year over the past nine seasons.
   - The script uses the `requests` library to retrieve web pages and `BeautifulSoup` to parse and extract relevant data.
   - The data is consolidated by matching players' names.

2. **Data Processing**:
   - The collected data is combined with additional data from a separate team database.
   - An Excel sheet is created to house the combined dataset, with the use of pivot tables and slicers to enable easy data navigation and analysis.

3. **Data Visualization**:
   - The consolidated data is imported into Tableau to create a dashboard that visualizes player performance trends over time.
   - The dashboard reveals key insights, such as years when forwards (a non-primary scoring position) contributed significantly to overall points, which coincides with periods of above-average team performance.

## Findings

- **Key Insight**: The Tableau dashboard illustrates that during seasons when forwards (a position not primarily relied upon for scoring) contributed significantly to points, CSUN performed above average compared to other seasons.
- This suggests a strategic advantage or adaptation by the team in leveraging non-traditional positions for scoring during these periods.
