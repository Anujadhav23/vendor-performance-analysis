# Vendor Performance Analysis

End-to-end data analytics project using SQL, Python, and Power BI for comprehensive vendor performance evaluation and insights.

## 📊 Project Overview

This project analyzes vendor performance using sales data, purchasing patterns, and inventory management metrics. It combines SQL data processing, Python exploratory data analysis, and Power BI visualization to deliver actionable business insights.

- **Dataset**: 15.2M+ records across 4 CSV files
- **Tools**: SQLite, Pandas, Seaborn, SciPy, Power BI
- **Live Dashboard**: [Power BI Report](https://app.powerbi.com/links/FOtIWxBK9S?ctid=56c1d497-700b-49cf-8f8d-3dd6b20d522f&pbi_source=linkShare)

## 🗂️ Project Structure

```
Portfolio1/
├── README.md                              # Project documentation
├── .gitignore                             # Git ignore rules
├── data/                                  # Raw data files
│   ├── purchases.csv                      # Purchase transactions
│   ├── sales.csv                          # Sales records
│   ├── vendor_invoice.csv                 # Vendor invoices
│   ├── begin_inventory.csv                # Initial inventory
│   └── end_inventory.csv                  # Final inventory
├── logs/                                  # Application logs
├── PurchaseContribution.csv               # Processed purchase analysis
├── vendor_sales_summary.csv               # Vendor sales summary
├── Exploratory Data Analysis.ipynb        # Initial data exploration
├── Vendor Performance Analysis.ipynb      # In-depth analysis & insights
├── Untitled.ipynb                         # Additional analysis notebook
├── ingestion_db.py                        # Database ingestion script
├── get_vendor_summary.py                  # Vendor summary extraction
├── show_column_names.py                   # Data column inspection
├── main_dashboard.pbix                    # Power BI dashboard file
├── Vendor_Performance_Report.pdf          # Detailed report
└── Vendor_Performance_Report_v2.docx      # Updated report

```

## 📈 Key Features

- **Data Integration**: Loads and processes 15.2M+ records from multiple CSV sources
- **SQL Analysis**: SQLite database for complex data queries and aggregations
- **Python EDA**: Exploratory analysis using Pandas, NumPy, and statistical methods
- **Visualization**: Seaborn and matplotlib for visual insights
- **Power BI Dashboard**: Interactive business intelligence dashboard for stakeholder presentation

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3.x** | Data processing and analysis |
| **SQLite** | Database and complex queries |
| **Pandas** | Data manipulation and aggregation |
| **NumPy** | Numerical computations |
| **Seaborn/Matplotlib** | Data visualization |
| **SciPy** | Statistical analysis |
| **Power BI** | Business intelligence & dashboards |
| **Git** | Version control |

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook/Lab
- Power BI Desktop (for dashboard modification)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Anujadhav23/vendor-performance-analysis.git
cd vendor-performance-analysis
```

2. Install Python dependencies:
```bash
pip install pandas numpy scipy seaborn matplotlib jupyter
```

3. Prepare data:
   - Ensure CSV files are in the `data/` directory
   - Run data ingestion: `python ingestion_db.py`

### Usage

1. **View Analysis**: Open Jupyter notebooks
```bash
jupyter notebook
```

2. **Extract Vendor Summary**:
```bash
python get_vendor_summary.py
```

3. **View Interactive Dashboard**: Open `main_dashboard.pbix` in Power BI Desktop

## 📊 Analysis Highlights

### Key Metrics Analyzed
- Vendor sales performance trends
- Purchase contribution analysis
- Inventory management efficiency
- Seasonal sales patterns
- Vendor reliability and consistency
- Cost and margin analysis

### Insights Generated
- Top performing vendors by revenue and volume
- Vendor concentration risk assessment
- Seasonal purchasing patterns
- Inventory optimization recommendations

## 📁 Data Files

- **purchases.csv**: Transaction-level purchase data
- **sales.csv**: Sales records with timestamps and amounts
- **vendor_invoice.csv**: Invoice details and payment terms
- **begin_inventory.csv**: Starting inventory levels
- **end_inventory.csv**: Ending inventory levels

*Note: Data files are not tracked in git (see .gitignore)*

## 📊 Dashboard

Access the live Power BI dashboard:
[**Vendor Performance Analysis Dashboard**](https://app.powerbi.com/links/FOtIWxBK9S?ctid=56c1d497-700b-49cf-8f8d-3dd6b20d522f&pbi_source=linkShare)

The dashboard includes:
- Vendor performance scorecards
- Sales trends and forecasts
- Purchasing pattern analysis
- Inventory metrics
- KPI tracking

## 📝 Notebooks

### Exploratory Data Analysis.ipynb
Initial data exploration, data quality checks, and descriptive statistics.

### Vendor Performance Analysis.ipynb
In-depth analysis including:
- Vendor segmentation
- Performance metrics
- Correlation analysis
- Recommendations and insights

## 🔍 Scripts

- **ingestion_db.py**: Loads CSV data into SQLite database
- **get_vendor_summary.py**: Generates vendor summary reports
- **show_column_names.py**: Lists and describes data columns

## 📈 Results & Reports

- `Vendor_Performance_Report.pdf` - Executive summary and key findings
- `Vendor_Performance_Report_v2.docx` - Detailed analysis report
- `PurchaseContribution.csv` - Calculated contribution metrics
- `vendor_sales_summary.csv` - Aggregated vendor metrics

## 📋 Project Deliverables

✅ Data ingestion pipeline  
✅ SQL database with normalized schema  
✅ Exploratory data analysis  
✅ Statistical analysis and insights  
✅ Interactive Power BI dashboard  
✅ Executive reports (PDF & DOCX)  
✅ Documented code and notebooks  

## 📧 Contact & Support

For questions or feedback regarding this analysis, please open an issue on GitHub.

### Connect With Me

- **LinkedIn**: [Aniket Jadhav](https://www.linkedin.com/in/aniket-45-jadhav/)
- **Portfolio Website**: [Data Analyst Portfolio](https://data-analyst-portfolio-website-nine.vercel.app/)
- **GitHub**: [Anujadhav23](https://github.com/Anujadhav23)

## 📄 License

This project is open source and available under the MIT License.

---

**Last Updated**: June 2026  
**Status**: Complete ✅
