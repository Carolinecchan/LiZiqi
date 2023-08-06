import pandas as pd

def data_analysis(table_path: str, keyword: str) -> pd.DataFrame:
    df = pd.read_excel(table_path)
    column_name = '含' + keyword
    non_nan = ~df["中文翻译"].isna()
    df.loc[(df["中文翻译"].str.contains(keyword,regex=False))&non_nan,column_name] = df['中文翻译']
    return df[keyword]