# Étape 1: Construire le frontend React
FROM node:18 AS build-frontend

WORKDIR /frontend

# Copier les fichiers package.json et package-lock.json
COPY frontend/package*.json ./

# Installer les dépendances
RUN npm install

# Copier le reste des fichiers frontend
COPY frontend/ .

# Construire le projet React
RUN npm run build

# Étape 2: Construire le backend Flask
FROM python:3.10 AS build-backend

WORKDIR /backend

# Copier le fichier requirements.txt
COPY backend/requirements.txt .

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Copier le reste des fichiers backend
COPY backend/ .

# Étape 3: Préparer l'image finale
FROM python:3.10

# Installer les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers construits du frontend
COPY --from=build-frontend /frontend/build /usr/share/nginx/html

# Copier les fichiers backend
COPY --from=build-backend /backend /app

# Copier la configuration Nginx
COPY nginx.conf /etc/nginx/nginx.conf

WORKDIR /app

# Exposer les ports
EXPOSE 80
EXPOSE 5000

# Démarrer Nginx et Flask
CMD ["sh", "-c", "nginx && gunicorn -b 0.0.0.0:5000 app:app"]
