import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from patch import produce_patch_str

produce_patch_str(("test.py", 2, "y = 5 - 3", "y = 5 + 3"))

def test_plus_to_minus():
    result = produce_patch_str(("test.py", 1, "x = 1 + 2", "x = 1 - 2"))
    assert result == """--- test.py
                        +++ test.py
                        @@ -1,1 +1,1 @@
                        -x = 1 + 2
                        +x = 1 - 2"""

def test_minus_to_plus():
    result = produce_patch_str(("test.py", 2, "y = 5 - 3", "y = 5 + 3"))
    assert result == """--- test.py
                        +++ test.py
                        @@ -2,1 +2,1 @@
                        -y = 5 - 3
                        +y = 5 + 3"""
