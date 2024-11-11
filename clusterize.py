import weaviate
import numpy as np
from sklearn.cluster import DBSCAN

# Подключение к Weaviate клиенту
client = weaviate.connect_to_custom(
    http_host="localhost", http_port=8084, http_secure=False, 
    grpc_host="localhost", grpc_port=50051, grpc_secure=False,
)

# Получение всех векторных представлений и текста из коллекции
collection = client.collections.get("CallsCollection")

# Извлечение векторов и текста из ответа
documents = [
    {
        "text": doc.properties['call_transcription'],  # Здесь предполагается, что текст находится в поле call_transcription
        "vector": doc.vector['call_transcription_vector']
    }
    for doc in collection.iterator(include_vector=True)
]

# Применение DBSCAN для кластеризации
vectors_np = np.array([doc["vector"] for doc in documents])
dbscan = DBSCAN(eps=0.045, min_samples=2, metric='cosine')  # Параметры можно настроить
labels = dbscan.fit_predict(vectors_np)

# Отображение текста с меткой кластера
for label, doc in zip(labels, documents):
    print(f"Кластер: {label}, Текст: {doc['text']}")

client.close()
