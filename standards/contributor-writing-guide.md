# Contributor Writing Guide

Use this short path before submitting an article.

1. Confirm the topic belongs in the [Knowledge Map](../KNOWLEDGE_MAP.md) and open an issue for a substantial new article.
2. Copy the [article template](../templates/article-template.md), keep every required section, and explain the decision and trade-offs rather than writing a tutorial.
3. Add matching metadata to the domain `graph.json`; then run `python scripts/validate-frontmatter.py` and `python scripts/validate-links.py` from the repository root.
4. Cite authoritative sources, use US English, and check the [article-quality checklist](article-quality.md) before opening a PR.

For the complete rules, start with the [standards index](README.md) and [contributing guide](../CONTRIBUTING.md).
