import turingmachine
import state
TESTDIR="/home/xubuntu/gdrive/teaching/2015/FIT3140/sample_code/turing_machine_simulator/"


print("****test 4****")
print(" ")
print(" ")


# We create a Turing Machine Object here ---
tm = turingmachine.parseTuringMachine("test4-blank-in-middle.xml")
tm.runtohalt()


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


# for state in states:
#         statename = state.attrib['name']
#         stateobj = State()
#         transitions = state.findall("transition")
#         for transition in transitions:
#             stateobj.add_transition(transition.attrib['seensym'],
#                                     transition.attrib['writesym'],
#                                     transition.attrib['newstate'],
#                                     transition.attrib['move'])
#         tmobj.addstate(statename, stateobj)



for state in tm.states:
    print "--------------For\t" + state + " is -->"
    # print tm.states.get(state).get_all_transition()

    # print "val " + str(tm.states.get(state).get_all_transition().values())

    # for x in tm.states.get(state).get_all_transition().values():
    #     print "is this the transition object?" + str(x)



    for x in tm.states.get(state).get_all_transition():
        print "\t\t: " + x
        print "\t------\t"
        print tm.states.get(state).get_all_transition()[x].get_next_state()
        print tm.states.get(state).get_all_transition()[x].get_next_direction()
        print tm.states.get(state).get_all_transition()[x].get_write_sym()
        print tm.states.get(state).get_all_transition()[x].get_seen_sym()





    #not implemented yet, The state class dosent have a method that works in our case yet
#    for trans in state.get
#       print "\t\t" + trans


print "\n\nNow can you take this turing machine object (tm) and parse it in to a xml file??"


print "end"