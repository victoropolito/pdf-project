import fitz
import os
import time
import gc

def obter_tamanho_arquivo(caminho):
    """Retorna o tamanho do arquivo em KB."""
    return os.path.getsize(os.path.abspath(caminho)) / 1024

def dividir_pdf(caminho_pdf, pasta_destino, contador=[1]):
    """Função recursiva para dividir o PDF até que todas as partes tenham tamanho <= 20000KB."""
    caminho_pdf = os.path.abspath(caminho_pdf)
    pasta_destino = os.path.abspath(pasta_destino)

    print(f'\nProcessando: {caminho_pdf}')
    
    with fitz.open(caminho_pdf) as doc:
        total_paginas = len(doc)
        
        if total_paginas == 1:
            caminho_parte = os.path.join(pasta_destino, f'parte_{contador[0]}.pdf')
            doc.save(caminho_parte)
            contador[0] += 1
            return
        
        metade = total_paginas // 2
        ranges = [(0, metade), (metade, total_paginas)]
        
        for inicio, fim in ranges:
            parte_numero = contador[0]

            caminho_parte = os.path.join(pasta_destino, f'parte_{parte_numero}.pdf')
            
            novo_pdf = fitz.open()
            for i in range(inicio, fim):
                novo_pdf.insert_pdf(doc, from_page=i, to_page=i)
            novo_pdf.save(caminho_parte, garbage=4, deflate=True)
            time.sleep(0.5) 
            tamanho_parte = obter_tamanho_arquivo(caminho_parte)
            print(f'Tamanho: {tamanho_parte:.2f} KB')

            if tamanho_parte > 20000:
                print(f'Dividindo novamente: {caminho_parte}')
                contador[0] += 1
                dividir_pdf(caminho_parte, pasta_destino, contador) 
                gc.collect()
                time.sleep(0.5)
                if os.path.exists(caminho_parte):
                    print(f'Removendo: {caminho_parte}')
                    os.remove(caminho_parte)
            else:
                contador[0] += 1

# PDF path and destination folder
caminho_pdf = "C:/Example/Example/Example/example.pdf"
pasta_destino = os.path.abspath("C:/Example/Example/Example")

os.makedirs(pasta_destino, exist_ok=True)
dividir_pdf(caminho_pdf, pasta_destino)