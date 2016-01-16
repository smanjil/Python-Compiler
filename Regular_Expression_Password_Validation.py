
__author__ = 'ano'

'''
	This program is written using Python!
'''

'''
	A class named RegularExpressionPasswordValidation is created below
	which consists of a constructor and a method..
'''

class RegularExpressionPasswordValidation:

	# class constructor __init__ is made
	# to initialize all the quintuples of DFA

	def __init__(self , set_states , start_state , set_final_states):
		self.Q = set_states                             # set of state
		self.q0 = start_state                           # start state
		self.F = set_final_states                       # set of final state
		return                                          # return none

	'''
		A method processPassword below
		to process the input string as password and return the
		transitions and whether the password is accepted or not..
		This method works for the string with combination of digits and letters
		but does not start with a letter...
	'''

	def processPassword(self , str):
		alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']   # list of alphabets
		digit = ['0','1','2','3','4','5','6','7','8','9']                                                                   # list of digits
		current_state = self.q0
		if len(str) >= 6 and len(str) <= 10:                                           # checks the length of password
			for i in str:                                                              # iterate over each character in string input if length is satisfied
				if str[0].isdigit() and current_state == 'q0':                         # checks if first character is digit
					next_state = 'q3'
					print current_state , ' , ' , i , ' --> ' , next_state
					current_state = next_state
					password_accepted = False                                           # if yes, set False
				elif current_state == 'q0':                                             # checks for state q0
					if i in alpha:                                                      # checks if the character is present in list alpha
						next_state = 'q1'
						print current_state , ' , ' , i , ' --> ' , next_state
						current_state = next_state
					password_accepted = True if next_state in self.F else False         # returns True or False when final state or not
				elif current_state == 'q1':
					if i in alpha:
						next_state = 'q1'
						print current_state , ' , ' , i , ' --> ' , next_state
						current_state = next_state
					elif i in digit:
						next_state = 'q2'
						print current_state , ' , ' , i , ' --> ' , next_state
						current_state = next_state
					password_accepted = True if next_state in self.F else False
				elif current_state == 'q2':
					if i in alpha or i in digit:
						next_state = 'q2'
						print current_state , ' , ' , i , ' --> ' , next_state
						current_state = next_state
					password_accepted = True if next_state in self.F else False
				elif current_state == 'q3':
					if i in alpha or i in digit:
						next_state = 'q3'
						print current_state , ' , ' , i , ' --> ' , next_state
						current_state = next_state
					password_accepted = True if next_state in self.F else False
				else:
					password_accepted = False
		else:                                                                              # password length does not satisfy
			print "\nYour password must be at least of length 6 and at most of 10!!!!"
			password_accepted = False                                                       # password is not accepted
		return password_accepted                                                        # return value stored in password_accepted


set_states = ['q0' , 'q1' , 'q2' , 'q3']                                # set of states
start_state = 'q0'                                                      # start state
set_final_states = ['q2']                                               # set of final states

# object 'r' for class RegularExpressionPasswordValidation is created and parameters are passed for the constructor..
r = RegularExpressionPasswordValidation(set_states , start_state , set_final_states)

# takes user input as password
str = raw_input("Enter a password : ")

#calls the method processPassword and formats the output
print("\n{} is accepted by DFA : {}\n" . format(str, r.processPassword(str)))
