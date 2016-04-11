# sanity-forensics - 1
**Category**: Sanity

**Problem**:
```
Someone tried to send us a message by leaving this image on an imageboard. Lucky for us they didn't choose 4chan. Can you find the message?
```
### Image 
![Image of NUSGreyhats logo](2b9d66fef4f09e03154b2e161d52010d.png)

## Solution
All you have to do is run `xxd 2b9d66fef4f09e03154b2e161d52010d.png | tail ` and you will get the flag!

```
root@kali:~/Desktop# xxd 2b9d66fef4f09e03154b2e161d52010d.png | tail
002a4c0: 0000 0000 0038 80c0 0800 0000 0000 0007  .....8..........
002a4d0: 1018 0100 0000 0000 e000 0223 0000 0000  ...........#....
002a4e0: 0000 1cf0 ff1f 00ba f2af 9765 6da3 f500  ...........em...
002a4f0: 0000 4e74 4558 7441 7274 6973 7400 576f  ..NtEXtArtist.Wo
002a500: 772c 2079 6f75 2063 616e 2774 2062 6520  w, you can't be 
002a510: 7374 756d 7065 6421 2054 6865 2066 6c61  stumped! The fla
002a520: 6720 6973 2058 4354 467b 4974 735f 3230  g is XCTF{Its_20
002a530: 3136 5f6e 3074 5f33 7831 665f 7363 7562  16_n0t_3x1f_scub
002a540: 6269 6e7d 2e1e c8de 2100 0000 0049 454e  bin}....!....IEN
002a550: 44ae 4260 82                             D.B`.
```

The flag: `XCTF{Its_2016_n0t_3x1f_scubbin}`