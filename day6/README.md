# DAY 6

## Args (Non-Keyword Arguments)

args allows you to pass a variable number of positional arguments to a function. The function receives them as a tuple. The name args is just a convention; you could call it ```*numbers``` or anything else, but ```*args``` is standard.

Think of it as a "catch-all" for any extra positional arguments.

**When to use it** : When you don't know how many arguments will be passed to your function. A great example is a function that needs to sum an unknown quantity of numbers.

## Kwargs (Keyword Arguments)

`**kwargs` allows you to pass a variable number of keyword arguments (key-value pairs) to a function. The function receives them as a dictionary. Like `*args`, the name kwargs is just a convention.

Think of it as a "catch-all" for any extra named arguments.

**When to use it** : When you want to handle named arguments that you haven't defined in advance. This is common in functions that need to be highly flexible, like creating a user profile where some details are optional.

## Lambda Function

A lambda function is a small, one-line, anonymous function. It's "anonymous" because it doesn't have a name like functions defined with def.

Syntax:

```python
lambda arguments: expression
```

It can have any number of arguments but only one expression, which is evaluated and returned.
