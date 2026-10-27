---
title: Caesar Cipher
---

The Caesar cipher replaces every letter with the one a fixed number of positions further down the alphabet, wrapping
around from Z to A. The shift is the key.

```text title="Shift by 3"
plain:  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
cipher: D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
```

## Breaking it

There are only 25 possible keys, so trying all of them takes a moment. Even without that, letter frequencies give the
shift away: the most common letter in German and English text is E, so the most common letter in the ciphertext most
likely stands for E.

```sh title="Print all 25 shifts"
text="Wkh txlfn eurzq ira"
for i in $(seq 1 25); do
  from=$(printf "%s" {A..Z} | cut -c$((i + 1))-26)$(printf "%s" {A..Z} | cut -c1-$i)
  echo "$i: $(echo "$text" | tr "A-Za-z" "$from${from,,}")"
done
```

## ROT13

ROT13 shifts by 13, half the alphabet, so encrypting twice returns the original text and the same command does both. It
hides spoilers, not secrets.

```sh
echo "Hello World" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
# Uryyb Jbeyq
```
