import os
import re

def renomear_pdfs(pasta):
    """Renomeia os arquivos PDF dentro da pasta em ordem crescente."""
    arquivos = [f for f in os.listdir(pasta) if f.startswith("parte_") and f.endswith(".pdf")]
    
    # Extrai os números dos arquivos usando regex e ordena
    arquivos.sort(key=lambda x: int(re.search(r'\d+', x).group()))
    
    for indice, arquivo in enumerate(arquivos, start=1):
        novo_nome = f"parte_{indice}.pdf"
        caminho_antigo = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, novo_nome)
        
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {arquivo} -> {novo_nome}")

# Caminho da pasta onde estão os PDFs
pasta_pdfs = "C:/Users/Victor/Downloads/PDFs/teste-arvore-dois"
renomear_pdfs(pasta_pdfs)