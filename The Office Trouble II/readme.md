# The Office Trouble II

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/50.jpeg?raw=true)

- In this challenge we need to crack the pdf password and find the `flag`.
- `PDF Crack` is a `tool` for recovering the pass for Encrypted PDF files. 
- Encrypted files means the metadata of the file was encrypted with some characters.

**It has some special features like:**

- Checks with the system password and also the user provided password.
- It can crack password by brute-forcing method only for character sets and only when we provide the maximum and minimum length of the password.
- Searches the password from the wordlist.
- Optimized search for owner-password when user-password is known.

## Installation

```
$ sudo apt-get install pdfcrack
```

## Usage

### Brute-forcing

```
$ pdfcrack -f <file_name>
```

### Wordlist Cracking

```
$ pdfcrack -f <file_name> -w <wordlist_file>
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/51.jpeg?raw=true)

- After decryption we get a password and now we will be able to open the pdf.
- Password --> `fear420`

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/52.jpeg?raw=true)
