# 0x06. Regular expression

##
- A regular expression is a pattern of characters.

- The pattern is used to do pattern-matching "search-and-replace" functions on text.
```
abc…	Letters
123…	Digits
\d	Any Digit
\D	Any Non-digit character
.	Any Character
\.	Period
[abc]	Only a, b, or c
[^abc]	Not a, b, nor c
[a-z]	Characters a to z
[0-9]	Numbers 0 to 9
\w	Any Alphanumeric character
\W	Any Non-alphanumeric character
{m}	m Repetitions
{m,n}	m to n Repetitions
*	Zero or more repetitions
+	One or more repetitions
?	Optional character
\s	Any Whitespace
\S	Any Non-whitespace character
^…$	Starts and ends
(…)	Capture Group
(a(bc))	Capture Sub-group
(.*)	Capture all
(abc|def)	Matches abc or def
```

## Tasks
## 0. Simply matching School
### File: 0-simply_match_school.rb

- Requirements:

- The regular expression must match School
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression  matching method