import pandas as pd
# # Define o número máximo de linhas a serem lidas
# max_linhas = 1

# # Lê as primeiras 'max_linhas' linhas do arquivo CSV
# data = pd.read_csv('2022_LoL_esports_match_data_from_OraclesElixir.csv', nrows=max_linhas)

# # Converte o DataFrame em JSON
# json_data = data.to_json(orient='records')

# # Salva o JSON em um arquivo
# with open('dados.json', 'w') as file:
#     file.write(json_data)

# print(data)