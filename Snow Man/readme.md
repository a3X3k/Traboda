# Snow Man

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/47.jpeg?raw=true)

- Download the file and we can understand that it comes under `Whitespace Steganography`.
- `Stegsnow` is a tool for concealing messages in text files by appending tabs and whitespaces at the end of lines.
- The `encoding` used by snow relies on the fact that whitespaces and new lines won't be displayed in text editors.

## Installation

```
$ sudo apt install stegsnow
```

## Decryption

```
$ stegsnow -C -p "<Password>" <Txt File>
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/48.jpeg?raw=true)

- After decrypting we will get a flag which is `Base-64` Encoded.
- Using [`Online Tool`](https://www.dcode.fr/base-64-encoding) we shall decrypt it.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/49.jpeg?raw=true)

```
inctfj{h4h4_st3gsn0w_i5_c00000001}
```
