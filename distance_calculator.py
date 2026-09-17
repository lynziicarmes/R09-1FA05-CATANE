import math

# Input the x- and y-coordinates of the two points
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the horizontal and vertical differences
x_difference = x2 - x1
y_difference = y2 - y1

# Calculate the distance using the distance formula
distance = math.sqrt(
    math.pow(x_difference, 2) + math.pow(y_difference, 2)
)

# Display the distance rounded to two decimal places
print("The distance between the two points is:", round(distance, 2))

# 1. What comments did you add, and why?
# - I added comments explaining the input, calculation of the coordinate differences, use of the distance formula, and the final output. These comments help explain what each main part of the program does.

# 2. What variable names or formatting did you improve?
# - I kept the coordinate variables `x1`, `y1`, `x2`, and `y2` because they clearly represent the coordinates. I improved the formatting by adding proper spaces around operators, organizing the distance calculation into multiple lines, and keeping the indentation consistent.

# 3. What did you include in your README.md file?
# - I included the project title, program description, instructions on how to run the program, the required inputs, sample output, and the author's name.

# 4. How did your changes make the program easier to understand?
# - The changes made the code more organized and readable. The comments explain the purpose of each section, while the improved spacing and formatting make the code easier to follow.

# 5. What is the link to your GitHub repository?
