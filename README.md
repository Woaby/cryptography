# Cryptography

A simple cryptography program using python.

## How it Works
First whe change the original character(s) with a string of randomly generated letters (both lowercase and uppercase):

For instance:
- h = RGahTfSU
- e = ASDdsffe
- l = BsdrAdrE
- l = BsdrAdrE
- o = tSdcwASa

After this, the program concatenates these modified strings, resulting in:

```
RGahTfSUASDdsffeBsdrAdrEBsdrAdrEtSdcwASa
```

When thats done, another layer of randomization is applied using a randomly generated seed. the seed formula is all ASCII values + random genererated seed fron the key. this process produces the final output:

```
cAEaadrAtddewAfrDhSfBsfdSRSrsdsrEUSATBdG
```

