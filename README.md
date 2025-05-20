# Plan for year task 2025

### The what

A website that contains the following:
- A system for signing up and logging in.
- A systen to add games to a personal library.
- A system to downloaded the games from said library.


A selection of games i have created in the past.

A database for the users and games.

<br>
<br>

### The how/with what
The site is built primarily with:
- HTML
- Python/Flask
<br>

Database is made with SQL.

Games are made with whatever they were made with when they were made.

Artwork mainly made in piskel.

<br>
<br>

### Design of the website 

#### Colors

The colors picked contrast well and are easy to read. I have gotten my (decently) color blind friend to see if he can read everything easily as well.

Background / game section text: #1f0933
<br>
Text / game section background: #D5C0F8
<br>
Header: #32075a
<br>
Button border: #9F87AF


<br>
<br>

### What is needed to use this project

#### SQL
The databases in this project uses sql so you will need to use a program to utilize this.
Some examples of programs:
- XAMPP
- ZAMP

#### Python libraries

In app.py

```
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
```
So you need to install these libraries (to be honest, I am not fully sure what re does)


