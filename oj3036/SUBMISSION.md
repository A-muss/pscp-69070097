# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```
3036
```

OJ submission ID, if submitted:

```
558209
```

OJ status:

```
Pass
```

Independent time spent on this problem:

```
10 minutes
```

How to count this time:

- Count only the time you actively worked on this problem independently.
- Start counting from when you first read the problem.
- Do not include breaks, meals, classes, sleep, time spent on other problems, or time when you were not working on this problem.
- If you used AI, count only the independent time before your first AI prompt.
- If you asked a friend, TA, or instructor for help, count only the independent time before your first help request.
- If you used both AI and human help, count only the independent time before the first outside help of any kind.
- If you did not use AI or human help, count the time before writing this `submission.md`.
- An estimate is acceptable, but it must be honest.

---

## 2. My Understanding

Write the problem in your own words.

Also explain the input, output, and important constraints.

If you do not fully understand the problem yet, write what you currently understand. Your understanding may be incomplete or incorrect, but you must make a genuine attempt.

```
ok so, we are in the castle that build like prymid that have many small tringle room inside and our goal is to go to the top of the castle. but theres a catch, you have to go there by destroing wall as few as possible.
now stay with me, we gonna receive 1 input, and thats gonna be the room we're in. the building's rooms are going to increase by 2 as the floor gose down start from the top. we have to figure it out what floor we are in, then figure out we're in odd or even room. finally, we just multiply the number of floor we're in by 2 and minus it by 1 (depending on even, odd room) and now we can print out the result
```

---

## 3. My First Plan

Write your first plan before getting help from AI, a friend, a TA, an instructor, or before finalizing your code.

If you used AI, write the plan you had before your first AI prompt.

If you asked a friend, TA, or instructor for help, write the plan you had before asking for help.

If you did not use AI or human help, write the plan you had before or while you started coding.

This can be rough. It may be incomplete or different from your final solution.

You may write pseudocode, a flowchart idea, or step-by-step thinking.

```
Step 1: receive the number of the room we're in
Step 2: check if we're in room 1 if yes print out 0 and return
Step 3: then check what floor we're in by compare it the the last room of that floor
Step 4: check if it the room that facing dowm (odd) or facing up (even)
Step 5: multiply the floor number by 2 and minus - 1 if it facing up (even)
Step 6: print out the value
```

---

## 4. My Final Approach

Briefly explain the final algorithm or method you actually used in your submitted code.

This section is different from Section 3:

- Section 3 is your first plan before AI, human help, or before the final code.
- Section 4 is the final method used in your actual solution.
- If your final approach is the same as your first plan, write that it is the same and briefly explain why.

Do not copy AI's explanation.

Do not copy another person's explanation.

```
i run it and passed on the first time (except the one that i try to brute force, for fun ofc.) so i use the plan that i first did
```

---

## 5. My Tests

Write at least 3 test cases that you tried or designed by yourself.

Try to choose test cases that are different from each other.

For each test case, explain why you chose it.

If the input or output has many lines, write them inside the text blocks.

### Test Case 1

Why I chose this case:

```
to check if my algorithm are correct
```

Input:

```
1
```

Expected output:

```
0
```

Actual output:

```
0
```

Result:

```
Pass
```

### Test Case 2

Why I chose this case:

```
to check if the math are correct
```

Input:

```
15
```

Expected output:

```
5
```

Actual output:

```
5
```

Result:

```
Pass
```

### Test Case 3

Why I chose this case:

```
to check if the math are correct
```

Input:

```
561
```

Expected output:

```
45
```

Actual output:

```
45
```

Result:

```
Pass
```

---

## 6. AI Use

Did you use AI for this problem?

```
No
```

If yes, also complete:

```text
ai_reflection.md
```

If you only asked a friend, TA, or instructor and did not use AI, you do not need to complete `ai_reflection.md`.

---

## 7. Human Help / Collaboration

Did you ask a friend, TA, instructor, or another person for help on this problem?

```
no
```

If yes, briefly explain what kind of help you received.

Allowed examples:

- explanation of the problem statement
- explanation of a programming concept
- hint about the approach
- debugging discussion
- test-case discussion
- help understanding an error message

Not allowed:

- copying another person's code
- submitting another person's solution
- asking another person to write the solution for you
- using another person's OJ submission
- asking another person to submit to the OJ for you

Who helped you?

```

```

What did they help with?

```

```

What did you still do by yourself?

```

```

Did you copy any code from another person?

```
no
```

---

## 8. Student Declaration

Write `Yes` for each statement.

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |
