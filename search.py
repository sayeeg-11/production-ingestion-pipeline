from src.retrieval import Retriever

retriever = Retriever()

query = input("Query: ")

results = retriever.search(query)

print("\nResults\n")

for i, result in enumerate(results, start=1):

    print(f"{i}. Score : {result['score']:.4f}")
    print(result["text"])
    print("-" * 80)