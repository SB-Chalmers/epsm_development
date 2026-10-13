# Guidance for coding agents

This repository is the EPSM developer handbook. Its readers include new developers and researchers, so use simple, welcoming language and explain unfamiliar terms.

## Before you change something

- Read `README.md` and the relevant section of `docs/engineering-style.md`.
- Keep the user's requested scope clear. This repository contains documentation and templates; its guidance does not authorize changes to other repositories.
- Preserve the distinction between today's software, proposed package boundaries and illustrative future APIs.
- Check source facts before changing versions, test counts or scientific validation claims. Keep dated review snapshots clearly dated.

## While you work

- Make a small, coherent change. Use concrete examples rather than abstract framework language.
- For code changes, begin with a test of observable behaviour. For documentation changes, verify the links and examples.
- Preserve useful Core-style docstrings, honest authorship and project-approved license information in templates.
- Keep logging, representation and evidence rules consistent across examples.
- Do not add a generic entity framework, live database connection or scientific calculation to this documentation repository.
- Never present a future API sketch as implemented behaviour or a skipped integration check as passing evidence.

## Before you finish

Run `python3 scripts/check_docs.py` and `python3 -m unittest discover -s tests -v`. Explain what changed, how it was checked and any remaining limitation. Use file links so the user can open the result.
