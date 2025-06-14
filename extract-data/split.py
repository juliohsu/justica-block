import os
from PyPDF2 import PdfReader, PdfWriter

def dividir_pdf_em_blocos_de_20(input_pdf_path):
    # Lê o PDF de entrada
    leitor = PdfReader(input_pdf_path)
    total_paginas = len(leitor.pages)

    # Cria a pasta 'splits' na raiz do projeto, se não existir
    pasta_saida = os.path.join(os.getcwd(), "splits")
    os.makedirs(pasta_saida, exist_ok=True)

    # Divide o PDF em blocos de 20 páginas
    for inicio in range(0, total_paginas, 20):
        escritor = PdfWriter()
        fim = min(inicio + 20, total_paginas)

        for i in range(inicio, fim):
            escritor.add_page(leitor.pages[i])

        numero_arquivo = (inicio // 20) + 1
        nome_arquivo = f"parte_{numero_arquivo}.pdf"
        caminho_completo = os.path.join(pasta_saida, nome_arquivo)

        with open(caminho_completo, "wb") as saida:
            escritor.write(saida)

        print(f"Arquivo salvo: {nome_arquivo} com páginas {inicio + 1} até {fim}")

# Exemplo de uso:
input_pdf = "./raw_pdfs/test.pdf"  # Substitua pelo nome do seu arquivo
dividir_pdf_em_blocos_de_20(input_pdf)
