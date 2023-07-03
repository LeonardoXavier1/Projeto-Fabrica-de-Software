import pandas as pd


planilhas = ["2014_LoL_esports_match_data_from_OraclesElixir",
             "2015_LoL_esports_match_data_from_OraclesElixir",
             "2016_LoL_esports_match_data_from_OraclesElixir",
             "2017_LoL_esports_match_data_from_OraclesElixir",
             "2018_LoL_esports_match_data_from_OraclesElixir"]


df_referencia = pd.read_csv("2019_LoL_esports_match_data_from_OraclesElixir.csv")


headers_referencia = df_referencia.columns.tolist()


for planilha in planilhas:
    df = pd.read_csv(planilha + ".csv")
    df = df.rename(columns=dict(zip(df.columns, headers_referencia)))
    df.to_csv(planilha + "_cabeçalhos_reescritos.csv", index=False)