from src.retrieval import Retriever
from src.prompt import PromptBuilder

retriever = Retriever()

query = input("You: ")

results = retriever.search(query)

prompt = PromptBuilder.build(
    query,
    results,
)

print("\n")
print("=" * 80)
print(prompt)
print("=" * 80)