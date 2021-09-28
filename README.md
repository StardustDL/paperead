<!--[![Paperead](https://socialify.git.ci/StardustDL/paperpead/image?description=1&font=Bitter&forks=1&issues=1&language=1&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Light)](https://github.com/StardustDL/paperpead)-->

# Paperead

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

### Command-line Management

Create/Delete/List materials and notes.

```sh
# Use current directory as data directory
paperead new/rm/list --help

# Custom data directory
paperead -D "path/to/dataDir" <COMMANDS>
```

### Serve Website

```sh
paperead serve

paperead -D "path/to/dataDir" serve
```

Then visit `http://localhost:3649`.

## Data Directory

Paperead works in a data directory. The directory's structure is like the following.

```
/
    material1/
        description.md
        assets/
        notes/
            note1.md
```

### Material Description

`<material>/description.md` contains the metadata and the description for the material.

```
---
# Metadata in YAML
name: Name
creation: 2021-09-26 09:00:00+00:00
modification: 2021-09-26 09:00:00+00:00
targets:
  image: "./assets/image.png"
tags:
- tag1
- tag2
extra:
  key1: "value1"
  key2: "value2"
---

Description in Markdown.
```

### Notes

`<material>/notes/<note>.md` contains the metadata and the content for the note for the material.

```
---
# Metadata in YAML
name: Name
creation: 2021-09-26 09:00:00+00:00
modification: 2021-09-26 09:00:00+00:00
---

Content in Markdown.
```

### Assets

`<material>/assets/` contains all additional files for the material, this will be directly served as static files,
and all `.md` files for the material can access these files by using `./assets/...` or `../assets/...` (just relative path).

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
