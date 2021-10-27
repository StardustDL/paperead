---
name: Data Directory
creation: 2021-10-02 09:15:41.501646+08:00
modification: 2021-10-02 09:15:41.501646+08:00
targets: {}
tags: []
extra: {}
---

# Data Directory

Paperead works in a data directory. The directory's structure is like the following.

```
/
  .paperead.yml
  material1/
    description.md
    assets/
    notes/
      note1.md
```

## Material Description

`<materialId>/description.md` contains the metadata in the frontmatter and the description for the material.

```
---
# Metadata in YAML
name: Name
creation: 2021-09-26 09:00:00+00:00
modification: 2021-09-26 09:00:00+00:00
schema: ""
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

- Do **NOT** use space in material ID.

Possible values for `schema`:

- `slides` Slides powered by Reveal.js
- Otherwise take the contents as a normal Markdown.

## Notes

`<materialId>/notes/<noteId>.md` contains the metadata (the structure is as same as material's description) and the content for the note for the material.

- Do **NOT** use space in note ID.

## Assets

`<materialId>/assets/` contains all additional files for the material, this will be directly served as static files,
and all `.md` files for the material can access these files by using `./assets/...` or `../assets/...` (just relative path).
