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

##  Repetition Token #0
### File: 1-repetition_token_0.rb
> Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## Repetition Token #1
### File: 2-repetition_token_1.rb
> Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## Repetition Token #2
### File: 3-repetition_token_2.rb

> Requirements:

> Find the regular expression that will match the above cases
> Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## Repetition Token #3
### File: 4-repetition_token_3.rb
> Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
- Your regex should not contain square brackets

## Not quite HBTN yet
### File: 5-beginning_and_end.rb
> Requirements:

- The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## Call me maybe
### File: 6-phone_number.rb

> Requirement:

- The regular expression must match a 10 digit phone number

## OMG WHY ARE YOU SHOUTING?
### File: 6-phone_number.rb
> Requirement:

- The regular expression must match a 10 digit phone number

## OMG WHY ARE YOU SHOUTING?
### File: 7-OMG_WHY_ARE_YOU_SHOUTING.rb
> Requirement:

- The regular expression must be only matching: capital letters

## Textme
### File: 100-textme.rb
>Requirements:

- Your script should output: ``` [SENDER],[RECEIVER],[FLAGS] ```
- The sender phone number or name (including country code if present)
- The receiver phone number or name (including country code if present)
- The flags that were used