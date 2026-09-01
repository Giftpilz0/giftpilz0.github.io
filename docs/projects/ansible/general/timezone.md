---
title: Timezone Role
---

Set the system timezone.

______________________________________________________________________

## Variables

| Variable                 | Type           | Options                 | Default    | Description                          |
| ------------------------ | -------------- | ----------------------- | ---------- | ------------------------------------ |
| `timezone_package_state` | string         | present, absent, latest | present    | desired state of timezone packages   |
| `timezone_package`       | list of string | ---                     | ["tzdata"] | list of packages to install          |
| `timezone_timezone`      | string         | ---                     | Etc/UTC    | system timezone (e.g. Europe/Berlin) |
