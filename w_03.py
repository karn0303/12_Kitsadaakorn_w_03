# BMI Calculator
# Result = W / {H^2 => h*h}

w = float (input("น้ำหนัก.(Kg.)"))
h = float (input("ส่วนสูง.(cm.)"))

r = w/((h/100)**2)

# r = w/((h/100)*(h/100))

print (r)

