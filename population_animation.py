import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FFMpegWriter

def setup_plot_style(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='y', which='both', left=False)
    ax.tick_params(axis='x', which='both', bottom=False)
    ax.set_xlabel('Total Population')
    ax.set_title('Top 10 Countries by Population (in millions)') 

def add_year_text(ax, year):
    ax.text(0.9, 0.1, str(year), transform=ax.transAxes, ha='center', fontsize=20)

def create_animation(df):
    frames = df['Time'].unique()
    fig, ax = plt.subplots(figsize=(12, 6))
    
    def animate(frame):
        ax.clear()
        pop_data_frame = df[df['Time'] == frame]
        top_countries = (
            pop_data_frame.nlargest(10, 'TPopulation1Jan')
            .sort_values('TPopulation1Jan', ascending=True)
        )
        ax.barh(top_countries['Location'], top_countries['TPopulation1Jan'])

        for i, row in top_countries.iterrows():
            ax.text(row['TPopulation1Jan'], row['Location'], f"{row['TPopulation1Jan']:,.2f}", va='center')

        setup_plot_style(ax)
        add_year_text(ax, frame)
        plt.tight_layout()

    anim = animation.FuncAnimation(fig, animate, frames=frames, interval=200)
    return anim

if __name__ == '__main__':
    try:
        df = pd.read_csv('./data/cleaned-data.csv')
        anim = create_animation(df)
        anim.save('video_pop.mp4', writer='ffmpeg', fps=10)
    except FileNotFoundError:
        print("Error: File './data/cleaned-data.csv' not found.")
