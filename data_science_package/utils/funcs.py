import pandas as pd

def str_to_float(df, columns):
    return df.apply(lambda x: pd.to_numeric(x))