---
layout: default
title: Caesar Cipher
parent: Cryptography
---

# {{ page.title }}

______________________________________________________________________

## Introduction

The Caesar Cipher, often referred to as the Caesar Shift, is a classic method of letter substitution within the field of cryptography. This method primarily focuses on circularly shifting characters within a message to achieve encryption. The security offered by the Caesar Cipher is quite limited, relying on a basic letter rotation. Deciphering a message encrypted with this technique involves the application of frequency analysis to determine the most common letters. For instance, in the case of German text, frequently occurring letters like "I," "E," and "N" are prominent. Analyzing the typical letter distribution in German text enables the deduction of the rotation applied and the subsequent revelation of the original message.

______________________________________________________________________

## Rot13

Represents a well-known variation of the Caesar Cipher. It operates exclusively on the 26 letters of the standard alphabet. This variation involves a systematic rotation of each letter by precisely 13 positions. Rot13's focus is on letter rotation, allowing for a straightforward decryption process through the application of the same rotation in reverse.

Here's an example of Rot13 transformation:

```
Original: Hello World
Encrypted: Uryyb Jbeyq
```
