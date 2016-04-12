# 9x3 - 2
**Category**: crypto

**Problem**:
```
Solve this: YAHORAUCLWRLAYENPNTTGMOEOCS. 
Flag is not in XCTF{} format, please submit in XCTF{plaintext}.
```

## Solution
The data is arranged in 9 rows and 3 columns. So all you have to do is split them 3 characters at a time. (Thanks Darren)
```
YAH
ORA
UCL
WRL
AYE
NPN
TTG
MOE
OCS
```

Reading from top to bottom from column to column will give you: `YOUWANTMOARCRYPTOCHALLENGES`

The flag: `XCTF{YOUWANTMOARCRYPTOCHALLENGES}`