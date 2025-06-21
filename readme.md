# Cursos Deportivos

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Node.js](https://img.shields.io/badge/node-22.x-green.svg)

## Descripción del Proyecto

Este proyecto es una plataforma web para la gestión de cursos deportivos. Permite a los usuarios buscar, registrarse y participar en diferentes actividades deportivas. La aplicación cuenta con un backend desarrollado en Python y un frontend en React/Node.js.

## Tabla de Contenidos

- [Requisitos Previos](#requisitos-previos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
  - [Clonar el Repositorio](#clonar-el-repositorio)
  - [Configuración del Entorno](#configuración-del-entorno)
  - [Instalación del Backend](#instalación-del-backend)
  - [Instalación del Frontend](#instalación-del-frontend)
- [Ejecución del Proyecto](#ejecución-del-proyecto)
- [Solución de Problemas](#solución-de-problemas)

## Requisitos Previos

Para ejecutar este proyecto necesitarás tener instalado:

- Python 3.x o superior
- pip (gestor de paquetes de Python)
- Node.js 22.x
- npm (incluido con Node.js)
- Git

## Estructura del Proyecto

```
cursosdeportivos/
├── backend/         # Servidor API Python
│   ├── app.py       # Punto de entrada principal
│   └── ...
├── frontend/        # Aplicación cliente (React/Node.js)
│   ├── src/         # Código fuente
│   └── ...
└── .env             # Archivo de configuración (necesita crearse)
```

## Instalación

### Clonar el Repositorio

```bash
git clone [URL_DEL_REPOSITORIO]
cd cursosdeportivos
```

### Configuración del Entorno

Crear un archivo `.env` en la raíz del proyecto con la siguiente estructura:

```
DB_HOST=valor_host
DB_USER=valor_usuario
DB_PASSWORD=valor_contraseña
DB_NAME=valor_nombre_db

SECRET_KEY=valor_clave_secreta
```

> **Nota**: Reemplaza los valores (`valor_host`, etc.) con la configuración específica para tu entorno.

### Instalación del Backend

```bash
cd backend
python -m venv venv
```

Para activar el entorno virtual:

**Windows**:
```bash
venv\Scripts\activate
```

**Linux/MacOS**:
```bash
source venv/bin/activate
```

Luego, instala las dependencias:
```bash
pip install -r requirements.txt
```

### Instalación del Frontend

```bash
cd frontend
npm install
```

## Ejecución del Proyecto

Para iniciar el backend:

```bash
cd backend
python app.py
```

El servidor backend estará disponible en `http://localhost:5000` (o el puerto configurado).

Para iniciar el frontend:

```bash
cd frontend
npm start
```

La aplicación frontend estará disponible en `http://localhost:5173/`.

## Solución de Problemas

### Problemas Comunes con el Backend

- **Error de conexión a la base de datos**: Verifica que los datos en el archivo `.env` sean correctos y que la base de datos esté en ejecución.
- **Módulos faltantes**: Si aparecen errores de módulos no encontrados, asegúrate de haber activado el entorno virtual e instalado todas las dependencias con `pip install -r requirements.txt`.

### Problemas Comunes con el Frontend

- **Errores de dependencias**: Si encuentras problemas con las dependencias, intenta borrar la carpeta `node_modules` y ejecutar `npm install` nuevamente.
- **Errores de conexión con el backend**: Verifica que el backend esté en ejecución y que las URLs de API estén configuradas correctamente.

---

Para más información o soporte, contacta al equipo de desarrollo.
