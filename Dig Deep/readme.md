# Dig Deep

- Download the image given.
- If we try to open we wont be able to find anything.
- So we have to analyze the chunks.
- Binwalk is a tool used mainly for searching embedded files and executable code within another data file.

## Installation

```
$ sudo apt install binwalk
```

## Usage

```
$ binwalk -e <file-name>
```

```
$ binwalk -e 1.jpg
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/72.jpeg?raw=true)

- Here in the above image, we see that there is a `JPG Image` and a `ZIP` in it and we see that, it is embedded within the `JPG` image file. 
- To extract it we can make use of a carving tool dd. 
- It can carve out data from specific offsets that are passed as arguments to the tool along the with the file that needs to be read. 

```
$ dd if=<filename> of=<filename> bs=1 skip=<offset>
```

- if = the file from which data has to be extracted is passed as an argument.
- of = has the name of the file that we give after extraction. 
- skip = is the offset of the file that has to be read.
- bs = i the byte skip argument that specifies the frequency of reading data from the given file.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/73.jpeg?raw=true)

- If we try to extract all files we will get three files. 

### PART - 1 --> Image 1

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/70.jpeg?raw=true)

### PART - 2 --> Text from the Zip FIle

```
Here is the part2 202015ed269630d
```

### PART - 3 --> Image 2

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/71.jpeg?raw=true)

- If we combine `3 Parts` we can get the `flag`.

```
flag{7b560d81c0202015ed269630d2b8b1993d2e7788}
```
