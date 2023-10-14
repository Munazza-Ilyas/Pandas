import os
import pandas as pd

IN_PATH = os.path.join("data", "countypres_2000-2020.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "election_report_pandas.csv")

df = pd.read_csv(IN_PATH)  

#Count
df_2020 = df[df['year'] == 2020]


result = df_2020.groupby(['year', 'state_po', 'candidate'])['candidatevotes'].sum().reset_index()

#Sort
sorted_result = result.sort_values(by=['state_po', 'candidatevotes'], ascending=[True, False])
sorted_result = sorted_result.rename(columns={'candidatevotes': 'votes'})
sorted_result = sorted_result.rename(columns={'state_po': 'state_code'})
sorted_result['votes'] = sorted_result['votes'].astype(int)

#Write to csv

columns_to_include = ["year", "state_code", "candidate", "votes"]
sorted_result.to_csv(OUTPUT_PATH, columns=columns_to_include, index=False)

