import matplotlib
import pandas as pd


def main():
    data = {"Volume": [0.0, 0.5, 1.0, 1.5, 2.0], "pH": [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)
    print(df)



if __name__ == '__main__':
    main()
