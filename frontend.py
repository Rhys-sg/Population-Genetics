import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure

def create_plot():
    # Create a figure and a set of subplots
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Plot something (example: a simple line plot)
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16])

    return fig


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Matplotlib in Tkinter")

    # Create the plot using the function
    fig = create_plot()

    # Create a canvas and add the figure to it
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    # Place the canvas on the Tkinter window
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Start the Tkinter main loop
    tk.mainloop()

if __name__ == "__main__":
    main()
