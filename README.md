# Laptop Sales & Performance Analysis (Python | Data Analytics Project)

An end-to-end exploratory data analysis project uncovering key pricing, performance, and market trends in the laptop industry.

This project demonstrates my ability as a data analyst to clean data, engineer features, generate insights, validate assumptions, and communicate findings clearly and responsibly.

---

## Project Overview

This dataset contains 1,000+ laptop listings with attributes such as:

- Brand, price, ratings, specs score  
- Processor, RAM, storage  
- Screen resolution, size  
- Graphics configuration  
- Warranty, OS  
- Engineered fields like price segments, resolution groups, RAM buckets  

The goal of this project is to understand:

- What drives laptop pricing  
- Which configurations dominate the market  
- How screen quality, RAM, CPU thread count, and GPU type influence pricing  
- How laptops distribute across budget, mid-range, and premium segments  
- Which specifications offer the highest value to customers  

---

## Tech Stack

- Python (pandas, numpy, matplotlib, seaborn)  
- Feature Engineering  
- Data Cleaning & Normalization  
- Exploratory Data Analysis (EDA)  
- Visualization  
- Statistical reasoning & insight storytelling  

---

## Data Cleaning & Feature Engineering

### price_range  
Defined four meaningful Indian-market price tiers:

- Budget (≤45K)  
- Mid-Range (45K–65K)  
- Upper Mid-Range (65K–90K)  
- Premium (>90K)  

### ram_bucket  
Mapped RAM into tiers:

- Entry (4–12 GB)  
- Standard (16 GB)  
- Performance (24–32 GB)  
- High-End (48–96 GB)  

### resolution_grouped  
Mapped raw resolutions into:

- HD  
- FHD  
- QHD  
- UHD  

### GPU Classification  
Separated GPU types into:

- Dedicated GPU  
- Integrated GPU (iGPU)  

---

## Key Insights

### 1. Price Segment Distribution  
Most laptops fall into the mid-range (45–85K), aligning with mainstream consumer demand.

### 2. RAM vs Price (Performance Jump Analysis)  
Major jumps observed at:
- 8GB → 16GB  
- 16GB → 24–32GB  

### 3. Screen Quality Price Drivers  
Median price increases as display quality improves:

| Resolution | Insight |
|-----------|---------|
| HD | Budget laptops |
| FHD | Mainstream baseline |
| QHD | Highest median price (gaming/creator segment) |
| UHD | Premium productivity laptops |

### 4. Dominant Configuration  
Most common configuration:  
**[Brand] + 16GB RAM + SSD**, representing **X%** of listings  
(actual value computed in notebook).

### 5. High-End Graphics Share  
65.78% of laptops feature a dedicated GPU, indicating a performance-oriented dataset.

### 6. OS Ratings — Analysis Withheld  
OS distribution is extremely imbalanced (930 Windows vs <40 macOS vs <10 others).  
To avoid misleading conclusions:

**OS rating comparison was intentionally omitted due to insufficient sample size.**

This reflects responsible analytics practice.

---

## High-Performance Threshold (Ethical Analysis)

A naïve rule (RAM ≥16GB and threads ≥12) returned a minimum price of ₹23,887.  
However, this was rejected because CPU metadata (e.g., Celeron N-series threads) was inconsistent in the dataset.

**Incorrect insights were not published — “no analysis is better than wrong analysis.”**

---

## Example Visuals

- Price segment distribution  
- RAM vs price line chart  
- Specs score distribution by processor brand  
- Median price by resolution group  
- GPU share visualization  

(All visuals are available in the Jupyter notebook.)

---

## What This Project Demonstrates

- Data cleaning and validation  
- Professional feature engineering  
- Business-relevant exploratory analysis  
- Clear and compelling visual communication  
- Responsible analytical judgment  
- Ability to avoid incorrect insights when data is insufficient  

These qualities match what hiring managers expect from a capable data analyst.

---

## Future Improvements

- Add a regression model to predict laptop price  
- Build a Power BI / Tableau dashboard  
- Integrate external CPU benchmark data  
- Improve GPU identification via model mapping  

---

## Author

**Debayan Mal**  
Data Analyst — Python | SQL | Statistics | Visualization  
LinkedIn: https://linkedin.com/in/debayan-mal-9a3479340

