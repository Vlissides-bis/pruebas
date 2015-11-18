from time import localtime

'''
List of activities to done along the day
'''
activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              19: 'Fucking',
              20: 'Drinking',
              22: 'Resting' }

time_now = localtime()
hour = time_now.tm_hour

def is_naughty(activity):
    if activity in ['Fucking', 'Drinking']:
	return True
    else:
        return False

'''
Find the current activity
'''
for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
        break
else:
    print 'Unknown, AFK or sleeping!'
