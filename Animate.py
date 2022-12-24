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

def read_next_number(file):

    num_str = file.readline()
    if num_str != "`\n" and num_str != '':
        num = int(num_str.replace("\n", ""))
        return num
    return None

def alg_title(alg):
    global title
    title = titles[alg]
    return title

def readAndAnimate(MainFile, bufFile1, bufFile2):
    Maindata=[]
    bufData1=[]
    bufData2=[]
    with open(MainFile, 'r') as Main, open (bufFile1, 'r') as Buf1, open (bufFile2,'r') as Buf2:
        num=read_next_number(Main)
        while num is not None:
            Maindata.append(num)
            num=read_next_number(Main)

        num=read_next_number(Buf1)
        while num is not None:
            bufData1.append(num)
            num=read_next_number(Buf1)

        num=read_next_number(Buf2)
        while num is not None:
            bufData2.append(num)
            num=read_next_number(Buf2)
    Plot (Maindata, bufData1, bufData2)

       
        
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
    # plt.xlabel(title)

    camera.snap()

def Show_Animation(animation_interval):
    animation = camera.animate(interval=animation_interval)
    plt.show()
