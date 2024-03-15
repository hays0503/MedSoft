# Используем легковесный базовый образ Debian Buster с предустановленным Python 3.9
FROM python:3.9-slim-buster

# Устанавливаем рабочий каталог в контейнере
WORKDIR /code

# Обновляем индекс пакетов и устанавливаем зависимости, необходимые для сборки некоторых пакетов
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates && \
    update-ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Копируем файлы зависимостей в рабочий каталог
COPY requirements.txt .

# Устанавливаем зависимости из файла
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

# Копируем исходный код приложения в рабочий каталог
COPY ./app /code/app

# Команда для запуска приложения
CMD uvicorn app.main:app --host 0.0.0.0 --reload