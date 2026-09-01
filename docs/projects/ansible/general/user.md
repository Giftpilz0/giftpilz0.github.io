---
title: User Role
---

Manage a local user account and its SSH authorized keys.

______________________________________________________________________

## Variables

| Variable                           | Type           | Options         | Default  | Description                                         |
| ---------------------------------- | -------------- | --------------- | -------- | --------------------------------------------------- |
| `user`                             | list of dict   | ---             |          | list of user accounts to manage                     |
| `user.user_username`               | string         | ---             |          | login name                                          |
| `user.user_state`                  | string         | present, absent |          | whether the user exists                             |
| `user.user_password`               | string         | ---             |          | plaintext password (hashed at runtime)              |
| `user.user_sudo_pwless`            | bool           | true, false     |          | grant passwordless sudo                             |
| `user.user_groups`                 | list of string | ---             |          | supplementary groups                                |
| `user.user_home`                   | bool           | true, false     |          | create home directory                               |
| `user.user_shell`                  | string         | ---             |          | login shell                                         |
| `user.user_comment`                | string         | ---             |          | GECOS comment field                                 |
| `user.user_pub`                    | list of string | ---             |          | SSH public keys to add to authorized_keys           |
| `user.user_install_key_to_targets` | bool           | true, false     |          | also install keys on user_key_target_users          |
|                                    |                |                 |          |                                                     |
| `user_key_target_users`            | list of string | ---             | ["root"] | list of users that receive all user SSH public keys |
