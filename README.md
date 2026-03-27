# my_mcp_server

Simple MCP (Model Context Protocol) server examples built with `FastMCP`.

## Files

- `mealdb_server.py`: MCP server with MealDB tools.
  - `search_meals_by_name(name: str)`
  - `list_categories()`
  - `random_meal()`
- `server.py`: Minimal hello-world MCP tool (`say_hello`).
- `server2.py`: Utility MCP tools (`add_numbers`, `repeat_text`).

## Requirements

- Python 3.10+
- `mcp` package
- `requests` package (needed by `mealdb_server.py`)

## Setup (Windows PowerShell)

```powershell
# from project root
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install mcp requests
```

If PowerShell blocks activation, run this once and retry:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Run

Use MCP Inspector (recommended for local testing):

```powershell
.\venv\Scripts\mcp dev mealdb_server.py
```

Run server directly:

```powershell
.\venv\Scripts\mcp run mealdb_server.py
```

Note: `mcp run` uses `stdio` by default, so it should be launched by an MCP client or with a compatible transport.

## Try Other Example Servers

```powershell
.\venv\Scripts\mcp dev server.py
.\venv\Scripts\mcp dev server2.py
```

## MealDB API

`mealdb_server.py` uses:

- Base URL: `https://www.themealdb.com/api/json/v1/1`
- Endpoints:
  - `/search.php?s=<name>`
  - `/categories.php`
  - `/random.php`
