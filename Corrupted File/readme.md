# Corrupted File

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/66.jpeg?raw=true)

- Download the `Zip` FIle.
- The zip file is `corrupted`.
- So edit the `Hex` chunks and then try to open the zip file.
- First start with the `Header--Magic Values` and then `Footer`.
- [`Online Tool`](https://hexed.it/)

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/67.jpeg?raw=true)

- Here we will be able to see the **Secret Information**.
- The given information in encrypted in **Base 64** format.
- So we shall [`decrypt`](https://www.base64decode.org/) it back to the ASCII.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/68.jpeg?raw=true)

```
flag{9e360084196a092a15c5c44b54934bfc}
```
