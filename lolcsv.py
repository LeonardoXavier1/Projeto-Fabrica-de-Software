import pandas as pd

#
planilhas = ["2014_LoL_esports_match_data_from_OraclesElixir",
             "2015_LoL_esports_match_data_from_OraclesElixir",
             "2016_LoL_esports_match_data_from_OraclesElixir",
             "2017_LoL_esports_match_data_from_OraclesElixir",
             "2018_LoL_esports_match_data_from_OraclesElixir"]


df_referencia = pd.read_csv("2019_LoL_esports_match_data_from_OraclesElixir.csv")


for planilha in planilhas:
    df = pd.read_csv(planilha + ".csv")
    headers_referencia = df_referencia.columns.tolist()
    headers_atual = df.columns.tolist()
    indices = [headers_atual.index(header) for header in headers_referencia]
    headers_reordenados = [headers_atual[i] for i in indices]
    df = df.rename(columns=dict(zip(headers_atual, headers_reordenados)))
    df.to_csv(planilha + "_cabeçalhos_reescritos.csv", index=False)
