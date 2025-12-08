import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('laptop_cleaned_data_v_1.xlsx')


###-------------------------------- Pie Chart of Price Range ----------------------------###

# Define price segment bins
bins = [0, 45000, 85000, df['price'].max()]
labels = ['Budget', 'Mid-Range', 'Premium']

# Create segment column
df['price_range'] = pd.cut(df['price'], bins=bins, labels=labels, include_lowest=True)

# Count distribution
segment_counts = df['price_range'].value_counts().sort_index()

plt.figure(figsize=(7,7))
plt.pie(
    segment_counts,
    labels=segment_counts.index,
    autopct='%1.1f%%',
    pctdistance=0.85
)

# Create center circle for donut effect
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Laptop Price Segment Distribution', fontsize=14)
plt.tight_layout()
plt.show()

###--------------------------------------------- Ram performance vs Prize --------------------------------###

def bucket_ram(x):
    if x < 16:
        return "Entry (4–12 GB)"
    elif x == 16:
        return "Standard (16 GB)"
    elif 16 < x <= 32:  # correct chained comparison
        return "Performance (24–32 GB)"
    elif x > 32:
        return "High-End (48–96 GB)"

df['ram_bucket'] = df['ram_size_gb'].apply(bucket_ram)

ram_bucket_price = (df.groupby('ram_bucket')['price']
                    .median()
                    .reindex(['Entry (4–12 GB)', 'Standard (16 GB)', 'Performance (24–32 GB)', 'High-End (48–96 GB)'])
                    .reset_index())


plt.figure(figsize=(10,6))
sns.lineplot( data=ram_bucket_price, x='ram_bucket', y='price', marker='o', linewidth=2)
x_shifts = [0.0, -0.05, 0.1, 0.0]
y_shifts = [8000, 8000, -15000, 5000]
for i, row in ram_bucket_price.iterrows():
    plt.text(i + x_shifts[i], row['price'] + y_shifts[i],  
             f"₹{int(row['price']):,}",ha='center',fontsize=10,color='red')
plt.title("Median Laptop Price Across RAM Categories", fontsize=14)
plt.xlabel("RAM Category", fontsize=12)
plt.ylabel("Median Price (INR)", fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

###----------------------------------------------- Spec by Processor -----------------------------------###

top3 = df['processor_brand'].value_counts().nlargest(3).index
df_top3 = df[df['processor_brand'].isin(top3)]
plt.figure(figsize=(10,6))
sns.boxplot(data=df_top3,x='processor_brand',y='specs_score',hue='processor_brand',palette='Set2',legend=False)
plt.title('Specs Score Distribution Across Top 3 Processor Brands', fontsize=14)
plt.xlabel('Processor Brand', fontsize=12)
plt.ylabel('Specs Score', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.show()

###---------------------------------------- Top configuration by parameters---------------------------------------###

config_counts = (
    df.groupby(['brand_grouped', 'ram_size_gb', 'storage_type'])
      .size()
      .reset_index(name='count')
      .sort_values('count', ascending=False)
)
top_config = config_counts.iloc[0]
total = len(df)
percentage = (top_config['count'] / total) * 100
print(
    f"The top configuration is {top_config['brand_grouped']} with "
    f"{int(top_config['ram_size_gb'])}GB RAM and {top_config['storage_type']} storage, "
    f"appearing {top_config['count']} times and accounting for {percentage:.2f}% of the market."
)

###-------------------------------------- Resolution Quality ---------------------------------------###

def classify_resolution(res_str):
    try:
        w, h = res_str.lower().split('x')
        h = int(h)
    except:
        return "Unknown"
    if h <= 900:
        return "HD"
    elif 1080 <= h <= 1200:
        return "FHD"
    elif 1400 <= h <= 1664:
        return "QHD"
    elif h >= 1800:
        return "UHD"
    else:
        return "Other"

df['resolution_quality'] = df['resolution'].apply(classify_resolution)

res_price = (df.groupby('resolution_quality')['price'].median().reindex(['HD', 'FHD', 'QHD', 'UHD', 'Other']).reset_index() )
res_price = res_price[(res_price['price'] > 0) & (res_price['price'].notna())]

plt.figure(figsize=(10,6))
sns.barplot(data=res_price, x='resolution_quality', y='price', hue='resolution_quality', legend=False, palette='Set2')
for i, row in res_price.iterrows():
    plt.text(
        i,
        row['price'] + 2000,     # slight vertical offset
        f"₹{int(row['price']):,}",
        ha='center',
        fontsize=10
    )
plt.title("Median Laptop Price Across Resolution Categories", fontsize=14)
plt.xlabel("Resolution Category", fontsize=12)
plt.ylabel("Median Price (INR)", fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.show()

###-------------------------------------------Market Share of Dedicated GPU-----------------------------------###

igpu_list = {
    "apple gpu", "apple m", "apple", "core",
    "integrated", "igpu", "integrated graphics", "integrated gpu"
}
def is_integrated_gpu(g):
    if pd.isna(g):
        return True
    g = g.lower()
    return any(keyword in g for keyword in igpu_list)
df['is_igpu'] = df['graphics'].apply(is_integrated_gpu)
df['has_dedicated_gpu'] = ~df['is_igpu']  # opposite of integrated
total = len(df)
dedicated_count = df['has_dedicated_gpu'].sum()
percentage = (dedicated_count / total) * 100
print(f"{percentage:.2f}% of all laptops feature dedicated graphics cards.")
