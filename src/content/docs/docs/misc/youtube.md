---
title: YouTube Download
---

[yt-dlp](https://github.com/yt-dlp/yt-dlp) downloads videos from YouTube and many other sites. It merges separate video
and audio streams with `ffmpeg`, so install that too.

## Examples

```sh title="Video, at most 1080p, as MKV"
yt-dlp \
  --embed-thumbnail \
  --merge-output-format mkv \
  --sponsorblock-mark all \
  -o '%(title)s.%(ext)s' \
  -S 'res:1080' \
  -f 'bv+ba' \
  'https://www.youtube.com/watch?v=…'
```

```sh title="Audio only, as M4A with metadata"
yt-dlp \
  --embed-metadata \
  --embed-thumbnail \
  -o '%(title)s.%(ext)s' \
  -f 'ba[ext=m4a]' \
  'https://www.youtube.com/watch?v=…'
```

| Option                    | Effect                                                                             |
| ------------------------- | ---------------------------------------------------------------------------------- |
| `-f 'bv+ba'`              | Best video stream plus best audio stream.                                          |
| `-S 'res:1080'`           | Sorts formats to prefer up to 1080p; still picks something if 1080p is missing.    |
| `-F`                      | Lists all available formats instead of downloading.                                |
| `--sponsorblock-mark all` | Marks sponsor segments as chapters; `--sponsorblock-remove sponsor` cuts them out. |
| `-o '%(title)s.%(ext)s'`  | Output file name template.                                                         |
| `-x --audio-format mp3`   | Extracts audio and converts it.                                                    |
| `-U`                      | Updates yt-dlp itself.                                                             |

:::tip
Quote URLs: an unquoted `&` (as in playlist links) ends the command in the shell. When downloads suddenly fail, update
with `yt-dlp -U` first; sites change often.
:::

## On an iPad with iSH

[iSH](https://ish.app) runs Alpine Linux:

```sh
apk add ffmpeg python3 py3-brotli py3-mutagen py3-pycryptodomex py3-websockets
wget -O /usr/local/bin/yt-dlp https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp
chmod +x /usr/local/bin/yt-dlp
```
