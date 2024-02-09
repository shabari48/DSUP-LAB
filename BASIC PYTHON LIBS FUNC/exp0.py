# Datatypes
print("DATATYPES")
print()
x=5
print(x,type(x))
print()

x='Hello'
print(x,type(x))
print()
x=40.6
print(x,type(x))
print()
x=1j+4
print(x,type(x))
print()
x=True
print(x,type(x))
print()
x=[1,'Hello World',44.6,1+2j] # List is ordered , changeable and indexed . Allows Duplicate 
print(x[2])
print(x,type(x))
print()

x=(1,'Hello World',44.6,1,1+2j) # Tuple is ordered , unchangeable and indexed . Allows Duplicate 
print(x,type(x))
print(x[2]) 
#x[2]=0 #Error occurs as Tuple is unchangeable
print()
x={1,2,1,33,44,2,67,877,332,44}  # Set is unordered , unchangeable and non-indexed . No Duplicate 
# print(x[2])  # Error occurs as Set is not indexed.
# x[2]=0       #Error occurs as Set is unchangeable
print(x,type(x))
print()
x={"Name":"Shabari","Age":"19","Place":"Svg"} # Dictionary is ordered and changeable. No duplicates allowed
print(x["Name"]) # Indexed using Key Values
x["Age"]="20"
print(x)
print()