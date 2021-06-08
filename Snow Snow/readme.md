# Snow Snow

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/1.jpeg?raw=true)

```
By the hint "Suspicious between these lines" we can understand that this challenge is based on the Whitespace Steganography.
```

- Reference --> https://wiki.bi0s.in/steganography/stegsnow/

```
By refering the wiki.bi0s.in we can get to know that there is a tool named Stegsnow which conceals messages in text files by appending tabs and whitespaces at the end of lines.
```

- Download the txt file which has to be decrypted.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/2.jpeg?raw=true)

## Installation

```
$ sudo apt install stegsnow
```

## Decryption

```
$ stegsnow -C <Filename>

Filename = 1.txt ( In my case )

$ stegsnow -C 1.txt
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/3.jpeg?raw=true)

- Now we get a flag which is being encrypted cryptographically.

```
ntio{eP1B35x4K3_aB3O0_q5_K00t}
```

- The next step is to decryt the flag using cryptography.

- Decryption Online Tool --> **https://www.dcode.fr/caesar-cipher**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/4.jpeg?raw=true)

- Finally we get the flag in the right format.

```
flag{wH1T35p4C3_sT3G0_i5_C00l}
```
