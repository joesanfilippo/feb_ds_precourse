###############################################################################
############################ Study Hall #1  ###################################
###############################################################################

# Daily challenge

'''Problem of the day! Put your solutions in a thread - keep yourselves
honest by not looking at other’s solutions within the thread until
you’ve given it a go on your own. I’ll cover the solution right at the
beginning of today’s study hall. A family has two pets. We know all
of the pets are either a dog or a cat. If the family doesn’t have
a preference of one type of animal over the other (equal probability
of each pet being a dog/cat), and we know that the family has one at
least one cat; what is the probability that both pets are cats?
'''

# Event A = two cats
# Event B = at least one cat
#
# Conditional prob. formula: P(A | B) = P(AB) / P(B) = (1/4)/(3/4) = 1/3
#
# [CC, CD, DC, DD]
# P(AB) = 1/4
# P(B) = 3/4
#
# 1/3

### Conf. Intervals Challenges 2 & 3

# import scipy.stats as stats
# import numpy as np

# sample_stddev = 2.75 / np.sqrt(50)
# print(stats.t.interval(alpha=0.95, df=49, loc=39.9, scale=sample_stddev))

############################################################################

### Vectors - final challenge

# Imports
# from sklearn.datasets import load_iris
# import numpy as np

# # Read in data set
# iris_dataset = load_iris()
# iris_vectors = iris_dataset['data']

# # # Find the average iris
# avg_iris1 = iris_vectors.mean(axis=0)

# # import numpy as np
# # from sklearn.datasets import load_iris

# # iris_dataset = load_iris()
# # iris_vectors = iris_dataset['data']

# # Find the average iris:
# mean_0 = iris_vectors[:, 0].mean()
# mean_1 = iris_vectors[:, 1].mean()
# mean_2 = iris_vectors[:, 2].mean()
# mean_3 = iris_vectors[:, 3].mean()

# # save np array consisting of 4 means as avg_iris
# avg_iris = np.array([mean_0, mean_1, mean_2, mean_3])

# print(avg_iris.shape == avg_iris1.shape)

###############################################################################
############################      OOP       ###################################
###############################################################################

# from to_import import avg
# import random

# lst = [random.randint(0, 10) for _ in range(10)]

# print(avg(lst))

# class Wheelset:
#     def __init__(self, diameter, width, color, material, count):
#         self.diameter = diameter
#         self.width = width
#         self.color = color
#         self.material = material
#         self.count = count

# dope_wheels = Wheelset(17, 23, 'silver', 'aluminum', 4)
# lame_wheels = Wheelset(13, 9, 'black', 'steel', 4)

# class Car:
#     def __init__(self, name, wheelset, color, spoiler_color=None, location=[0, 0]):
#         self.name = name
#         self.wheelset = wheelset
#         self.color = color
#         self.location = location
#         self.spoiler_color = spoiler_color
#         self.oversized = False

#         if wheelset.count > 4:
#             self.oversized = True

#       def drive_north(self, distance)
#           self.location[0] += distance/10

class Person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

        if age >= 21:
            self.adult = True
        else:
            self.adult = False

lance = Person('Lance', 70, 38)
print(lance.adult)

# no_sp_car = Car('Pontiac', 'Red')
# sp_car = Car('Ferrari', dope_wheels, 'red', 'red', [110, 135])

# print(sp_car.location)
# sp_car.drive_north(10)
# print(sp_car.location)
