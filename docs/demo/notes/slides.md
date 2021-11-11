---
name: Slides
creation: 2021-10-27 18:28:14.497444+08:00
modification: 2021-10-27 18:28:14.497444+08:00
targets: {}
tags: []
extra: {}
schema: 'slides'
---

## Paperead

![](./assets/logo.svg)

---

## Features

- Horizontal & vertical slides
- Code highlighting
- Relative media files
- Math in LaTeX

===

## Usage

Set `schema` to `slides`.

All you need to know is markdown

with three additional rules


- Use `===` to seperate horizontal slides.
- Use `---` to seperate vertical slides.
- Use `notes` with a `:` for speaker notes

---

## Hotkeys

- Press **CTRL+Shift+F** to search slide content.
- Press **S** to open the notes window.
- **Alt+click** to zoom in on elements (CTRL+click in Linux).
- Press the **ESC** or **O** keys to toggle the overview mode on and off.
- Press **F** to view your presentation in fullscreen mode. Press the **ESC** key to exit.

notes: some notes

===

## Demo

$$a^2+b^2=c^2$$

```js [1-2|3|4]
let a = 1;
let b = 2;
let c = x => 1 + 2 + x;
c(3);
```
