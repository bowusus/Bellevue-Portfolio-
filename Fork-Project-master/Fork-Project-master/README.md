# Pipe Communication and Collatz Conjecture Program
## Overview
This program demonstrates inter-process communication (IPC) using pipes in a Linux/UNIX environment. 
It uses a parent-child process setup created via fork(). 
The program calculates the Collatz Conjecture (also known as the "3n + 1 problem") for a given positive integer 
input using two pipes to exchange data between the parent and child processes.

## Collatz Conjecture
The Collatz Conjecture works as follows:

Start with any positive integer n.
If n is even, divide it by 2: n = n / 2.
If n is odd, multiply it by 3 and add 1: n = 3n + 1.
Repeat steps 2 and 3 until n becomes 1.
The program outputs:

Each intermediate value of n.
The total number of steps taken to reach 1.
The peak maximum value encountered during the process.
## How It Works
Parent Process
Accepts a positive integer n0 from the command line.
Writes the starting number n0 to the first pipe (num1).
Reads updated values from the second pipe (num2) until the value becomes 1.
Tracks:
Each intermediate value.
The number of steps to reach 1.
The peak maximum value encountered.
Outputs the sequence, steps, and peak maximum to the terminal.
## Child Process
Reads the starting number from the first pipe (num1).
Performs the Collatz Conjecture calculations:
If the number is even, divide it by 2.
If the number is odd, calculate (3 * n + 1).
Writes the updated value back to the parent via the second pipe (num2).
Continues until the value becomes 1.
## Key Features
Pipes: Two pipes (num1 and num2) facilitate bidirectional communication between the parent and child processes.
Fork: fork() is used to create a child process.
Collatz Conjecture: Calculates and prints the sequence of numbers.
Step Counting and Peak Tracking: Tracks the number of iterations (steps) and the largest number encountered.
## Program Execution
Compilation
To compile the program, use gcc:
gcc -o collatz_pipe collatz_pipe.c
## Run the Program
The program accepts a single positive integer n0 as a command-line argument:
./collatz_pipe 27
