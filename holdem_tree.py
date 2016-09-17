#
# Copyright (C) 2007, 2008 Loic Dachary <loic@dachary.org>
# Copyright (C) 2004, 2005, 2006 Mekensleep
#
# Mekensleep
# 24 rue vieille du temple
# 75004 Paris
#       licensing@mekensleep.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301, USA.
#
# Authors:
#  Loic Dachary <loic@dachary.org>
#
# 
import sys
sys.path.insert(0, ".")
sys.path.insert(0, ".libs")

from pokereval import PokerEval

iterations_low = 100000
iterations_high = 200000

pokereval = PokerEval()
emptyhand = ["__","__"]
#evalpockets = [["As","Js","Ah","Jh"], ["__","__","__","__"]]
#print "winners omaha = %s\n" % pokereval.winners(game = "omaha", pockets = [ ["tc", "ac", "ks", "kc" ],  ["th", "ah", "qs", "qc" ],  ["8c", "6h", "js", "jc" ]], dead = [], board = ["7h", "3s", "2c", "7s", "7d"])

#print "f7 result = %s\n" % pokereval.poker_eval(game = "omaha", fill_pockets = 1, iterations = iterations_high, pockets = [ ["2h", "2c", "6s", "Jd"],   ["__", "__", "__", "__"]], dead = [], board = ["__", "__", "__", "__", "__"])
#print "(AJ)(AJ) result = %s\n" % pokereval.poker_eval(game = "omaha", fill_pockets = 1, iterations = iterations_high, pockets = evalpockets, dead = [], board = ["__", "__", "__", "__", "__"])['eval'][0]['ev']

def evaluate(hand_to_evaluate):
    return pokereval.poker_eval(game = "holdem", fill_pockets = 1, iterations = iterations_high, pockets = hand_to_evaluate, dead = [], board = ["__", "__", "__", "__", "__"])['eval'][0]['ev']    

#print str(evalpockets[0]) + ", " + str(evaluate(evalpockets))

with open("holdem_hands_output.txt","ab") as out:
    with open("holdem_hands.txt") as holdem_hands:
        for line in holdem_hands:
            line = line.strip('\n').replace("'",'').replace(' ','')
            #print (line)
            line = line.replace(")",'').replace("(",'').split(",")
            #print line[0]
            #print (line[0][0])

            #print type(line)
            #print line
            #print line[0]
            

            #print line
            #newhand2 = line.split(",")
            #print newhand
            #print newhand2
            #newhand = ['2h','2d']
            #newhand2
            #print newhand   
            evalpockets = [line, emptyhand]
            print str(evalpockets[0]) + ", " + str(evaluate(evalpockets))
            out.write(str(evalpockets[0]) + ", " + str(evaluate(evalpockets)) + "\n")


"""
(AJ)(AJ)
(AT)(AT)
(AQ)(AQ)
(AJ)(AT)
write a converter from initial starting hands to pockets array
if grouped by parenthesis then convert to spades; if not then pull from the next available suit i.e. hearts then diamonds then clubs
"""
pokereval = None


"""
find a way to get an exhaustive list of all 52*51*50*49 omaha preflop hands
for each, calculate it's average winning percent on showdown against 1 random hand (take note of runtime and see what it takes to run against 2, 3 random)
after doing so, store each result and it's corresponding win %
for each hand, bring all possible flops; when the flop comes store the flop % and notice the change in equity from the long term 
did the flop make the hand value go up, down, or stay neutral?
is there a way to cluster the flops by +1%; +5%; +10% - i have am interested to see the distribution of flop textures against their long term associated equity
do the same on the turn; same on the river
do the same against the top 20% of hands; top 10% of hands; top 5% of hands

some technical thoughts:
- if i am having calculation issues ill have to set up the following system
- queue of all omaha hands that i want calculated
- that can be input to the emulator
- each instance that will run the emulator will need it's software installed first (that could be the hard part since this program depends on a C library...)


other future features:
- see your hand or opponents hand at showdown
- mobile app that indicates your opponent is playing x% of hands based on this hand strength
- let's say there are 5 hands you've seen him play - 1010J6 then he would play 99J7

- you can plug in your hand and see how favorable a flop that is for you in the long run
"""