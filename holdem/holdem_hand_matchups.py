import itertools
deck = [ 
['Ts', 'Qh'],
['Ts', 'Qd'],
['Ts', 'Qc'],
['Ts', 'Qs'],
['Ts', 'Kh'],
['Ts', 'Kd'],
['Ts', 'Kc'] ]



values = itertools.combinations(deck, 2)


with open("holdem_hand_matchups.txt", "ab") as out:
	for item in values:
		out.write(str(item)+"\n")