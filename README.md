# Supermarket Sales Data Analysis

This project performs data analysis and visualization on a supermarket sales dataset using Python.  
The program analyzes stock status, purchasing behavior, product quantity, and price distribution using graphical charts.

# Technologies Used

- Python
- Pandas
- Matplotlib

# Features

- Load supermarket sales dataset from a CSV file
- Analyze stock status of products (Full, Low, Empty)
- Analyze purchased vs not purchased products
- Analyze quantity of products
- Analyze price distribution
- Visualize results using charts

# Dataset

The dataset contains information about supermarket products.

Example:

Product,Stock_Status,Purchased,Quantity,Price  
Rice,Full,Yes,25,50  
Milk,Low,Yes,12,30  
Oil,Empty,No,0,120  

# Result Visualization

The program generates four visualizations to analyze supermarket data.

## Figure 1 – Stock Status Analysis

Bar chart showing the number of products with *Full, Low, and Empty stock status*.

![Stock Status Analysis](figure1.png)

## Figure 2 – Purchased vs Not Purchased

Pie chart showing the percentage of *purchased and not purchased products*.

![Purchased vs Not Purchased](figure2.png)

## Figure 3 – Product Quantity Analysis

Bar chart showing the *quantity available for each product*.

![Product Quantity](figure3.png)

## Figure 4 – Price Distribution

Histogram showing the *distribution of product prices* in the dataset.

![Price Distribution](figure4.png)

# Project Files

supermarket_analysis.py  
supermarket_sales.csv  
figure1_stock_status.png  
figure2_purchase_status.png  
figure3_quantity_analysis.png  
figure4_price_distribution.png  
README.md  

# How to Run the Project

1. Install required libraries

pip install pandas matplotlib

2. Place the dataset file in the same folder as the Python program.

3. Run the program

python supermarket_analysis.py

# Author

Keerthiga  
B.Tech Information Science Engineering
