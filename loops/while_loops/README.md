
The assessment task for the `while` loop operator

Task

Create a discount countdown timer that collects all countdown values in a list using a **while loop**.

1. Create a new variable named `current_number` and set it equal to `start_number`.
    
2. Use a **while loop** to count down while `current_number` is greater than `0`.
    
3. During each iteration, append the current value of `current_number` to the `countdown_values` list.
    
4. Decrease `current_number` by `1` during each iteration.
    
5. After the loop completes, print `Discount countdown complete!` and then print the `countdown_values` list.

---


I explain the way that i understand the code: 

Firstly i already have 2 variable 

1. `start_number = 5`: this is the integer number that i got
2. `countdown_value = []`: this is python list

Looking at the first question what they want me to do is: 

```markdown
Create a new variable named `current_number` and set it equal to `start_number`.
```

So from what i understand here is they want me to create a new variable which is `current_number` for the countdown.

```python
current_number = start_number
```

What i understand from here is now the variable have update to the start number. Next let's move on to the second question: 

```markdown
Use a **while loop** to count down while `current_number` is greater than `0`.
```

From what i understand here i need to tell python that if `5 is more bigger than 0` start the countdown 

```python
while current_number > 0:
```

Than a third question come in that make me a little bit confuse 

```markdown
During each iteration, append the current value of `current_number` to the `countdown_values` list.
```

After a while thinking i finally understand the question, so what the question want me to do add the `current_number` inside the list `countdown_values` and:

```markdown
Decrease `current_number` by `1` during each iteration.
```

```python
countdown_values.append(current_number)
```

Everytime the condition is **TRUE** it keep print the number until it reach `0`. So from here i can move to another questions.

```markdown
Decrease `current_number` by `1` during each iteration.
```

So what they want is the real countdown for example: 5,4,3,2,1.... 

```python
current_number -= 1
```

This tell `current_number` to decrease everytime the condition is **TRUE** 

And finally last question: 

```markdown
After the loop completes, print `Discount countdown complete!` and then print the `countdown_values` list.
```

I just need to print it out and i used `f string` to make it more readable and faster.

```python
print (f"Discount countdown complete!: {current_number}")
print (countdown_values)
```

So the output will be: 


```bash
Discount countdown complete! 4[5]Discount countdown complete! 3[5, 4]Discount countdown complete! 2[5, 4, 3]Discount countdown complete! 1[5, 4, 3, 2]Discount countdown complete! 0[5, 4, 3, 2, 1]
```

That notes from me. 


## Goodluck future me 
