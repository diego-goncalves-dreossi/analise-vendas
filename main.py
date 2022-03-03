# Importar no código:
# Twilio é uma biblioteca onde podemos trabalhar com SMS 
# Pandas é uma biblioteca para analise de dados
# Openpyxl , assim como pandas, é boa para integar o Python com Excel
import os
import pandas as pd
from twilio.rest import Client
import credenciais as c

# Apaga tela
os.system('cls')
# Passo a passo de solução

# Abrir os arquivos em Excel
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

# Conta SID de twilio.com/console




for m in lista_meses:
    # Busca todos os arquivos baseado nos meses listados
    tabela_vendas = pd.read_excel(f'dados/{m}.xlsx')
    
    print(f'{m.capitalize()}',end=': ')
    # Se algum valor da coluna
    if(tabela_vendas['Vendas'] > 55000).any():
        # loc[linha,coluna] é um método que retorna o valor de uma tabela, usando linha e coluna como parâmetros. Nesse caso a linha se encontra usando uma condição. O .values[0] retorna o valor.
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas =  tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]

        """
        print('\n',end='')
        print('-'*35)
        print(f'Encontrou alguém que bateu a meta.\nVendedor: {vendedor}\nVendas: {vendas}')
        print('-'*35)
        """

        # Enviar SMS
        mensagem = c.client.messages.create(to='+5516991708956', from_='+19033212069' ,body=f'Encontrou alguém que bateu a meta.\nVendedor: {vendedor}\nVendas: {vendas}')
       
        print(mensagem.sid)
        
    else:
        print('Não encontrado nenhum vendedor que bateu a meta.') 


# print(tabela_vendas)

# Para cada arquivo:

# Verificar se algum valor na coluna vendas daquele arquivo é 55 mil.
# Se for maior do que 55 mil : enviamos um SMS com o Nome, o mês e as vendas do vendedor.



