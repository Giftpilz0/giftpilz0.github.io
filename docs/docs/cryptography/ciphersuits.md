---
layout: default
title: Cipher Suites
parent: Cryptography
---

______________________________________________________________________

## Introduction

Cipher Suites are combinations of security techniques used in protocols like TLS for secure communication. They include methods for exchanging keys, verifying identities, encrypting data, and ensuring data integrity.

______________________________________________________________________

## Example Protocols

| Key Exchange | Authentication | Encryption  | Hashing  |
| ------------ | -------------- | ----------- | -------- |
| DHE          | ECDSA          | CHACHA20    | Poly1305 |
| ECDHE        | RSA            | AES-128-GCM | SHA384   |
| RSA          | DSA            | AES-256-CBC | SHA256   |

**Example Cipher Suite:**

TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384

- Key Exchange: Setting up the session key
- Authentication: Checking the server's identity
- Encryption: Protecting data during transmission
- Hashing: Confirming data integrity

For a detailed list of options, you can visit [TLS Parameters on IANA](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml).

______________________________________________________________________

## TLS Handshake

During the TLS handshake, parties choose a Cipher Suite for their communication.

### Client Hello

The process begins with the client sending a "Client Hello" message, listing the Cipher Suites it supports.

### Server Hello

Then, the server selects a Cipher Suite from the client's list and sends a "Server Hello" message back to the client.
