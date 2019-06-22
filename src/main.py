#########################
#                       #
#   OpenPyLexer v0.01   #
#    by Millo Evers     #
#                       #
#########################

# Thanks for using OpenPyLexer (OPL). OPL is an open-source Python lexer that anyone can use when making their own programming languages in Python.
# It is designed to be efficient for the programmer and the end-user. Everything is fully commented so anyone can understand what's going on.
# test.lang is where you structure your language and use it for testing. It has a basic structure already put in that can be used to learn how to structure properly.

# This imports everything that python needs to produce a lexer.
import lexer

# All of the code used is in this function named 'main'
def main():

	# Reads current source flow in test.lang and stores it in 'content'
	content = ""
	with open('test.lang', 'r') as file:
		content = file.read()

	#
	##
	### Lexer
	##
	#

	# Calls lexer and initializes it with source code
	lex = lexer.Lexer(content)
	# Calls for tokenization.
	tokens = lex.tokenize()

# Runs the lexer.
main()
