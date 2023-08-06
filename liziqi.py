import pandas as pd
import os


def data_analysis(table_path: list, keyword: str) -> int:
    df1 = pd.read_csv(table_path[0])
    df2 = pd.read_csv(table_path[1])
    column_name = '含' + keyword
    column_chinese = column_name + '中文翻译'
    non_nan_1 = ~df1["英文翻译"].isna()
    df1.loc[(df1["英文翻译"].str.contains(keyword, regex=False)) & non_nan_1, column_name] = df1['英文翻译']
    df1.loc[(df1["英文翻译"].str.contains(keyword, regex=False)) & non_nan_1, column_chinese] = df1['中文翻译']
    non_nan_2 = ~df2["英文翻译"].isna()
    df2.loc[(df2["英文翻译"].str.contains(keyword, regex=False)) & non_nan_2, column_name] = df2['英文翻译']
    df2.loc[(df2["英文翻译"].str.contains(keyword, regex=False)) & non_nan_2, column_chinese] = df2['中文翻译']
    re_df1 = df1.loc[:, ['cid', 'votes', column_name, column_chinese]].dropna()
    re_df2 = df2.loc[:, ['cid', 'votes', column_name, column_chinese]].dropna()
    re_df1 = re_df1.sort_values(by='votes', ascending=False)
    re_df2 = re_df2.sort_values(by='votes', ascending=False)
    sum1 = str(len(re_df1))
    sum2 = str(len(re_df2))
    sum = sum1 + sum2
    os.makedirs(column_name, exist_ok=True)
    path1_csv = column_name + '/New' + sum1 + column_name + '.csv'
    # path1_xlsx = column_name + '/New' + sum1 + column_name + '.xlsx'
    path2_csv = column_name + '/Luo' + sum2 + column_name + '.csv'
    # path2_xlsx = column_name + '/Luo' + sum2 + column_name + '.xlsx'
    re_df1.to_csv(path1_csv)
    re_df2.to_csv(path2_csv)
    # re_df1.to_excel(path1_xlsx)
    # re_df2.to_excel(path2_xlsx)
    return sum


list_file = ['New Year snacks 翻译.csv', 'Liuzhou Luosifen翻译.csv']
data_analysis(list_file, 'culture')
