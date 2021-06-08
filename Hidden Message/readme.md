# Hidden Message

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/88.jpeg?raw=true)

- We are provided with the **Python Script** and **JPEG Image**

## Python Script 

```
import string
import base64

def encode(x):
    return x.encode("hex") 

if _name=="main_":
	print("63486c306147397561584e6d6457343d")
	print("decode this to get the pass")
	encoded_data = encode(base64.b64encode(""))
	print(encoded_data)
```

- We have to debug it to make it excute to get the necessary output.
- First Change the `encode()` function to `decode()`.
- Then in order to pass the `parameter` to the `decode` function it should be in `ASCII` format.
- But we have `Hex` here.
- So we have to convert the given hex to `ASCII` format.
- [`Online Tool`](https://www.rapidtables.com/convert/number/hex-to-ascii.html)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/89.jpeg?raw=true)

- After several `debugging` we shall get the final script.

```
import string
import base64

def decode(x):
    return x.decode('utf8') 

if _name=="main_":
	print("63486c306147397561584e6d6457343d")
	print("decode this to get the pass")
	encoded_data = decode(base64.b64decode("cHl0aG9uaXNmdW4="))
	print(encoded_data)
```

- Next Step is to run the script.

```
pythonisfun
```

- Steghide is used to embed and extract secret messages in images. 
- It supports all the general formats of images like .png, .jpg etc.

## Installation

```
$ sudo apt install steghide
```

## Usage

```
$ steghide extract -sf <Filename>
Enter passphrase : ********
wrote extracted data to "<Filename>.txt".
```

- We have to enter the password which we got from the `Python Script`.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/90.jpeg?raw=true)
