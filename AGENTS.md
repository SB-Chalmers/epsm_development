# Guidance for coding agents

This repository is the EPSM developer handbook. Write for new developers and researchers. Use plain English, explain unfamiliar terms and follow `docs/writing-guide.md`.

## Before you change something

- Read `README.md` and the relevant section of `docs/engineering-style.md`.
- Read the project, I/O and examples guides for work in those areas. Use `use_cases/README.md` to find the shared expected behaviour.
- Keep the user's requested scope clear. This repository contains documentation and templates; its guidance does not authorize changes to other repositories.
- Read `docs/branches-and-releases.md` before changing branches. Start ordinary work on a `codex/<short-name>` branch from `dev` and target `dev` for review. Preserve existing local work. Do not promote a feature to `main` as part of an ordinary task.
- Preserve the distinction between today's software, proposed package boundaries and illustrative future APIs.
- Check source facts before changing versions, test counts or scientific validation claims. Keep dated review snapshots clearly dated.

## While you work

- Make one small change with a clear purpose. Explain it with a concrete example.
- For code changes, begin with a test of observable behaviour. For documentation changes, verify the links and examples.
- Preserve useful Core-style docstrings and honest authorship. Follow `docs/licensing.md`: use MIT for EPSM-owned material, retain accurate copyright notices and preserve third-party and data terms.
- Keep logging, representation and evidence rules consistent across examples. Use the shared glossary, model ownership and plotting guide for those changes.
- Keep file/service access in I/O modules and use documented public APIs for data passed between packages. Do not import a private helper from another package to save a few lines.
- Keep `examples/` notebooks small and ordered. Show the package's own modules before integrations. Label extra prerequisites and future API sketches clearly.
- Do not add a generic entity framework, live database connection or scientific calculation to this documentation repository.
- Never present a future API sketch as implemented behaviour or a skipped integration check as passing evidence.

## Before you finish

Run `python3 scripts/check_docs.py`, `python3 -m unittest discover -s tests -v` and `python3 scripts/run_examples.py`. When changing the API documentation templates or renderer, also run `python scripts/build_api_example.py` with the optional documentation requirements installed. Explain what changed, how it was checked and any remaining limitation. Use file links so the user can open the result.
