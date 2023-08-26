# Cryptography Simplified with Python

This repository contains Python code that offers a straightforward approach to cryptography.

## How it Works
This code implements a simple encryption technique by initially substituting original characters with a string of randomly generated letters (both lowercase and uppercase):

For instance:
- h = RGahTfSU
- e = ASDdsffe
- l = BsdrAdrE
- l = BsdrAdrE
- o = tSdcwASa

After character substitution, the program concatenates these modified strings, resulting in:

```
RGahTfSUASDdsffeBsdrAdrEBsdrAdrEtSdcwASa
```

Following concatenation, an additional layer of randomization is applied using a randomly generated seed. The seed calculation involves summing up all ASCII values and including a user-defined input. Ultimately, this process produces the final output:

```
RGahTfSUASDdsffeBsdrAdrEBsdrAdrEtSdcwASa
```

Discover a simplified approach to cryptography with this Python code!
