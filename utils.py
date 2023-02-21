import datetime
import matplotlib.pyplot as plt

# helper function to convert dates
def humanize_unixtime(unix_time):
    time = datetime.fromtimestamp(int(unix_time)).strftime('%d-%m-%Y %H.%M')
    return time


def clean_dataframe(df):
    # drop columns that we don't need
    df['charStats'] = df['charStats'].astype(str)
    df.drop(columns=['mode2', 'quoteLength', 'afkDuration', 'tags', 'bailedOut', 'blindMode', 'lazyMode', 'difficulty', 'funbox', 'numbers', 'punctuation', 'language'], inplace=True)

    # sort values by unix timestamp
    df.sort_values('timestamp', inplace=True)

    # clean the isPb column
    df['isPb'].fillna(False, inplace=True)
    df['isPb'] = df['isPb'].astype(bool)
    return df


def plot_wpm(df):
    plt.scatter(df.index, df['wpm'], c='blue')
    plt.title('WPM (January 2021 to Present)')
    plt.xlabel('test #')
    plt.ylabel('wpm')
    plt.show()
