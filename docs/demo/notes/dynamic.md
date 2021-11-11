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

print(f"This content is dynamic generated from {os.getenv('PAPEREAD_FILE', '<unknown file>')} at {datetime.now()} in {os.getcwd()}.")

print("Only work for **dynamic** server hosting.")

print("> Static website generator will get the snapshot at the build time.")

print("# Example Code")

fence = "`"*3

print(f"""
~~~markdown
{fence}python:exec
from datetime import datetime
import os

print("# Dynamic Content")

print(f"This content is dynamic generated from {{os.getenv('PAPEREAD_FILE', '<unknown file>')}} at {{datetime.now()}} in {{os.getcwd()}}.")
{fence}
~~~
""")
```
