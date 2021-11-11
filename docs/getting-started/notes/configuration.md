---
name: Configuration
creation: 2021-10-21 12:40:35.211721+08:00
modification: 2021-10-21 12:40:35.211721+08:00
targets: {}
tags: []
extra: {}
---

# Configuration

`.paperead.yml` under the data directory contains configuration. If it is not existed, default configuration will be used.

```yml
site:
  subtitle: ''
  title: ''
  description: ''

server:
  # Port to serve
  port: 3649
  # Password to protect the website (Basic Auth with username 'admin'), empty for public access
  auth: ""
  # Readonly mode
  readonly: false
  # Timeout in seconds for dynamic content resolving
  dynamicTimeout: 60.0
  
build:
  # Build output directory
  dist: ./dist
  # Static website host: empty, python, netlify
  host: empty
```

You can use `init` command to generate default configuration file.

```sh
paperead init
```