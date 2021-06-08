# Winter Sport

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/84.jpeg?raw=true)

- After downloading the pdf file we wont be able to find anything.
- Hence we have to `analyze` the embeded data in it.
- `Peepdf` is a Python based tool to explore `PDF` files in order to find out if the file can be harmful or not. 
- The aim of this tool is to provide all the necessary components that a security researcher could need in a `PDF` analysis without using 3 or 4 tools to make all the tasks. 
- With peepdf it's possible to see all the objects in the document showing the suspicious elements, supports all the most used filters and encodings, it can parse different versions of a file, object streams and encrypted files.

## Usage

```
$ ./peepdf.py -i pdffile.pdf
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/85.jpeg?raw=true)

- As we can see there is an embedded file in the pdf.
- So now we need to extract the embedded file using the stream command

```
$ PDF> stream 8 > <Filename>
$ xdg-open <Filename>

File Name --> f1

$ PDF> stream 8 > f1
$ xdg-open f1
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/86.jpeg?raw=true)

- After opening the zip file we shall get a pdf.
- If we open the **PDF** then we will be able to find that there is something hidden in the **whitespace**.
- We shall understand that its **White Space Steganography**.
- 
- By [`refering`](https://wiki.bi0s.in/steganography/stegsnow/) we shall get to know that there is a tool named Stegsnow which conceals messages in text files by appending tabs and whitespaces at the end of lines.
- Download the txt file which has to be decrypted.

## Installation

```
$ sudo apt install stegsnow
```

## Decryption

```
$ stegsnow -C <Filename>

Filename = omg.pdf

$ stegsnow -C omg.pdf
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/87.jpeg?raw=true)

```
inctf{w3lcom3_t0_7h3_w0rld_0f_whit3sp4c3}
```
