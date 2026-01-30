# Computer Price Analysis Project

## Overview

In this project, we analyzed a dataset containing information about different computer components and their prices. The dataset includes features such as speed, HD size, RAM size, screen size, touch screen, USB ports, battery life, backlit keyboard, resolution, graphics type, CD drive, multi-core, premium brand, ads, and trend. The goal of the project was to explore the relationship between different computer components and their prices, and to perform data cleaning steps such as imputation of missing values and capping of outliers.

## Data Cleaning

The dataset contained missing values in some of the features. To handle these missing values, we performed imputation using the mean value of the respective feature. We also identified outliers in the price feature and capped them at a certain threshold to reduce their impact on the analysis.

## Data Analysis

We performed various exploratory data analysis techniques to understand the relationship between different computer components and their prices. Some of the key insights from the analysis are:

- There is a positive correlation between speed and price, with faster computers generally being more expensive.
- Computers with a touch screen tend to be more expensive than those without a touch screen.
- Computers with a dedicated graphics card tend to be more expensive than those with an integrated graphics card.
- There is a positive correlation between battery life and price, with computers having longer battery life generally being more expensive.
- Computers with a backlit keyboard tend to be more expensive than those without a backlit keyboard.

## Visualization

We created various visualizations to illustrate the relationships between different computer components and their prices. Some of the key visualizations are:

- A scatter plot of speed vs. price, with a regression line to show the trend.
- A histogram of price for computers with and without a touch screen.
- A violin plot of price vs. speed, with jitter to show the distribution of prices for different speed values.
- A strip plot of price vs. backlit keyboard, with jitter to show the distribution of prices for computers with and without a backlit keyboard.
- A point plot of price vs. graphics type, with different markers for integrated and dedicated graphics.

## Conclusion

In this project, we explored the relationship between different computer components and their prices. We found that certain features such as speed, touch screen, graphics type, battery life, and backlit keyboard have a significant impact on the price of a computer. We also performed data cleaning steps such as imputation of missing values and capping of outliers to ensure the accuracy of our analysis. The insights gained from this analysis can be useful for consumers looking to purchase a new computer, as well as for manufacturers looking to price their products competitively.

## Requirements

To run this project, you will need the following dependencies installed in your Python environment:

- pandas
- numpy
- matplotlib
- seaborn
- colorama

You can install these dependencies using `pip install -r requirements.txt`.

## Data

The dataset used in this project is included in the repository as `computers.csv`. The dataset contains 1000 rows and 16 columns.
