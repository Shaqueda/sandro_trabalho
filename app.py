import tkinter as tk
from tkinter import filedialog, messagebox
from rembg import remove

def selecionar_imagem(entrada_var):
    caminho = filedialog.askopenfilename(
        title="Selecionar imagem",
        filetypes=[("Imagens", "*.png *.jpg *.jpeg")]
    )
    if caminho:
        entrada_var.set(caminho)

def salvar_como(saida_var):
    caminho = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Imagem PNG", "*.png")],
        title="Salvar imagem sem fundo"
    )
    if caminho:
        if not caminho.lower().endswith(".png"):
            caminho += ".png"
        saida_var.set(caminho)

def remover_fundo(entrada, saida):
    if not entrada or not saida:
        messagebox.showwarning("Aviso", "Informe a imagem de entrada e o local para salvar.")
        return

    try:
        with open(entrada, 'rb') as input_file:
            input_data = input_file.read()
            output_data = remove(input_data)

        with open(saida, 'wb') as output_file:
            output_file.write(output_data)

        messagebox.showinfo("Sucesso", f"Fundo removido com sucesso!\nArquivo salvo em:\n{saida}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao remover o fundo:\n{e}")

def main():
    janela = tk.Tk()
    janela.title("Removedor de Fundo")
    janela.geometry("450x220")
    janela.resizable(False, False)

    entrada_var = tk.StringVar()
    saida_var = tk.StringVar()

    tk.Label(janela, text="Imagem de entrada:").pack(pady=(10, 0))
    tk.Entry(janela, textvariable=entrada_var, width=60).pack(padx=10)
    tk.Button(janela, text="Selecionar imagem", command=lambda: selecionar_imagem(entrada_var)).pack(pady=5)

    tk.Label(janela, text="Salvar imagem como:").pack(pady=(10, 0))
    tk.Entry(janela, textvariable=saida_var, width=60).pack(padx=10)
    tk.Button(janela, text="Escolher local para salvar", command=lambda: salvar_como(saida_var)).pack(pady=5)

    tk.Button(
        janela,
        text="Remover Fundo",
        command=lambda: remover_fundo(entrada_var.get(), saida_var.get()),
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold")
    ).pack(pady=15)

    janela.mainloop()

if __name__ == "__main__":
    main()