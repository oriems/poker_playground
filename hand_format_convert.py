
#initialization
#starting hands ranked file
#omaha_hands_file = "omaha_starting_hands_ranked.txt"
omaha_hands_file = "omaha_hands_sample.txt"
#create array of 4 suits spades, hearts, diamonds, clubs
suits = ["s","h","d","c"]
#create array of arrays with format; we'll use this to run the pypoker.py program to get associated EV for the given hand against HU random; 3-way random; 4-way random; 5-way random; and then take those associated EV's to rank and group each hand;
	#eval_hand = [["As","Js","Ah","Jh"], ["__","__","__","__"]]
	#need to create an empty array to fill, we'll add it later
hand_to_eval = []
#create empty string for the hand that will be evaluated; this comes from the infile line by line; we'll use to write to the output file

#iterate through the different suits

#set action = 1 when processing same suit hands
action = 0;
suited_stack = []

#from bibin r
# start reading line by line
# start reading character by character
# if the character is ( then start pushing the following characters into a stack; first in last out
# keep pushing the characters into the stack until you hit )
# once you hit ) then take action 1
# action 1 will process the cards in the stack and assign the same suit
# if the next character is not ( then proceed with action 2
# action 2 will start pushing into another stack until you hit (
# once you hit ( or the end of the line, pull out the items in the stack and begin assigning unique suits 1 by 1
with open("outputfile_sample.txt", "ab") as out:
	with open(omaha_hands_file) as f:
	    for line in f:
	    	line = line.strip('\n')
	    	suits = ["s","h","d","c"]
	    	action = 0
	    	suited_stack = []
	    	temp_suit = ""
	    	hand_to_eval = []
	    	for char in line:
	    		#the first time we see a ( character we know more suits are to come, let's set action = 1 and goto the next character
	    		if char == '(':
	    			action = 1
	    			continue
	    		#when we hit the ) character we need to start processing suited_stack by popping out the elements from the bottom of the stack
	    		if char == ')':
	    			temp_suit = str(suits.pop())
	    			for card in suited_stack:
	    				hand_to_eval.append(card+temp_suit)
	    			action = 0
	    			suited_stack = []
	    			continue
	    		#we've already seen ( character and need to start adding upcoming cards to the suited_stack
	    		if action == 1:
	    			suited_stack.append(char)
	    			continue
	    		if action == 0:
	    			temp_suit = str(suits.pop())
	    			hand_to_eval.append(char+temp_suit)
	    	out.write(str(hand_to_eval)+"\n")


#run the program for all 16.4K hands, and output to file with original format i.e. (AJ)(AJ); then comma delimmit with associated ev