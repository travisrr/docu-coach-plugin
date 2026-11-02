# Docu-Coach plugin

Public Agent Plugins package for the Docu-Coach connector. The server itself stays in [travisrr/docu-coach](https://github.com/travisrr/docu-coach). This repository has no secrets and no private application code.

The remote server is `https://www.docu-coach.com/mcp`. A member signs in on the Docu-Coach consent screen. Tools are read-only.

## Contents

- `plugin.json` and `mcp.json` are the Agent Plugins package.
- `skills/get-started/SKILL.md` is the setup skill.
- `assets/` holds the logo.
- `server.json` is the official MCP Registry document. Its name is `io.github.travisrr/docu-coach`.
- `scripts/build-chatgpt-zip.py` writes `dist/docu-coach-chatgpt.zip`.

## Build the ChatGPT ZIP

```sh
python3 scripts/build-chatgpt-zip.py
```

The ZIP contains `plugin.json`, `mcp.json`, the get-started skill, `assets/logo.png`, and `LICENSE`. ChatGPT listing fields in `plugin.json` are 30 characters or fewer. Do not put client secrets, reviewer passwords, or API tokens in this repository.

## Links

- Documentation: https://www.docu-coach.com/docu-coach-mcp
- Privacy: https://www.docu-coach.com/privacy-policy
- Terms: https://www.docu-coach.com/terms-and-conditions
