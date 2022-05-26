# Q1 You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

the_little_mermaid = 3
brother_bear = 5
hercules = 1 
print(3*(the_little_mermaid + brother_bear + hercules))

# Q2 Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google = 400
amazon = 380
facebook = 350
print(google*6 + facebook*10 + amazon*4)

# Q3 A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

class_not_full = True
schedule_free = True
can_enroll = class_not_full and schedule_free
print(can_enroll)

# Q4 A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

premium_member = True
more_than_2_items = True
offer_still_valid = True

offer_applied = (premium_member or more_than_2_items) and offer_still_valid

print(offer_applied)

# Q5 Create a variable that holds a boolean value for each of the following conditions:
username = 'codeup'
password = 'notastrongpassword'

# the password must be at least 5 characters
if len(password) >= 5:
    print(True)
# the username must be no more than 20 characters
if len(username) > 20:
    print(True)
# the password must not be the same as the username
if username != password:
    print(True)
# bonus neither the username or password can start or end with whitespace
if username != " % " and password != " % ":
    print(True)