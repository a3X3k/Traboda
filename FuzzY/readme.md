# FuzzY

### Description

- Bob and Charlie were sending some messages among themselves,and I planned to intercept their messages and get something out of it, however, they are clever enough that no secret gets leaked. 
- Please help me out to get the secret!!

### Solution

- Download the [`PCAP`](https://github.com/a3X3k/Traboda/blob/main/FuzzY/1.pcap) file.
- Analyse it using `Wireshark`.
- Following the `TCP` stream gives some useful information.

![](https://github.com/a3X3k/Traboda/blob/main/FuzzY/2.png?raw=true)

- We shall get the `Base64` `Encoded` text and the `PGP` message with a `URL`.

```
aGVsbG93b3JsZA
```

```
-----BEGIN PGP MESSAGE-----
Version: OpenPGP v2.0.8
Comment: https://sela.io/pgp/

wcBMA8fXP+32fyviAQf/T+NzsOgQ+ejW16GeK6h9WS9IDelAN9GLY5x5o9ilBlEL
G4IPati4/zqd+kyV5mmA7k2eKnNByRnxElpp0PoGULX0ykjBTcXuLtNXzGWcDsFF
xAkH8PduoPCcnNGWrCU6D8ZuWNtp7oeZ1krUZP+Kg9sfjjKfx0aUFhWs9SQH6mif
AlbJQwxKi2xXv0UsHvg4Mz4TpVstoO5XcN9d4V+gygc+wx0K61JwAFw96xptNi9y
hdMz/c7yW56JwBfwyiHvYmgLdWYJW9OEoQIj7Rwh1v8mD846vbvEDmagQ0Ra/K6q
lnxa37gBFE+4kYpSXP7yqr8QMhmGDpMROJoJqxYyY9JxAe6317HZ+UUEOmNR+0tB
EmPl/VVaoPc5q6RQ/cxwY4VhR4DtPsG9Gw237Sx+xSTAG5JbmtBf4KfQdVbeaXn1
PYPYBeCVL6nb6uPz6ZHBJ2SODWg9+Ssas+Gd5P7Q0zSA/35qYdamnAqUM/ujM2nN
k2U=
=+x+V
```

- In order to `decipher` it we need, a `Passphrase` and a `PGP PRIVATE KEY`

#### Passphrase

- We got the `Base64` `Encoded` text which can be the `Passphrase`.
- So lets decrypt it.

![](https://github.com/a3X3k/Traboda/blob/main/FuzzY/3.png?raw=true)

```
helloworld
```

#### PGP PRIVATE KEY

- We didn't get the `PGP PRIVATE KEY` yet.
- So let's analyse the `PCAP` further. 
- Doing `strings` analysis shows that there is an `PNG` Image.

![](https://github.com/a3X3k/Traboda/blob/main/FuzzY/10.png?raw=true)

- So now let's find the `packet` which has the `PNG` in it.
- In `Wireshark` we have the filter, `frame contains <>`.
- So applying `frame contains PNG` filter gives us the packet.

![](https://github.com/a3X3k/Traboda/blob/main/FuzzY/5.png?raw=true)

![](https://github.com/a3X3k/Traboda/blob/main/FuzzY/6.png?raw=true)

![](https://github.com/a3X3k/Traboda/blob/main/FuzzY/7.png?raw=true)

- So I made a [`Python Script`](https://github.com/a3X3k/Traboda/blob/main/FuzzY/1.py) to extract the `PNG` data using scapy.

```
from scapy.all import *

f=rdpcap('1.pcap')
b=''

for i in f:
	if IP not in i:
		continue
	if i.haslayer(DNS):
		if i[IP].src == '192.168.42.129':
			b+=str(i)[224:]

f=open('1.png','w')
f.write(b)
f.close()
```

- Now we shall get the [`Image`](https://github.com/a3X3k/Traboda/blob/main/FuzzY/1.png)

![](https://github.com/a3X3k/Traboda/blob/main/FuzzY/1.png?raw=true)

- Decoding it using `zbarimg` it gives the `PGP PRIVATE KEY`.

![](https://github.com/a3X3k/Traboda/blob/main/FuzzY/8.png?raw=true)

```
-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: BCPG C# v1.6.1.0

lQOsBFvO/9wBCACgT4fK4dJm+M14jotXPUeKueo8xfFDunNUx/ZaSQbp5Y0i64OZ
dPkQk4E2zCgXaYKNRhiIx2RUy27GBf7xjtDb0gh/HNhC41f5ZzYrNQBEcabcr0hn
VfwiEzAqmTg+5TNsG26ZD2kuO1/J5zbKxI1D3g/9//fe5Nw8GucDiOntKgvFEXeV
ETZ0llbP/mh8SAn5+naJiJJri9y3GF+QhX7wYP+W6mBkano8X/Yk2B2qWIRT6wRU
DMQy1ptavyv5EJhYbsQGeAMu7WPJN+mLutAE2E1Xj03Sevsx2ynN8b/jF/HYp/mZ
SzZ+TbHlRUoMC4+hYh5XfXy7Cx9HSI0uIDShABEBAAH/AwMCEv0ZoXbeXxxg3ioH
/Y0lUhYOormsNzbrBjl1ipyWTDmRAf9BhmAPrX9K5GPAFAurGOj8QOQEWGrOyXfk
gYtHXzGk1K6ItCitgxdBqHgbti23Ht8SmVWw3/pijPXXerXXMqj6NQ95ma6bYPsU
PRtE1qtiEs+T8ln6ZBU9BCNyuZDceBY6btZS0cp88wB1xEPorhXVtjiV1cjDRSFG
licqXh4fr4Qe0TUEeZK1uTqlhdj6YvKoFP94OKGxeM0eR1R/H/zyOtJVMMsEZLGr
GNSVBZBN0B6l9wAMa+DGpuHIX25I197vP3x0v0gvP/57bF9og9mj2JzntM9NJsR1
2zAgplgX4IUp4SGPvcNbLE5c9yIEj77SAOBumrF3IcUYNN9IXvIHQh8qzOWmI5q+
NFCKin0tQNCAx4ef+4ThkyPezRovlFxG6T4HMF1YjYrlVMgiN034opaCKoFXd3EF
4UufN3vV0IYB7AfxWLeNAJyPCreDSyYyLFGx+ONpM5JKk/1cwH8H0XQuLXY+TuGj
iF6QWkRkVcAYv0F7r2wPaVOVa8465s34fY94Rv1+KCpsjNFc3FrAJhz84jETxxqr
s44U/zmGh0/tixjs9vB1C/i7csYWXYJYiPsPmcp5sOE4M1PtYsIfuOlaJ12e/IV9
YnNK+RLghYQ0MghUMHZeg8aqKY7SATDB1SuK+YKmhXte/E/VhTBUy+3RautMIUwS
w9R1z2Hh4POZ4kp8yj9PnEujoQ5XtZuruhNyiWEwWYf1GPuDSoeEYcIRj18h8dL+
OSvsS1DqgPxH9hy8iidLDq1ZkrQ0w08Du9zjVY02f4OoRunzXbis6P3Y0mRf4iif
bYdqVg3snMwY5u9lEaIYqmtcGibgybah394CgTt0xrQTa2FydGlrOTk3QGdtYWls
LmNvbYkBHAQQAQIABgUCW87/3AAKCRDH1z/t9n8r4qnlB/9N1BBWSf6lfmejPh3R
DZ+QrBsCELm8qBeawlsY9To6UUdrIoC9vzIwKAgil2K2MC9z/laZQcep0WepnOar
5KSUyhPI50/aE97yfA0v4lKkylb0OPt8E0S4gIxTlRhpht2K4lsRaD+2wyRvMRuU
/Grgxd5TVVm9KfXQBCAxgFgX2OdZ2/Yb2GJQ4M6DquISIBar+i39a9bdZ9kP70ox
jfgG8SLXPxzBiHIULUy4X+80VafKWw1/AzN2t4CTRtIMHu7jeUqpws+MB6TxTLBA
G/JSdb+W3ceHseJ9YXqVIhfrlKt8T3QAqErjQjPN0YB9KDaELwDM1rxFryy8zuAB
zdZ/
=rb5z
-----END PGP PRIVATE KEY BLOCK-----
```

- So now we have a `PGP MESSAGE`, a `PGP PRIVATE KEY` and a `Passphrase`.
- So now let's [`Decrypt`](https://www.igolder.com/PGP/decryption/) it

![](https://github.com/a3X3k/Traboda/blob/main/FuzzY/9.png?raw=true)

- Finally we got the `Flag`.

```
flag{eNcryP7!ng_t0_PgP_1s_r34LLy_Pre3tY_g00D_pr1V4cY}
```


