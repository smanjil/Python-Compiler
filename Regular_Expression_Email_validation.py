
__author__ = 'ano'

'''
	This program is written using Python!
'''

'''
	A class named RegularExpressionEmailValidation is created below
	which consists of a constructor and a method..
'''

class RegularExpressionEmailValidation:

	# class constructor __init__ is made
	# to initialize all the quintuples of DFA

	def __init__(self , set_states , start_state , set_final_states):
		self.Q = set_states             # set of states of DFA
		self.q0 = start_state           # start state of DFA
		self.F = set_final_states       # set of final states
		return                          # returns none

	'''
		A method processEmail below
		to process the input string as email and return the
		transitions and whether the email is accepted or not..
	'''

	def processEmail(self , str):
		alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']   # list of alphabets
		digit = ['0','1','2','3','4','5','6','7','8','9']                                                                   # list of digits
		current_state = self.q0
		new = ''
		for i in str:                                                   # iterate over each character in string input
			if str[0].isdigit():                                        # checks if first character is digit
				email_accepted = False                                  # if yes, set False
			elif current_state == 'q0':                                 # checks for state q0
				if i in alpha:                                          # checks if the character is present in list alpha
					next_state = 'q1'
					print current_state , ' , ' , i , ' --> ' , next_state
					current_state = next_state
				email_accepted = True if next_state in self.F else False        # returns True or False when final state or not
			elif current_state == 'q1':                                         # checks for q1
				if i in alpha or i in digit:
					next_state = 'q1'
					print current_state , ' , ' , i , ' --> ' , next_state
					current_state = next_state
				elif i == '@':                                                  # checks if @ is triggered in string
					next_state = 'q2'
					print current_state , ' , ' , i , ' --> ' , next_state
					current_state = next_state
				email_accepted = True if next_state in self.F else False        # returns True or False when final state or not
			elif current_state == 'q2':
				if i in alpha:
					next_state = 'q3'
					print current_state , ' , ' , i , ' --> ' , next_state      # print transitions
					current_state = next_state
				email_accepted = True if next_state in self.F else False
			elif current_state == 'q3':
				if i in alpha:
					next_state = 'q3'
					print current_state , ' , ' , i , ' --> ' , next_state
					current_state = next_state
				elif i == '.':
					next_state = 'q4'
					print current_state , ' , ' , i , ' --> ' , next_state
					current_state = next_state
				email_accepted = True if next_state in self.F else False
			elif current_state == 'q4':
				if i in alpha:
					new += i                                                  # appends each character afer '.' to new to know domain
					next_state = 'q4'
					print current_state , ' , ' , i , ' --> ' , next_state
					current_state = next_state
					if new == 'com':                                               # checks is new has 'com' in it
						next_state = 'q5'
						print current_state , ' , ' , new , ' --> ' , next_state
						current_state = next_state
				email_accepted = True if next_state in self.F else False
			elif current_state == 'q5':
				if i == '.':
					next_state = 'q6'
					print current_state , ' , ' , i , ' --> ' , next_state
					current_state = next_state
				email_accepted = True if next_state in self.F else False
			elif current_state == 'q6':
				if i in alpha:
					next_state = 'q7'
					print current_state , ' , ' , i , ' --> ' , next_state
					current_state = next_state
				email_accepted = True if next_state in self.F else False
			elif current_state == 'q7':
				if i in alpha:
					next_state = 'q8'
					print current_state , ' , ' , i , ' --> ' , next_state
					current_state = next_state
				email_accepted = True if next_state in self.F else False
			elif current_state == 'q8':
				if i in alpha:
					next_state = 'q8'
					print current_state , ' , ' , i , ' --> ' , next_state
					current_state = next_state
				email_accepted = True if next_state in self.F else False
			else:
				email_accepted = False
		return email_accepted                                               # returns the value of email_accepted


set_states = ['q0' , 'q1' , 'q2' , 'q3' , 'q4' , 'q5' , 'q6' , 'q7' , 'q8' , 'q9']        # set of states
start_state = 'q0'                                                          # start state
set_final_states = ['q5' , 'q8']                                            # set of final states

# object 'r' for class RegularExpressionEmailValidation is created and parameters are passed for the constructor..
r = RegularExpressionEmailValidation(set_states , start_state , set_final_states)

# takes user input as email address
str = raw_input("Enter an email address : ")

#calls the method processEmail and formats the output
print("\n{} is accepted by DFA : {}\n" . format(str, r.processEmail(str)))
