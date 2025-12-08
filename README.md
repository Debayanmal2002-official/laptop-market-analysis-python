# Laptop Sales & Performance Analysis (Python | Data Analytics)

An end-to-end data cleaning and exploratory analysis project based on a messy Kaggle laptop dataset.  
The original dataset contained incorrect values, inconsistent formats, missing entries, and noisy text fields.  
I first built a 750+ line cleaning script, then refactored it into a **200-line automated cleaning pipeline** using functions and rule-based transformations.

This project demonstrates my ability to work with **real-world messy data**, build reusable pipelines, and extract business insights responsibly.

---
## Tech Stack

- Python (pandas, numpy, matplotlib, seaborn)  
- Feature Engineering  
- Data Cleaning & Normalization  
- Exploratory Data Analysis (EDA)  
- Visualization  
- Statistical reasoning & insight storytelling

---
## Key Steps

### **1. Data Cleaning & Refactoring**
- Removed impossible/incorrect values  
- Normalized CPU, RAM, storage, resolution, and GPU fields  
- Imputed missing values using context-aware logic  
- Combined redundant OS categories  
- Automated the pipeline using modular functions  

### **2. Feature Engineering**
Created analytical features including:
- `price_range`  
- `ram_bucket`  
- `resolution_grouped`  
- GPU classification (`is_igpu`, `has_dedicated_gpu`)  

---
## Key Insights from EDA

- **Mid-range (45K–85K)** laptops dominate the market
  
![Price_range_Distribution](plots/price_range_pie.png)

- Major price jumps occur at **16GB RAM** and **24–32GB RAM**

![Price_by_RAM_Categories](plots/ram_vs_price.png) 

- Display quality strongly influences pricing (**QHD has highest median price**)
  
![Median_Price_by_Resolution_Type](plots/median_resolution.png)

- Box plot of top 3 processor brand

![Top_3_Processor_Brand_Box_Plot](plots/Specs_score_vs_Processsor_Brand.png)

- Most common configuration:  **[Brand] + 16GB RAM + SSD**, representing **X%** of listings (actual value computed in pyfile) 
- **65.78%** of laptops feature a **dedicated GPU** 

---
## Ethical Analysis Note

Many additional data analysis was done, but not shown to incompleteness of data.
Example: A filter-based “high performance threshold” falsely classified a ₹23,887 laptop due to incorrect CPU metadata in the Kaggle dataset.  
The insight was intentionally **discarded**, demonstrating responsible analytical judgment. Also OS rating analysis was **intentionally skipped** due to extreme data imbalance  
  (*“No analysis is better than wrong analysis.”*)

---
## Author

**Debayan Mal**  
Data Analyst — Python | SQL | Statistics | Visualization  
LinkedIn: https://linkedin.com/in/debayan-mal-9a3479340

