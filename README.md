[![Paperead](https://socialify.git.ci/StardustDL/paperead/image?description=1&font=Bitter&forks=1&issues=1&language=1&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Light)](https://github.com/StardustDL/paperead)

![](https://github.com/StardustDL/paperead/workflows/CI/badge.svg) [![Netlify Status](https://api.netlify.com/api/v1/badges/fb053a29-d62b-469d-9253-d8208fec5863/deploy-status)](https://app.netlify.com/sites/paperead/deploys) ![](https://img.shields.io/github/license/StardustDL/paperead.svg) [![](https://img.shields.io/pypi/v/paperead.svg?logo=pypi)](https://pypi.org/project/paperead/) [![Downloads](https://pepy.tech/badge/paperead)](https://pepy.tech/project/paperead)

[Paperead](https://github.com/StardustDL/paperead) A tiny tool to present and manage your reading and notes.

- Platform ![](https://img.shields.io/badge/Linux-yes-success?logo=linux) ![](https://img.shields.io/badge/Windows-yes-success?logo=windows) ![](https://img.shields.io/badge/MacOS-yes-success?logo=apple) ![](https://img.shields.io/badge/BSD-yes-success?logo=freebsd)
- Python ![](https://img.shields.io/pypi/implementation/paperead.svg?logo=pypi) ![](https://img.shields.io/pypi/pyversions/paperead.svg?logo=pypi) ![](https://img.shields.io/pypi/wheel/paperead.svg?logo=pypi)
- [Documents](https://paperead.netlify.app/)

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
python -m paperead -D "path/to/dataDir" serve
# endpoint: http://localhost:3649/api

# Run frontend
cd src/web
npm run dev
# endpoint: http://localhost:3000
```
