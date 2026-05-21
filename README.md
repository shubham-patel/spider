# Spider

A recursive web link extractor written in Python 3. Given a starting URL, it crawls the page, extracts all `href` links, and recursively follows them — mapping every reachable URL on the target site.

> **Disclaimer:** For educational purposes and authorized testing only. Only use on websites you own or have explicit permission to test. The author is not responsible for any misuse.

---

## How it works

1. Fetches the starting URL
2. Extracts all `href` links via regex
3. Resolves relative links to absolute URLs
4. Recursively crawls each new link within the same domain
5. Prints every discovered URL

## Requirements

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 spider.py
```

```
Enter URL in proper format (e.g. 'https://www.google.com'):
```

**Recommended test target:** [http://testphp.vulnweb.com](http://testphp.vulnweb.com) — a deliberately vulnerable web app safe to test against.

---

## Part of [H-Tools](https://github.com/shubham-patel/H-Tools)

Built during B.Tech studies. H-Tools bundles this and other networking/security utilities in a single CLI menu.
