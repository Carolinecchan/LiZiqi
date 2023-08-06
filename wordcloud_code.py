import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

df1 = pd.read_csv('New Year snacks 翻译.csv')
df2 = pd.read_csv('Liuzhou Luosifen翻译.csv')
text = " ".join(review for review in list(df1['英文翻译']))
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
wordcloud.to_file("first_review.png")