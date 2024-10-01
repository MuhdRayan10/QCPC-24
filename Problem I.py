# Problem I - Gold Balloon - Drive the car

from sys import stdin, stdout

s, n = tuple(map(int, stdin.readline().split()))

# Storing all change moments in the format (m_i, c_i)
changes = [tuple(map(int, stdin.readline().split())) for _ in range(n)] + [(s+1, 0)]

current = (0, 0)
speed = 0
distance = 0


# Sort list in terms of time of increment (m_i) 
# Sorting in descending order to pop easily
changes.sort(reverse=True, key=lambda x:x[0])

for _ in range(n+1):
  new_change = changes.pop()

  time_diff = new_change[0] - current[0] # Constant speed during this time interval

  distance += time_diff * speed
  speed += new_change[1]

  current = new_change
  
stdout.write(str(distance))



