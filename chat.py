from src.retrieval import Retriever

retriever = Retriever()

while True:

    query = input("\nYou : ")

    if query.lower() == "exit":
        break

    results = retriever.search(query)

    print("\nRetrieved Chunks\n")

    for i, result in enumerate(results, start=1):

        print(f"{i}. Score : {result['score']:.4f}")
        print(result["text"][:400])
        print("-" * 80)