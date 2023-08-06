import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

df1 = pd.read_csv('New Year snacks 翻译.csv')
df2 = pd.read_csv('Liuzhou Luosifen翻译.csv')
df1['英文翻译'] = df1['英文翻译'].astype(str)
df2['英文翻译'] = df2['英文翻译'].astype(str)
text1 = " ".join(review for review in df1['英文翻译'])
text2 = " ".join(review for review in df2['英文翻译'])
text = text1 + " " + text2
wordcloud = WordCloud(max_font_size=100, max_words=300, background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
wordcloud.to_file("first_review.png")