"""
Create a script that prints an emoji (via emoji) and an optional message (pretty printed with
rich). Use this outline and replace all None placeholders.
"""

#!/usr/bin/env python3
"""Print a chosen emoji and optional message from the command line."""
import argparse
from emoji import emojize
from rich import print

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Prints out specified emoji along with a message") # TODO: replace None with a helpful description of the f(x)
    parser.add_argument("--name", default=":red_heart:", help="Type an emoji") # TODO: default like ":rocket:" and a clear help string
    parser.add_argument("--msg", default="I love you", help="Type a message") # TODO: default empty string and clear help
    return parser

def render_emoji(name: str, msg: str) -> str:
    """Return the combined emoji + message string."""
    symbol = emojize(name, language="alias") # DO NOT Change this line the first None is needed
    output = f"{symbol} {msg.strip()}" # TODO: build f-string combining symbol + msg (strip trailing spaces)
    return output

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    # # TODO: ensure args.name and args.msg become strings
    name = args.name # e.g., str(args.name)
    msg = args.msg # e.g., str(args.msg)
    result = render_emoji(name, msg)
    print(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
