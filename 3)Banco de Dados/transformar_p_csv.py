import pandas as pd
import chardet

#TRANSFORMAR DADOS PARA CSV ACEITÁVEL NOS BANCOS DE DADOS
# Caminho do arquivo
arquivo = '2023/1T2023.csv'

# Detecta a codificação do arquivo
with open(arquivo, 'rb') as f:
    result = chardet.detect(f.read())
encoding_detectado = result['encoding']
print(f'Codificação detectada: {encoding_detectado}')

# Tentar carregar o arquivo CSV corretamente
try:
    df = pd.read_csv(arquivo, encoding=encoding_detectado, sep=';', on_bad_lines='warn', dtype=str)

    # Exibi informações principais
    print("Primeiras linhas do dataframe carregado:")
    print(df.head())

    # Salvar o arquivo modificado

    df.to_csv('2023/1T2023_modificado.csv', encoding='utf-8', sep=',', index=False)

    print(f'Arquivo modificado salvo')
except Exception as e:
    print(f'Ocorreu um erro ao tentar ler o arquivo: {e}')




# FILTRAR E EXCLUIR LINHAS ESPECIFICAS
'''# Nome do arquivo de entrada e saída
arquivo_entrada = "2023/1T2023_filtrado2.csv"  # Substituir pelo nome do seu arquivo
arquivo_saida = "2023/1T2023_filtrado3.csv"

# Carregar o arquivo CSV, detectando a codificação
df = pd.read_csv(arquivo_entrada, encoding="latin1", sep=";", dtype=str)

# Remover espaços extras e caracteres invisíveis da coluna REG_ANS
df["REG_ANS"] = df["REG_ANS"].str.strip().str.replace(r'\s+', '', regex=True)

# Filtrar as linhas [linha] ------ [valor]
df_filtrado = df[df["REG_ANS"] != "361038"]

# Salvar o novo arquivo CSV sem as linhas removidas
df_filtrado.to_csv(arquivo_saida, index=False, sep=";", encoding="utf-8")

print(f"Arquivo salvo como {arquivo_saida}")'''
