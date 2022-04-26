import requests
import pandas as pd


def clean_country(country_name: str) ->str:
    """
    clean international_team value
    :param country_name: international team name
    :return: clean country name
    """
    if '(' in country_name:
        country_name_clean = country_name.split(' ')[0]
    else:
        country_name_clean = country_name
    return country_name_clean

#Scrape_URL

def scrape_url(rugby_url: str)-> pd.DataFrame:
    """
    scrape data from rugby wiki page

    :param rugby_url: rugby records url
    :return: raw dataframe
    """
    page = requests.get(rugby_url)
    df = pd.read_html(page.text)[0]
    return df

#clean df
def clean_df(df: pd.DataFrame)-> pd.DataFrame:
    """
    clean rugby df
    :param df: raw df
    :return: clean df
    """
    df.drop(columns=['Tries', 'Con', 'Pen', 'DG', 'Ref', 'TierRank'], inplace=True)
    df.columns = ["world_rank", 'points', "player", 'position', 'international_team', 'years_active', 'caps',
                  'average_points_per_game']
    df['international_team'] = df['international_team'].apply(clean_country)
    return df
if __name__ == '__main__':
    rugby_url = "https://en.wikipedia.org/wiki/List_of_leading_rugby_union_test_point_scorers"

    df = scrape_url(rugby_url)
    df_clean = clean_df(df)
    print(df_clean)

    df_clean.to_csv('rugby.csv', index = False)

