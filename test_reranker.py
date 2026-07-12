from src.reranking import Reranker

reranker = Reranker()

query = "What is Artificial Intelligence?"

chunks = [
    {
        "text": "Artificial Intelligence is the simulation of human intelligence in machines."
    },
    {
        "text": "Basketball is played with five players on each team."
    },
    {
        "text": "Machine Learning is a subset of Artificial Intelligence."
    }
]

results = reranker.rerank(
    query=query,
    chunks=chunks,
    top_k=3
)

print("\nReranked Results\n")

for i, chunk in enumerate(results, start=1):
    print(f"{i}. Score: {chunk['rerank_score']:.4f}")
    print(chunk["text"])
    print()