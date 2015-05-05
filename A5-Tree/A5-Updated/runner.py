import turingmachine
import state
import View



print("****test 4****")
print(" ")
print(" ")


#An Attempt at creating a Turing Machine:
newTM = turingmachine.TuringMachine('01b','4','1011001101',[1,2,3,4,5],'b')
#       REQUIRED INPUT FOR A NEW TM
#            alphabet (str): The alphabet
#           initialstate (str): The name of the initial state
#            initialtape (str): The initial contents of the state
#            finalstates (List): A list of the names of the final states
#            blank (str): The blank symbol for this TM



# We create a Turing Machine Object here ---
tm = turingmachine.parseTuringMachine("test4-blank-in-middle.xml")
tm.runtohalt()

#testing that you can use the create a state object (from State class) by using Turing machine instead of importing State
WhatAState = turingmachine.State()
print 'this is a state here: %s\n\n' % WhatAState


testState = state.State()
secondTestState = state.State()

print "Adding a new state now..........."
print "with a transition to......"
secondTestState.add_transition('1','0','a','L')
# add a state to the turing machine that has already been parsed.
tm.addstate('Jackie Chan', secondTestState)



print "Adding another new state now"
# add a state to the turing machine that has already been parsed.
tm.addstate("Hey, I' a new state",testState)
print "The new state object is %s" % testState

print "\nThe new states associated with the turing machine are:"

for state in tm.states:
    print "\t" + state
    #not implemented yet, The state class dosent have a method that works in our case yet
#    for trans in state.get
#       print "\t\t" + trans


print "\n\nNow can you take this turing machine object (tm) and parse it in to a xml file??"


print "end"

View.ScreenApp().run()