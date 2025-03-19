import fitz
import tkinter as tk
from tkinter import filedialog

def dividir_pdf(arquivo_pdf, ranges, pasta_destino):
    doc = fitz.open(arquivo_pdf)
    partes = []
    
    for i, (inicio, fim) in enumerate(ranges):
        novo_pdf = fitz.open()
        for num in range(inicio - 1, fim):
            novo_pdf.insert_pdf(doc, from_page=num, to_page=num)
        
        nome_arquivo = f"{pasta_destino}/parte_24.{i+1}.pdf"
        novo_pdf.save(nome_arquivo, garbage=4, deflate=True)
        partes.append(nome_arquivo)
    
    return partes
  
pasta_destino = "C:/Users/Victor/Downloads/PDFs/teste-arvore"
root = tk.Tk()
root.withdraw()
arquivo_pdf = filedialog.askopenfilename(title="Selecione um arquivo PDF", filetypes=[("PDF files", "*.pdf")])

if arquivo_pdf:
    ranges_paginas = [(1, 60), (61, 156)]
    partes = dividir_pdf(arquivo_pdf, ranges_paginas, pasta_destino)
    print("PDF dividido com sucesso! Arquivos gerados:", partes)
