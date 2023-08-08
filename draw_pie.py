import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import seaborn as sns
import numpy as np

from language import language_area_analysis


def draw_pie_title(data: list, label: list, name: str) -> plt.pie:
    # plt.figure(figsize=(15,8))
    # patches, texts, autotexts = plt.pie(data, labels, autopct='%1.2f%%', pctdistance=0.7, textprops={'fontsize': 10})
    # for autotext in autotexts:
    #     autotext.set_horizontalalignment('center')
    #     autotext.set_fontstyle('italic')
    # plt.title(name, fontdict={"fontsize": 16}, pad=20)
    # plt.savefig(name + ".png", dpi=500)

    porcent = [100*i/sum(data) for i in data]
    colors = sns.color_palette()
    patches, texts = plt.pie(data, startangle=90, radius=1.2, colors=colors)
    labels = ['{0} - {1:1.2f} %'.format(i, j) for i,  j in zip(label, porcent)]
    sort_legend = True
    if sort_legend:
        patches, labels, dummy = zip(*sorted(zip(patches, labels, data), key=lambda x: x[2], reverse=True))
    plt.legend(patches, labels, loc='best', bbox_to_anchor=(-0.1, 1.), fontsize=8)
    plt.savefig(name + ".png", bbox_inches='tight', dpi=500)


def draw_pie_bar_title(data: list, labels: list, explode: list, bar_ratios: list, bar_labels: list, name: str) -> plt.pie:
    # make figure and assign axis objects
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
    fig.subplots_adjust(wspace=0)
    # pie chart parameters
    # overall_ratios = [.27, .56, .17]
    # labels = ['Approve', 'Disapprove', 'Undecided']
    # explode = [0.1, 0, 0]
    # rotate so that first wedge is split by the x-axis
    angle = -180 * data[0]
    wedges, *_ = ax1.pie(data, autopct='%1.1f%%', startangle=angle, labels=labels, explode=explode)
    # bar chart parameters
    # bar_ratios = [.33, .54, .07, .06]
    # bar_labels = ['Under 35', '35-49', '50-65', 'Over 65']
    bottom = 1
    width = .2
    # Adding from the top matches the legend.
    for j, (height, label) in enumerate(reversed([*zip(bar_ratios, bar_labels)])):
        bottom -= height
        bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label, alpha=0.1 + 0.03 * j)
        ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')
    ax2.set_title(name)
    ax2.legend()
    ax2.axis('off')
    ax2.set_xlim(- 2.5 * width, 2.5 * width)
    # use ConnectionPatch to draw lines between the two plots
    theta1, theta2 = wedges[0].theta1, wedges[0].theta2
    center, r = wedges[0].center, wedges[0].r
    bar_height = sum(bar_ratios)
    # draw top connecting line
    x = r * np.cos(np.pi / 180 * theta2) + center[0]
    y = r * np.sin(np.pi / 180 * theta2) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData, xyB=(x, y), coordsB=ax1.transData)
    con.set_color([0, 0, 0])
    con.set_linewidth(4)
    ax2.add_artist(con)
    # draw bottom connecting line
    x = r * np.cos(np.pi / 180 * theta1) + center[0]
    y = r * np.sin(np.pi / 180 * theta1) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData, xyB=(x, y), coordsB=ax1.transData)
    con.set_color([0, 0, 0])
    ax2.add_artist(con)
    con.set_linewidth(4)
    plt.savefig(name + ".png", dpi=500)


data = [3051, 15692, 40582, 7168, 2014, 2092, 1905, 777, 1321, 9102, 4852]
labels = ['Languages of Other African Countries', 'Languages of Other Asian Countries', 'English', 'Chinese', 'Arabic', 'Russian', 'Spanish', 'French', 'Portuguese', 'Languages of Other European Countries', 'Emoji']
# explode = [0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# df = pd.read_csv('Language.csv')
# df = df.loc[df['地区'] == 'Languages of Other African Countries']
# bar_ratios = df['count'].to_list()
# bar_ratios = [i/sum(bar_ratios) for i in bar_ratios]
# bar_labels = df['Language'].to_list()
# draw_pie_title(data=data, labels=labels, explode=explode, bar_ratios=bar_ratios, bar_labels=bar_labels, name='Language distribution')
# print(bar_ratios, bar_labels)

draw_pie_title(data=data, label=labels, name='Language distribution')
