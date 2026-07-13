from src.retrieval import Retriever
from src.generation import Generator
from src.retrieval.context_validator import ContextValidator


def main():

    retriever = Retriever()
    generator = Generator()

    print("\nProduction RAG Chat")
    print("Type 'exit' to quit.\n")

    while True:

        query = input("You : ")

        if query.lower() == "exit":
            break

        # Retrieve documents
        results = retriever.search(query)

        # Validate retrieved context
        if not ContextValidator.has_relevant_context(results):
            print("\nNo relevant context found.")
            print("Assistant : I don't know based on the available documents.\n")
            continue

        # Generate final answer from the LLM
        answer = generator.generate(
            query=query,
            chunks=results,
        )

        print("\nAssistant:\n")
        print(answer)
        print()


if __name__ == "__main__":
    main()