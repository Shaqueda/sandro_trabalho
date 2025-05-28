
# Removedor de Fundo de Imagem (Desktop GUI)

Aplicativo desktop com interface gráfica que permite **remover o fundo de imagens automaticamente** com tecnologia de inteligência artificial. Simples, intuitivo e eficiente, com suporte a **arrastar e soltar**, **modo claro/escuro**, e **salvamento personalizado** da imagem final.

---

## Captura de Tela

# Tema Escuro
![Screenshot do aplicativo](https://github.com/user-attachments/assets/6fc81d09-5709-4a34-bf75-9d3a19d0c977)
# Tema Claro
![Screenshot do aplicativo](https://github.com/user-attachments/assets/0a008cba-417a-448f-ade9-9c7430923c1e)
---

## Funcionalidades

- Remoção automática de fundo de imagens com um clique
- Interface amigável feita com Tkinter
- Suporte a **arrastar e soltar** imagens
- Alternância entre **tema claro e escuro**
- Compatível com formatos `.png`, `.jpg`, `.jpeg`, `.bmp`
- Processamento assíncrono (sem travar a interface)

---

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [rembg](https://github.com/danielgatis/rembg) – modelo de IA para remoção de fundo
- [Pillow](https://python-pillow.org/) – manipulação de imagens
- [tkinter](https://docs.python.org/3/library/tkinter.html) – interface gráfica
- [tkinterdnd2](https://pypi.org/project/tkinterdnd2/) – suporte a arrastar e soltar

---

## Instalação

### Requisitos

- Python 3.8 ou superior
- pip

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/removedor-de-fundo.git
cd removedor-de-fundo
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install rembg pillow tkinterdnd2
```

---

## Como Usar

1. Execute o aplicativo:

```bash
python app.py
```

2. Escolha uma imagem:
   - Clique em **"Selecionar Imagem"** para escolher manualmente, ou
   - **Arraste e solte** uma imagem na área indicada.

3. Clique em **"Remover Fundo"** para iniciar o processamento.

4. Após o processo, escolha onde salvar a imagem com fundo removido.

5. Você pode alternar entre o tema claro e escuro clicando em **"Alternar Tema"**.

---

## Autores

Marcos Alexandre - [![Ver no GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?logo=github)](https://github.com/Shaqueda?tab=repositories)

Mateus Jairan - [![Ver no GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?logo=github)](https://github.com/mateusjairan?tab=repositories)

Ivys Souza - [![Ver no GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?logo=github)](https://github.com/IvysSouza07?tab=repositories)

