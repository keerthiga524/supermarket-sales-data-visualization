import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("supermarket_sales.csv")

print("Supermarket Dataset")
print(data)

# 1 Stock Status Analysis
stock_status = data["Stock_Status"].value_counts()

plt.figure()
stock_status.plot(kind="bar")
plt.title("Stock Status Analysis")
plt.xlabel("Stock Status")
plt.ylabel("Number of Products")
plt.show()

# 2 Purchased vs Not Purchased
purchase_status = data["Purchased"].value_counts()

plt.figure()
purchase_status.plot(kind="pie", autopct='%1.1f%%')
plt.title("Purchased vs Not Purchased")
plt.ylabel("")
plt.show()

# 3 Quantity Analysis
plt.figure()
plt.bar(data["Product"], data["Quantity"])
plt.title("Product Quantity Analysis")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=90)
plt.show()

# 4 Price Distribution
plt.figure()
plt.hist(data["Price"])
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()
