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

> Must show all processes, for all users, including those which might not have a TTY
> Display in a user-oriented format
> Show process hierarchy

