# What would the code in Figure 3.4 do if the statement x = 25
# were replaced by x = -25?

x = -25
epsilon = 0.01
num_guesses = 0
low = 0.0 # infinite loop because -25 is lower than lowest bound. will search forever
high = max(1.0, x)
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print('num_guesses =', num_guesses)
print(ans, 'is clsoe to square root of', x)