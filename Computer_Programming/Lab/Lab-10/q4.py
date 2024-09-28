import matplotlib.pyplot as plt 
def collect(l:list):
    l.sort()
    meow = dict()
    for i in l:
        if i in meow:
            meow[i] += 1
        else:
            meow[i] = 1
    x = list(meow.keys())
    y = list(meow.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(x,y, color = "green", width = 1)
    plt.yticks([])
    ax = plt.gca() 
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.show()
    ax.text(1.05, 0, 'x', transform=ax.transAxes, fontsize=12, va='center', ha='center')  # x-axis label
    ax.text(0, 1.05, 'y', transform=ax.transAxes, fontsize=12, va='center', ha='center', rotation=0)

collect([1,2,3,4,5,6,2,3,4,5,6,1,2,5,6,2,3,3,3,3,3,3,3,3,3,3,4,5,6,3,4,5,6,1,8])