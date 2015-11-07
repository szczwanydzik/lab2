'''
Created on 5 lis 2015

@author: Prezes
'''

#  Wzorowane na przykładzie Rona Zacharskiego
from math import sqrt

users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

def manhattan(rating1, rating2):
    person1 = rating1.keys()
    person2 = rating2.keys()
    distance = 0
    comparison = False
    
    for key in person1:
        if key in rating2.keys():
            comparison = True
            distance = distance + abs(rating2[key] - rating1[key])
            
        if comparison:
            return distance
        else:
            return -1
def testManhattan(rating1,rating2,distance):
    if manhattan(rating1, rating2) == distance:
        return True
    else:
        return False
    
    
    pass

                
def computeNearestNeighbor(username, users):
    nameOfNearestNeighbor = ""
    distances = []
    
    for name2 in users:
        distance = 0
        if username!=name2:
            distance - manhattan(users[username], users[username])
            distances.append((distance, name2))
            
    return sorted(distances)
    return nameOfNearestNeighbor

def recommend(username, users):
    nearestName = computeNearestNeighbor(username, users)[0][1]
    print username
    print 'Najbliższy sąsiad to: %s' %nearestName
    recommendations = []
    ratingOfNearest = users[nearestName]
    print('Jego rekomendacje to: ')
    print(ratingOfNearest)
    
    userRating = users[username]
    
    for artist in ratingOfNearest:
        if not artist in userRating:
            recommendations.append((artist, ratingOfNearest[artist]))
    
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

#examples

print( recommend('Gosia', users))

