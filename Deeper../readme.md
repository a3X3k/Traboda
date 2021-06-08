# Deeper..

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/81.jpeg?raw=true)

- Lets download the image.
- If we try to open we wont be able to find anything.
- So we have to analyze the chunks.
- `Binwalk` is a tool used mainly for searching embedded files and executable code within another data file.

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

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/76.jpg?raw=true)

- Here in the above image, we see that there is a `ZIP` in it and we see that, it is embedded within the `JPG` image file. 
- To extract it we can make use of a carving tool dd. 
- It can carve out data from specific offsets that are passed as arguments to the tool along the with the file that needs to be read. 

```
$ dd if=<filename> of=<filename> bs=1 skip=<offset>
```

- if = the file from which data has to be extracted is passed as an argument.
- of = has the name of the file that we give after extraction. 
- skip = is the offset of the file that has to be read.
- bs = i the byte skip argument that specifies the frequency of reading data from the given file.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/82.jpeg?raw=true)

- Now we open the `ZIP` file then we will be able to find the `Audio`.
- Next step is to analyze the Audio.
- [`Online Tool`](https://databorder.com/transfer/morse-sound-receiver/)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/83.jpeg?raw=true)

```
inctf{H34R_W1TH_Y0UR_3Y35}
```
