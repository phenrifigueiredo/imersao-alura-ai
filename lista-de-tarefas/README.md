# 📝 Aplicação de Lista de Tarefas (To-Do List)

Bem-vindo ao seu primeiro projeto web! Esta aplicação foi criada com os três pilares fundamentais do desenvolvimento de software para a web: **HTML**, **CSS** e **JavaScript**.

---

## 🏛️ Os Três Componentes Principais

Para quem está começando, uma ótima analogia é pensar na aplicação como um ser humano:

1. **`index.html` (O Esqueleto / Estrutura)**
   - Define quais elementos existem na página: o campo de digitação, os botões, os textos e onde a lista de tarefas vai se posicionar.
   - Ele não se preocupa com cores nem com o funcionamento, apenas organiza os blocos na tela.

2. **`style.css` (A Roupa / Visual)**
   - Dá beleza, cores, tipografia, bordas arredondadas e sombras à página.
   - Controla o alinhamento com **Flexbox** e adiciona efeitos visuais:
     - **Tarefas Pendentes**: Fundo claro, borda lateral azul (`#3e63dd`) e etiqueta azul *"Pendente"*.
     - **Tarefas Concluídas**: Fundo esverdeado suave (`#f0fdf4`), borda lateral verde (`#10b981`), texto tachado em itálico, etiqueta verde *"✓ Concluída"* e opacidade reduzida para destacar as pendências.

3. **`script.js` (O Cérebro / Lógica)**
   - Ouve as ações que você faz (digitar, clicar em adicionar, marcar concluído ou clicar em excluir).
   - Mantém uma lista de objetos de dados na memória.
   - Aplica a classe CSS `.completed` e a etiqueta adequada conforme o estado `concluida` da tarefa.
   - Manipula o HTML dinamicamente com base nas tarefas cadastradas.
   - Salva tudo no `localStorage` do navegador para que suas tarefas permaneçam salvas mesmo que você feche ou recarregue a página!

---

## 🚀 Como testar e usar

Você **não precisa instalar nada** para rodar esse projeto:

1. Abra a pasta `lista-de-tarefas` no seu explorador de arquivos.
2. Dê um duplo clique no arquivo `index.html` para usar a aplicação.
3. Dê um duplo clique no arquivo `run_tests.html` para abrir o painel de testes automatizados e ver todas as validações passando em tempo real.

---

## 🔍 O que observar no código para aprender

- **No `index.html`**:
  - Veja como usamos a tag `<form>` e `<input required>` para validar campos automaticamente.
  - Observe os atributos `id="..."` que servem de identificadores para o JavaScript encontrar cada elemento.

- **No `style.css`**:
  - Veja o uso de `display: flex;` para alinhar itens lado a lado com facilidade.
  - Observe a classe `.task-item.completed` que muda o visual da tarefa quando ela é marcada como feita.

- **No `script.js`**:
  - Veja os métodos de Array modernos do JavaScript:
    - `.push()`: para adicionar um item.
    - `.map()`: para alternar o estado de conclusão de uma tarefa.
    - `.filter()`: para remover uma tarefa ou limpar as concluídas.
  - Observe o uso de `localStorage.setItem` e `localStorage.getItem` para persistência dos dados.
