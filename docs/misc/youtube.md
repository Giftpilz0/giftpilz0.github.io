---
layout: default
title: Youtube Download
parent: Misc
---

# {{ page.title }}

______________________________________________________________________

{: .note }

> yt-dlp ist eine Software zum Downloaden von Videos aus diversen Quellen

______________________________________________________________________

Video

```bash
# Video
yt-dlp -r 3M -i -o '%(title)s.%(ext)s' -f 'bestvideo+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 https://www.youtube.com/watch?v=

# Audio
yt-dlp -r 3M -i -o '%(title)s.%(ext)s' -f 'bestaudio[ext=m4a]' --embed-thumbnail --add-metadata https://www.youtube.com/watch?v=

# Erweitert
yt-dlp \
  --limit-rate 5M \
  --embed-thumbnail \
  --output '%(title)s.%(ext)s' \
  --format-sort "res:1440,vcodec:vp9" \
  --merge-output-format mp4 \
  https://www.youtube.com/watch?v=
```
