# C0rRupt3d

![](https://github.com/a3X3k/Traboda/blob/main/C0rRupt3d/3.png?raw=true)

### Description 

- The dimension of a playground is given as 1359x789. 
- Can you find out the most important information hidden in this file using the given data?

### Solution 

- [`Download`](https://github.com/a3X3k/Traboda/blob/main/C0rRupt3d/2.png) the `file`.
- We shall understand that there are some errors in the `Hex` values.
- So let's correct it.

![](https://github.com/a3X3k/Traboda/blob/main/C0rRupt3d/6.png?raw=true)

![](https://github.com/a3X3k/Traboda/blob/main/C0rRupt3d/7.png?raw=true)

- Still we wont be able to see the Image.
- It gives the `CRC` error since the `Height` and the `Width` is set to `0`.
- In the challenge description, we shall get the dimensions.
- [`Convert`](https://www.calculator.net/hex-calculator.html) it to `Hex` and correct the `Hex` Chunks.

![](https://github.com/a3X3k/Traboda/blob/main/C0rRupt3d/4.png?raw=true)

![](https://github.com/a3X3k/Traboda/blob/main/C0rRupt3d/5.png?raw=true)

- Finally we get the [`Image`](https://github.com/a3X3k/Traboda/blob/main/C0rRupt3d/1.png) with the `Flag`.

```
shaktictf{Th15_iS_IT_54268096}
```
