# import special libraries already built in python
import random, urllib2

# list of options to select from
the_url = 'https://raw.githubusercontent.com/BYUFootball/volcanion/62ee27e26791cb57b28e6cfb0727489c70d6c4a2/activities.fe'
list_raw_text = urllib2.urlopen(the_url).read()

print "DEBUG: " + str(list_raw_text.split())

possible_activities = list_raw_text.split()

# choice of what we are going to do
the_activity = random.choice(possible_activities)

# display the results to the end user
print "Possible activities are: " + str(possible_activities)
print "What we'll do today: " +  the_activity
# import special libraries already built in python







# choice of what we are going to do
the_other_activity = random.choice(possible_activities)
while the_activity != the_other_activity:
    print "Repicking"
    the_other_activity = random.choice(possible_activities)

# display the results to the end user
print "What we'll do today: " +  the_other_activity
