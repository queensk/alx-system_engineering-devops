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

# 4 bad luck, 8 is your chance
## 5-4_bad_luck_8_is_your_chance

> The number 4 (四, pinyin: sì; Cantonese Yale: sei) is considered an unlucky number in Chinese because it is nearly homophonous to the word "death" (死 pinyin: sǐ; Cantonese Yale: séi).[citation needed] Thus, some buildings in East Asia omit floors and room numbers containing 4, similar to the Western practice of some buildings not having a 13th floor because 13 is considered unlucky. 

>Write a Bash script that loops from 1 to 10 and:

- displays bad luck for the 4th loop iteration
- displays good luck for the 8th loop iteration
- displays Best School for the other iterations

- Requirements:

- You must use the while loop (for and until are forbidden)
- You must use the if, elif and else statements

```
root@9918562e7569:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./5-4_bad_luck_8_is_your_chance
Best School
Best School
Best School
bad luck
Best School
Best School
Best School
good luck
Best School
Best School
root@9918562e7569:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing#
```

# Superstitious numbers
## 6-superstitious_numbers
>Write a Bash script that displays numbers from 1 to 20 and:

- displays 4 and then bad luck from China for the 4th loop iteration
- displays 9 and then bad luck from Japan for the 9th loop iteration
- displays 17 and then bad luck from Italy for the 17th loop iteration
- Requirements:

- You must use the while loop (for and until are forbidden)
- You must use the case statement

# 6. Superstitious numbers
## 6-superstitious_numbers

>Write a Bash script that displays numbers from 1 to 20 and:

- displays 4 and then bad luck from China for the 4th loop iteration
- displays 9 and then bad luck from Japan for the 9th loop iteration
- displays 17 and then bad luck from Italy for the 17th loop iteration
- Requirements:

- You must use the while loop (for and until are forbidden)
- You must use the case statement

```
root@9918562e7569:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./6-superstitious_numbers
1
2
3
4
bad luck from China
5
6
7
8
9
bad luck from Japan
10
11
12
13
14
15
16
17
bad luck from Italy
18
19
20
root@9918562e7569:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing#
```
