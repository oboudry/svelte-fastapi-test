<script lang="ts">
  import { onMount } from 'svelte';

  interface Todo {
    id: number;
    title: string;
    completed: boolean;
  }

  let todos: Todo[] = [];
  let newTodoTitle = '';
  const API_URL = 'http://127.0.0.1:8000/api';

  async function fetchTodos() {
    try {
      const response = await fetch(`${API_URL}/todos`);
      todos = await response.json();
    } catch (error) {
      console.error('Error fetching todos:', error);
    }
  }

  async function addTodo() {
    if (!newTodoTitle.trim()) return;
    
    try {
      const response = await fetch(`${API_URL}/todos`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: newTodoTitle, completed: false })
      });
      const newTodo = await response.json();
      todos = [...todos, newTodo];
      newTodoTitle = '';
    } catch (error) {
      console.error('Error adding todo:', error);
    }
  }

  async function toggleTodo(todo: Todo) {
    try {
      const response = await fetch(`${API_URL}/todos/${todo.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: todo.title, completed: !todo.completed })
      });
      const updatedTodo = await response.json();
      todos = todos.map(t => t.id === todo.id ? updatedTodo : t);
    } catch (error) {
      console.error('Error updating todo:', error);
    }
  }

  async function deleteTodo(id: number) {
    try {
      await fetch(`${API_URL}/todos/${id}`, { method: 'DELETE' });
      todos = todos.filter(t => t.id !== id);
    } catch (error) {
      console.error('Error deleting todo:', error);
    }
  }

  function handleKeyPress(event: KeyboardEvent) {
    if (event.key === 'Enter') {
      addTodo();
    }
  }

  onMount(() => {
    fetchTodos();
  });
</script>

<main>
  <div class="container">
    <h1>📝 Todo List</h1>
    
    <div class="input-section">
      <input
        type="text"
        bind:value={newTodoTitle}
        on:keypress={handleKeyPress}
        placeholder="What needs to be done?"
        class="todo-input"
      />
      <button on:click={addTodo} class="add-btn">Add</button>
    </div>

    <div class="todos-list">
      {#if todos.length === 0}
        <p class="empty-state">No todos yet. Add one above!</p>
      {:else}
        {#each todos as todo (todo.id)}
          <div class="todo-item" class:completed={todo.completed}>
            <input
              type="checkbox"
              checked={todo.completed}
              on:change={() => toggleTodo(todo)}
              class="todo-checkbox"
            />
            <span class="todo-title">{todo.title}</span>
            <button on:click={() => deleteTodo(todo.id)} class="delete-btn">
              ✕
            </button>
          </div>
        {/each}
      {/if}
    </div>

    <div class="stats">
      <span>{todos.filter(t => !t.completed).length} items left</span>
      <span>{todos.filter(t => t.completed).length} completed</span>
    </div>
  </div>
</main>

<style>
  main {
    min-height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2rem;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  }

  .container {
    max-width: 600px;
    margin: 0 auto;
    background: white;
    border-radius: 12px;
    padding: 2rem;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  }

  h1 {
    text-align: center;
    color: #333;
    margin-bottom: 2rem;
    font-size: 2.5rem;
  }

  .input-section {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
  }

  .todo-input {
    flex: 1;
    padding: 0.75rem 1rem;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    font-size: 1rem;
    transition: border-color 0.3s;
  }

  .todo-input:focus {
    outline: none;
    border-color: #667eea;
  }

  .add-btn {
    padding: 0.75rem 1.5rem;
    background: #667eea;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.3s;
  }

  .add-btn:hover {
    background: #5568d3;
  }

  .todos-list {
    margin-bottom: 1.5rem;
  }

  .empty-state {
    text-align: center;
    color: #999;
    padding: 2rem;
    font-style: italic;
  }

  .todo-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 8px;
    margin-bottom: 0.5rem;
    transition: all 0.3s;
  }

  .todo-item:hover {
    background: #e9ecef;
    transform: translateX(4px);
  }

  .todo-item.completed {
    opacity: 0.6;
  }

  .todo-checkbox {
    width: 20px;
    height: 20px;
    cursor: pointer;
  }

  .todo-title {
    flex: 1;
    font-size: 1rem;
    color: #333;
  }

  .todo-item.completed .todo-title {
    text-decoration: line-through;
    color: #999;
  }

  .delete-btn {
    padding: 0.25rem 0.5rem;
    background: #ff6b6b;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    transition: background 0.3s;
  }

  .delete-btn:hover {
    background: #ee5a52;
  }

  .stats {
    display: flex;
    justify-content: space-between;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 8px;
    font-size: 0.9rem;
    color: #666;
  }
</style>
