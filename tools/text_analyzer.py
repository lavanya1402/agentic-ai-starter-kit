def basic_text_stats(text: str) -> dict:
    """A simple local tool for text analysis."""
    words = text.split()
    sentences = [s for s in text.replace("?", ".").replace("!", ".").split(".") if s.strip()]

    return {
        "character_count": len(text),
        "word_count": len(words),
        "sentence_count": len(sentences)
    }
