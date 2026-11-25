"""
Entry for the Worst Superpower competition.
This program writes one invented useless superpower to /output/entry.txt.
The joke: stopping time is a flagship power, granted here in unlimited
quantity, but for exactly zero seconds each time — so despite endless
uses with no cooldown, it can never change anything at all.
"""

import os

TEXT = "I can stop time completely, for exactly zero seconds, as often as I like, with no cooldown."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
