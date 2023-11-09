import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

def makePlot():
    with open("output2.csv") as f:
        reader = csv.reader(f)
        x_values = []
        y_values = []
        
        for row in reader:
            x_values.append(int(row[0]))
            y_values.append(int(row[13]))
            
        # Set up the plot
        fig, ax = plt.subplots()
        ax.set_xlim(min(x_values), max(x_values))
        ax.set_ylim(min(y_values), max(y_values))
        line, = ax.plot([1], [316], lw=2)
        line.set_color('dimgrey')
        
        sns.lineplot(x=[1], y=[316], ax=ax, lw=2)
        plt.fill_between(x_values, 250, 399, color="gold")
        plt.fill_between(x_values, 400, 799, color="mediumseagreen")
        plt.fill_between(x_values, 800, 1199, color="royalblue")
        plt.fill_between(x_values, 1200, 1300, color="mediumorchid")  
        plt.xlabel("GameId")
        plt.ylabel("TotalLp")
        plt.title("Ranked Climb to Masters!")

        ax.set_title('Real-time Plot')

        def update(num):
            sns.lineplot(x=x_values[:num], y=y_values[:num], ax=ax, lw=2)

        ani = animation.FuncAnimation(fig, update, frames=range(1, len(x_values)+1), repeat=True)
        plt.show()