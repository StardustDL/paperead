---
name: How to Write
creation: 2021-11-11 11:19:55.698213+08:00
modification: 2021-11-11 11:19:55.698213+08:00
targets: {}
tags: []
extra: {}
schema: ''
---

# Document Structure

Material's description and notes share the same document structure.

```
---
# Metadata in YAML
name: Name
---

Description in Markdown.
```

# Metadata

```yaml
# Title
name: Name
# Creating Time
creation: 2021-09-26 09:00:00+00:00
# Modification Time
modification: 2021-09-26 09:00:00+00:00
# Content Schema
schema: ""
# Target Links
targets:
  image: "./assets/image.png"
# Tags
tags:
- tag1
- tag2
# Extra Information
extra:
  key1: "value1"
  key2: "value2"
```

# Content

`schema` specifies how the content organize.

|Schema|Description|Guide|Demo|
|-|-|-|-|
|`raw`|Raw HTML text|[💡](/writing/raw)|[✨](/demo/raw)|
|`html`|HTML document|[💡](/writing/html)|[✨](/demo/html)|
|`slides`|Slides|[💡](/writing/slides)|[✨](/demo/slides)|
|`media`,`image`,`link`|Multimedia|[💡](/writing/media)|[✨](/demo/media-media)[✨](/demo/media-image)[✨](/demo/media-link)|
|`dynamic:`|Dynamic generated content|[💡](/writing/dynamic)|[✨](/demo/dynamic)|
|otherwise|Normal Markdown|[💡](/markdown)|[✨](/markdown)|

## Cross links

```markdown
[Link to other material](/<meterialId>)

[Link to other note](/<materialId>/<nodeId>)

[Link to assets from material description](./assets/something)

[Link to assets from notes](../assets/something)
```