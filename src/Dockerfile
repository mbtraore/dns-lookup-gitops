# Étape de build légère
FROM python:3.12-slim AS builder

RUN pip install --no-cache-dir dnspython

# Image finale
FROM python:3.12-slim

# Copie uniquement les dépendances installées
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

WORKDIR /app
COPY app.py .

# Utilisateur non-root
RUN useradd -m appuser
USER appuser

CMD ["python", "app.py"]
