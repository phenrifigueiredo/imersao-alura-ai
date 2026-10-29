# Imersão Alura 🚀

Repositório organizado com os desafios desenvolvidos durante os estudos da **Imersão Alura**.

---

## 📁 Estrutura dos Desafios

| Desafio | Projeto / Conteúdo | Arquivos / Pasta | Tecnologias |
| :---: | :--- | :--- | :--- |
| **Desafio 1** | Calculadora Interativa no Terminal | [`desafio_1_calculadora.py`](./desafio_1_calculadora.py) | Python 3 |
| **Desafio 2** | Testes Unitários Automatizados da Calculadora | [`desafio_2_test_calculadora.py`](./desafio_2_test_calculadora.py) | Python `unittest` |
| **Desafio 3** | Aplicação Web: Lista de Tarefas (To-Do List) | [`desafio-3-lista-de-tarefas/`](./desafio-3-lista-de-tarefas/) | HTML5, CSS3, JavaScript |

---

## 🧮 Desafio 1: Calculadora em Python
Calculadora modular com menu interativo no terminal e operações matemáticas:
- **Operações:** Adição (`+`), Subtração (`-`), Multiplicação (`*`), Divisão (`/`) com proteção contra divisão por zero, Potenciação (`**`) e Porcentagem (`%`).
- **Execução:**
  ```bash
  python desafio_1_calculadora.py
  ```

---

## 🧪 Desafio 2: Testes Automatizados da Calculadora
Bateria de testes unitários para garantir a confiabilidade de todas as funções matemáticas da calculadora:
- **Testes implementados:** Verificação de operações positivas, negativas, decimais, elemento neutro e divisão por zero.
- **Execução dos testes:**
  ```bash
  python -m unittest -v desafio_2_test_calculadora.py
  ```

---

## 📝 Desafio 3: Lista de Tarefas (Web)
Aplicação visual de lista de tarefas (*To-Do List*) com interface responsiva e moderna:
- **Funcionalidades:** Adicionar, marcar como concluída, excluir tarefas, limpar concluídas e contador dinâmico de pendências.
- **Diferenciação Visual:** Tarefas pendentes contam com borda azul e etiqueta *"Pendente"*; concluídas recebem borda verde, etiqueta *"✓ Concluída"*, texto tachado em itálico e opacidade suave para foco.
- **Persistência:** Dados salvos automaticamente no `localStorage` do navegador.
- **Bateria de Testes:** Suíte visual automatizada integrada no arquivo [`desafio-3-lista-de-tarefas/run_tests.html`](./desafio-3-lista-de-tarefas/run_tests.html).
- 👉 [Veja a documentação completa do Desafio 3](./desafio-3-lista-de-tarefas/README.md)
