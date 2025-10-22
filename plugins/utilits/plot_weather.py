import os
import matplotlib.pyplot as plt

def plot_weather(df_pivot):
    plt.figure(figsize=(12, 6))

    for city in df_pivot.columns:
        plt.plot(df_pivot.index, df_pivot[city], marker='o', label=city)

    plt.title("Temperature in different cities")
    plt.xlabel("Date")
    plt.ylabel("Temperature, °C")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    folder = '/home/dimaa/airflow/plugins/diagrams'
    os.makedirs(folder, exist_ok=True)

    files = [f for f in os.listdir(folder) if f.startswith("plot_") and f.endswith(".png")]
    next_num = len(files) + 1
    filename = os.path.join(folder, f"plot_{next_num}.png")

    plt.savefig(filename)
    plt.close()
    print(f"Saved: {filename}")
