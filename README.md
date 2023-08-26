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

When thats done, an additional layer of randomization is applied using a randomly generated seed. the seed formula is all ASCII values + user input. this process produces the final output:

```
cAEaadrAtddewAfrDhSfBsfdSRSrsdsrEUSATBdG
```

