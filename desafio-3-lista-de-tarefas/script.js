/* ==========================================================
   LÓGICA DA APLICAÇÃO (JavaScript)
   
   O JavaScript é o "cérebro" da aplicação:
   1. Captura as ações do usuário (cliques, digitação).
   2. Modifica a lista de dados (adiciona, remove, conclui).
   3. Atualiza a tela (DOM) com base nos dados.
   4. Salva no navegador (LocalStorage) para não perder ao recarregar.
========================================================== */

// 1. SELEÇÃO DE ELEMENTOS DO HTML
const todoForm = document.getElementById("todo-form");
const taskInput = document.getElementById("task-input");
const taskList = document.getElementById("task-list");
const emptyState = document.getElementById("empty-state");
const taskCount = document.getElementById("task-count");
const clearCompletedBtn = document.getElementById("clear-completed");

// 2. ESTADO DA APLICAÇÃO (Nossos dados)
// Carrega as tarefas salvas no LocalStorage ou inicia com uma lista vazia
let tarefas = JSON.parse(localStorage.getItem("minhas_tarefas")) || [];

// ==========================================================
// FUNÇÕES PRINCIPAIS
// ==========================================================

/**
 * Salva a lista de tarefas atual no LocalStorage do navegador
 */
function salvarTarefas() {
  localStorage.setItem("minhas_tarefas", JSON.stringify(tarefas));
}

/**
 * Atualiza toda a interface visual (HTML) a partir do array de tarefas
 */
function renderizarTarefas() {
  // Limpa a lista atual na tela
  taskList.innerHTML = "";

  // Se a lista estiver vazia, exibe a mensagem de estado vazio
  if (tarefas.length === 0) {
    emptyState.style.display = "block";
  } else {
    emptyState.style.display = "none";
  }

  // Cria e insere cada elemento de tarefa na tela
  tarefas.forEach((tarefa) => {
    // Cria o item da lista <li>
    const li = document.createElement("li");
    li.className = `task-item ${tarefa.concluida ? "completed" : ""}`;

    // Cria a área clicável com checkbox e texto
    const contentDiv = document.createElement("div");
    contentDiv.className = "task-content";
    contentDiv.onclick = () => alternarConclusao(tarefa.id);

    const checkbox = document.createElement("div");
    checkbox.className = "task-checkbox";

    const spanText = document.createElement("span");
    spanText.className = "task-text";
    spanText.textContent = tarefa.texto;

    contentDiv.appendChild(checkbox);
    contentDiv.appendChild(spanText);

    // Cria a etiqueta (badge) de status visual
    const badge = document.createElement("span");
    badge.className = `task-badge ${tarefa.concluida ? "badge-completed" : "badge-pending"}`;
    badge.textContent = tarefa.concluida ? "✓ Concluída" : "Pendente";

    // Cria o botão de excluir (lixeira)
    const deleteBtn = document.createElement("button");
    deleteBtn.className = "btn-delete";
    deleteBtn.innerHTML = "&times;"; // Símbolo de 'X' elegante
    deleteBtn.title = "Excluir tarefa";
    deleteBtn.onclick = (e) => {
      e.stopPropagation(); // Evita marcar a tarefa como concluída ao clicar em excluir
      removerTarefa(tarefa.id);
    };

    // Cria contêiner de ações (etiqueta + botão de excluir)
    const actionsDiv = document.createElement("div");
    actionsDiv.className = "task-actions";
    actionsDiv.appendChild(badge);
    actionsDiv.appendChild(deleteBtn);

    // Monta o item completo
    li.appendChild(contentDiv);
    li.appendChild(actionsDiv);

    // Insere o <li> dentro do <ul>
    taskList.appendChild(li);
  });

  // Atualiza o contador de pendências
  atualizarContador();
}

/**
 * Adiciona uma nova tarefa ao array
 */
function adicionarTarefa(texto) {
  const textoLimpo = texto.trim();
  if (textoLimpo === "") return;

  const novaTarefa = {
    // Gera um identificador único combinando timestamp e número aleatório
    id: `${Date.now()}-${Math.random().toString(36).substr(2, 6)}`,
    texto: textoLimpo,
    concluida: false
  };

  tarefas.push(novaTarefa);
  salvarTarefas();
  renderizarTarefas();
}

/**
 * Alterna entre concluída e pendente
 */
function alternarConclusao(id) {
  tarefas = tarefas.map((tarefa) => {
    if (tarefa.id === id) {
      return { ...tarefa, concluida: !tarefa.concluida };
    }
    return tarefa;
  });

  salvarTarefas();
  renderizarTarefas();
}

/**
 * Remove uma tarefa pelo seu ID
 */
function removerTarefa(id) {
  tarefas = tarefas.filter((tarefa) => tarefa.id !== id);
  salvarTarefas();
  renderizarTarefas();
}

/**
 * Remove todas as tarefas marcadas como concluídas
 */
function limparConcluidas() {
  tarefas = tarefas.filter((tarefa) => !tarefa.concluida);
  salvarTarefas();
  renderizarTarefas();
}

/**
 * Atualiza o texto que exibe quantas tarefas estão pendentes
 */
function atualizarContador() {
  const pendentes = tarefas.filter((t) => !t.concluida).length;
  if (pendentes === 1) {
    taskCount.textContent = "1 tarefa pendente";
  } else {
    taskCount.textContent = `${pendentes} tarefas pendentes`;
  }
}

// ==========================================================
// EVENTOS DO USUÁRIO (Listeners)
// ==========================================================

// Quando o formulário for enviado (Enter ou clique em 'Adicionar')
todoForm.addEventListener("submit", (evento) => {
  evento.preventDefault(); // Impede o recarregamento padrão da página
  adicionarTarefa(taskInput.value);
  taskInput.value = ""; // Limpa o campo de texto
  taskInput.focus();
});

// Quando clicar em 'Limpar concluídas'
clearCompletedBtn.addEventListener("click", limparConcluidas);

// Executa a primeira renderização assim que o script carregar
renderizarTarefas();
