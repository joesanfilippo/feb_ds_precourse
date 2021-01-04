###############################################################################
########################### Problem of the day ################################
###############################################################################

# Big O - bubble sort
# (n-2)*(n-1) = O(n^2)

# O(n * log(n)): Merge Sort, Quick Sort, Timp Sort

# def bubble_sort(arr):
#     if not len(arr) > 1:
#         return arr

#     temp = float()

#     for idx in range(len(arr) - 1):
#         for i in range(len(arr)-1):
#             if arr[i] > arr[i + 1]:
#                 temp = arr[i]
#                 arr[i] = arr[i + 1]
#                 arr[i + 1] = temp
#             else:
#                 pass

#     return arr

# lst = [1, 6, 8, 10, 4, 12, 17, 2, 4]

# print(bubble_sort(lst))

###############################################################################
########################### OOP ###############################################
###############################################################################

# Define a class Card, with an __init__ method that instantiates the object with
#  two attributes, suit, and rank.

# class Card():
#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank

# Building on your previous class declaration, now you need to assign the attribute
# points based on the rank. The rank will always be between 1 and 13, with 11, 12,
# and 13 representing Jack, Queen and King, respectively - all worth 10 points.
# Aces have rank = 1 and are worth 11 points.

# class Card():
#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank

#         if rank >= 10:
#             self.points = 10
#         elif rank == 1:
#             self.points = 11
#         else:
#             self.points = rank

# my_card = Card('hearts', 9)
# my_card.suit = 'clubs'
# print(my_card.suit)

# class GalvanizeCourse:

#     # Define constructor
#     def __init__(self, name, location, size=0):
#         self.name = name
#         self.location = location
#         self.size = size
#         self.questions_asked = []

#     def __len__(self):
#         return(self.size)

#     def __gt__(self, other):
#         return self.size > other.size

#     def __eq__(self, other):
#         if self.name == other.name and \
#            self.location == other.location and \
#            self.size == other.size and \
#            self.questions_asked == other.questions_asked:
#             return True
#         else:
#             return False

#     # Define methods
#     def add_question(self, question):
#         self.questions_asked.append(question)

#     def add_students(self, num):
#         self.size += num

#         # If the class is 20 or larger, print and update boolean
#         if self.size >= 20:
#             print('Capacity Reached!!')
#             self.at_capacity = True

#     def check_if_at_capacity(self):
#         return self.at_capacity

# our_course = GalvanizeCourse('Intro Python', 'Boulder', 15)
# our_course1 = GalvanizeCourse('Intro Python', 'Boulder', 12)
# our_course.add_students(3)

# print(our_course == our_course)

# class Card():
#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank

#         if rank >= 10:
#             self.points = 10
#         elif rank == 1:
#             self.points = 11
#         else:
#             self.points = rank

# Building on your previous class declaration, the last thing you're going
# to do is to define a __repr__() method, which controls how your class will
# be displayed as a string (str).

# hearts_9 = Card('hearts', 9)
# clubs_king = Card('clubs', 13)
# spades_ace = Card('spades', 1)

# print(hearts_9) # Prints "9 of hearts"
# print(clubs_king) # Prints "King of clubs"
# print(spades_ace) # Prints "Ace of spades"

# class Card():
#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank

#         if rank >= 10:
#             self.points = 10
#         elif rank == 1:
#             self.points = 11
#         else:
#             self.points = rank

#     def __repr__(self):
#         d = {11: 'Jack', 12: 'Queen', 13: 'King', 1: 'Ace'}

#         if self.rank > 10 or self.rank == 1:
#             return f'{d[self.rank]} of {self.suit}'

#         return f'{self.rank} of {self.suit}'

# hearts_9 = Card('hearts', 1)

# card_str = str(hearts_9)

# print(card_str)

# your code here

class Deck:
    def __init__(self, shuffled=False):
        self.stack = []
        self.shuffled = shuffled
