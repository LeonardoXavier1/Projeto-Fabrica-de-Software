import pandas as pd
import glob
import os

diretorio = "C:/trabalhosFacul/py"  # Altere para o diretório correto onde estão suas planilhas


padrao = "*_LoL_esports_match_data_from_OraclesElixir*.csv"
caminhos = glob.glob(os.path.join(diretorio, padrao))
dataframes = []

for caminho in caminhos:
    df = pd.read_csv(caminho)
    dataframes.append(df)

df_final = pd.concat(dataframes, ignore_index=True)
df_final.to_csv("planilha_completa.csv", index=False)
