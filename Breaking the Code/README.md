# Encryption & Decryption of Messages with RSA Encryption
---

# Intro

[RSA encryption](https://brilliant.org/wiki/rsa-encryption/) allows people to exchange information securely over the Internet without worrying about third parties eavesdropping on their communications. It makes use of a public key and a private key.

* `Public Key` numbers: `n` and `e`. Only useful to encrypt messages, not to decrypt them (encryption key). This numbers are sent by the receptor to the sender of the message and it doesn't matter if someone else obtain this numbers
* `Private Key` number: `d`. This number is only know by the receiver.

Where
- p : Should always be 13 or greater
- q : Should always be 17 or greater
- e : Greater than 1 and less than ϕ(𝑛). It is important that ϕ(𝑛) is not divisible by e
- n = (p*q)
- ϕ(𝑛) = (p-1)*(q-1)
- d = int((i*ϕ(𝑛)+1)/e)


---

# Usage 
Encryption and decription are used as follow:
1. Text with the mesage is created
2. Message is cypher by `Encryption.py`, using the public key numbers sent by the receiver. Message is now a secuence of numbers.
3. Cypher message is sent to the receiver.
4. Cypher message is decypher using `Decryption.py` with the private code. Message is now the original text (now in lowercase).

In this program it is defined:
- p = 13
- q = 17
- e = 5
