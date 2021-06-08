### You Can't See Me

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/5.jpeg?raw=true)

- If we try to open the given **PNG** image it gives the **Invalid Format Error**. 

```
--> We can understand that there are some errors in the Hex values.
```

- Reference --> **https://wiki.bi0s.in/steganography/pngcheck/** 

```
--> By refering the wiki.bi0s.in we can get to know that there is an official PNG tester and debugger tool named Pngcheck which tests the PNG image files for corruption, display size, type, compression info.
```

#### Installation

```
$ sudo apt install pngcheck
```

#### Installation and Process

```
$ pngcheck <Filename>

--> Filename = 1.png ( In my case )

$ pngcheck 1.png
```

- If we execute this command we can get to know that there is an error in the **PNG**

#### Errors

```
Error 1 --> IHDR Chunk

Error 2 --> IDAT Chunk
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/6.jpeg?raw=true)

#### Decryption

- The next step is to correct the errors using the Hex Editor.

- Ghex is a tool which helps us to view and edit the hex data or hex dump of an image.

#### Tool Installation

```
$ sudo apt install ghex
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/7.jpeg?raw=true)

#### Usage

```
$ ghex <Filename>

Filename --> 1.png ( Initial Image ) --> In my case
         --> 2.png ( After Correcting Errors in IHDR Chunk ) --> In my case
         --> 3.png ( After Correcting Errors in IDAT Chunk ) --> In my case
```
 - Finally we get the flag in the corrected **PNG Image**.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/8.jpeg?raw=true)

### My - First - Stegnography

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/9.jpeg?raw=true)

- Reference --> **https://wiki.bi0s.in/steganography/steghide/** 

- Here we get two **JPEG** images and download the images.
- Since two images are given we can have a wild guess that this challenge can be solved using **Steghide** tool.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/11.jpeg?raw=true)
![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/12.jpeg?raw=true)

```
--> By refering the wiki.bi0s.in we can get to know that there is a tool named Steghide which is used to embed and extract secret messages in images. 

--> It supports all the general formats of images like .png, .jpg etc.
```

#### Installation

```
$ sudo apt install steghide
```

#### Usage 

```
$ steghide extract -sf <Filename>

 (output)$ Enter passphrase : ********

 (output)$ wrote extracted data to "xxx.txt"
```

#### Decryption

```
$ steghide extract -sf 1.jpeg
```

- Then it prompts us to enter the **Passphrase**.
- Since we dont have any **Passphrase** we can just click **ENTER**.
- Now the **Passphrase** for the next image has been extracted in the file named **password.txt**.

```
$ steghide extract -sf 2.jpeg

(output)$ d4rk_s1d3
```

- Then it prompts us to enter the **Passphrase**.
- Since we have **Passphrase** we can enter **d4rk_s1d3** and click **ENTER**.
- Now the data has been extracted in the file named **plans.txt**.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/10.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/13.jpeg?raw=true)

```
Flag --> inctfj{w3_4r3_pl4nt1ng_4_b0mb}
```
