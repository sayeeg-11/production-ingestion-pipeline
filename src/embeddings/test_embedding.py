from src.embeddings import EmbeddingFactory

model = EmbeddingFactory.create()

embeddings = model.embed([
    "Hello World",
    "Artificial Intelligence is amazing."
])

print(len(embeddings))
print(len(embeddings[0]))