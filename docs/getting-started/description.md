---
name: Getting Started
creation: 2021-10-02 08:32:57.816903+08:00
modification: 2021-10-02 08:32:57.816903+08:00
targets: {}
tags: []
extra: {}
---

# Getting Started

Here is the simple guide. For more details, see notes of this material (click the button notes at the top right corner).

## Install

Use pip:

```sh
pip install paperead
```

Or use pipx:

```sh
pipx install paperead
```

## Create a data directory

```sh
mkdir data

cd data
```

## Write a new material

```sh
paperead new first-material

code ./first-material
# Use text editor to edit description.md
```

## Write a new note

```sh
paperead new first-material -N first-note

# Use text editor to edit ./first-material/notes/first-note.md
```

## Serve the website

```sh
paperead serve
```

## Visit the website

Visit `http://localhost:3649`.
