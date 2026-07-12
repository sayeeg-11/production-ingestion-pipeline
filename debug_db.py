from src.vectorstores import FAISSStore

db = FAISSStore()
db.load()

print(f"Total vectors : {db.index.ntotal}")
print(f"Metadata entries : {len(db.metadata)}")

count = 0

for item in db.metadata:
    text = item["text"].lower()

    if "sayee" in text:
        count += 1
        print("=" * 80)
        print(text[:500])

print(f"\nFound {count} chunks containing 'sayee'")