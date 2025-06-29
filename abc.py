# vikas.py
import sys

def say_hello():
    if len(sys.argv) > 1:
        user_name = sys.argv[1]
    else:
        user_name = "DefaultUser"
    print(f"Hello, {user_name}! Welcome to GitHub from Jenkins.")

say_hello()
