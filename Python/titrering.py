import matplotlib.pyplot as plt
import pandas as pd


def main():
    data = {"Volume": [0.0, 0.5, 1.0, 1.5, 2.0], "pH": [2, 1, 8, 9, 12]}
    df = pd.DataFrame(data)
    print(df)
    df.set_index("Volume", inplace=True)
    df["pH"].plot()
    plt.show()

if __name__ == '__main__':
    main()
