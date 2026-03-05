# Usamos una versión ligera de Python
FROM python:3.9-slim

# Directorio de trabajo
WORKDIR /app

# Copiamos los archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

# Exponemos el puerto del backend
EXPOSE 5000

# Comando para arrancar
CMD ["python", "app.py"]