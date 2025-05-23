# Selenium Login Demo (Python)

Este proyecto es una demostración de pruebas automatizadas E2E usando Selenium y Pytest para automatizar el flujo de login en un sitio de práctica.

Sitio bajo prueba: [https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)

## 🧰 Tecnologías utilizadas

- Python
- Selenium
- Pytest

## 🧪 ¿Qué se prueba?

- Login exitoso con credenciales válidas.
- Login fallido con credenciales incorrectas.
- Captura de pantallas si el test falla.

## 🚀 Cómo ejecutar

1. Clona el repositorio
2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Example:

🔐 Configuración de credenciales

- Este proyecto usa un archivo .env para manejar las credenciales de acceso sin exponerlas directamente en el código.
- Crea un archivo .env en la raíz del proyecto con el siguiente contenido:

USERNAME=demo_user
PASSWORD=demo_pass

## ⚠️ El archivo .env está en el .gitignore y no se sube al repositorio, así que asegúrate de crearlo localmente antes de correr las pruebas.
