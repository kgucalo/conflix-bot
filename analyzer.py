def analyze_text(text: str) -> str:
    if any(w in text.lower() for w in ['ты', 'всегда', 'никогда']):
        return "обвинительный тон"
    elif "извини" in text.lower():
        return "мягкий, примирительный тон"
    else:
        return "нейтральный или непонятный"
