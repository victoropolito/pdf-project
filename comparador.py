import fitz  # PyMuPDF
import hashlib
import os

def calcular_hash_pagina(pagina):
    """Gera um hash do texto da página para comparação."""
    texto = pagina.get_text("text")
    return hashlib.md5(texto.encode('utf-8')).hexdigest()

def verificar_pagina_em_pdfs(pasta, pdf_referencia):
    """Verifica se a página 1 do PDF de referência está presente em qualquer outro PDF da pasta e remove."""
    caminho_referencia = os.path.join(pasta, pdf_referencia)
    
    with fitz.open(caminho_referencia) as doc_ref:
        if doc_ref.page_count == 0:
            print("O PDF de referência está vazio!")
            return
        
        hash_pagina_1 = calcular_hash_pagina(doc_ref[0])  # Hash da página 1
    
    paginas_para_remover = {}

    for arquivo in os.listdir(pasta):
        caminho_pdf = os.path.join(pasta, arquivo)
        
        if arquivo == pdf_referencia or not arquivo.endswith(".pdf"):
            continue  # Ignora o próprio arquivo de referência e não-PDFs
        
        with fitz.open(caminho_pdf) as doc:
            for num_pagina in range(len(doc)):
                if calcular_hash_pagina(doc[num_pagina]) == hash_pagina_1:
                    print(f"Página repetida encontrada! {arquivo} (Página {num_pagina + 1}) é igual à Página 1 de {pdf_referencia}")
                    
                    if caminho_pdf not in paginas_para_remover:
                        paginas_para_remover[caminho_pdf] = []
                    
                    paginas_para_remover[caminho_pdf].append(num_pagina)

    # Remover as páginas e salvar novos PDFs
    for caminho_pdf, paginas in paginas_para_remover.items():
        remover_pagina_e_salvar(caminho_pdf, paginas)

def remover_pagina_e_salvar(caminho_pdf, paginas_index):
    """Remove páginas duplicadas e salva um novo PDF sem reescrever o original."""
    with fitz.open(caminho_pdf) as doc:
        novo_pdf = fitz.open()
        
        for i, pagina in enumerate(doc):
            if i in paginas_index:
                continue  # Pula as páginas duplicadas
            novo_pdf.insert_pdf(doc, from_page=i, to_page=i)
        
        novo_nome = caminho_pdf.replace(".pdf", "_sem_duplicata.pdf")
        novo_pdf.save(novo_nome)
        novo_pdf.close()
        print(f"Novo PDF salvo: {novo_nome}")

# Caminho da pasta onde estão os PDFs
pasta_pdfs = "C:/Users/Victor/Downloads/PDFs/livro"
# Nome do PDF de referência
pdf_referencia = "Youmans and Winn Neurological Surgery - 8th Edition-2022.pdf"

verificar_pagina_em_pdfs(pasta_pdfs, pdf_referencia)
