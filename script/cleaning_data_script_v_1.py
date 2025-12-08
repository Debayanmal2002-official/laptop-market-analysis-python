import pandas as pd
import numpy as np
import re

###-----------------------------Calling Dataset and setting up for cleaning--------------------###

df = pd.read_excel('laptop_raw_data.xlsx')

#Dropping Unnecessary
df.drop(columns=['image_url'], inplace=True)
df.rename(columns={'resoultion': 'resolution'}, inplace=True)

# Remove non-ASCII + lowercase for all object columns
obj_cols = df.select_dtypes(include=['object']).columns

for col in obj_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.encode('ascii', 'ignore')  # remove non-ascii
        .str.decode('ascii')            # back to string
        .str.lower()                    # lowercase
        .str.strip()                    # optional tidy
    )
    df[col] = df[col].replace(['nan','none',''],np.nan)

### ------------------------------- Calling Standard Definition ------------------------------###

from standard_cleaning_dafinition import (
    simple_impute_median,
    impute_by_group_mode,
    clean_col_by_list,
    normalize_col_by_list
)

### -------------------------------------- Standard Keywords -------------------------------###

gpu_key = {'rtx', 'gtx', 'geforce', 'nvidia', 'radeon', 'rx', 'vega', 'iris',
           'uhd', 'hd graphics', 'arc', 'adreno', 'mali', 'powervr','graphics','integrated'}
rom_key = {'ssd', 'hdd', 'emmc', 'nvme', 'sata', 'pcie'}
ram_key = {'ddr', 'lpddr', 'ram'}
scr_key = {'inch','inches', 'display', 'screen', 'panel', 'amoled', 'oled', 'lcd', 'ips'}
res_key = {'pixel','pixels'}
os_key = {'windows', 'macos', 'chromeos', 'linux', 'ubuntu', 'dos', 'android','chrome os'}
extra_key = {'warranty'}
cpu_key = {'cpu','i3','i5','i7','i9','pentium','celeron', 'atom','xeon','n100','n200',
           'n300','n305','n4020','n4120','n5030','n5100','n5105','n6000','n6005',
           'ryzen','athlon','a4','a6','a9','a10','a12','mediatek','kompanio','mt8183',
           'mt8192','t618','k1350','snapdragon','sc7180'}

non_os_list = extra_key | res_key
non_cpu_list = gpu_key|rom_key|ram_key|scr_key|os_key|extra_key|res_key
non_ram_list = gpu_key|rom_key|scr_key|os_key|extra_key
non_rom_list = gpu_key|ram_key|scr_key|os_key|extra_key|res_key|cpu_key
non_gpu_list = rom_key|ram_key|scr_key|os_key|extra_key|res_key|cpu_key
non_scr_list = gpu_key|rom_key|os_key|extra_key|res_key|cpu_key|cpu_key

###------------------------------------------CLEANING--------------------------------------------###

### Cleaning Columns

os_list = {'windows':['windows 11 os', 'windows 11  os', 'windows os', 'windows 10 os'],
           'macos':['macos 11 os', 'mac os'],
           'dos':['dos 11 os', 'dos os', 'dos 10 os'],
           'android':['android 11 os', 'android os', 'android 10 os'],
           'ubuntu':['ubuntu 11 os', 'ubuntu os'],
           'linux':['linux 11 os', 'linux os', 'linux 10 os'],
           'chromeos':['chrome os os', 'chrome os','chromeos']
           }

cpu_list = {'intel':['intel','core','i3','i5','i7','i9','pentium','celeron',
                     'atom','xeon','n100','n200','n300','n305','n4020','n4120',
                     'n5030','n5100','n5105','n6000','n6005'],
            'amd': ['amd','ryzen','athlon','a4','a6','a9','a10','a12'],
            'apple': ['apple', 'm1', 'm2', 'm3'],
            'arm':['arm','mediatek','kompanio','mt8183','mt8192','t618','k1350',
                   'snapdragon','sc7180','octa core','octa-core']
}

rom_list = {'hdd':['hard disk','hdd'],'ssd':['ssd'],'emmc':['emmc']}

gpu_list = {
    "nvidia": ["nvidia", "geforce", "rtx", "gtx", "mx", "quadro", "tesla", "titan", "nvs"],
    "amd": ["amd", "radeon", "rx", "vega", "firepro"],
    "intel": ["intel","inte", "iris xe", "iris", "uhd", "hd graphics", "xe graphics", "arc"],
    "apple": ["apple gpu", "apple m", "apple", "core"],
    "qualcomm": ["adreno", "qualcomm"],
    "arm": ["mali", "arm"],
    "imagination": ["powervr", "imagination"],
    # The 'unknown' brand is now mapped to None (which will be converted to np.nan)
    None: ["integrated graphics", "integrated gpu", "graphics card"]}

df = clean_col_by_list(df, 'os', non_os_list)
df = normalize_col_by_list(df, 'os', os_list)

df['processor_brand'] = df['processor']
df = clean_col_by_list(df, 'processor_brand', non_cpu_list)
df = normalize_col_by_list(df, 'processor_brand', cpu_list)

