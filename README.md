# Hola Neurona Streamlit

Una aplicación web interactiva construida con Streamlit para explorar conceptos relacionados con redes neuronales. 
[Link app desplegada](https://holaneurona-rxy.streamlit.app/)

## Descripción

Este proyecto es una aplicación de demostración desarrollada con Streamlit, diseñada para proporcionar una interfaz web interactiva.  La aplicación está completamente containerizada con Docker para facilitar su despliegue.

## Características

- Interfaz web interactiva con Streamlit
- Containerización con Docker
- Configuración lista para producción con docker-compose
- Fácil despliegue y configuración

## Requisitos

- Python 3.x
- Docker (opcional, para ejecutar con contenedores)
- Docker Compose (opcional, para ejecutar con contenedores)

## Instalación

### Instalación Local

1. Clona el repositorio:
```bash
git clone https://github.com/rxy94/hola_neurona_streamlit.git
cd hola_neurona_streamlit
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
streamlit run streamlit_app.py
```

4. Abre tu navegador en `http://localhost:8501`

### Instalación con Docker

1. Clona el repositorio:
```bash
git clone https://github.com/rxy94/hola_neurona_streamlit.git
cd hola_neurona_streamlit
```

2. Construye y ejecuta con docker-compose:
```bash
docker-compose up --build
```

3. Abre tu navegador en `http://localhost:8501`

### Usando solo Docker

```bash
docker build -t hola-neurona-streamlit .
docker run -p 8501:8501 hola-neurona-streamlit
```

## Tecnologías

- **[Streamlit](https://streamlit.io/)**: Framework para crear aplicaciones web interactivas en Python
- **Docker**: Containerización de la aplicación
- **Python**: Lenguaje de programación principal

## Uso

Una vez que la aplicación esté en ejecución, podrás interactuar con ella a través de tu navegador web. La interfaz de Streamlit te permitirá explorar las diferentes funcionalidades de manera intuitiva.

## Licencia

Este proyecto no tiene una licencia especificada actualmente. 

## Autor

**rxy94**
- GitHub: [@rxy94](https://github.com/rxy94)

---

⭐️ Si este proyecto te ha sido útil, considera darle una estrella en GitHub!
