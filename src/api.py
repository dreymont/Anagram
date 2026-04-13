from fastapi import FastAPI, HTTPException
from src.main import group_anagrams
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/anagrams/{word}")
def get_anagrams(word: str):
    with open("src/wordlist.txt", encoding="iso-8859-1") as f:
        keywords = tuple(f.read().split('\n'))

    same_length = [w for w in keywords if len(w) == len(word)]
    groups = group_anagrams(same_length)
    for group in groups:
        if word in group:
            return {"anagrams": group}

    raise HTTPException(status_code=404, detail=f"No anagrams found for '{word}'")
