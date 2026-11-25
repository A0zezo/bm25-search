# bm25-search

BM25 ranking implemented from scratch in plain Python (term frequency, inverse document frequency, length normalization), with a small demo corpus.

## Run

```bash
pip install -r requirements.txt
python bm25.py your query here
pytest
```

## Output (reproduced)

```
$ python3 bm25.py hybrid keyword vector
5.848  [6] Hybrid search combines keyword scores with vector similarity.

$ python3 bm25.py why normalize document length
2.705  [3] Document length normalization stops long documents from dominating the ranking.
0.893  [2] Inverse document frequency gives rare words more weight than common words.
0.893  [1] Term frequency counts how often a word appears in a document.

$ pytest -q
5 passed in 0.01s
```

## Limits

- Whitespace/alphanumeric tokenizer only, no stemming or stop words. Eight-sentence demo corpus, so this shows the mechanism, not search quality.
