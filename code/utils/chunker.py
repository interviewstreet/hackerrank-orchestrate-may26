import re

def chunk_text(text: str, chunk_size: int = 512, overlap: int = 64) -> list[dict]:
    """
    Splits markdown text into overlapping chunks.
    Preserves the last seen heading so each chunk carries section context.
    Returns list of {text, heading}.
    """
    # normalise whitespace
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    words      = text.split()
    chunks     = []
    i          = 0
    current_heading = ""

    heading_re = re.compile(r"^#{1,4}\s+(.+)$", re.MULTILINE)

    while i < len(words):
        window = words[i : i + chunk_size]
        chunk_text_str = " ".join(window)

        # track the most recent heading visible in this window
        for m in heading_re.finditer(chunk_text_str):
            current_heading = m.group(1).strip()

        chunks.append({
            "text":    chunk_text_str,
            "heading": current_heading,
        })
        i += chunk_size - overlap

    return chunks