s = '1.23,2.4,3.123'
total = 0
s=s.split(',')
for i in s:
    total = total + float(i)
print total
