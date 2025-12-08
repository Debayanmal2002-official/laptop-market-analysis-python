import pandas as pd
import numpy as np

def simple_impute_median(d_f, value_col, group_col):
    d_f[value_col] = d_f[value_col].fillna(d_f.groupby(group_col)[value_col].transform('median'))
    d_f[value_col] = d_f[value_col].fillna(d_f[value_col].median())
    return d_f

def impute_by_group_mode(
        df: pd.DataFrame,
        value_col: str,
        group_col
) -> pd.Series:
    from typing import Union, List
    group_col: Union[str, List[str]]
    def get_group_mode(series):
        mode_values = series.mode()
        return mode_values.iloc[0] if not mode_values.empty else pd.NA
    mode_fill_values = df.groupby(group_col)[value_col].transform(get_group_mode)
    imputed_series = df[value_col].fillna(mode_fill_values)
    return imputed_series

def clean_col_by_list(d_f, col, not_in_col_list ):
    # Remove Wrong Data Type
    pattern_1 = '|'.join(map(str, not_in_col_list))
    mask = d_f[col].str.contains(pattern_1, case=False, na=False)
    d_f.loc[mask, col] = np.nan
    return d_f

def normalize_col_by_list(d_f, col, col_list):
    # Replace Data
    flat_col_list = {old: new for new, group in col_list.items() for old in group}
    for old, new in flat_col_list.items():
        contains_mask = d_f[col].astype(str).str.contains(old, case=False, na=False)
        d_f.loc[contains_mask, col] = new
    return d_f