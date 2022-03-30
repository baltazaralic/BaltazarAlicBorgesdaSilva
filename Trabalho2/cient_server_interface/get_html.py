from bs4 import BeautifulSoup
from urllib3 import *

http = PoolManager()
url1 = "https://thebookisonthetable.herokuapp.com/state/sala"
url2 = "https://thebookisonthetable.herokuapp.com/state/cozinha"
url3 = "https://thebookisonthetable.herokuapp.com/state/quarto"
url4 = "https://thebookisonthetable.herokuapp.com/state/banheiro"
nome = []
nome.append("sala")
nome.append("cozinha")
nome.append("quarto")
nome.append("banheiro")
rawa = []
rawa.append("")
rawa.append("")
rawa.append("")
rawa.append("")

def get_html_f():
    global rawa
    html1 = http.request('GET', url1)
    html2 = http.request('GET', url2)
    html3 = http.request('GET', url3)
    html4 = http.request('GET', url4)
    raw = []
    raw.append(str(BeautifulSoup(html1.data, "html.parser")))
    raw.append(str(BeautifulSoup(html2.data, "html.parser")))
    raw.append(str(BeautifulSoup(html3.data, "html.parser")))
    raw.append(str(BeautifulSoup(html4.data, "html.parser")))
    resp = ""
    for i in range(4):
        if(rawa[i] != raw[i]):
            resp = nome[i] + "=" + raw[i]
            break
    rawa = raw
    return resp

url1s = "https://thebookisonthetable.herokuapp.com/comodos/sala"
url2s = "https://thebookisonthetable.herokuapp.com/comodos/cozinha"
url3s = "https://thebookisonthetable.herokuapp.com/comodos/quarto"
url4s = "https://thebookisonthetable.herokuapp.com/comodos/banheiro"

def set_html_f(name):
    global url1s, url2s, url3s, url4s
    if name == "sala":
        http.request('GET', url1s)
    if name == "cozinha":
        http.request('GET', url2s)
    if name == "quarto":
        http.request('GET', url3s)
    if name == "banheiro":
        http.request('GET', url4s)
