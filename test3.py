def greet(friend, money):
   if friend:
      print "Hi!"
      money = money - 20
   return money

money = 15
money = greet(True, money)
print "Money:", money
print ""	
