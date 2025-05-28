"""
Autores: 
Marcos Alexandre Moraes da Silva
Ivys Emanoel Cordeiro de Souza Lima
Mateus Jairan Rodrigues
"""
"""
Aplicativo desktop com interface gráfica para remoção de fundo de imagens.
Permite arrastar e soltar imagens ou selecionar arquivos manualmente.
Utiliza a biblioteca rembg para processar imagens com inteligência artificial.

Requisitos:
- rembg
- pillow
- tkinterdnd2
"""
# Importações necessárias
from rembg import remove  # Biblioteca para remover fundo de imagens
from PIL import Image, ImageTk  # Manipulação de imagens
from tkinterdnd2 import DND_FILES, TkinterDnD  # Drag & Drop no Tkinter
import io  # Manipulação de dados binários em memória
import os  # Interações com sistema de arquivos
import threading  # Para não travar a interface durante o processamento
import tkinter as tk
from tkinter import filedialog, messagebox  # Componentes extras do Tkinter

# CONFIGURAÇÕES DE TEMA (Claro e Escuro)
tema_claro = {
    "bg": "#f2f7f5",           # Cor de fundo da janela
    "fg": "#2c786c",           # Cor principal de destaque
    "fg_btn": "white",         # Texto de botões
    "highlight": "#90d1c4",    # Cor ao passar o mouse
    "text": "#333",            # Texto padrão
    "card": "#ffffff"          # Fundo dos cards e labels
}

tema_escuro = {
    "bg": "#2b2b2b",
    "fg": "#66b2a6",
    "fg_btn": "white",
    "highlight": "#3caea3",
    "text": "#f2f2f2",
    "card": "#3c3c3c"
}

tema = tema_escuro  # Tema padrão ao iniciar

# CRIAÇÃO DA JANELA PRINCIPAL
window = TkinterDnD.Tk()
window.title("Removedor de Fundo")

# Define tamanho da janela e posicionamento inicial
window_width = 540
window_height = 420
x = 0  # canto esquerdo
y = 0  # topo
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.resizable(False, False)

selected_image_path = None  # Caminho da imagem selecionada

# FUNÇÕES DE TEMA
def aplicar_tema():
    """Aplica as cores do tema atual a todos os elementos da interface"""
    window.configure(bg=tema["bg"])
    label1.config(bg=tema["bg"], fg=tema["fg"])
    label2.config(bg=tema["card"], fg=tema["text"])
    botao1.config(bg=tema["fg"], fg=tema["fg_btn"], activebackground=tema["highlight"])
    botao2.config(bg=tema["fg"], fg=tema["fg_btn"], activebackground=tema["highlight"])
    toggle_btn.config(bg=tema["highlight"], fg=tema["bg"], activebackground=tema["fg"])
    footer.config(bg=tema["bg"], fg=tema["text"])

def alternar_tema():
    """Alterna entre tema claro e escuro"""
    global tema
    tema = tema_escuro if tema == tema_claro else tema_claro
    aplicar_tema()

# INTERFACE GRÁFICA (WIDGETS)
# Título principal
label1 = tk.Label(window, text="REMOVEDOR DE FUNDO DE IMAGEM",
                  font=("Segoe UI", 17, "bold"))
label1.pack(pady=(20, 10))

# Área para arrastar ou selecionar imagem
label2 = tk.Label(window, text="Arraste e solte uma imagem aqui ou clique em 'Selecionar Imagem'",
                  font=("Segoe UI", 11), relief="ridge", padx=10, pady=10,
                  width=60, height=4, wraplength=450, justify="center")
label2.pack(pady=10)

# FUNÇÃO: Selecionar imagem manualmente
def selecionar_imagem():
    """Abre o diálogo para escolher uma imagem"""
    global selected_image_path
    file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")])
    if file_path:
        selected_image_path = file_path
        label2.config(text=file_path)

# FUNÇÃO: Processar e remover fundo da imagem
def remover_fundo():
    """Inicia o processo de remoção de fundo em thread separada"""
    def processar():
        if not selected_image_path:
            messagebox.showwarning("Aviso", "Nenhum arquivo selecionado.")
            return

        # Janela de carregamento
        carregando = tk.Toplevel(window)
        carregando.title("Processando...")
        carregando.geometry("280x80")
        carregando.configure(bg=tema["bg"])
        carregando.transient(window)
        carregando.grab_set()

        tk.Label(carregando, text="Removendo fundo, aguarde...",
                 font=("Segoe UI", 11), bg=tema["bg"], fg=tema["text"]).pack(pady=20)

        try:
            # Leitura da imagem original
            with open(selected_image_path, "rb") as img:
                input_data = img.read()
                output_data = remove(input_data)

            # Converte os dados de volta para imagem
            result = Image.open(io.BytesIO(output_data)).convert("RGBA")

            # Nome sugerido para salvar a imagem processada
            base = os.path.splitext(os.path.basename(selected_image_path))[0]
            suggested_name = f"{base}-editado.png"

            # Diálogo para salvar a imagem com fundo removido
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG Files", "*.png")],
                                                     initialfile=suggested_name,
                                                     title="Salvar imagem sem fundo")
            carregando.destroy()

            if save_path:
                result.save(save_path, "PNG")
                messagebox.showinfo("Sucesso", f"Fundo removido com sucesso!\nSalvo em:\n{save_path}")
            else:
                messagebox.showwarning("Cancelado", "Operação cancelada pelo usuário.")
        except Exception as e:
            carregando.destroy()
            messagebox.showerror("Erro", f"Erro ao remover o fundo:\n{str(e)}")

    # Roda a função de processamento em uma nova thread para não travar a interface
    threading.Thread(target=processar).start()

# BOTÕES DE AÇÃO
# Botão de seleção de imagem
botao1 = tk.Button(window, text="Selecionar Imagem", command=selecionar_imagem,
                   font=("Segoe UI", 11, "bold"), width=24, height=2, relief="flat", cursor="hand2", bd=0)
botao1.pack(pady=(10, 5))

# Botão para remover o fundo
botao2 = tk.Button(window, text="Remover Fundo", command=remover_fundo,
                   font=("Segoe UI", 11, "bold"), width=24, height=2, relief="flat", cursor="hand2", bd=0)
botao2.pack(pady=5)

# Botão de alternância de tema
toggle_btn = tk.Button(window, text="Alternar Tema", command=alternar_tema,
                       font=("Segoe UI", 10, "bold"), width=18, relief="flat", cursor="hand2", bd=0)
toggle_btn.pack(pady=10)

# Rodapé
footer = tk.Label(window, text="Powered by rembg", font=("Segoe UI", 9))
footer.pack(side="bottom", pady=10)

# SUPORTE A ARRASTAR E SOLTAR (DRAG & DROP)
def drop(event):
    """Função chamada ao soltar uma imagem na área de drop"""
    global selected_image_path
    if event.data:
        path = event.data.strip("{}")  # Remove chaves em caminhos do Windows
        selected_image_path = path
        label2.config(text=path)

label2.drop_target_register(DND_FILES)
label2.dnd_bind('<<Drop>>', drop)

# INICIALIZAÇÃO FINAL
aplicar_tema()  # Aplica tema escolhido
window.mainloop()  # Inicia a interface gráfica
