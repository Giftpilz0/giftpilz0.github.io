---
title: Virtual Audio Devices
---

______________________________________________________________________

## Creating Virtual Audio Sink

To create a virtual audio sink that can act as a dummy output device:

```bash
pactl load-module module-null-sink sink_name=VirtualSink sink_properties=device.description=VirtualSink
```

This command creates:

- A null sink named "VirtualSink"

## Creating Virtual Microphone

To create a virtual microphone that captures audio from the virtual sink:

```bash
pactl load-module module-loopback source=VirtualSink.monitor sink=@DEFAULT_SINK@ latency_msec=1
```

This command creates:

- A loopback module that captures audio from the monitor of VirtualSink
- Routes the captured audio to the default sink

## Managing Virtual Audio Devices

### List Active Modules

To see all active PulseAudio modules:

```bash
pactl list short modules
```

### Removing Virtual Audio Devices

To remove the virtual audio devices, identify the module IDs from the list above, then unload them:

```bash
pactl unload-module <module_id>
```

Example:

```bash
pactl unload-module 536870916
pactl unload-module 536870917
```
