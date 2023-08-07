import matplotlib.pyplot as plt
import seaborn as sns


def draw_pie(data: list, label: list) -> plt.pie:
    data = [value1, value2, value3, ...]
    labels = ['label1', 'label2', 'label3', ...]
    colors = sns.color_palette("ch:s=.25,rot=-.25", as_cmap=True)
    plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
    plt.show()