df = clean_col_by_list(df, 'ram', non_ram_list)
df['ram'] = df['ram'].str.replace(r'\b(sdram|ram)\b', '', case=False, regex=True).str.strip()
df['ram'] = df['ram'].str.replace('slpddr', 'lpddr', regex=False)
df['ram'] = df['ram'].str.replace(r'\blpddr\s+', 'lpddr', regex=True)
df['ram'] = df['ram'].str.replace(r'\bddr\s+', 'ddr', regex=True)
df['ram'] = df['ram'].str.replace(r'\s{2,}', ' ', regex=True).str.strip()
df['ram_size'] = df['ram'].str.extract(r'(\d+)\s*gb', flags=re.IGNORECASE)
df['ram_size'] = df['ram_size'].str.replace(r'[^\d]','',regex=True).astype('Int64')
df['ram_type'] = df['ram'].str.extract(r'\s+gb\s*(.*)', flags=re.IGNORECASE, expand=False).str.strip()
df['ram_type'] = df['ram_type'].replace('',np.nan)

df = clean_col_by_list(df, 'storage', non_rom_list)
df['storage_size'] = df['storage'].str.extract(r'(\d+\s*(?:gb|tb))', flags=re.IGNORECASE, expand=False).str.strip()

extracted_parts = df['storage_size'].str.extract(r'(\d+)\s*(gb|tb)', flags=re.IGNORECASE)
df['storage_num'] = extracted_parts[0]
df['storage_unit'] = extracted_parts[1]
df['storage_num'] = pd.to_numeric(df['storage_num'], errors='coerce')
df['storage_size'] = np.where(df['storage_unit'] == 'tb',df['storage_num']*1000, df['storage_num'])
df['storage_size'] = df['storage_size'].astype('Int64')
df = df.drop(columns=['storage_unit', 'storage_num'])
df['storage_type'] = df['storage']
df = normalize_col_by_list(df, 'storage_type', rom_list)

df = clean_col_by_list(df, 'graphics', non_gpu_list)
df['graphics_brand'] = df['graphics']
df = normalize_col_by_list(df, 'graphics_brand', gpu_list)

df = clean_col_by_list(df, 'screen_size', non_scr_list)
df['screen_size'] = df['screen_size'].str.replace(r'\b(inch|inches)\b', '', case=False, regex=True).str.strip()
df['screen_size'] = df['screen_size'].astype('float64')

df['resolution'] = df['resolution'].str.extract(r'(\d{3,4}\s*x\s*\d{3,4})', expand=False)
df['resolution'] = df['resolution'].str.replace(r'\s*x\s*', 'x', regex=True)
df['resolution'] = df['resolution'].replace('',np.nan)


df.loc[df['cores'].astype(str).str.lower().str.contains("ram", na=False), 'cores'] = np.nan
df['cores'] = df['cores'].replace({r'\bocta\b': '8', r'\bhexa\b': '6', r'\bquad\b': '4',
                                   r'\bdual\b': '2', r'\bdeca\b': '10',}, regex=True)
df['cores'] = df['cores'].str.replace(r'\bcore\b','cores',regex = True)

df.loc[~df['threads'].str.contains(r'thread|threads', case=False, na=False, regex=True), 'threads'] = np.nan
df['threads'] = df['threads'].astype(str).str.extract(r'(\d+)', expand=False)
df['threads'] = df['threads'].astype(float).astype('Int64')

df.loc[~df['warranty'].str.contains(r'year|yr|months|yrs|warranty', case=False, na=False, regex=True),'warranty'] = np.nan
df['warranty'] = df['warranty'].replace({r'\bmonths\b': 'year'}, regex=True)
df['warranty'] = df['warranty'].astype(str).str.extract(r'(\d+)', expand=False)
df['warranty'] = df['warranty'].astype(float).astype('Int64')

### Filling NaN Values

columns_to_impute = [('specs_score', 'brand'),('screen_size', 'brand'),('threads', 'processor_brand'),
                     ('warranty', 'brand'),('ram_size', 'brand'),('storage_size', 'brand')]
for impute_col, group_col in columns_to_impute:
    df = simple_impute_median(df, impute_col, group_col)

imputation_pairs = [('resolution', 'screen_size'),('os', 'brand'),('cores', 'processor_brand'),
                    ('ram_type', 'processor_brand'),('storage_type', 'brand'),
                    ('graphics_brand', 'processor_brand')]
for value_col, group_col in imputation_pairs:
    df[value_col] = impute_by_group_mode(df=df, value_col=value_col, group_col=group_col)


THRESHOLD = 10

brand_counts = df['brand'].value_counts()
brand_to_group = brand_counts[brand_counts < THRESHOLD].index
df['brand_grouped'] = df['brand'].replace(brand_to_group, 'Other')

resolution_counts = df['resolution'].value_counts()
resolutions_to_group = resolution_counts[resolution_counts < THRESHOLD].index
df['resolution_grouped'] = df['resolution'].replace(resolutions_to_group, 'Other')

###-------------------------------------- Finalizing & Saving ---------------------------------###

df.rename(columns={'screen_size': 'screen_size_inches',
                   'ram_size':'ram_size_gb',
                   'warranty': 'warranty_years',
                   'storage_size':'storage_size_gb'}, inplace=True)
print(df.info())

# saving
df.to_excel("laptop_cleaned_data_v_1.xlsx", index=False)

