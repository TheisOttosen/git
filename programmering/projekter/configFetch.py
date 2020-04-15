from bs4 import BeautifulSoup as BS4
import requests

URL = "https://pastebin.com/CuTpZ2qX"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
page = requests.get(URL, headers=headers)
soup = BS4(page.content, "html.parser")

cfg = soup.find(id="paste_code").get_text()

print(cfg)

text_file = open("G:\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg\EXEC.cfg", "w")
n = text_file.write(cfg)
text_file.close()