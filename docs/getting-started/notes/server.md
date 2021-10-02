---
name: Website Server
creation: 2021-10-02 09:14:40.767973+08:00
modification: 2021-10-02 09:14:40.767973+08:00
targets: {}
tags: []
extra: {}
---

# Website Server

```sh
paperead serve

paperead -D "path/to/dataDir" serve
```

Then visit `http://localhost:3649`.

RESTful APIs:

- `/api/`
  - GET (`index.json`): Get API metadata
- `/api/materials/`
  - GET (`index.json`): Get all ids for materials
  - POST: Create or update a material
- `/api/materials/<id>/`
  - GET (`index.json`): Get data of the material
  - DELETE: Delete the material
- `/api/materials/<id>/assets/<path>`
  - GET: Access assets of the material
- `/api/materials/<id>/notes/`
  - GET (`index.json`): Get all ids for notes of the material
  - POST: Create or update a note of the material
- `/api/materials/<id>/notes/<nid>/`
  - GET (`index.json`): Get data of the note of the material
  - DELETE: Delete the note of the material

Paperead can also build a static website.

```sh
paperead build
```

The built website will be at `./dist`, which can be hosted in any static HTTP server.

> Before building, existed `dist` directory will be deleted. So DO NOT make your files in `dist` directory.
