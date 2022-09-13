from os import error, replace
from utils import load_data, load_template,addlist, build_response
import urllib

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        print(partes)
        corpo = partes[1]
        params = {}
        print("Chegou corpo")
        for chave_valor in corpo.split('&'):
            if chave_valor.startswith("titulo"):
                params["titulo"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
            if chave_valor.startswith("detalhes"):
                params["detalhes"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
        addlist(params)
        return build_response(code=303, reason='See Other', headers='Location: /')
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content)
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)
    body = load_template('index.html').format(notes=notes)
    return build_response() + body.encode()