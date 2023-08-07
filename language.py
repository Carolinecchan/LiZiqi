import pandas as pd


def language_analysis(table_path: list) -> pd.DataFrame:
    dfl = pd.read_csv('语种类型及数量.csv')
    dfl.drop(columns=['数字'], inplace=True)
    df1 = pd.read_csv(table_path[0])
    df2 = pd.read_csv(table_path[1])
    df1.replace(to_replace=['unknown', 'Sinhala 僧伽罗语', 'sinhala 僧伽罗语', '中文（繁体）', '布尔语(南非荷兰语)'], value=['Emoji', '僧伽罗语', '僧伽罗语', '中文', '布尔语'], inplace=True, regex=False)
    df2.replace(to_replace=['unknown', 'Sinhala 僧伽罗语', 'sinhala 僧伽罗语', '中文（繁体）', '布尔语(南非荷兰语)'], value=['Emoji', '僧伽罗语', '僧伽罗语', '中文', '布尔语'], inplace=True, regex=False)
    df1 = df1['语言'].value_counts().rename_axis('语种').reset_index(name='counts')
    df2 = df2['语言'].value_counts().rename_axis('语种').reset_index(name='counts')
    df = df1.merge(df2, how='outer', on='语种')
    df.fillna(0, inplace=True)
    df['count'] = df['counts_x'] + df['counts_y']
    df.drop(columns=['counts_x', 'counts_y'], inplace=True)
    df['count'] = df['count'].astype(int)
    df = pd.merge(df, dfl, on='语种', how='left')
    df.loc[df['语种'] == 'Emoji', 'Language'] = 'Emoji'
    df.loc[df['语种'] == 'Emoji', '地区'] = 'Emoji'
    df.loc[df['语种'] == '马拉雅拉姆语', 'Language'] = 'Malayalam'
    df.loc[df['语种'] == '马拉雅拉姆语', '地区'] = '亚洲'
    df.loc[df['地区'] == '亚洲', '地区'] = 'Languages of Other Asian Countries'
    df.loc[df['地区'] == '欧洲', '地区'] = 'Languages of Other European Countries'
    df.loc[df['地区'] == '非洲', '地区'] = 'Languages of Other African Countries'
    df.to_csv('Language.csv')
    return df


list_file = ['New Year snacks 翻译.csv', 'Liuzhou Luosifen翻译.csv']
a = language_analysis(list_file)
print(language_analysis(list_file))
a.to_excel('language.xlsx')
