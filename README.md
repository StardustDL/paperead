[![Paperead](https://socialify.git.ci/StardustDL/paperead/image?description=1&font=Bitter&forks=1&issues=1&language=1&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Light)](https://github.com/StardustDL/paperead)

![](https://github.com/StardustDL/paperead/workflows/CI/badge.svg) ![](https://img.shields.io/github/license/StardustDL/paperead.svg) [![](https://img.shields.io/pypi/v/paperead.svg?logo=pypi)](https://pypi.org/project/paperead/) [![Downloads](https://pepy.tech/badge/paperead)](https://pepy.tech/project/paperead)

[Paperead](https://github.com/StardustDL/paperead) A tiny tool to present and manage your reading and notes.

- Platform ![](https://img.shields.io/badge/Linux-yes-success?logo=linux) ![](https://img.shields.io/badge/Windows-yes-success?logo=windows) ![](https://img.shields.io/badge/MacOS-yes-success?logo=apple) ![](https://img.shields.io/badge/BSD-yes-success?logo=freebsd)
- Python ![](https://img.shields.io/pypi/implementation/paperead.svg?logo=pypi) ![](https://img.shields.io/pypi/pyversions/paperead.svg?logo=pypi) ![](https://img.shields.io/pypi/wheel/paperead.svg?logo=pypi)

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

### Website Server

```sh
paperead serve

paperead -D "path/to/dataDir" serve
```

Then visit `http://localhost:3649`.

RESTful APIs:

- `/api/materials/`
  - GET: Get all ids for materials
  - POST: Create or update a material
- `/api/materials/<id>`
  - GET: Get data of the material
  - DELETE: Delete the material
- `/api/materials/<id>/assets/<path>`
  - GET: Access assets of the material
- `/api/materials/<id>/notes/`
  - GET: Get all ids for notes of the material
  - POST: Create or update a note of the material
- `/api/materials/<id>/notes/<nid>`
  - GET: Get data of the note of the material
  - DELETE: Delete the note of the material

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

`<material>/notes/<note>.md` contains the metadata (the structure is as same as material's description) and the content for the note for the material.

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
