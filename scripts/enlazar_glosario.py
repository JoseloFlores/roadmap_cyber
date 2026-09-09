#!/usr/bin/env python3
"""Glosario referencial: ancla cada entrada del GLOSARIO.md y convierte en
enlaces (<a target="_blank">) todas las apariciones de esos terminos en los
modulos de Fase_1_Fundamentos.

Es idempotente: las anclas y enlaces ya existentes no se duplican.
"""

import os
import re
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSSARY = os.path.join(ROOT, "GLOSARIO.md")
MODULES_DIR = os.path.join(ROOT, "Fase_1_Fundamentos")


def slugify(term):
    s = unicodedata.normalize("NFKD", term)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[^a-z0-9\-]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


ROW_RE = re.compile(r'^\|\s*(?:<a id="[^"]*"></a>\s*)?\*\*(.+?)\*\*\s*\|')


def add_anchors(path):
    """Anade <a id=\"slug\"></a> a cada fila de termino del glosario."""
    terms = []
    out = []
    changed = False
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    for line in lines:
        m = ROW_RE.match(line)
        if m:
            term = m.group(1).strip()
            slug = slugify(term)
            if not re.search(r'<a id="%s"></a>' % re.escape(slug), line):
                line = line.replace(
                    "**%s**" % term, '<a id="%s"></a>**%s**' % (slug, term), 1
                )
                changed = True
            terms.append((term, slug))
        out.append(line)
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(out))
    return terms


PLACEHOLDER = "\x00%d\x00"

EXISTING_LINK_RE = re.compile(r'href="[^"]*#([^"]*)"\s+target="_blank"')


def protect(text):
    store = []

    def stash(m):
        store.append(m.group(0))
        return PLACEHOLDER % (len(store) - 1)

    # inline code
    text = re.sub(r"`[^`]*`", stash, text)
    # markdown links [text](url)
    text = re.sub(r"\[[^\]]*\]\([^)]*\)", stash, text)
    # html anchors <a ...>...</a>
    text = re.sub(r"<a\b[^>]*>.*?</a>", stash, text, flags=re.DOTALL)
    return text, store


def restore(text, store):
    for i, s in enumerate(store):
        text = text.replace(PLACEHOLDER % i, s)
    return text


def linkify_line(line, terms, rel, linked):
    text, store = protect(line)
    for term, slug in sorted(terms, key=lambda t: -len(t[0])):
        if slug in linked:
            continue
        href = "%s#%s" % (rel, slug)
        pat = r"(?<!\w)" + re.escape(term) + r"(?!\w)"
        def repl(m, h=href, s=slug, L=linked):
            L.add(s)
            return '<a href="%s" target="_blank">%s</a>' % (h, m.group(0))
        text = re.sub(pat, repl, text, count=1, flags=re.IGNORECASE)
    return restore(text, store)


def process_modules(terms):
    count = 0
    for dirpath, _, files in os.walk(MODULES_DIR):
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(GLOSSARY, os.path.dirname(path)).replace(os.sep, "/")
            with open(path, encoding="utf-8") as f:
                txt = f.read()
            linked = set(EXISTING_LINK_RE.findall(txt))
            lines = txt.split("\n")
            out = []
            in_fence = False
            modified = False
            for line in lines:
                if line.strip().startswith("```"):
                    in_fence = not in_fence
                    out.append(line)
                    continue
                if in_fence:
                    out.append(line)
                    continue
                new = linkify_line(line, terms, rel, linked)
                if new != line:
                    modified = True
                out.append(new)
            if modified:
                with open(path, "w", encoding="utf-8") as f:
                    f.write("\n".join(out))
                count += 1
    return count


def main():
    terms = add_anchors(GLOSSARY)
    print("Terminos en glosario: %d" % len(terms))
    n = process_modules(terms)
    print("Modulos modificados: %d" % n)


if __name__ == "__main__":
    main()
