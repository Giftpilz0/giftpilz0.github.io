---
title: YouTube Download
---

______________________________________________________________________

## Overview

:::note
yt-dlp is software for downloading videos from various sources
:::

## Usage Examples

### Video (1080p)

```bash
yt-dlp \
  --embed-thumbnail \
  --merge-output-format mkv \
  --sponsorblock-mark all \
  -o '%(title)s.%(ext)s' \
  -S 'res:1080' \
  -f 'bv+ba' \
  https://www.youtube.com/watch?v=
```

### Audio

```bash
yt-dlp \
  --add-metadata \
  --embed-thumbnail \
  -o '%(title)s.%(ext)s' \
  -f 'ba[ext=m4a]' \
  https://www.youtube.com/watch?v=
```

## Setup yt-dlp using ISH on iPad

Only works using Alpine Linux 3.15

```bash
apk add ffmpeg python3 py3-brotli py3-mutagen py3-pycryptodomex py3-websockets && \
wget -O /bin/yt-dlp https://github.com/yt-dlp/yt-dlp/releases/download/2023.07.06/yt-dlp && \
chmod +x /bin/yt-dlp
```
