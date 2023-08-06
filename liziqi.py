import pandas as pd

dict1 = {}
df = pd.read_excel("/Users/pro/Desktop/New Year snacks 翻译.xlsx")
non_nan = ~df["中文翻译"].isna()
df.loc[(df["中文翻译"].str.contains('喜欢',regex=False))&non_nan,'含喜欢'] = df['中文翻译']
dict1['含喜欢'] = 3663
df.loc[(df["中文翻译"].str.contains('好',regex=False))&non_nan,'含好'] = df['中文翻译']
dict1['含好'] = 5839

if __name__ == '__main__':
    df['含喜欢'].to_string()
    df['含喜欢'].info()
    df['含好'].to_string()
    df['含好'].info()