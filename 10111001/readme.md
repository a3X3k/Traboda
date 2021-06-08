# 10111001

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/36.jpeg?raw=true)

- This challenge is based on `LSB Steganography`.
- `Zsteg` is also a tool like Jsteg but it is used to detect `LSB Steganography` only in the case of `PNG` and `BMP` images.

## Installation

```
$ sudo apt install ruby
$ sudo gem install zsteg
```

## Usage

```
$ zsteg <filename>
```

- If we run this we can find some meaningful data embedded in the `LSB`'s of the `PNG` image. 
- This meaningful data can help us in solving the challenge.
- Among the LSB's we can see a line this, 
- This is the Flag --> `NFXGG5DGNJ5TI3K7ORUDGX2MGNAVG5C7GVUUO3RRMYYWGNDOKRPWEVKUL4YV6YZUJZPXI4RQOVBEYM27LEYHKXZUL5WDAVD5`.
- It is encoded in `Base32` format.
- We need to decode it to get the `flag`.
- `Online Tool` --> https://emn178.github.io/online-tools/base32_decode.html

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/37.jpeg?raw=true)

```
inctfj{4m_th3_L3ASt_5iGn1f1c4nT_bUT_1_c4N_tr0uBL3_Y0u_4_l0T}
```
