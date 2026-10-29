# Imersão Alura 🚀

Repositório com os projetos desenvolvidos durante os estudos da **Imersão Alura**.

---

## 📁 Projetos

### 1. 📝 [Lista de Tarefas (Web)](./lista-de-tarefas)
Aplicação visual de lista de tarefas (*To-Do List*) desenvolvida com HTML5, CSS3 e JavaScript puro:
- **Funcionalidades:** Adicionar, concluir e excluir tarefas, limpar concluídas e contador dinâmico.
- **Interface Visual:** Diferenciação visual imediata entre tarefas pendentes (borda azul, etiqueta "Pendente") e concluídas (borda verde, etiqueta "✓ Concluída", texto tachado em itálico e opacidade suave).
- **Persistência:** Armazenamento automático no `localStorage` do navegador.
- **Qualidade:** Bateria de testes automatizados com suíte visual no próprio navegador ([`run_tests.html`](./lista-de-tarefas/run_tests.html)).
- 👉 [Veja a documentação completa da Lista de Tarefas](./lista-de-tarefas/README.md)

---

### 2. 🧮 Calculadora em Python
Um projeto de calculadora em Python desenvolvido inicialmente durante a imersão, com arquitetura modular, boas práticas, tratamento de erros, cálculo de porcentagem e testes automatizados.

#### 🚀 Funcionalidades
- **Adição (`+`)**
- **Subtração (`-`)**
- **Multiplicação (`*`)**
- **Divisão (`/`)** com proteção contra divisão por zero
- **Potenciação (`**`)**
- **Cálculo de Porcentagem (`%`)**
- **Menu interativo no terminal** com opção de saída limpa
- **Testes unitários automatizados** com a biblioteca padrão `unittest`

#### 🛠️ Como Executar a Calculadora
```bash
python calculadora.py
```

Para executar os testes da calculadora:
```bash
python -m unittest -v test_calculadora.py
```
