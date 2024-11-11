import weaviate
import json

# Подключение к Weaviate клиенту
client = weaviate.connect_to_custom(
    http_host="localhost", http_port=8084, http_secure=False, 
    grpc_host="localhost", grpc_port=50051, grpc_secure=False,
)

# Название коллекции
collection_name = "CallsCollection"

# Инициализация списка для хранения документов
exported_data = []

# Итерация по документам в коллекции и добавление в список
for doc in client.collections.get(collection_name).iterator(include_vector=True):
    document = {
        "text": doc.properties['call_transcription'],
        "vector": doc.vector['call_transcription_vector']
    }
    exported_data.append(document)

# Сохранение в JSON-файл
with open("calls_collection.json", "w", encoding="utf-8") as f:
    json.dump(exported_data, f, ensure_ascii=False)

client.close()
