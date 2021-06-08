# Traffic 13

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/53.jpeg?raw=true)

- As given we have to analyze the `Network` packages sent and received.
- `Wireshark` is the most commonly used network protocol analyser and the de facto standard across many commercial and non-profit enterprises.
- It shows the protocol of each packet captured and also the protocol hierarchy of the network whose pcap was made.
- The hex buffer of each packet can be analysed separately and layer by layer.

## Installation

```
$ sudo apt install wireshark-qt
```

- Open `WireShark` and analyze the `TCP` packages.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/54.jpeg?raw=true)

- After analyzing various `TCP` packages we shall find the `flag`.

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/55.jpeg?raw=true)

- But the flag is encryted.

```
vapgsw{o3j4er_0s_plO3E_GUe3ng5}
```

- So we have to decrypt it using the [`Online Tool`](https://www.dcode.fr/caesar-cipher). 

![Bi0s](https://github.com/a3X3k/Training/blob/main/Forensics/Assets/56.jpeg?raw=true)

```
inctfj{b3w4re_0f_cyB3R_THr3at5}
```
