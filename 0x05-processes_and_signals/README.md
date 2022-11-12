# 0x05. Processes and signals
	
> A PID (i.e., process identification number) is an identification number that is automatically assigned to each process when it is created on a Unix-like operating system.

> A process is an executing (i.e., running) instance of a program. Each process is guaranteed a unique PID, which is always a non-negative integer.

> The process init is the only process that will always have the same PID on any session and on any system, and that PID is > 1. This is because init is always the first process on the system and is the ancestor of all other processes.

> A very large PID does not necessarily mean that there are anywhere near that many processes on a system. This is because such numbers are often a result of the fact that PIDs are not immediately reused, in order to prevent possible errors.

# Tasks

# What is my PID
## File: 0-what-is-my-pid

> Write a Bash script that displays its own PID.

# List your processes
## File: 1-list_your_processes
> Write a Bash script that displays a list of currently running processes.

> Requirements:

> Must show all processes, for all users, including those which might not have a TTY
> Display in a user-oriented format
> Show process hierarchy

# 1. List your processes
## File: 1-list_your_processes

> Write a Bash script that displays a list of currently running processes.

> Requirements:

- Must show all processes, for all users, including those which might not have a TTY
- Display in a user-oriented format
- Show process hierarchy

# 2. Show your Bash PID
## File: 2-show_your_bash_pid
>Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

>Requirements:

- You cannot use pgrep
- The third line of your script must be # shellcheck disable=SC2009

# 3. Show your Bash PID made easy
## File: 3-show_your_bash_pid_made_easy
> Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

> Requirements:

- You cannot use ps

# 4. To infinity and beyond
## File: 4-to_infinity_and_beyond
> Write a Bash script that displays To infinity and beyond indefinitely.

> Requirements:

- In between each iteration of the loop, add a sleep 2