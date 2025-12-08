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

### 1) **Laptop Market Share according to Price Range**
  
![Price_range_Distribution](plots/price_range_pie.png)

- The laptop market is heavily concentrated in the mid-range and premium tiers, **Mid-range (45K–85K)** laptops dominate the market, showing a clear consumer shift toward higher performance and better build quality rather than low-cost devices.

### 2) **Price and RAM size relation**

![Price_by_RAM_Categories](plots/ram_vs_price.png) 

- Laptop prices increase sharply with RAM capacity, with major jumps at 16GB and 32GB, indicating clear performance tiers and strong alignment between RAM configuration and customer segment.

### 3) Display quality strongly influences pricing (**QHD has highest median price**)
  
![Median_Price_by_Resolution_Type](plots/median_resolution.png)

- Higher-resolution displays are strongly correlated with higher laptop prices.
QHD laptops show the highest median price due to their association with gaming and creator-grade hardware, while UHD models occupy the premium productivity segment. FHD represents the mainstream sweet spot, and HD remains confined to entry-level devices.

### 4) Box plot of top 3 processor brand

![Top_3_Processor_Brand_Box_Plot](plots/Specs_score_vs_Processsor_Brand.png)

- Intel and AMD deliver nearly identical median specs scores, showing strong competition in the mainstream market. AMD exhibits wider performance variability, spanning budget to high-end models, while Intel shows more high-performance outliers. Apple maintains consistent performance but in a narrower band, reflecting its premium ecosystem rather than raw hardware diversity.

### 5) Most common configuration: The top configuration is **HP** with **16GB** RAM and **SSD** storage, appearing **150** times and accounting for **14.84%** of the market. 

### 6) **65.78%** of laptops feature a **dedicated GPU** 

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

