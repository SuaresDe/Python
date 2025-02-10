import requests
import xlsxwriter
import os
from datetime import datetime

def get_quote(currency):
    url = f"https://economia.awesomeapi.com.br/json/last/{currency}-BRL"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        return float(dados[f"{currency}BRL"]["bid"])  
    else:
        return None

def create_spreadsheet():
    today = datetime.today().strftime("%d-%m-%Y")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f"dollar-euro-quote-{today}.xlsx")

    spreadsheet = xlsxwriter.Workbook(file_path)
    spreadsheet1 = spreadsheet.add_worksheet()

    decimal_format = spreadsheet.add_format({'num_format': '0.00'})

    spreadsheet1.write("A1", "Currency")
    spreadsheet1.write("B1", "Quote")

    dolar = get_quote("USD")
    euro = get_quote("EUR")

    spreadsheet1.write("A2", "USD")
    spreadsheet1.write("B2", dolar, decimal_format)  

    spreadsheet1.write("A3", "EUR")
    spreadsheet1.write("B3", euro, decimal_format)   

    spreadsheet.close()
    print(f"Arquivo salvo em: {file_path}")

def main():
   create_spreadsheet()
        

if __name__ == "__main__":
    main()