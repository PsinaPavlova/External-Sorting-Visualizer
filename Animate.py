import matplotlib.pyplot as plt
from celluloid import Camera

fig, (ax1, ax2, ax3) = plt.subplots(3)
camera = Camera(fig)
comparisons = 0
mainGraph = ax1.bar
buf1Graph = ax2.bar
buf2Graph = ax3.bar
titles = {'1': "Natural Merge Sort",
          '2': 'Balanced Merge Sort'}


def alg_title(alg):
    global title
    title = titles[alg]
    return title


def Plot(mainData, buf1, buf2):
    x = list(range(len(mainData)))

    colors = list(len(mainData) * 'b')
    ax1.bar(x, mainData, color=colors)

    x = list(range(len(buf1)))
    colors = list(len(buf1) * 'b')
    ax2.bar(x, buf1, color=colors)

    x = list(range(len(buf2)))
    colors = list(len(buf2) * 'b')
    ax3.bar(x, buf2, color=colors)

    # plt.title(title)
    plt.show()
    plt.xlabel(title)

    camera.snap()


alg_title('1')
Plot([1, 2, 4, 5, 4, 5, 6, 7, 8, 9, 9], [
     8, 5, 3, 5, 1, 2, 3, 4, 5, 5], [7, 4, 2, 3])
