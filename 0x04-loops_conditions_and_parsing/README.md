B# 0x04. Loops, conditions and parsing

# 0. Create a SSH RSA key pair

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

# 1. For Best School loop
## 1-for_best_school

> What is the advantage of using #!/usr/bin/env bash over #!/bin/bash

> The first form (#!/usr/bin/env bash) is better, as it will work when Bash is in your path, but isn't in /bin. Often, both will work. However, if your script runs on a system where /bin/bash isn't Bash (or isn't a symlink to it), then #!/bin/bash won't work as it isn't in that location, but #!/usr/bin/env bash will.

> syntax 
```
for NAME [in LIST ]; do COMMANDS; done
```

```
sylvain@ubuntu$ head -n 2 1-for_best_school 
#!/usr/bin/env bash
# This script is displaying "Best School" 10 times
sylvain@ubuntu$ ./1-for_best_school 
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
```

# 2. While Best School loop
## 2-while_best_school
> Write a Bash script that displays Best School 10 times.
- Requirements:
- You must use the while loop (for and until are forbidden)

```
sylvain@ubuntu$ ./2-while_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
```
# 3. Until Best School loop
## 3-until_best_school
> Write a Bash script that displays Best School 10 times.
- Requirements:
- You must use the until loop (for and while are forbidden)

#  If 9, say Hi!
## 4-if_9_say_hi
>Write a Bash script that displays Best School 10 times, but for the 9th iteration, displays Best School and then Hi on a new line.
-Requirements:

- You must use the while loop (for and until are forbidden)
- You must use the if statement
```
sylvain@ubuntu$ ./4-if_9_say_hi
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Hi
Best School
sylvain@ubuntu$ 
```
