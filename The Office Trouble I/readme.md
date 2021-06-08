# The Office Trouble I

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/21.jpeg?raw=true)

- Try cracking the password using the `Frackzip` tool.
- Try `Dictionary` Attack using `Rockyou.txt` file.

## Installation

```
$ sudo apt install fcrackzip
```

## Usage

### Brute Force Attack

```
$ fcrackzip -v -b -u -p <file_name.zip>
```

### Dictionary Attack

```
$ fcrackzip -v -u -D -p <path_to_wordlist_file> <file_name.zip>
```

- [`Rockyou.txt File`](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/22.jpeg?raw=true)

- Here we use `Dictionary Attack`.

```
$ fcrackzip -v -u -D -p rockyou.txt 1.zip
```

- We get the password and then if we try to unzip it using the **password** then we shall get the extracted image which contains the **flag**.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/23.jpeg?raw=true)

```
inctfj{dw1ght_1s_cr4zy_bu7_awes0me}
```
