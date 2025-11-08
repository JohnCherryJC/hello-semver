# hello.py
import sys

def greet(name="World"):
    return f"Hello, {name}! Welcome to Semantic Versioning Demo."

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(greet(name))
