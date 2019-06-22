#
# This is the main code for the lexer.
#


import re

class Lexer(object):

	def __init__(self, source_code):
		self.source_code = source_code

	def tokenize(self):
		
		# Where all lexer tokens are stored
		tokens = []

		# Creates a word list of the source code
		source_code = self.source_code.split()

		# Keeps track of word index in source code
		source_index = 0

		# Goes through every word in source code in order to generate tokens.
		while source_index < len(source_code):

			word = (source_code[source_index])

			# Recognises variables and creates token for it
			if word == "var": tokens.append(["VAR_DECLERATION", word])

			# This will recognise a word and create an identifier token for it
			elif re.match('[a-z]', word) or re.match('[A-Z]', word):
				tokens.append(['IDENTIFIER', word])

			# This will recognise an integer and create an identifier token for it
			elif re.match('[0-9]', word):
				tokens.append(['INTEGER', word])

			# This will recognise an operator and create an identifier token for it
			elif word in "=/*=-+":
				tokens.append(['OPERATOR', word])

			# This will recognise an operator and create an identifier token for it
			elif word in ";":
				tokens.append(['SEMICOLON', word])

			# Increases word index after checking it
			source_index += 1

		print(tokens)

		return tokens
