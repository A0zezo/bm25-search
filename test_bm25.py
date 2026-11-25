from bm25 import BM25, tokenize

DOCS = ["the cat sat on the mat", "dogs chase cats", "a long long document about python programming and many other things",
        "python snake"]


def test_tokenize():
    assert tokenize("Hello, World-42!") == ["hello", "world", "42"]


def test_exact_match_ranks_first():
    assert BM25(DOCS).search("cat mat")[0][1] == 0


def test_rare_term_beats_common():
    d = ["python python", "python rare", "python x", "python y"]
    assert BM25(d).search("rare")[0][1] == 1


def test_length_normalization():
    r = BM25(DOCS).search("python")
    assert r[0][1] == 3


def test_no_match():
    assert BM25(DOCS).search("zzz") == []
