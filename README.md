# Calculadora em Python 🧮

Um projeto de calculadora em Python desenvolvido inicialmente durante a **Imersão Alura**, agora refatorado com arquitetura modular, boas práticas, tratamento de erros, cálculo de porcentagem e testes automatizados.

## 🚀 Funcionalidades

- **Adição (`+`)**
- **Subtração (`-`)**
- **Multiplicação (`*`)**
- **Divisão (`/`)** com proteção contra divisão por zero
- **Potenciação (`**`)**
- **Cálculo de Porcentagem (`%`)**
- **Menu interativo no terminal** com opção de saída limpa
- **Testes unitários automatizados** com a biblioteca padrão `unittest`

## 📁 Estrutura do Projeto

```text
calculadora/
├── calculadora.py       # Código principal com as funções e menu interativo
├── test_calculadora.py  # Testes unitários das funções matemáticas
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md            # Documentação do projeto
```

## 🛠️ Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado.

### Executando a calculadora
Abra o terminal na pasta do projeto e execute:

```bash
python calculadora.py
```

### Executando os testes automatizados
Para verificar se todas as operações matemáticas estão funcionando:

```bash
python -m unittest -v test_calculadora.py
```
