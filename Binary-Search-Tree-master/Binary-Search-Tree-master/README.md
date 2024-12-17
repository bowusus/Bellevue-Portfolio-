# Binary Search Tree Implementation
## Overview
This project is a Binary Search Tree (BST) implementation written in C++ for operations on a non-linear data structure. The program allows users to perform key operations on a BST, such as insertion, deletion, searching, and traversals, through command-line input.

## Key Features
The program supports the following commands:

insert: Insert a new key into the binary search tree.
delete: Remove a specific key from the binary search tree.
search: Search for a specific key and check if it exists in the tree.
min: Find and display the minimum value (smallest key) in the tree.
max: Find and display the maximum value (largest key) in the tree.
next: Find and display the in-order successor of a given key.
previous: Find and display the in-order predecessor of a given key.
list: Display all keys in the BST in sorted order (in-order traversal).
parent: Display the parent of a specified key.
child: Display the children of a specified key.
help: Display a list of all supported commands for reference.
quit: Exit the program.

## How It Works
Program Execution Flow
Users input a command (e.g., insert, search, min, etc.).
The program processes the input, converts the command to lowercase for case insensitivity, and executes the corresponding BST operation.
If required, users can provide a key as input for commands like insert, delete, search, next, etc.
The program continues to accept commands until the user inputs quit to terminate.
## Commands
Command	           Description	                                             Input Example
insert	            Insert a key into the binary search tree.	                insert 45
delete	            Remove a key from the binary search tree.               	delete 45
search	            Search for a key in the binary search tree.             	search 45
min	                Find and display the smallest key in the tree.	              min
max	                Find and display the largest key in the tree.	                max
next	              Find the in-order successor of a key.                      	next 45
previous	          Find the in-order predecessor of a key.	                previous 45
list	              Display all keys in the tree in sorted order.	              list
parent	            Display the parent of a specified key.	                  parent 45
child	              Display the children of a specified key.	                  child 45
help	              Display all available commands.	                            help
quit	              Exit the program.	                                          quit

## Program Structure
Main Components:
main(): Handles user input and processes commands through the BinarySearchTree class.
BinarySearchTree Class: Implements all the core methods for BST operations. It is defined in the BST_Methods.h file.
Header Files:
PreCompiled_Header.h: Contains precompiled headers (e.g., standard libraries) for efficiency.
BST_Methods.h: Defines the BinarySearchTree class and its methods for BST operations.
