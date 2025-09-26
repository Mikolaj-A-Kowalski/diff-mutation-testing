from typing import List, Tuple, TextIO
import re

def parse_diff(diff: TextIO) -> List[Tuple[str, int, str]]:

    filename = ""

    line_number_start = 0
    line_count = 0
    current_line = 0

    diff_lines = []

    for line in diff:
        if line[:5] == "diff ":
            filename = get_filename(line)
            # Use value of 0 to indicate that actual file has not started
            current_line = 0
        elif line[:2] == "@@":
            line_number_start, line_count = get_line_number(line)
            current_line = 1
        elif current_line > 0:
            if line[0] == "+":
                diff_lines.append((filename, current_line, line[1:]))
            current_line += 1

    return diff_lines


def get_filename(diff_line: str) -> str:

    pattern = r'b/(\S+)'
    f = re.search(pattern, diff_line) 
    
    return f.group(1)

def get_line_number(line: str) -> Tuple[int, int]:

    pattern = r'\+(\d+),(\d+)'
    l_search = re.search(pattern, line) 
    
    return (int(l_search.group(1)), int(l_search.group(2)))
