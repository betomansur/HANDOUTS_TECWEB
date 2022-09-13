import json
from database import Database,Note


def extract_route(requisicao):
    try:
        return requisicao.split(" ")[1][1:]
    except:
        print("deu ruim")
        print(requisicao)
    
def read_file(path):
    lista = str(path).split(".")
    if lista[-1]=="txt" or lista[-1]=="html" or lista[-1]=="css" or lista[-1]=="js":
        with open(path, "rt") as file:
            text = file.read()
            return text
    else:
        with open(path, "rb") as file:
            binary = file.read()
        return binary

def load_data():
    tabela = Database("Tabela")
    notes = tabela.get_all()
    return notes



def load_template(file_path):
    file = open("templates/"+file_path)
    content = file.read()
    file.close()
    return content

def addlist(params):
    tabela = Database("Tabela")
    print(params)
    tabela.add(Note(title=params['titulo'], content=params['detalhes']))



def build_response(body='', code=200, reason='OK', headers=''):
    c = ("{}".format(code))
    if body != "":
        stri = 'HTTP/1.1 200 OK\n\n' + body
    elif code != 200:
        if headers != '':
            stri = "HTTP/1.1" + " " + c + " " +reason + "\n"+ headers + "\n\n"
        else:
            stri = "HTTP/1.1" + " " + c + " " +reason + "\n\n"
    else:
        stri = 'HTTP/1.1 200 OK\n\n'
    return stri.encode()

