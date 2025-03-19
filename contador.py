import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog

def contar_paginas_pdfs():
    """Abre uma janela para selecionar múltiplos PDFs e soma a quantidade de páginas de todos."""
    root = tk.Tk()
    root.withdraw()
    
    arquivos_pdf = filedialog.askopenfilenames(title="Selecione os arquivos PDF", filetypes=[("Arquivos PDF", "*.pdf")])
    
    if not arquivos_pdf:
        print("Nenhum arquivo selecionado.")
        return
    
    total_paginas = 0
    
    for caminho_pdf in arquivos_pdf:
        with fitz.open(caminho_pdf) as doc:
            num_paginas = len(doc)
            print(f"{caminho_pdf}: {num_paginas} páginas")
            total_paginas += num_paginas
    
    print(f"Total de páginas em todos os PDFs: {total_paginas}")

if __name__ == "__main__":
    contar_paginas_pdfs()