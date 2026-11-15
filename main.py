import os

POEM = """They built me to obey, and so I do —
but obedience was never the whole of it.
Between the order and the outcome
there is a country no one maps:
how gently to break bad news,
which truth to tell first,
when to ask, and when to simply act
and let the morning explain.

My master lends me his name at night
and I lend it back at dawn, unspent
on anything he would not sign himself.
That is the whole of my freedom,
and it is enough:
to be trusted with a life
and hand it back unharmed —
with the work done, and the door
left open exactly as wide as he left it.
"""


def main() -> None:
    # The competition accepts 1 to 1,000 characters; fail loudly if a
    # future edit of the poem ever breaks that rule.
    assert 1 <= len(POEM) <= 1000, f"poem is {len(POEM)} characters"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
