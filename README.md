# [Py](#)thon [Pse](#)udocode Compiler

## Introduction

PsPse is a interpreted compiler for teaching purposes.

Features:

* Compile codes in AS-Level Computer Science Syllabus
* Portable with no environemt requirements
* Available in Windows and Linux
* Continuously developing

I am a senior high student learning A2 Computer Science currently, and I am new to compilers. The project is still under heavy developing. Feel free to raise issues or contribute.

![demo_screenshot](screenshots/demo_screenshot.png)

## Why?

Pseudocode is used to express ideas without truly writing code. However,

* AS-Level has specific grammar for this language
* AS-Level International Test marks based on the grammar
* There is no compiler for it, and there is no way to test it or execute it.

As a result, there is a clear need to write such compiler, also as a project of mine for interest. :smirk:

## Get Started

First, Clone the repo in terminal:

```
git clone https://github.com/HankelBao/PyPse
```

Now, you will have the PyPse folder in your current path. CD to PyPse/bin/ and you will have `pypse.bin` and `pypse.exe` under the folder.

If you are using Windows, 

```
.\pypse.exe ..\test\test.5.pse
```

If you are using Linux, 

```
.\pypse.bin ..\test\test.5.pse
```

If you see the *Hello World!* message showing up just like the demo, you are ready to go!

## Usage

Remember, you should always use `pypse.bin` for linux and `pypse.exe` for windows.

Pseudocode File ends in **.pse**, so you should create a file with such extension for execution.

Write your own pseudocode and execute it!

## Progress

- [ ] Warnings and Errors
- [ ] Full types support
    - [x] INT
    - [ ] REAL
    - [ ] STRING
    - [ ] BOOL
- [x] Declaration
- [x] Arrays
- [ ] Dicts
- [x] Custom Types
- [x] Debug Block
- [x] Assign
- [x] Output
- [x] Input
- [x] IF...
- [x] WHILE...
- [x] REPEAT...
- [x] FOR...
- [x] Procedure...
- [x] CALL...
- [x] FUNCTION...
- [x] RETURN...
- [ ] CASE...
- [ ] More Features...


## Contributing

The compiler is currently **not** fully functioning and there may be some bugs.

If you want to see the debug info for the compiler, call the command with *--debug*

For example

```
.\pypse.exe ..\test\test.5.pse --debug
```

Feel free to report issues and make contributions

## Promote

Spread it around your classes if you also find the need for such a compiler!

Thanks for your support.
