---
name: Dynamic Content
creation: 2021-11-11 12:10:39.284533+08:00
modification: 2021-11-11 12:10:39.285534+08:00
targets:
  demo: /demo/dynamic
tags: []
extra: {}
schema: ''
---

# Schema

`dynamic:<target schema>`

The target schema is the schema for the generated content.

Only work for **dynamic** server hosting.

> Static website generator will get the snapshot at the build time.

# Content

Write your generator in Python code in a fenced Markdown code block with language `python:exec`; anything else will be ignored.

- The code is run as the same enviroment that paperead runs on. Be **careful** for the security.
- The working directory is as same as the directory of the file. You can access the file path by environment variable `PAPEREAD_FILE`.
- The code must finish in 1 minute (can be configured by `server.dynamicTimeout` field) and write the generated content to stdout.
- If the code crash or timeout, then an empty content is generated. The error will be logged.

~~~markdown
```python:exec
from datetime import datetime
import os

print("# Dynamic Content")

print(f"This content is dynamic generated at {datetime.now()}} in {{os.getcwd()}.")
```
~~~
