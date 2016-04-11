# sanity-forensics - 1
**Category**: Sanity

## Problem
```
Someone tried to send us a message by leaving this image on an imageboard. Lucky for us they didn't choose 4chan. Can you find the message?
```
### Image 
![Image of NUSGreyhats logo](2b9d66fef4f09e03154b2e161d52010d.png)

## Solution
All you have to do is run `xxd 2b9d66fef4f09e03154b2e161d52010d.png | tail ` and you will get the flag!

