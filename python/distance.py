def distance(lat1, lat2):
    """Returns approx miles between lat1 and lat2"""
    return 69 * abs(lat1 - lat2)

check = distance(32.769387, 96.645774)
print check
