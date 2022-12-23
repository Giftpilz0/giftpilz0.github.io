---
layout: default
title: Cheat Sheet
parent: Regex
---

# {{ page.title }}

______________________________________________________________________

[test regex](https://regex101.com/)

General tokens

| Expression | Function                                                                           |
| ---------- | ---------------------------------------------------------------------------------- |
| \\n        | Matches a newline character.                                                       |
| \\r        | Matches a carriage return, unicode character U+2185.                               |
| \\t        | Matches a tab character. Historically, tab stops happen every 8 characters.        |
| \\0        | Matches a null character, most often visually represented in unicode using U+2400. |

Character classes

| Expression | Function                                                   |
| ---------- | ---------------------------------------------------------- |
| \[abc\]    | Matches either an a, b or c character.                     |
| \[^abc\]   | Matches any character except for an a, b or c.             |
| \[a-z\]    | Matches any characters between a and z, including a and z. |
| \[a-zA-Z\] | Matches any characters between a-z or A-Z.                 |

Meta Sequences

| Expression | Function                                                   |
| ---------- | ---------------------------------------------------------- |
| .          | Matches any character.                                     |
| a\|b       | Matches either what is before the \| or what is after it.  |
| \\s        | Matches any space, tab or newline character.               |
| \\S        | Matches anything other than a space, tab or newline.       |
| \\d        | Matches any decimal digit.                                 |
| \\D        | Matches anything other than a decimal/digit.               |
| \\w        | Matches any letter, digit or underscore.                   |
| \\W        | Matches anything other than a letter, digit or underscore. |
| \\         | Converts metacharacters to literal characters.             |

Quantifiers

| Expression | Function                                                    |
| ---------- | ----------------------------------------------------------- |
| \*         | Matches zero or more consecutive.                           |
| ?          | Matches an character or nothing.                            |
| +          | Matches one or more consecutive.                            |
| {3,6}      | Matches between 3 and 6 (inclusive) consecutive characters. |
| \*?        | Matches as few characters as possible.                      |

Anchors

| Expression | Function                                                        |
| ---------- | --------------------------------------------------------------- |
| ^          | Matches the start of a string without consuming any characters. |
| $          | Matches the end of a string without consuming any characters.   |

Modifiers

| Expression | Function                                                                                                                                                       |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| g          | Also known as global mode, it instruct the engine not to stop after the first match has been found, but rather to continue until no more matches can be found. |
| s          | This enables the dot metacharacter . to also match newlines. The whole string is treated as a single line input.                                               |
| m          | The ^ and $ anchors now match at the beginning/end of each line respectively, instead of beginning/end of the entire string or input.                          |
