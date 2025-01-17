# Drome Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

Given the head of a singly linked list, write a function is_palindrome that returns `True` if the list is a palindrome and `False` if it is not a palindrome.

For example:
5 → 4 → 2 is NOT a palindrome
5 → 4 → 5 is a palindrome

The list will be represented using the provided `Node` class.

It is guaranteed that the list will not have any cycles.

Adapted from: https://leetcode.com/problems/palindrome-linked-list/

## Examples

### Additional Palindrome Examples

5 → 4 → 5

a → b → c → c → b → a

3 → 3

5 _(only one element in list)_

_(empty list)_

### Additional Not-Palindrome Examples

5 → 4 → 2

a → b → c → E → b → a
