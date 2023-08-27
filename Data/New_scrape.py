import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

scraper = pd.read_html("https://fbref.com/en/comps/Big5/2022-2023/shooting/players/2022-2023-Big-5-European-Leagues-Stats")

print(type(scraper[0]))
scraper[0].to_csv('./Data/new_scrape.csv')