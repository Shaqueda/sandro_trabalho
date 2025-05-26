# Removedor de Fundo - Interface Gráfica com Tkinter

Este é um aplicativo simples desenvolvido em Python com interface gráfica usando `Tkinter`, que permite remover o fundo de imagens com um clique, utilizando a biblioteca `rembg`.

## 🖼️ Funcionalidades

- Selecionar uma imagem de entrada (`.png`, `.jpg`, `.jpeg`)
- Escolher onde salvar a imagem com o fundo removido
- Remover o fundo da imagem com um clique
- Interface gráfica amigável e intuitiva

## 💻 Tecnologias utilizadas

- Python 3.8+
- [rembg](https://github.com/danielgatis/rembg)
- tkinter (nativo do Python)
- pillow
- numpy
- onnxruntime

## ⚙️ Instalação

1. **Clone ou baixe os arquivos do projeto.**

2. **(Opcional) Crie um ambiente virtual:**

```bash
python -m venv venv
venv\Scripts\activate  # No Windows
```

3. **Instale as dependências:**

```bash
pip install rembg pillow numpy onnxruntime
```

## ▶️ Como usar

1. Execute o arquivo `app.py`:

```bash
python app.py
```

2. Na interface do programa:
   - Clique em **"Selecionar imagem"** para escolher a imagem original.
   - Clique em **"Escolher local para salvar"** e selecione onde salvar a imagem com fundo removido.
   - Clique em **"Remover Fundo"** para processar a imagem.

## 📦 Como gerar um executável (.exe)

Se quiser transformar o projeto em um executável para Windows:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole app.py
```

O executável será gerado na pasta `dist`.

## 📁 Estrutura básica do projeto

```
removedor-fundo/
│
├── app.py
├── README.md
└── (outros arquivos)
```

## 📝 Licença

Este projeto é livre para fins educacionais e pessoais.

## ✨ Autor

**Marcos Alexandre Moraes da Silva**
