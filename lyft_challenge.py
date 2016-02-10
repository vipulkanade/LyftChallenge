# Lyft programming challenge solution
# By Vipul Kanade

import math

def findCircularDistance(pointA, pointB):

    # Convert the latitude and longitude values to radians
    latitude1 = math.radians(pointA[0])
    latitude2 = math.radians(pointB[0])
    longitude1 = math.radians(pointA[1])
    longitude2 = math.radians(pointB[1])
    deltaLat = latitude1 - latitude2
    deltaLong = longitude1 - longitude2

    # Use the distance formula to find the distance between the
    # two points (multiplying by mean Earth radius, in miles)
    angle = math.atan2(math.sqrt(math.pow((math.cos(latitude2) *
                                           math.sin(deltaLong)), 2) +
                                 math.pow((math.cos(latitude1) * math.sin(latitude2) -
                                           math.sin(latitude1) * math.cos(latitude2) *
                                           math.cos(deltaLong)), 2)),
                    (math.sin(latitude1) * math.sin(latitude2) + math.cos(latitude1) *
                     math.cos(latitude2) * math.cos(deltaLong)))

    return 3958.76 * angle

# Given two start and two end points and determine the shorter of two detour distances
def findDetourDistance(startA, endA, startB, endB):

    # Determine the two detour distances
    detourA = (findCircularDistance(startA, startB) + findCircularDistance(startB, endB) +
              findCircularDistance(endB, endA) - findCircularDistance(startA, endA))
    detourB = (findCircularDistance(startB, startA) + findCircularDistance(startA, endA) +
              findCircularDistance(endA, endB) - findCircularDistance(startB, endB))

    # Returning whichever detour is shorter
    if detourB >= detourA:
        return detourA
    else:
        return detourB
