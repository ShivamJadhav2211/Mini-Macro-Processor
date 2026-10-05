# Mini Macro Processor

This project is a simple Mini Macro Processor built using Python. It demonstrates how macros are defined, stored, and expanded in a program.

## Features

* Define macros
* Detect macro calls
* Expand macros
* Handle macro parameters
* Generate expanded code

## Technology Used

* Python
* Compiler Design

## How It Works

1. Read the input program.
2. Find the macro definition.
3. Store the macro.
4. Find the macro call.
5. Replace the macro call with its macro body.
6. Display the expanded program.

## How to Run

```bash
python macro_processor.py
```

## Example

**Input:**

```text
MACRO
ADD &A, &B
MOV R1, &A
ADD R1, &B
MEND

ADD X, Y
```

**Output:**

```text
MOV R1, X
ADD R1, Y
```

## Author

Shivam Pankaj Jadhav
