
__author__ = 'ano'

'''
	This program is written using Python!
'''

'''
	A class named DFA_First is created below
	which consists of a constructor and a method..
'''

class DFA_First:

	# class constructor __init__ is made
	# to initialize all the quintuples of DFA

	def __init__(self , set_states , set_alphabets , transition_dict , start_state , set_final_states):
		self.Q = set_states                     # set of states of DFA
		self.sigma = set_alphabets              # set of alphabets or input symbols(not used only defined here)
		self.delta = transition_dict            # set of transition functions
		self.q0 = start_state                   # start state of DFA
		self.F = set_final_states               # set of final states of DFA
		return                                  # returns none

	'''
		A method process_string below
		to process the input string and return the
		transitions and whether the string is accepted or not..
		This method works for the string starting with 0 and ending with 11..
	'''

	def process_string(self , str):
		current_state = self.q0
		print "\n"
		for i in str:                                           # iterate over the characters in input string
			#print i
			new = current_state
			current_state = self.delta[(current_state , i)]     # current_state and input symbol is passed in transition function delta
			print new , ' , ' ,  i , '-->>' , current_state     # transition is shown here
			#print current_state
			if current_state in self.F:                         # checks whether the state after certain transitions is in final state and set True
				string_accepted = True
			else:                                               # otherwise set False
				string_accepted = False
		return string_accepted                                  # return the value set in string_accepted


'''
	Below all the quintuples of DFA are assigned a set of values or value..
	set_states represent set of all states in a DFA ,
	set_alphabets is the input symbols for DFA ,
	transition_dict is a dictionary containing the transition from a state to another taking a input symbol ,
	start_state is the initial state of DFA ,
	set_final_state is the final state or the accepting state of DFA.
'''

set_states = ['q0' , 'q1' , 'q2' , 'q3' , 'q4']
set_alphabets = ['0' , '1']
transition_dict = {
	('q0' , '0') : 'q1' ,
    ('q0' , '1') : 'q2' ,
    ('q1' , '0') : 'q1' ,
    ('q1' , '1') : 'q3' ,
    ('q3' , '0') : 'q1' ,
    ('q3' , '1') : 'q4' ,
    ('q4' , '0') : 'q1' ,
	('q4' , '1') : 'q4' ,
	('q2' , '0') : 'q2' ,
	('q2' , '1') : 'q2'
}
start_state = 'q0'
set_final_states = 'q4'

#object 'd' for class DFA_First is created and parameters are passed for the constructor..
d = DFA_First(set_states , set_alphabets , transition_dict , start_state , set_final_states)

#asks the user for input string, only number with 0 or 1
str = raw_input("Enter a string of numbers (0 or 1) : ")

#calls the method process_string and formats the output
print("\n{} is accepted by DFA : {}" . format(str, d.process_string(str)))
