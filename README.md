# Svelte + FastAPI Todo List

A full-stack todo list application built with Svelte (TypeScript + Vite) on the frontend and FastAPI on the backend.

## 🚀 Quick Start

### Prerequisites

- **Node.js** (v18 or higher)
- **Python** 3.12 or higher
- **uv** - Python package manager ([installation guide](https://docs.astral.sh/uv/))

### Running the Application

From the root directory, run both frontend and backend simultaneously:

```bash
npm run dev
```

This command uses `concurrently` to start:
- **Backend**: FastAPI server on `http://127.0.0.1:8000`
- **Frontend**: Vite dev server on `http://localhost:5173`

### Running Services Individually

**Backend only:**
```bash
cd backend
uv run uvicorn app.main:app --reload
```

**Frontend only:**
```bash
cd frontend
npm run dev
```

## 📁 Project Structure

```
svelte-fastapi/
├── backend/              # FastAPI backend
│   ├── app/
│   │   └── main.py      # API routes and models
│   ├── pyproject.toml   # Python dependencies
│   └── uv.lock          # Locked dependencies
├── frontend/            # Svelte frontend
│   ├── src/
│   │   ├── App.svelte   # Main todo list component
│   │   └── main.ts      # Application entry point
│   ├── package.json     # Node dependencies
│   └── vite.config.ts   # Vite configuration
└── package.json         # Root package with dev script
```

## 🛠️ Development Setup

### Initial Setup

1. **Install root dependencies:**
   ```bash
   npm install
   ```

2. **Install frontend dependencies:**
   ```bash
   cd frontend
   npm install
   ```

3. **Backend dependencies** are managed by `uv` and will be installed automatically when running the dev server.

### VS Code Setup for Svelte

To enable automatic formatting of Svelte files on save:

1. Create `frontend/.vscode/settings.json`:
   ```json
   {
     "editor.formatOnSave": true,
     "[svelte]": {
       "editor.defaultFormatter": "svelte.svelte-vscode"
     }
   }
   ```

2. Install the recommended extension:
   - [Svelte for VS Code](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode)

## 🔌 API Endpoints

The FastAPI backend provides the following REST API endpoints:

- `GET /api/hello` - Test endpoint
- `GET /api/todos` - Get all todos
- `POST /api/todos` - Create a new todo
- `PUT /api/todos/{todo_id}` - Update a todo
- `DELETE /api/todos/{todo_id}` - Delete a todo

### API Documentation

When the backend is running, visit:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🏗️ Tech Stack

### Frontend
- **Svelte 5** - Reactive UI framework
- **TypeScript** - Type safety
- **Vite** - Fast build tool and dev server
- **CSS** - Styling (no framework)

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **CORS Middleware** - Cross-origin requests

## 📝 Features

- ✅ Create, read, update, and delete todos
- ✅ Mark todos as completed/incomplete
- ✅ Real-time todo counter
- ✅ Responsive UI
- ✅ Type-safe frontend and backend
- ✅ Hot module replacement (HMR)

## 🔧 Building for Production

### Frontend
```bash
cd frontend
npm run build
```

The built files will be in `frontend/dist/`.

### Backend

The backend can be deployed using any ASGI server. For production:

```bash
cd backend
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

**Note:** Update CORS settings in `backend/app/main.py` for production to restrict allowed origins.

## 💾 Data Storage

Currently, the application uses **in-memory storage** for todos. This means:
- Data is lost when the server restarts
- Not suitable for production use

For production, consider integrating a database:
- **SQLite** - Simple file-based database
- **PostgreSQL** - Full-featured relational database
- **MongoDB** - NoSQL document database

## 🎨 Customization

### Changing API URL

The frontend connects to the backend at `http://127.0.0.1:8000/api`. To change this, update the `API_URL` constant in `frontend/src/App.svelte`.

### Styling

The application uses vanilla CSS in `frontend/src/app.css` and component-scoped styles in `App.svelte`. Modify these files to customize the appearance.

## 📚 Learn More

- [Svelte Documentation](https://svelte.dev/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Vite Documentation](https://vite.dev/)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)

## 🤝 Contributing

This is a starter template. Feel free to:
- Add new features
- Improve the UI/UX
- Add database integration
- Implement authentication
- Add tests

## 📄 License

This project is open source and available under the MIT License.
