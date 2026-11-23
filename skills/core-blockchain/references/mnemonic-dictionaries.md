# Mnemonic dictionaries

Use the exact wordlist and word order supported by the target wallet when creating, validating, or recovering a mnemonic. A language name alone does not establish compatibility. Check the wallet's implementation and its treatment of Unicode normalization, word separators, checksum validation, and passphrases. Never infer a recovery phrase or private key from a wordlist.

## Mnemonic length and passphrase

Use 24 mnemonic words by default when the wallet supports them. The word count can vary: 12 words are another common choice, and a wallet may support other counts such as 16. Verify the target wallet's format and checksum rules before using a nonstandard count; do not assume a 16-word phrase is accepted by a BIP-39 implementation.

In BIP-39 mnemonic-to-seed derivation, the salt is `"mnemonic" + passphrase`. With an empty passphrase, the salt is `"mnemonic"`. The optional value often called the “25th word” is a separate passphrase, not another mnemonic word. CorePass uses a PIN in that role, so its salt is `"mnemonic" + PIN`. Other applications may use a password or another value for hidden wallets or added security. One UI option is an emoji as the “25th word.” Preserve the exact passphrase and the wallet's Unicode normalization behavior when restoring a wallet; different values derive different wallets. A 12-word or other supported mnemonic can likewise be used with a passphrase.

The following sources are available for language-specific dictionary work. The [Bitcoin BIP-39 wordlist index](https://github.com/bitcoin/bips/blob/master/bip-0039/bip-0039-wordlists.md) documents the canonical lists and language-specific considerations. Lists from other repositories are separate dictionaries; their presence here does not mean every BIP-39 wallet accepts them.

| Language | Dictionary source | Notes |
| --- | --- | --- |
| Chinese (Simplified) | [Bitcoin BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_simplified.txt) | Canonical BIP-39 list. |
| Czech | [Bitcoin BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039/czech.txt) | Canonical BIP-39 list. |
| English | [Bitcoin BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) | Canonical BIP-39 list. |
| French | [Bitcoin BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039/french.txt) | Canonical BIP-39 list; may be supplied by `bip39_mnemonic`. |
| German | [`nibyou/bip-39`, `de_DE.json`](https://github.com/nibyou/bip-39/blob/main/langs/de_DE.json) | External list; preserve its exact ordering. |
| Japanese | [Bitcoin BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039/japanese.txt) | Canonical BIP-39 list; see the wordlist index for ideographic-space handling. |
| Korean | [Bitcoin BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039/korean.txt) | Canonical BIP-39 list; may be supplied by `bip39_mnemonic`. |
| Portuguese | [Bitcoin BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039/portuguese.txt) | Canonical BIP-39 list. |
| Russian | [`PROWLERx15/bip39-mnemonic-generator`, `russian.json`](https://github.com/PROWLERx15/bip39-mnemonic-generator/blob/main/bip39%20wordlists/russian.json) | External list; preserve its exact ordering. |
| Slovak | [`rastislavcore/slovak-wordlist`](https://github.com/rastislavcore/slovak-wordlist/blob/main/base-wordlist-slovak.txt) | External base list; reproduce the ordering from its [`build.js`](https://github.com/rastislavcore/slovak-wordlist/blob/main/build.js). |
| Spanish | [Bitcoin BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039/spanish.txt) | Canonical BIP-39 list. |
| Turkish | [`PROWLERx15/bip39-mnemonic-generator`, `turkish.json`](https://github.com/PROWLERx15/bip39-mnemonic-generator/blob/main/bip39%20wordlists/turkish.json) | External list; preserve its exact ordering. |

For mnemonic interoperability, validate the selected source against the target implementation, including all 2,048 entries and their indices. The source list controls the words; the wallet's mnemonic-to-seed and key derivation implementation controls recovery. See [Core HD wallet derivation](core-protocol.md#hd-wallet-derivation) for path and backend checks.
