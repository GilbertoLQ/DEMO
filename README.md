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
3. Ejecutar test
   ```bash
   pytest -v
   ```
   o
   ```bash
   pytest --html=report.html
   ```

## Advertencia

Los archivos que estan en estas carpetas estan vacias:

- ./integration
- ./performance
- ./test/e2e/components
- ./test/e2e/flows
- ./test/e2e/validation
- ./test/e2e/pages/dashboard
- ./test/e2e/pages/profile

## Manejo de ENV

- Las credenciales se definen en los YAML de configuración. No se suben valores reales, solo ejemplos
- Se incluye un módulo (s3_loader.py) que simula cómo se podría obtener y leer una configuración YAML desde un bucket de Amazon S3.
