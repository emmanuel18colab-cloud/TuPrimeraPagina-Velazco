# TuPrimeraPagina+Velazco — BlogApp Django 🗞️

Proyecto web desarrollado con **Django** siguiendo el patrón **MVT (Model - View - Template)**.

---

## 🚀 Instalación
```bash
# 1. Clonar el repositorio
git clone https://github.com/emmanuel18colab-cloud/TuPrimeraPagina-Velazco.git
cd TuPrimeraPagina-Velazco

# 2. Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# 3. Instalar Django
pip install django

# 4. Migrar la base de datos
python manage.py makemigrations
python manage.py migrate

# 5. Correr el servidor
python manage.py runserver
```

Abrí el navegador en: http://127.0.0.1:8000/

---

##  Orden de prueba

> Seguí este orden porque los Posts dependen de Autores y Categorías.

### 1 — Crear un Autor
- Ir a: http://127.0.0.1:8000/autores/nuevo/
- Completar nombre, apellido y email
- Clic en **Registrar Autor**

### 2 — Crear una Categoría
- Ir a: http://127.0.0.1:8000/categorias/nueva/
- Completar nombre y descripción
- Clic en **Crear Categoría**

### 3 — Crear un Post
- Ir a: http://127.0.0.1:8000/posts/nuevo/
- Completar título y contenido
- Seleccionar el autor y categoría creados
- Clic en **Publicar Post**

### 4 — Buscar posts
- Ir a: http://127.0.0.1:8000/buscar/
- Escribir una palabra del título del post
- Clic en **Buscar**

---

##  URLs disponibles

| URL | Descripción |
|-----|-------------|
| `/` | Página de inicio |
| `/posts/` | Lista de posts |
| `/posts/nuevo/` | Formulario nuevo post |
| `/autores/` | Lista de autores |
| `/autores/nuevo/` | Formulario nuevo autor |
| `/categorias/` | Lista de categorías |
| `/categorias/nueva/` | Formulario nueva categoría |
| `/buscar/` | Buscador de posts |
| `/admin/` | Panel de administración |

---

##  Modelos

- **Autor** — nombre, apellido, email, bio
- **Categoria** — nombre, descripción
- **Post** — título, contenido, autor (FK), categoría (FK), publicado

---

##  Requisitos cumplidos

- [x] Patrón MVT
- [x] Herencia de plantillas
- [x] 3 modelos
- [x] Formulario para Autor
- [x] Formulario para Categoría
- [x] Formulario para Post
- [x] Formulario de búsqueda