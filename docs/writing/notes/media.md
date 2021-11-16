---
name: Multimedia
creation: 2021-11-11 12:00:40.930084+08:00
modification: 2021-11-11 12:00:40.930084+08:00
targets:
  video-demo: /demo/media-video
  audio-demo: /demo/media-audio
  image-demo: /demo/media-image
  link-demo: /demo/media-link
tags: []
extra: {}
schema: ''
---

# Schema

- `video` for video.
- `audio` for audio.
- `image` for images.
- `link` for links.

# Content

```markdown
# Item 1 Title

[url](url to the target)

Other description...

# Item 2 Title

[url](url to the target)

Other description...
```

## Extra metadata

### Video

```markdown
![cover](url to the cover image file.)
[subtitle](url to the subtitle file (.srt).)
[thumbnails](url to the thumbnails image file.)
```

### Audio

```markdown
![cover](url to the cover image file.)
[lrc](url to the lyric file (.lrc).)
[author](Author name.)
```
