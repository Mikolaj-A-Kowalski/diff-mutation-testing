from typing import Tuple

def produce_patch_str(mutation: Tuple[str, int, str, str]):

    filename, line_number, old_line, new_line = mutation
    patch_str = "--- {filename}\n+++ {filename}\n".format(filename=filename)
    patch_str += "@@ -{line_number},1 +{line_number},1 @@\n".format(line_number=line_number)
    patch_str += "-"+old_line+"\n"
    patch_str += "+"+new_line

    return patch_str
