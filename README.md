[![Paperead](https://socialify.git.ci/StardustDL/paperead/image?description=1&font=Bitter&forks=1&issues=1&language=1&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Light)](https://github.com/StardustDL/paperead)

![](https://github.com/StardustDL/paperead/workflows/CI/badge.svg) [![Netlify Status](https://api.netlify.com/api/v1/badges/fb053a29-d62b-469d-9253-d8208fec5863/deploy-status)](https://app.netlify.com/sites/paperead/deploys) ![](https://img.shields.io/github/license/StardustDL/paperead.svg) [![](https://img.shields.io/pypi/v/paperead.svg?logo=pypi)](https://pypi.org/project/paperead/) [![Downloads](https://pepy.tech/badge/paperead)](https://pepy.tech/project/paperead)

[Paperead](https://github.com/StardustDL/paperead) is a tiny tool to present and manage your reading and notes.

- Platform ![](https://img.shields.io/badge/Linux-yes-success?logo=linux) ![](https://img.shields.io/badge/Windows-yes-success?logo=windows) ![](https://img.shields.io/badge/MacOS-yes-success?logo=apple) ![](https://img.shields.io/badge/BSD-yes-success?logo=freebsd)
- Python ![](https://img.shields.io/pypi/implementation/paperead.svg?logo=pypi) ![](https://img.shields.io/pypi/pyversions/paperead.svg?logo=pypi) ![](https://img.shields.io/pypi/wheel/paperead.svg?logo=pypi)

## Features

- File-system based storage
  - Simple and readable
  - Easy to use with VSCode
- Notes in markdown
  - CommonMark
  - LaTex Math
  - Media (locally hosted or remote files)
  - Code highlighting
  - Lists and tables
  - Graphs
- Rich pages
  - Slides powered by reveal.js
  - Image, audio, and video.
  - PDF and links.
  - Dynamic generated (use Python script).
  - Raw HTML.
- Builtin web server
  - Basic authentication
  - Readonly mode
  - RESTful API
- Frontend in browser
  - Dynamic markdown rendering
  - Builtin reader mode
- Static website generator

For details about features, installation and usage, visit [documents](https://paperead.netlify.app/) website powered by Paperead.

## Install

Use pip:

```sh
pip install paperead
```

## Usage

```sh
paperead new first-material
paperead new first-material -N first-note

paperead serve

# Visit http://localhost:3649
```

## Development

```sh
# Run backend

cd src/main
pip install -r requirements.txt
python -m paperead -D "path/to/dataDir" serve
# endpoint: http://localhost:3649/api

# Run frontend
cd src/web
npm install
npm run restore
npm run dev
# endpoint: http://localhost:3600
```
