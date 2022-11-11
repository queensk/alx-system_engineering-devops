# 0x04. Loops, conditions and parsing


## 0-RSA_public_key.pub


> Run the following command to create an SSH key pair. You can leave the passphrase blank if you do not wish to "unlock" your key each time you use it:

> ubuntu
```
ssh-keygen -t rsa
```

>Windows
```
ssh-keygen
```
## 1-for_best_school

###  For Best School loop
What is the advantage of using #!/usr/bin/env bash over #!/bin/bash

> The first form (#!/usr/bin/env bash) is better, as it will work when Bash is in your path, but isn't in /bin. Often, both will work. However, if your script runs on a system where /bin/bash isn't Bash (or isn't a symlink to it), then #!/bin/bash won't work as it isn't in that location, but #!/usr/bin/env bash will.

> syntax 
```
for NAME [in LIST ]; do COMMANDS; done
```

