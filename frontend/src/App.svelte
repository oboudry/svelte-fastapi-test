<script lang="ts">
  import { onMount } from 'svelte';
  import './App.css';

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
