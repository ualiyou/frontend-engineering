# Security Policy

Frontend Engineering is a documentation and knowledge-base repository. It ships **no runtime application and no published package**, so the classic "vulnerable dependency in production" surface is minimal. Even so, we take a few classes of issue seriously.

## What counts as a security issue here

- **Malicious or unsafe example code** — a snippet in `examples/`, `recipes/`, or an article that, if copied into a real project, would introduce a vulnerability (e.g. an XSS-prone pattern presented as safe, an insecure auth flow, a `dangerouslySetInnerHTML` example without sanitization).
- **Supply-chain risk in tooling** — a compromised or malicious dependency used by our GitHub Actions or local scripts.
- **Leaked secrets** — any credential, token, or private URL accidentally committed.
- **CI/workflow abuse** — a workflow misconfiguration that could allow privilege escalation via pull requests.

## Reporting a vulnerability

**Please do not open a public issue for security reports.**

Use GitHub's **[Private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)** (Security tab → "Report a vulnerability"). If that is unavailable, contact the maintainers listed in [`GOVERNANCE.md`](GOVERNANCE.md).

Please include: the file or workflow affected, a description of the risk, and — for unsafe example code — a corrected version if you have one.

## Our commitment

- We aim to acknowledge a report within **5 business days**.
- We will confirm the issue, agree on a fix, and credit you in the fix's pull request unless you prefer to remain anonymous.
- For unsafe example code, the fix is to correct the example and add a note explaining the risk, so readers learn from it.

## Supported versions

The `main` branch is the only supported version. Content is versioned by release tag (see [`.github/MILESTONES.md`](.github/MILESTONES.md)), but fixes always land on `main` first.
