# My - First - Stegnography

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/9.jpeg?raw=true)

- Reference --> https://wiki.bi0s.in/steganography/steghide/

- Here we get two **JPEG** images and download the images.
- Since two images are given we can have a wild guess that this challenge can be solved using **Steghide** tool.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/11.jpeg?raw=true)
![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/12.jpeg?raw=true)

- By refering the wiki.bi0s.in we can get to know that there is a tool named `Steghide`. 
- `Steghide` is used to embed and extract secret messages in images. 
- It supports all the general formats of images like .png, .jpg etc.

## Installation

```
$ sudo apt install steghide
```

## Usage 

```
$ steghide extract -sf <Filename>

 (output)$ Enter passphrase : ********

 (output)$ wrote extracted data to "xxx.txt"
```

## Decryption

```
$ steghide extract -sf 1.jpeg
```

- Then it prompts us to enter the `Passphrase`.
- Since we dont have any `Passphrase` we can just click `ENTER`.
- Now the **Passphrase** for the next image has been extracted in the file named **Password.txt**.

```
$ steghide extract -sf 2.jpeg

(output)$ d4rk_s1d3
```

- Then it prompts us to enter the **Passphrase**.
- Since we have **Passphrase** we can enter `d4rk_s1d3` and click **ENTER**.
- Now the data has been extracted in the file named `plans.txt`.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/10.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/13.jpeg?raw=true)

```
inctfj{w3_4r3_pl4nt1ng_4_b0mb}
```
