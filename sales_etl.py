import pandas as pd

# Step 1: Read the raw CSV
df = pd.read_csv("sales.csv")

# Step 2: Drop rows with any missing values
df_cleaned = df.dropna()

# Step 3: Save cleaned data to a new CSV
df_cleaned.to_csv("cleaned_sales.csv", index=False)

# Step 4: Group by City and save as Excel
city_sales = df_cleaned.groupby("City")["Amount"].sum().reset_index()
city_sales.to_excel("city_sales.xlsx", index=False)

# Step 5: Group by SalesPerson and save as Excel
salesperson_sales = df_cleaned.groupby("SalesPerson")["Amount"].sum().reset_index()
salesperson_sales.to_excel("salesperson_sales.xlsx", index=False)

print("✅ ETL process complete. Reports saved.")
