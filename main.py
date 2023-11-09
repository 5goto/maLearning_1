import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings(action='once')

pd.set_option('display.max_columns', None)

data_file = pd.read_csv('./data/acquiredDataset.csv')
data_file.iloc[:, 2:10] *= 1e-6


def get_metadata(dataframe):
    '''
    A function that fetches all the Metadata Information about the Dataframe
    This function can be reused for all Pandas Dataframe
    '''
    print("\nBASIC INFORMATION\n")
    print(dataframe.info())
    print("=" * 100)
    print("STATISTICAL INFORMATION")
    print("=" * 100)
    print("Dataframe Shape\n", dataframe.shape)
    print("=" * 100)
    print("Number of Duplicate Rows\n", dataframe.duplicated().sum())
    print("=" * 100)
    print("NULL Values Check")
    print(dataframe.isnull().sum())
    print("=" * 100)


def build_and_show_pair(data):
    plt.figure(figsize=(10, 8), dpi=80)
    sns.pairplot(data, plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
    plt.show()


def build_and_show_bar_cart(data):
    sns.pairplot(data, kind="scatter", hue="attention", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
    plt.show()


if __name__ == '__main__':
    get_metadata(data_file)
    build_and_show_pair(data_file)
    build_and_show_bar_cart(data_file)
