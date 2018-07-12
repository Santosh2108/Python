#A) finding area of the sphere

r = int(raw_input('Enter the radius of the sphere: ')) 
area=(4/3.0)*3.14*(r**3) 
print ('the area of the sphere is',area )

#B) Wholesale rate
coverprice=24.95 
discount=40/100.0 
shippingcost=3 
additional=0.75 
count=60 
discountprice=coverprice*discount 
totalprice=(coverprice-discountprice)*count 
total= totalprice+shippingcost+(count-1)*additional 
print ('price for 60 books',total )

#C) Time calculation
timeleft = 6 * 3600 + 52 *60 
easy = 2 * (8 * 60 + 15 ) 
fast = 3 * (7 * 60 + 12 ) 
totaltime = easy + fast + timeleft 
hours = totaltime/ 3600 
remainingseconds= totaltime % 3600 
minutes = remainingseconds /60 
seconds = remainingseconds % 60 
print ('Hours:',hours)
print ('minutes:', minutes)
print ('seconds:', seconds)
