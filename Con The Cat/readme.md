# Con-The-Cat

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/43.jpeg?raw=true)

- Download the `PNG` image.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/44.jpeg?raw=true)

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
$ binwalk -e 1.png
```

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/45.jpeg?raw=true)

- Here in the above image, we see that there is a `JPG Image` that has a compressed `Images` in it and we see that, it is embedded within the `JPG` image file. 
- To extract it we can make use of a carving tool dd. 
- It can carve out data from specific offsets that are passed as arguments to the tool along the with the file that needs to be read. 

```
$ dd if=<filename> of=<filename> bs=1 skip=<offset>
```

- if = the file from which data has to be extracted is passed as an argument.
- of = has the name of the file that we give after extraction. 
- skip = is the offset of the file that has to be read.
- bs = i the byte skip argument that specifies the frequency of reading data from the given file.

```
$ dd if=1.png of=2.png bs=1 skip=7821
```

- Here 7821 is one of the offsets of the file.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/46.jpeg?raw=true)

```
inctfj{y0u_c4nt_s33_m3!!}
```
