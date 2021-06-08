# Security 101

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/14.jpeg?raw=true)

- Download and unzip the zip file.
- When you unzip you can find that 2 files are extracted out of which one is a image and one is the password protected file.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/16.jpeg?raw=true)

- Hint is given as **Nerd : Some people keep their username as password. Why would they do that ? Me : Hmm ...**
- We can understand that username is meant to be the creator of the image or the owner of the image.
- So next step is to analyse the extracted image.
- **Tool -->** http://fotoforensics.com/analysis.php?id=f38a1f992968fda2c000b2f25fe70a8796e1b43a.33254
- Now if you try to view the meta data of the image then you can find that the **Creator** is **R3DDIT_US3R**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/15.jpeg?raw=true)

- Now if you try to extract the one of the other previously password protected extracted file with the password as **R3DDIT_US3R** then you can extract one another which contains the flag.

- Here we are giving the password as **R3DDIT_US3R** since the hint is given as **Some people keep their username as password.**

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/17.jpeg?raw=true)

```
inctfj{1ts_4ll_f1ne_tru5t_m3}
```
