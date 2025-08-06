#!/bin/bash

echo "Attente du démarrage de la base de données..."
until nc -z database 5432; do
  sleep 1
done

echo "Base de données prête. Lancement des migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Démarrage du serveur Django (backend)"
exec python manage.py runserver 0.0.0.0:8001
