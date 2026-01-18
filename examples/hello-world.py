#!/usr/bin/env python3
"""
Simple Hello World example for the cellsemantics welcome repository.

This is a basic example to demonstrate the structure of example files.
"""


def greet(name: str = "World") -> str:
    """
    Generate a greeting message.
    
    Args:
        name: The name to greet (default: "World")
    
    Returns:
        A greeting string
    """
    return f"Hello, {name}!"


def main():
    """Main function to run the example."""
    print(greet())
    print(greet("cellsemantics"))


if __name__ == "__main__":
    main()
