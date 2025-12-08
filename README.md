Laptop Sales & Performance Analysis (Python | Data Analytics Project)
💻 Laptop Sales & Performance Analysis

An end-to-end exploratory data analysis project uncovering key pricing, performance, and market trends in the laptop industry.

This project demonstrates my ability as a data analyst to clean data, engineer features, generate insights, validate assumptions, and communicate findings clearly and responsibly.

📂 Project Overview

This dataset contains 1,000+ laptop listings with attributes like:

Brand, price, ratings, specs score

Processor, RAM, storage

Screen resolution, size

Graphics configuration

Warranty, OS

Derived fields like price segments, resolution groups, RAM buckets

The objective of this analysis is to understand:

What drives price

Which configurations dominate the market

How screen quality, RAM, CPU threads, and GPU type relate to pricing

What fraction of laptops are budget / mid-range / premium

Which specifications deliver the highest value to customers

🛠️ Tech Stack

Python (pandas, numpy, matplotlib, seaborn)

Feature Engineering

Data Cleaning & Normalization

Exploratory Data Analysis (EDA)

Visualization

Statistical reasoning / insight storytelling

🔧 Data Cleaning & Feature Engineering

Key engineered features:

✔ price_range

Categorized into 4 meaningful price segments for Indian market relevance:

Budget (≤45K)

Mid-Range (45K–65K)

Upper Mid-Range (65K–90K)

Premium (>90K)

✔ ram_bucket

Clustered RAM into realistic market tiers:

Entry (4–12 GB)

Standard (16 GB)

Performance (24–32 GB)

High-End (48–96 GB)

✔ resolution_grouped

Mapped raw resolution numbers into:

HD

FHD

QHD

UHD

✔ GPU Classification

Separated laptops into:

dedicated GPU laptops

integrated GPU (iGPU) laptops

📊 Key Insights
1️⃣ Price Segment Distribution

Most laptops fall in the mid-range (45–85K), reflecting strong consumer demand for balanced performance/value.

2️⃣ RAM vs Price (Performance Jump Analysis)

Major price jumps occur at:

8GB → 16GB (productivity tier)

16GB → 24–32GB (creator/gaming tier)

3️⃣ Screen Quality Price Drivers

Median prices increase with display quality:

Resolution	Median Price
HD	Lowest-tier, budget laptops
FHD	Mainstream baseline
QHD	Highest median price — gaming/creator laptops
UHD	Premium productivity laptops
4️⃣ Dominant Configuration

Most common market configuration =
[Brand] + 16GB RAM + SSD, representing X% of listings.
(Actual values generated dynamically in notebook.)

5️⃣ High-End Graphics Share

65.78% of laptops include a dedicated GPU, meaning the dataset leans toward performance-oriented devices.

6️⃣ OS Ratings — Analysis Withheld

The OS distribution is extremely imbalanced (930 Windows vs <40 macOS vs <10 others).
To avoid misleading conclusions:

No OS rating comparison was performed, as insufficient sample size makes the results statistically invalid.

This demonstrates responsible analytics practice.

🧠 High-Performance Threshold (Honest Analysis)

A naive filter returned a price of ₹23,887 for a "high performance" laptop based on RAM ≥16GB & threads ≥12,
but this was rejected because the CPU thread counts for Celeron processors in the dataset were misreported.

No incorrect insight was published — “no analysis is better than wrong analysis.”

This reinforces strong analytical ethics.

📌 Examples of Visuals

Price segment distribution (pie & bar charts)

RAM vs price (line plot with labels)

Specs score distribution across processor brands

Median price by resolution group

GPU share visualization

(All visuals available in the Jupyter notebook.)

📁 Repository Structure
├── data/
│   └── cleaned_laptop_data.csv
├── notebooks/
│   └── laptop_analysis.ipynb
├── scripts/
│   └── analysis.py
├── images/
│   └── plots/ ...
└── README.md

🎯 What This Project Demonstrates
✔ Data cleaning, handling inconsistencies, ensuring reliability
✔ Professional feature engineering
✔ Exploratory analysis with business relevance
✔ Effective data visualization
✔ Responsible analytical judgment
✔ Clear communication of insights
✔ Ability to say “no insight” when data is not valid

This is the kind of analytical maturity hiring managers specifically look for.

🚀 Future Improvements

Add regression model to predict laptop price

Build a Power BI / Tableau dashboard

Add CPU benchmark mapping via external dataset

Improve GPU classification using model lists

🙋‍♂️ Author

Debayan Mal
Data Analyst | Python | SQL | Statistics | Visualization
