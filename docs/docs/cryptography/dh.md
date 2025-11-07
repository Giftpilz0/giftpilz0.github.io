---
title: Diffie-Hellman Key Exchange
---

______________________________________________________________________

## Introduction

The Diffie-Hellman key exchange is a crucial solution to a fundamental problem in secure communication: the secure exchange of encryption keys. Traditional key exchange methods are vulnerable to interception, which is why the Diffie-Hellman method is widely adopted.

______________________________________________________________________

## How It Works

Diffie-Hellman key exchange offers two main variants: DHE and ECDHE. ECDHE, which employs Elliptic Curve Cryptography (ECC), provides efficient computation and higher security with shorter keys. Diffie-Hellman is widely used in secure communication protocols like TLS, SSH, and IPsec to enhance key exchange security.

1. Both parties generate public and private keys.
1. They agree on prime numbers and a base for key generation.
1. Parties keep private keys secret and share their public keys.
1. Using received public keys and the agreed base, both parties compute a shared session key.
1. This key enables a secure communication channel.
1. Sensitive data is never sent in plain text.

```mermaid
stateDiagram-v2
    common_base_a: Common Base
    common_base_b: Common Base
    secret_param_a1: Secret Parameter Alice
    secret_param_b1: Secret Parameter Bob
    secret_param_a2: Secret Parameter Alice
    secret_param_b2: Secret Parameter Bob
    Publick_Key_a1: Publick Key Alice
    Publick_Key_b1: Publick Key Bob
    Publick_Key_a2: Publick Key Alice
    Publick_Key_b2: Publick Key Bob
    Publick_Key_Exchange: Publick Key Exchange
    secret_key: Common Secret

    classDef keyExchange color:white,font-weight:bold,stroke-width:2px,stroke:yellow
    class secret_key keyExchange

    Alice --> common_base_a
    Bob --> common_base_b
    common_base_a --> secret_param_a1: Base + Parameter
    common_base_b --> secret_param_b1: Base + Parameter
    secret_param_a1 --> Publick_Key_a1: equals
    secret_param_b1 --> Publick_Key_b1: equals
    Publick_Key_a1 --> Publick_Key_Exchange
    Publick_Key_b1 --> Publick_Key_Exchange
    Publick_Key_Exchange --> Publick_Key_b2
    Publick_Key_Exchange --> Publick_Key_a2
    Publick_Key_b2 --> secret_param_a2: Publick Key Bob + Parameter
    Publick_Key_a2 --> secret_param_b2: Publick Key Alice + Parameter
    secret_param_a2 --> secret_key: equals
    secret_param_b2 --> secret_key: equals
```
