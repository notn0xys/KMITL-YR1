import matplotlib.pyplot as plt 
def pie_chart(x:list):
    nyan1 = dict()
    for i in x:
        if i not in nyan1:
            nyan1[i] = 1
        else:
            nyan1[i] += 1
    plt.pie(nyan1.values())
    plt.show() 
pie_chart([3,1,3,3,2,3,3,2,3,2,4,3,3,3,3,4,3,4,3,3,3,4,3])
