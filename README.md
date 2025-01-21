# CSUN_MBB_Analysis
A deeper look into the CSUN Men's Basketball team performance (2015-2023). Analyzing the impact of specific positions and how CSUN has ranked within the conference alongside machine learning approaches with macro data to predict seed outcome based on selected features.

## Tableau Dashboard
You can view the interactive Tableau dashboard for this project [here](https://public.tableau.com/app/profile/george.patterson4334/viz/CSUNAnalysis/TeamHistoryDashboard).

## Project Overview

This project is a comprehensive data analysis of individual player statistics for the California State University, Northridge (CSUN) men's basketball team. The analysis focuses on player positions and points scored over the past nine seasons (Excluding covid year 2020). The data was collected using a Python web scraper I developed, processed in Excel, and visualized with Tableau to uncover insights about team performance, specifically regarding the contribution of forwards.

Additionally, I have included a Machine Learning analysis for a macro dataset (`cbb.csv`) including all teams in Division 1 basketball and used the information to predict the seed placement of a team based on given features. The optimal Support Vector Classifier model finds an accuracy of 78.7% in its predictions.

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

- **Key Insight**: The Tableau dashboard reveals that seasons in which forwards—traditionally not the primary scorers—made substantial contributions to the team’s total points coincided with CSUN achieving an above-average win/loss ratio.
- This suggests that to enhance performance in future seasons, CSUN should focus on recruiting high-scoring forwards.

## (Additional) Machine Learning Summary

The `cbb.csv` dataset includes various statistical features which I have used to predict team seed (placement within conference for the season). Seeds have been grouped into categories: "High," "Medium," or "Low." The project demonstrates data preprocessing, feature engineering, and the application of two machine learning models for classification.

Models Implemented:

**Random Forest Classifier:**
- Achieved an accuracy of 77.2% on the test set.
- The weighted average F1-score: 0.77.
- Feature importance analysis revealed key factors influencing predictions.

**Support Vector Classifier (SVC):**
- Achieved a slightly higher accuracy of 78.7% on the test set.
- Utilizes a linear kernel to classify team seeds based on scaled feature data.

**Key Features:**
- Data cleaning and handling missing values.
- Correlation analysis to identify relationships between features.
- Feature scaling with StandardScaler for consistent performance across models.
- Detailed model evaluation with precision, recall, and F1-scores.
- Visualizations include a correlation heatmap and feature importance bar chart.
  
**Conclusion:**

The project highlights the effectiveness of Random Forest and SVC models for predicting basketball team performance categories, with SVC being the most accurate. The most influential features included ADJOE, ADJDE, and 2P_D. Looking at the analysis, one noticable comparison we can inspect is 2 pointers have a much greater influence on a teams seasonal outcome as opposed to 3 pointers. Using this information, a coach can make actionable choices to improve team performance.


