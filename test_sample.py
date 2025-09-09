#!/usr/bin/env python3
"""
A simple test file for MCP PRIME to analyze.
"""

def greet(name: str, age: int = 25) -> str:
    """
    Greet a person with their name and age.
    
    Args:
        name: The person's name
        age: The person's age (default: 25)
        
    Returns:
        A greeting string
    """
    return f"Hello {name}, you are {age} years old!"

class Calculator:
    """A simple calculator class."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.value = 0
    
    def add(self, x: float) -> float:
        """Add a value to the current result."""
        self.value += x
        return self.value

def _private_function():
    """This function should be ignored."""
    pass