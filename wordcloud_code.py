import numpy as np
import pandas as pd
from os import path
import stylecloud

import matplotlib.pyplot as plt

df1 = pd.read_csv('New Year snacks 翻译.csv')
df2 = pd.read_csv('Liuzhou Luosifen翻译.csv')
df1['英文翻译'] = df1['英文翻译'].astype(str)
df2['英文翻译'] = df2['英文翻译'].astype(str)
text1 = " ".join(review for review in df1['英文翻译'])
text2 = " ".join(review for review in df2['英文翻译'])
text = text1 + " " + text2
# wordcloud = WordCloud(max_font_size=100, max_words=300, background_color="white").generate(text)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()
# wordcloud.to_file("first_review.png")
stylecloud.gen_stylecloud(text=text,
                          size=512,
                          icon_name='fas fa-heart',
                          palette='cartocolors.sequential.Magenta_5',
                          output_name='test_ciyun.png')
# stylecloud.gen_stylecloud(text=text,
#                           size=512,
#                           icon_name='fas fa-heart',
#                           palette='tableau.Tableau_20',
#                           output_name='test_ciyun.png')