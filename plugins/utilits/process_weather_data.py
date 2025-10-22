import pandas as pd


def pivot_weather_data(df: pd.DataFrame) -> pd.DataFrame:
    df_pivot = df.groupby(['time', 'city'])['temperature'].mean().unstack()
    return df_pivot


def calculate_all_diffs(df_pivot: pd.DataFrame) -> pd.DataFrame:
    cities = df_pivot.columns.tolist()
    diff_dict = {}

    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            col_name = f"{cities[i]}-{cities[j]}"
            diff_dict[col_name] = df_pivot[cities[i]] - df_pivot[cities[j]]

    df_diff = pd.DataFrame(diff_dict, index=df_pivot.index)
    return df_diff
