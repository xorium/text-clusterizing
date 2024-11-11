# Кластеризация текстов
## Подготовка к запуску
Собираем Docker образ с моделью-векторизатором (переводит текст в embedding'и):
```bash
docker build -f e5-large-instruct.Dockerfile -t e5-large-instruct .
```

Запускаем БД Weaviate для хранения векторов:
```bash
docker compose up -d
```

Устанавливаем python-зависимости:
```bash
pip install -r requirenments.txt
```

## Запуск импорта данных в БД
Предварительно необходимо в самом коде реализовать итератор документов `document_iterator` (простой пример-заглушка уже реализован)
```bash
python data_import.py
```

## Запуск кластеризации импортированных в БД данных
```bash
python clusterize.py
```

## Экспорт данных в JSON файл из БД
```bash
python export.py
```