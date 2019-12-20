#importspp0
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.56786"}

dataark = pd.read_excel("p-e.xlsm") # læser datasæt.
webadresser = dataark.adresser # laver en variabel med adresser.
