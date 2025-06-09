# 📊 Sales Report ETL Project

This is a hands-on ETL project built using **Python and Pandas** to automate sales data processing. It reads raw sales data from a CSV file, cleans missing entries, groups the data by **City** and **Salesperson**, and exports the summary reports in Excel format.

The script is scheduled to run daily using **Windows Task Scheduler**, making it ideal for real-world automation scenarios.

---

## 🚀 Features

- ✅ Cleans and preprocesses raw sales data (removes missing rows)
- 📈 Aggregates sales totals:
  - By **City** → `city_sales.xlsx`
  - By **SalesPerson** → `salesperson_sales.xlsx`
- 💾 Saves cleaned data as `cleaned_sales.csv`
- 🕒 Fully automated daily execution using Task Scheduler
- 🛠️ Simple to extend and modify for real-world ETL use cases

---

## 🧰 Tools & Technologies

- **Python**
- **Pandas**
- **Excel Writer** (`.to_excel()`)
- **Windows Task Scheduler**
- **GitHub** (version control)

---

## 📁 Project Files

| File Name                 | Description                             |
|--------------------------|-----------------------------------------|
| `sales_etl.py`           | Main ETL script                         |
| `sales.csv`              | Raw input data (sample)                 |
| `cleaned_sales.csv`      | Cleaned output data                     |
| `city_sales.xlsx`        | Summary: Total sales by city            |
| `salesperson_sales.xlsx` | Summary: Total sales by salesperson     |
| `README.md`              | Project overview and usage instructions |

---

## 🧪 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Ravibellam123/sales-report-project.git
   cd sales-report-project
Install required Python package: pip install pandas
Run the script: python sales_etl.py
Output Excel files and cleaned CSV will be created in the same folder.
