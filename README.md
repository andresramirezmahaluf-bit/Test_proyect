# G-Take Dashboard Prototype

Este proyecto es un prototipo de interfaz de usuario (UI) para un dashboard moderno, diseñado con un enfoque estético futurista "Dark Mode".

## 🛠️ Stack Tecnológico

El proyecto ha sido construido utilizando tecnologías web estándar sin dependencias de frameworks pesados (`Vanilla Code`):

*   **HTML5 Semantic**: Estructura semántica del documento (`<nav>`, `<header>`, `<main>`, `<section>`).
*   **CSS3 (Vanilla)**: Estilos puros sin preprocesadores.
    *   **CSS Variables**: Uso intensivo de `:root` para gestionar la paleta de colores y mantener la consistencia del tema.
    *   **CSS Grid**: Utilizado para el layout principal del dashboard (sistema de grilla 2 columnas).
    *   **Flexbox**: Utilizado para la alineación de componentes internos (navegación, tarjetas, listas).
*   **JavaScript**: Mínimo (o nulo en esta versión estática), enfocado solo en la carga de recursos externos.

## 🎨 Características Técnicas de Diseño

### 1. Sistema de Diseño (Design System)
*   **Glassmorphism**: Implementación de efecto vidrio esmerilado utilizando `backdrop-filter: blur(14px)` y colores `rgba` con transparencia.
*   **Tipografía**:
    *   Fuente: **Plus Jakarta Sans** (Google Fonts).
    *   Pesos: 400 (Regular), 500 (Medium), 600 (SemiBold), 700 (Bold).
*   **Iconografía**:
    *   Librería: **Phosphor Icons** (cargada vía CDN).
    *   Estilo: Iconos rellenos (`ph-fill`) y negrita (`ph-bold`).

### 2. Paleta de Colores
Definida en variables CSS para fácil mantenimiento:
*   `--bg-dark`: `#0B0C15` (Fondo principal)
*   `--primary-blue`: `#3B66F5` (Color de acento principal)
*   `--secondary-cyan`: `#4CC9F0` (Detalles y gradientes)
*   `--glass-bg`: `rgba(30, 32, 50, 0.5)` (Superficies de vidrio)

### 3. Estructura de Archivos
```text
/
├── g-take-dashboard/
│   ├── index.html    # Estructura principal
│   └── styles.css    # Hoja de estilos completa
├── extract_colors.py # Script de utilidad (Python) para análisis de color
└── README.md         # Documentación técnica
```

## 🚀 Despliegue y Uso
Simplemente abrir el archivo `index.html` en cualquier navegador web moderno (Chrome, Firefox, Edge). No requiere servidor local ni compilación.
