#!/usr/bin/env python3
"""Render a private, offline taste report using only the Python standard library."""
import argparse
import json
from pathlib import Path


def render(data, template):
    for key in ("headline", "intro", "signature", "share", "scope"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f"{key} must be a nonempty string")
    stories = data.get("stories")
    if not isinstance(stories, list) or not stories:
        raise ValueError("stories must be a nonempty list")
    for story in stories:
        for key in ("title", "insight", "origin", "limit"):
            if not isinstance(story.get(key), str):
                raise ValueError(f"story.{key} must be a string")
        if not isinstance(story.get("moments"), list) or not story["moments"]:
            raise ValueError("each story needs evidence moments")
        for moment in story["moments"]:
            for key in ("date", "quote", "context", "source"):
                if not isinstance(moment.get(key), str):
                    raise ValueError(f"moment.{key} must be a string")
    # Data never becomes executable markup, including quotes containing </script>.
    payload = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    marker = "__REPORT_DATA__"
    if template.count(marker) != 1:
        raise ValueError("expected exactly one data placeholder")
    return template.replace(marker, payload)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    template = Path(__file__).resolve().parent.parent / "assets" / "report.html"
    result = render(json.loads(args.data.read_text(encoding="utf-8")), template.read_text(encoding="utf-8"))
    # Refuse overwrites, including accidental overwrites of the input.
    with args.output.open("x", encoding="utf-8") as output:
        output.write(result)
    print(args.output.resolve())


if __name__ == "__main__":
    main()
