# You Can't See Me

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/5.jpeg?raw=true)

- If we try to open the given `PNG` image it gives the **Invalid Format Error**. 

```
We can understand that there are some errors in the Hex values.
```

- [`Bi0s Wiki Reference`](https://wiki.bi0s.in/steganography/pngcheck/)

- By refering the wiki.bi0s.in we can get to know that there is an official `PNG` tester and debugger tool named `Pngcheck`.
- `Pngcheck` tests the `PNG` image files for corruption, display size, type, compression info.

## Installation

```
$ sudo apt install pngcheck
```

## Installation and Process

```
$ pngcheck <Filename>

Filename = 1.png ( In my case )

$ pngcheck 1.png
```

- If we execute this command we can get to know that there is an error in the **PNG**.

## Errors

```
Error 1 --> IHDR Chunk

Error 2 --> IDAT Chunk
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/6.jpeg?raw=true)

## Decryption

- The next step is to correct the errors using the `Hex` Editor.
- `Ghex` is a tool which helps us to view and edit the hex data or hex dump of an image.

## Tool Installation

```
$ sudo apt install ghex
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/7.jpeg?raw=true)

## Usage

```
$ ghex <Filename>

Filename --> 1.png ( Initial Image ) --> In my case
         --> 2.png ( After Correcting Errors in IHDR Chunk ) --> In my case
         --> 3.png ( After Correcting Errors in IDAT Chunk ) --> In my case
```
 - Finally we get the `flag` in the corrected **PNG Image**.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/8.jpeg?raw=true)
