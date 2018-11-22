# [P](#)y[P](#)se - A Pseudocode Compiler in Python

## Introduction

PsPse is a full-featured interpreted compiler for teaching purposes.

Features:

* Compile all codes in AS-Level Computer Science Syllabus
* Portable with no environemt requirements
* Available in Windows and Linux
* Continuously developing based on my interest

I am new to comiplers, and the project is still under heavy developing. Feel free to raise issues or contribute.

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
git clone https://github.com/HankelBao/PyPseTest
```

Now, you will have the PyPseTest folder in your current path. CD to it and you will have `pypse.bin` and `pypse.exe` under the folder.

If you are using Windows, 

```
.\pypse.exe test.5.pse
```

If you are using Linux, 

```
.\pypse.bin test.5.pse
```

If you see the *Hello World!* message showing up just like the demo, you are ready to go!

## Usage

Remember, you should always use `pypse.bin` for linux and `pypse.exe` for windows.

Pseudocode File ends in **.pse**, so you should create a file with such extension for execution.

Write your own pseudocode and execute it!

If you want to see the debug info for the compiler, call the command with *--debug*

For example

```
.\pypse.exe test.5.pse --debug
```

## Contributing

The compiler is currently **not** fully functioning and there may be a lot of bugs.

Feel free to report issues and spread it around your classes if you also find the need for such a compiler.

Thans for your support.