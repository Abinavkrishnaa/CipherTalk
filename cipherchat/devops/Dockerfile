# Use official Python image
FROM python:3.13.2
# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client
# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=cipherchat.settings

# Set working directory inside the container
WORKDIR /app

# Copy only requirements file first (to optimize Docker caching)
COPY ../requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project from the root directory
COPY ../ /app/

# Expose the port Django runs on
EXPOSE 8000

# Run migrations, collect static files, and start Daphne ASGI server
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && daphne -b 0.0.0.0 -p 8000 cipherchat.asgi:application"]
