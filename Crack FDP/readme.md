# Crack FDP

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/57.jpeg?raw=true)

- Download the `PDF`. 
- In this challenge we need to crack the pdf password and find the `flag`.
- PDF Crack is a tool for recovering the pass for Encrypted PDF files. 
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

### Brute - Forcing :

```
$ pdfcrack -f <file_name>
```

### Wordlist Cracking : 

```
$ pdfcrack -f <file_name> -w <wordlist_file>
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/58.jpeg?raw=true)

```
Password --> diosayudameenelesut
```

- After decryption we get a password and now we will be able to open the pdf.
- We can see the `flag` inside the file.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/59.jpeg?raw=true)

```
flag{1ae06a29a7abd6c07dba8976698f756b987f734d}
```
