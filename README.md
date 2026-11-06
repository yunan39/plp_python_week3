plp_python_week3
Python Week 3 Assignment

grade_reporter.py: Evaluates a list of scores, assigns letter grades using conditionals, tracks pass/fail counts, and calculates the rounded average.
bug_hunt.py: A corrected while-loop script that accurately calculates and prints the sum of numbers from 1 to 5.

Reflection
The third bug (the off-by-one error in the loop condition `count < 5` instead of `count <= 5`) was the hardest to find because it produced no syntax or runtime error message—the program ran smoothly and just output the wrong number (10 instead of 15). I knew something was wrong because the logic was supposed to sum numbers up to 5, but the loop terminated too early and completely omitted the number 5 from the total.
