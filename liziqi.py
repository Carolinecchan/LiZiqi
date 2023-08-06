import pandas as pd


def data_analysis(table_path: str, keyword: str) -> pd.DataFrame:
    df = pd.read_excel(table_path)
    column_name = '含' + keyword
    non_nan = ~df["中文翻译"].isna()
    df.loc[(df["中文翻译"].str.contains(keyword, regex=False)) & non_nan, column_name] = df['中文翻译']
    return df[column_name].dropna()


def comment_sum(df1: pd.DataFrame, df2: pd.DataFrame) -> int:
    return len(df1)+len(df2)


print(data_analysis('Liuzhou Luosifen翻译.xlsx','美食').to_string())
print(data_analysis('New Year snacks 翻译.xlsx','美食').to_string())
print('评论总数： ',comment_sum(data_analysis('Liuzhou Luosifen翻译.xlsx', '美食'), data_analysis('New Year snacks 翻译.xlsx', '美食')))
