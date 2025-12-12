marks = []
print("Enter your marks(Type 'done' to stop)")

def calculate_percentage(*marks):
    if len(marks) == 0:
        return 0
    
    total = sum(marks)
    percentage = total/((len(marks)*100)*100)
    return percentage

while True:
    value = input()
    if value.lower() == 'done':
        break
    marks.append(float(value))

p = calculate_percentage(*marks)
print("Percentage:",p)
