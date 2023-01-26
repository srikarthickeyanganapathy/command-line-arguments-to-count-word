# command-line-arguments-to-count-word
## AIM:
To write a python program for getting the word count from the contents of a file using command line arguments.
## EQUIPEMENT'S REQUIRED: 
PC
Anaconda - Python 3.7
## ALGORITHM: 
### Step 1:
import sys

### Step 2:
initially make count = 0

### Step 3:
open the content file using command line arguments.

### Step 4:
by using for loop name the function as "line"

### Step 5:
split the line using .split

### Step 6:
split the line using .split

## PROGRAM:
```python
import sys
count=0
with open(sys.argv[1],'r') as f1:
        for line in f1:
            word= line.split()
            count += len(word)
print("word Count in file = ",count)         
```

### OUTPUT:
![output](./output.png)

## RESULT:
Thus the program is written to find the word count from the contents of a file using command line arguments.
