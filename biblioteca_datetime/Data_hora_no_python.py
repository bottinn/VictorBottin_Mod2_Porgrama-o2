"""Pytz é uma biblioteca do Python que permite calcular 
fusos horários e resolver problemas com horários ambiguos no final do horário de verão 
O tzdata é um "pacote" de dados de Python que fornece dados de fuso horário IANA .
Ele é principalmente usado pelo módulo "zoneinfo"
da biblioteca padrão, 
mas  também pode ser usado como fonte de dados de fuso horário para outras bibliotecas de fuso horário;
"""
#Exercício 1
'''OBtenha a data e hora atual do computador em que está executando, e as imprime no terminal do Visual Studio Code'''
from datetime import datetime
DataeHoraAtual = datetime.now()
print(DataeHoraAtual)

#Exercício 2
'''Obtenha a data atual (dia, mês, ano) e mostre na tela'''
Hoje = datetime.today()
print(Hoje)
#Exercício 3
from datetime import datetime, date, time, timedelta
agora = datetime.now()
DataFormada = agora.strftime("%d/%m/%Y")
HoraFormada = agora.strftime("%H:%M:%S")
print(DataFormada)
print(HoraFormada)

from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') 
DataAgoraNoPaisQueFoiLocalizadoLocale = datetime.now()
Data_Formada = DataAgoraNoPaisQueFoiLocalizadoLocale.strftime("%x")
Hora_formada = DataAgoraNoPaisQueFoiLocalizadoLocale.strftime("%X")
print("Data Formada:", Data_Formada)
print("Hora Formada:", Hora_formada)
