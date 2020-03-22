# vuq 0.1
It's not a golfing lang.

### Explanation
Vuq is a rule-based language. You define a block for a rule to live in, you then define the rule to your needs.
A function must always be attached to the rule block, this will be run until the rule is true.
Parameters are referred to with commas, the amount matching their index.

### Syntax
- ``` ` ``` - Line comment
- ``` [ ] ``` - A rule block
- ``` u=1 ``` - A rule
- ``` \ ``` - Ends a rule
- ``` -w,u> ``` - A function
- ``` , ``` - A function parameter
- ``` + - * / ``` - Arithmetic operators
- ``` 1 2 3 4 5 6 7 8 9 ``` - Numeric numbers

### Quirks
- Vuq, in it's limitless attempts to not use many characters or spaces, does not have `>`, you must instead use `!<`.
- The function of a rule, and therefor a rule, will always return `true`, as it can't return until it has finished.

### Factorial
```
[           `1. Begins a block
   g=1      `  1.1. Requires the variable G to equal 1 to exit the block
   \        `  1.2. Ends the rule
   -g>      `  1.3. Sets the blocks function, taking in G
   ,        `  1.4. Refers to G
   +1       `  1.5. Adds 1 to G
]           `  1.6. Ends the block

[           `2. Begins a block
   i=3      `  2.1. Requires I to equal 3 to exit the block
   \        `  2.2. Ends the rule
   -i,g>    `  2.3. Sets the blocks function, taking in I and G
   ,,       `  2.4. Refers to G
   *        `  2.5. Multiplies the first value by the second
   ,        `  2.6. Refers to I
   _        `  2.7. Separate variables
   ,        `  2.8. See #2.5
   +1       `  2.9. Adds 1 to I
]           `  2.10. Ends the block
```

### Credits
- [@DeflatedPickle](https://github.com/DeflatedPickle)
    - Wrote the ANTLR4 grammar
    - Started writing demo's in Raku, Kotlin and Python
    - Wrote the blown out factorial description, based on the example
    - Made the choice decision to use multiple commas to refer to parameters
- [@Gigabitten](https://github.com/Gigabitten)
    - Helped with the initial idea
    - Reigned in my idiocy
    - Wrote and explained the factorial example to me
    - Stuck in a call for 6 hours to concept this
- [@Me43489](https://github.com/Me43489)
    - Helped with the initial idea
    - Came up with the concept of rules
    - Tried to not get me to use commas for parameters (they half won)
    - Stuck in a call for 4 hours to concept this
