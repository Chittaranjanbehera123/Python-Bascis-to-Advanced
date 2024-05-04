# Example: Display Grade of the Student as per the Percentage entered by student.
per = float(input("Enter your Percentage:"))
if per>=90:
    print("Distinction: A+")
else:
    if per>=80:
        print(" Higher Fisrt class: A")
    else:
        if per>=75:
            print("First class: B+")
        else:
            if per>=60:
                print("First class: B")
            else:
                if per>=50:
                    print("Second class: C")
                else:
                    if per>=40:
                        print("Passed class: D")
                    else:
                        print("Sorry failed")

per = int(input("Enter Percentage: "))
if per>=90:
    print("A+ Garde")
elif (per<90 and per>60):
    print("A Garde")
elif (per<60 and per>=35):
    print("B grade")
elif (per<50 and per>=35):
    print("C Grade")
else:
    print("F")


# Example2:
# Leap Year:
# The normally year 365 years
n = int(input("Enter your leap year:"))

if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print(n, "is a leap year")
        else:
            print(n, "is not a leap year")
    else:
        print(n, "is a leap year")
else:
    print(n, "is not a leap year")


# Example3:
# Print all Trigonmetric ratios of angle 
import math

def print_trigonometric_ratios(angle_degrees):
    # Convert angle to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate trigonometric ratios
    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)
    tan_value = math.tan(angle_radians)
    csc_value = 1 / sin_value
    sec_value = 1 / cos_value
    cot_value = 1 / tan_value

    # Print the results
    print(f"Sine ({angle_degrees} degrees): {sin_value}")
    print(f"Cosine ({angle_degrees} degrees): {cos_value}")
    print(f"Tangent ({angle_degrees} degrees): {tan_value}")
    print(f"Cosecant ({angle_degrees} degrees): {csc_value}")
    print(f"Secant ({angle_degrees} degrees): {sec_value}")
    print(f"Cotangent ({angle_degrees} degrees): {cot_value}")

# Example: Print trigonometric ratios for an angle of 30 degrees
print_trigonometric_ratios(30)
    

