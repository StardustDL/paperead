[![Paperead](https://socialify.git.ci/StardustDL/paperpead/image?description=1&font=Bitter&forks=1&issues=1&language=1&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Light)](https://github.com/StardustDL/paperpead)

![](https://github.com/StardustDL/paperpead/workflows/CI/badge.svg) ![](https://img.shields.io/github/license/StardustDL/paperpead.svg) [![](https://img.shields.io/pypi/v/paperpead.svg?logo=pypi)](https://pypi.org/project/paperpead/) [![Downloads](https://pepy.tech/badge/paperpead)](https://pepy.tech/project/paperpead)

[Paperead](https://github.com/StardustDL/paperpead) A tiny tool to present and manage your reading and notes.

- Platform ![](https://img.shields.io/badge/Linux-yes-success?logo=linux) ![](https://img.shields.io/badge/Windows-yes-success?logo=windows) ![](https://img.shields.io/badge/MacOS-yes-success?logo=apple) ![](https://img.shields.io/badge/BSD-yes-success?logo=freebsd)
- Python ![](https://img.shields.io/pypi/implementation/paperpead.svg?logo=pypi) ![](https://img.shields.io/pypi/pyversions/paperpead.svg?logo=pypi) ![](https://img.shields.io/pypi/wheel/paperpead.svg?logo=pypi)

## Install

Use pip:

```sh
pip install paperead
```

Or use pipx:

```sh
# Install pipx
pip install --user pipx
pipx ensurepath

# Install Schemdule
pipx install paperead

# Upgrade
pipx upgrade paperead
```

## Usage

```sh
paperead -D "path/to/dataDir" serve
```

Then visit `http://localhost:3649`.

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
