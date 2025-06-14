import os
from PyPDF2 import PdfReader, PdfWriter

def dividir_pdf(input_pdf_path, paginas_por_parte):
    leitor = PdfReader(input_pdf_path)
    total_paginas = len(leitor.pages)

    # Cria a pasta 'splits' na raiz do projeto, se não existir
    pasta_saida = os.path.join(os.getcwd(), "splits")
    os.makedirs(pasta_saida, exist_ok=True)

    # Divide o PDF de acordo com o número de páginas escolhido
    for inicio in range(0, total_paginas, paginas_por_parte):
        escritor = PdfWriter()
        fim = min(inicio + paginas_por_parte, total_paginas)

        for i in range(inicio, fim):
            escritor.add_page(leitor.pages[i])

        numero_arquivo = (inicio // paginas_por_parte) + 1
        nome_arquivo = f"parte_{numero_arquivo}.pdf"
        caminho_completo = os.path.join(pasta_saida, nome_arquivo)

        with open(caminho_completo, "wb") as saida:
            escritor.write(saida)

        print(f"Arquivo salvo: {nome_arquivo} com páginas {inicio + 1} até {fim}")

input_pdf = "raw_pdfs/test.pdf"
paginas_por_parte = 20

dividir_pdf(input_pdf, paginas_por_parte)
