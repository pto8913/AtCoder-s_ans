N = int(input())
M = int(input())
AB = [[int(i) for i in input().split()]for _ in range(M)]
AB.sort()
friends = set()
friendsOfFriends = set()
for a, b in AB:
  if a == 1:
    friends.add(b)
  elif a in friends:
    if b not in friends:
      friendsOfFriends.add(b)
  elif b in friends:
    if a not in friends:
      friendsOfFriends.add(a)
print(len(friends)+len(friendsOfFriends))