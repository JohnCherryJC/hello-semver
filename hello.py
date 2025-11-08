# hello.py
import sys

def greet(name="World"):
    return f"Hello, {name}! Welcome to SemVer Demo."

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(greet(name))

# Пример:
def greet(name="World", lang="en"):
    greetings = {"en": "Hello", "ru": "Привет"}
    return f"{greetings.get(lang,'Hello')}, {name}!"
