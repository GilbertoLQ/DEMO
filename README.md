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

## Manejo de ENV

- Las credenciales se definen en los YAML de configuración. No se suben valores reales, solo ejemplos
- Se incluye un módulo (s3_loader.py) que simula cómo se podría obtener y leer una configuración YAML desde un bucket de Amazon S3.

## Schema demo

<!-- DEMO/
├── 📂 config/
│   ├── 📂 envs/                  # YAMLs locales (simulan S3)
│   │   ├── 📜 dev.yml            # Config desarrollo
│   │   ├── 📜 qa.yml            # Config qa
│   │   └── 📜 prod.yml           # Config producción
│   ├── 📂 schemas/               # Modelos Pydantic
│   │   ├── 📜 app.py             # AppConfig
│   │   ├── 📜 auth.py            # Credentials
│   │   └── 📜 db.py              # DatabaseConfig
│   ├── 📂 loaders/               # Cargadores de config
│   │   ├── 📜 local_loader.py    # Loader (local)
│   │   └── 📜 s3_loader.py       # Ejemplo (S3)
│   └── 📜 __init__.py            # Interface principal
├── 📂 pages/                     # Page Objects
│   └── 📜 login_page.py
├── 📂 tests/
│   └── 📜 test_login.py
├── 📂 utils/
│   ├── 📜 driver_manager.py      # Manejo de WebDriver
│   └── 📜 helpers.py             # Funciones auxiliares
├── 📜 conftest.py                # Fixtures de pytest
├── 📜 pytest.ini                 # Config pytest
└── 📜 requirements.txt           # Dependencias
