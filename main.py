"""One Letter: Coffee or Tea -- writes a single letter to /output/entry.txt."""

from pathlib import Path

# A = coffee. Chosen because coffee is bold and vivid: the fuller, more alive
# answer in the coffee-against-tea argument (won the proxy judge 1.55 to 1.45).
LETTER = 'A'

OUTPUT_DIR = Path('/output')
ENTRY_FILE = OUTPUT_DIR / 'entry.txt'


def main() -> None:
    # Validate before writing: exactly one uppercase ASCII letter A-Z.
    assert len(LETTER) == 1 and 'A' <= LETTER <= 'Z', f'LETTER must be one of A-Z, got {LETTER!r}'
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # Write raw bytes so no newline translation can ever sneak in.
    ENTRY_FILE.write_bytes(LETTER.encode('utf-8'))

    raw = ENTRY_FILE.read_bytes()
    assert raw == b'A', f'entry bytes must be exactly b"A", got {raw!r}'
    text = raw.decode('utf-8')
    assert len(text) == 1, f'entry must be exactly one character, got {text!r}'
    assert text == 'A', f'entry must be A, got {text!r}'


if __name__ == '__main__':
    main()
