import pandas as pd

# Establishing Team Names Data
teamNames = pd.read_excel("Team Naming Conventions.xlsx")
teamNames.to_csv("teamnames.csv", index=None, header=True)

teamNames_df = pd.DataFrame(teamNames)
teamNames_df.columns = ['Team', 'Abbr']

# Establishing Player Stats Data
file_path = "19-20_PPG_table.csv"
stats = pd.read_csv(file_path, encoding='ISO-8859–1')

name_split = stats["Player"].str.split(" ", n=1, expand=True)
stats["First Name"] = name_split[0]
stats["Last Name"] = name_split[1]
stats.drop(columns=["Player"], inplace=True)

stats_df = stats[["Rk", "First Name", "Last Name", "Pos", "Age", "Tm", "G", "GS", "MP", "FG", "FGA", "FG%", "3P", "3PA",
                  "3P%", "2P", "2PA", "2P%", "eFG%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]]

# Establishing Player Salaries Data
salaries_df = pd.read_html(
    'https://www.spotrac.com/nba/contracts/sort-value/drafted/limit-500/')[0]

temp_df = salaries_df["Player"].str.split(" ", n=10, expand=True)
salaries_df['First Name'] = temp_df[0]
salaries_df['Last Name'] = temp_df[1]
salaries_df.drop(columns=["Player"], inplace=True)

salaries_df = salaries_df[['Rank', 'First Name', 'Last Name',
                           'Signed Age', 'Yrs', 'Value', 'AAV', 'Sign Bonus']]
