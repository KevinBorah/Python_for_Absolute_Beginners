# Exercises
# Now it's your turn. Try this practice below.

# The core idea in this chapter was about dictionaries and data structures in general. Create a simple program that creates a dictionary called d such that the following runs without error and prints what is expected:

# d = create d using core concepts above.

# print(d["Sam"])          # outputs 7
# print(d['rolls'])        # outputs ['rock', 'paper', 'scissors']
# print(d.get('Sarah'))    # outputs None
# print(d.get('Jeff', -1)) # outputs -1
# print(d['done'])         # outputs True

d = {
    "Sam": 7,
    'rolls': ['rock', 'paper', 'scissors'],
    'done': True
}
print(d['done'])

# <K2>
