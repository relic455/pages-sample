"""Greeting helpers used by documentation examples."""

from dataclasses import dataclass

DEFAULT_LANGUAGE = "en"


def format_greeting(name: str, prefix: str = "Hello", excited: bool = False) -> str:
    """Return a formatted greeting string."""
    punctuation = "!" if excited else "."
    return f"{prefix}, {name}{punctuation}"


@dataclass
class Greeter:
    """Format greetings using a shared prefix."""

    prefix: str = "Hello"
    language: str = DEFAULT_LANGUAGE

    def greet(self, name: str, excited: bool = False) -> str:
        """Return a greeting for the provided name."""
        return format_greeting(name, prefix=self.prefix, excited=excited)
