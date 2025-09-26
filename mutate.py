# mutate.py
from typing import List, Tuple

def mutate_line(
    file: str, 
    line_number: int, 
    oldline: str
) -> Tuple[str, int, str, str] | None:
    """
    Try to mutate a single line by flipping the first '+' <-> '-' operator.
    Returns (file, line_number, oldline, newline) if mutated, else None.
    """
    if "+" in oldline and "++" not in oldline:
        newline = oldline.replace("+", "-", 1)
    elif "-" in oldline and "--" not in oldline:
        newline = oldline.replace("-", "+", 1)
    else:
        return None

    if newline == oldline:
        return None

    return (file, line_number, oldline.rstrip("\n"), newline.rstrip("\n"))


def mutate_candidates(
    candidates: List[Tuple[str, int, str]]
) -> List[Tuple[str, int, str, str]]:
    """
    Loop over candidate tuples and collect valid mutations.
    
    Args:
        candidates: list of (file, line_number, oldline)
    
    Returns:
        List of (file, line_number, oldline, newline) for lines that mutate.
    """
    results = []
    for file, line_number, oldline in candidates:
        mutated = mutate_line(file, line_number, oldline)
        if mutated is not None:
            results.append(mutated)
    return results
