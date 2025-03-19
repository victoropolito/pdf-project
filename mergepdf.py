import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog

def merge_pdfs(arquivos, arquivo_saida):
    pdf_final = fitz.open()
    
    if not arquivos:
        print("Nenhum arquivo PDF selecionado.")
        return
    
    for arquivo in arquivos:
        pdf_temp = fitz.open(arquivo)
        pdf_final.insert_pdf(pdf_temp)
    
    pdf_final.save(arquivo_saida)
    print(f"PDF mesclado salvo em: {arquivo_saida}")

root = tk.Tk()
root.withdraw()
arquivos = filedialog.askopenfilenames(title="Selecione os PDFs para mesclar", filetypes=[("PDF files", "*.pdf")])

if arquivos:
    arquivo_saida = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Salvar PDF mesclado como")
    if arquivo_saida:
        merge_pdfs(arquivos, arquivo_saida)
