"""Office Joke Open entry: writes one single-line office joke."""
import os

JOKE = "Our printer only jams five minutes before a deadline, which is impressive time management for a machine with no calendar."

ENTRY_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"length {len(text)} out of range"
    assert "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open(os.path.join(ENTRY_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"chars: {len(text)}")


if __name__ == "__main__":
    main()
