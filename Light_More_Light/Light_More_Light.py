# Light, More Light
# Initially all bulbs are off. 
# if there are n bulbs in a corridor, he walks along the corridor back and forth n times.
# On the ith walk he toggles only the switches whose position is divisible by i.
# He does not press any switch when coming back to his initial position.
# Determine the final state of the last bulb in the corridor. Is it on or off?
import math as m

T = int(input())
for i in range(T):
    N = int(input())
    S = m.sqrt(N)
    print("no" if N==(S*S) else "yes")



