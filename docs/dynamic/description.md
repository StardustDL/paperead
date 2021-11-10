---
name: Dynamic Content
creation: 2021-11-10 20:22:35.315083+08:00
modification: 2021-11-10 20:22:35.315083+08:00
targets: {}
tags: []
extra: {}
schema: 'dynamic:'
---

```python:exec
from datetime import datetime
import os

print("# Dynamic Content")

print(f"This content is dynamic generated at {datetime.now()} in {os.getcwd()} .")

print("Only work for **dynamic** server hosting.")

print("> Static website generator will get the snapshot at the build time.")

print("# How to use")

print("""
1. Set schema to `dynamic:<target schema>` for dynamic generated content.
    - The target schema is the schema for the generated content.
2. Write your generator in Python code in a fenced Markdown code block with language `python:exec`.
    - The code is run as the same enviroment that paperead runs on. Be **careful** for the security.
    - The working directory is as same as the directory of the file.
    - The code must finish in 1 minute and write the generated content to stdout.
    - If the code crash or timeout, then an empty content is generated. The error will be logged.
""")

print("# Example Code")

fence = "`"*3

print(f"""
~~~markdown
{fence}python:exec
from datetime import datetime
import os

print("# Dynamic Content")

print(f"This content is dynamic generated at {datetime.now()} in {os.getcwd()}.")
{fence}
~~~
""")
```
