import pandas as pd

df = pd.read_excel('MOCK_DATA.xlsx')

modelo_inserido = input('Insira o modelo do carro que quer pesquisar: ')

if isinstance(modelo_inserido, str):
    df_filtered = df[df['car_model'] == modelo_inserido]
    print(f'\nExibindo resultados para: {modelo_inserido}:\n\n', df_filtered)
else:
    print('Entrada inválida. Tente novamente.\n')
