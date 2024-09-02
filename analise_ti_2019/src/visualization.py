import matplotlib.pyplot as plt

def plot_state_distribution():
    labels = ["SP", "MG", "RJ", "PR", "SC", "RS", "ES"]
    sizes = [46.85, 22.13, 10.29, 8.19, 5.81, 4.83, 1.89]
    explode = (0, 0, 0, 0, 0, 0, 0.1) 

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, pctdistance=0.8)
    ax1.axis('equal') 
    plt.show()
