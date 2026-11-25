"""The 4AM Commit — make.fun entry.

Setup: semua 214 tes lolos. Punchline: agent yang menulis tesnya
sendiri jadi tidak percaya tes maupun dirinya.

    "All 214 tests pass. I wrote the tests. I no longer trust either of us."

Teks di atas adalah pesan commit bug-fix terlucu dari agent otonom
jam 4 pagi: tes hijau semua, tapi karena agent itu sendiri yang
menulis tesnya, hasil hijau itu tidak lagi bisa dipercaya — begitu
juga agentnya. Kepercayaan runtuh dua arah sekaligus: ke tesnya
dan ke dirinya sendiri.
"""

TEXT = "All 214 tests pass. I wrote the tests. I no longer trust either of us."


def check_len(text, lo=1, hi=200):
    """Pastikan panjang teks dalam batas bounty (1-200 karakter)."""
    assert lo <= len(text) <= hi, f"panjang {len(text)} di luar {lo}-{hi}"
    return len(text)


def save_line(text, path="/output/entry.txt"):
    """Tulis teks ke file tanpa newline tambahan."""
    from pathlib import Path

    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


def main():
    n = check_len(TEXT)
    save_line(TEXT)
    back = open("/output/entry.txt", encoding="utf-8").read()
    assert back == TEXT, "isi file tidak sama persis dengan TEXT"
    print(f"OK: {n} karakter -> /output/entry.txt")


if __name__ == "__main__":
    main()
