import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def draw_pie(data: list, labels: list, name: str) -> plt.pie:
    colors = sns.color_palette("ch:s=.25,rot=-.25")
    plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
    plt.savefig(name + ".png", dpi=300)


data = [40582, 7168, 2014, 2092, 1905, 777, 1321, 15692, 9102, 3051, 4852]
labels = ['English', 'Chinese', 'Arabic', 'Russian', 'Spanish', 'French', 'Portuguese', 'Languages of Other Asian Countries', 'Languages of Other European Countries', 'Languages of Other African Countries', 'Emoji']
draw_pie(data=data, labels=labels, name='Language distribution')
