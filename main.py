from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def mostrar_taller():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Taller sobre Grafos</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                color: #333;
                margin: 40px;
                line-height: 1.6;
            }
            h1, h2, h3 {
                color: #2c3e50;
            }
            pre {
                background: #f4f4f4;
                border-left: 5px solid #3498db;
                padding: 10px;
                overflow-x: auto;
            }
            code {
                font-family: Consolas, monospace;
            }
            .section {
                margin-bottom: 40px;
            }
        </style>
    </head>
    <body>
        <h1>Taller sobre Grafos</h1>

        <div class="section">
            <h2>1. ¿Qué es un grafo?</h2>
            <p>Un <strong>grafo</strong> es una estructura que representa relaciones entre objetos. Está compuesto por <strong>nodos</strong> (vértices) y <strong>aristas</strong> (enlaces) que conectan esos nodos.</p>
        </div>

        <div class="section">
            <h2>2. ¿Para qué se utilizan?</h2>
            <p>Se utilizan para modelar sistemas como redes sociales, mapas, rutas, sistemas eléctricos, estructuras de datos y mucho más. Son esenciales en ciencias de la computación y matemáticas.</p>
        </div>

        <div class="section">
            <h2>3. Partes y tipos de grafos</h2>
            <ul>
                <li><strong>Nodo o vértice:</strong> Elemento individual.</li>
                <li><strong>Arista:</strong> Conexión entre dos nodos.</li>
                <li><strong>Peso:</strong> Valor asignado a una arista (opcional).</li>
            </ul>
            <p><strong>Tipos:</strong> Dirigido, no dirigido, ponderado, no ponderado.</p>
            <pre><code>     A
    / \\
   B---C
   |   |
   D---E</code></pre>
        </div>

        <div class="section">
            <h2>4. Campo de acción o aplicación</h2>
            <p>Los grafos se aplican en análisis de redes sociales, transporte, internet, biología, inteligencia artificial, y más. Son útiles porque permiten representar relaciones complejas y resolver problemas de conectividad, búsqueda y optimización.</p>
        </div>

        <div class="section">
            <h2>5. Ejemplos en Python</h2>

            <h3>BFS (Breadth-First Search) – Búsqueda por amplitud</h3>
            <pre><code>from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(neigh for neigh in graph[vertex] if neigh not in visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
bfs(graph, 'A')  # Salida: A B C D E F</code></pre>

            <h3>DFS (Depth-First Search) – Búsqueda por profundidad</h3>
            <pre><code>def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dfs(graph, 'A')  # Salida: A B D E F C</code></pre>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)
