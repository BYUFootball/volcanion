# import special libraries already built in python
import random

# list of options to select from
possible_activities = ['a', 'b', 'c']

# choice of what we are going to do
the_activity = random.choice(possible_activities)

# display the results to the end user
print "Possible activities are: " + str(possible_activities)
print "What we'll do today: " +  the_activity
