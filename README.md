# Clasificación de digitos con una CNN

Red neuronal convolucional CNN

## Setup
1. Variables de entorno:
```bash
export PIPENV_VENV_IN_PROJECT=1
export FLASK_APP=src
export FLASK_ENV=development
```

2. Instalación de las dependencias:
```bash
pipenv install
```

3. Ejecucion aplicación:
```bash
pipenv run flask run --debug
```

## Production
Script
```bash
./start.sh
```

Ejecución de la aplicación
```bash
# Run the app
pipenv run gunicorn -w 4 'src:app'
```
