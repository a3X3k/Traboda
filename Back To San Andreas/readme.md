# Back to San Andreas

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/31.jpeg?raw=true)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/32.jpeg?raw=true)

- Here when we try to open the `image` then we cannot find anything.
- So next step is to analyze the `JPEG` image.
- `Jsteg` is a package for hiding data inside `JPEG` files with a technique known as `steganography`. 
- This is accomplished by copying each bit of the data into the `Least Significant Bits (LSB)` of the image. 

## Installation

```
$ sudo wget -O /usr/bin/jsteg https://github.com/lukechampine/jsteg/releases/download/v0.1.0/jsteg-linux-amd64
$ sudo chmod +x /usr/bin/jsteg
$ sudo wget -O /usr/bin/slink https://github.com/lukechampine/jsteg/releases/download/v0.2.0/slink-linux-amd64
$ chmod +x /usr/bin/slink
```

## Revealing data

```
$ jsteg reveal <in.jpg> <output file name>
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/33.jpeg?raw=true)

- The data will be extracted in the specified file.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/34.jpeg?raw=true)

- If we open the file we can see that there is a link.
- Now if we open the link then we shall see the `flag`.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/35.jpeg?raw=true)

```
inctfj{gr0ve_5treet_f0r_l1fe}
```
