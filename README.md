# QCPC-24
General overview and approaches we took while participating in the Qatar Collegiate Programming Contest (Silver medalists)

Hey everyone! My name is Rayan and I was part of the team 'The Two Indents', and we got second place in the highschool section of the QCPC out of 70+ teams! I just wanted a neat place to put up the questions for future participants (cause I myself struggled to find any to practice with). So here we go!


## Problem I

You are driving a car on a long straight road. Initially, the car's speed is 0 meters per second. You will drive for exactly S seconds.

During the drive, there are N distinct moments when the speed of the car increases. For each second from 1 to S, the car maintains a constant speed, but at specific second m_i in time, the speed increases by some value c_i. 

Your task is to compute the total distance travelled by the car after S seconds.

### Input

The first line contains two integers: S(1 <= S <= 10^9) and N(1 <= N <= 100) - the total duration of the drive in seconds and the number of speed increase moments.
The next N lines each contain two integers: m_i (1 <= m_i <= S) and c_i (1 <= c_i <= 1000) - the second when a speed increase happens and the amount by which the speed increases at that moment.

### Output

Print a single integer - the total distance (in meters) the car travels after driving for S seconds.

