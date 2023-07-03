import pandas as pd
import os


caminho = "C:/trabalhosFacul/py/"  # Use "/" em vez de "\"

planilha_referencia = "2019_LoL_esports_match_data_from_OraclesElixir"
planilhas = [
    "2014_LoL_esports_match_data_from_OraclesElixir",
    "2015_LoL_esports_match_data_from_OraclesElixir",
    "2016_LoL_esports_match_data_from_OraclesElixir",
    "2017_LoL_esports_match_data_from_OraclesElixir",
    "2018_LoL_esports_match_data_from_OraclesElixir"
]

caminho_planilha_referencia = os.path.join(caminho, f"{planilha_referencia}.csv")


df_referencia = pd.read_csv(caminho_planilha_referencia)


for planilha in planilhas:
    caminho_planilha_renomeada = os.path.join(caminho, f"{planilha}_renomeado.csv")
    df_renomeada = pd.read_csv(caminho_planilha_renomeada)
    colunas_referencia = df_referencia.columns
    df_renomeada.columns = colunas_referencia
    caminho_planilha_atualizada = os.path.join(caminho, f"{planilha}_atualizado.csv")
    df_renomeada.to_csv(caminho_planilha_atualizada, index=False)
