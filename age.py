
'''

#get age as input
age = int(input("Enter age: "))
#classify 
adj = "typical"
if age < 20:
    adj = "young"
elif age > 30:
    adj = "mature"

#output classification
print(f'At {age:d} you appear to be a {adj:s} college student')'''

#write modules
def get_integer_input(prompt):
    age = int(input(prompt))
    return age
def classify(param):
    adj = "typical"
    if param < 20:
        adj = "young"
    elif param > 30:
        adj = "mature"
    return adj
def describe_age(age, adjective):
#output classification
    print(f'At {age:d} you appear to be a {adjective:s} college student')
    
def main():
#get age as input
    age = get_integer_input("Enter age: ")
#classify
    adjective = classify(age)
    describe_age(age, adjective)
main()
 

