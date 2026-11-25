"""BM25 ranking implemented from scratch (no dependencies)."""
import math
import re
from collections import Counter


def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())


class BM25:
    def __init__(self, docs, k1=1.5, b=0.75):
        self.docs = docs
        self.k1, self.b = k1, b
        self.tf = [Counter(tokenize(d)) for d in docs]
        self.len = [sum(t.values()) for t in self.tf]
        self.avg = sum(self.len) / len(docs)
        df = Counter(w for t in self.tf for w in t)
        n = len(docs)
        self.idf = {w: math.log(1 + (n - c + 0.5) / (c + 0.5)) for w, c in df.items()}

    def score(self, query, i):
        s = 0.0
        for w in tokenize(query):
            f = self.tf[i].get(w, 0)
            if f:
                s += self.idf[w] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * self.len[i] / self.avg))
        return s

    def search(self, query, k=3):
        r = sorted(((self.score(query, i), i) for i in range(len(self.docs))), reverse=True)
        return [(s, i, self.docs[i]) for s, i in r[:k] if s > 0]


if __name__ == "__main__":
    import sys
    docs = [l.strip() for l in open("corpus.txt") if l.strip()]
    for s, i, d in BM25(docs).search(" ".join(sys.argv[1:])):
        print(f"{s:.3f}  [{i}] {d}")
