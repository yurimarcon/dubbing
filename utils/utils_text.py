from typing import List

def process_text(text: str, max_length: int) -> List[str]:
    """
    Divide um texto em vários segmentos, onde cada segmento tem um comprimento máximo de caracteres.

    Args:
        text (str): O texto a ser dividido.
        max_length (int): O comprimento máximo de cada segmento.

    Returns:
        List[str]: Uma lista de segmentos de texto.
    """
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        if len(' '.join(current_chunk + [word])) <= max_length:
            current_chunk.append(word)
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks