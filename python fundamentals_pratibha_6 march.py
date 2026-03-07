#task1
username = input("Enter Username: ")
password = input("Enter Password: ")

# Username validation
if len(username) < 5:
    print("Error: Username must be at least 5 characters long.")

# Password validation
elif len(password) < 8:
    print("Error: Password must be at least 8 characters long.")

elif not any(char.isupper() for char in password):
    print("Error: Password must contain at least 1 uppercase letter.")

elif not any(char.isdigit() for char in password):
    print("Error: Password must contain at least 1 number.")

else:
    print("Login details are valid.")

    #Task 2- Even and Odd Number Analyzer

    numbers = []

    # Accept 10 numbers from user
    for i in range(10):
        num = int(input("Enter number: "))
        numbers.append(num)

    even_numbers = []
    odd_numbers = []

    # Separate even and odd numbers
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
        else:
            odd_numbers.append(n)

    # Calculate sums
    sum_even = sum(even_numbers)
    sum_odd = sum(odd_numbers)

    # Output
    print("\nTotal numbers:", len(numbers))
    print("Even Numbers:", even_numbers)
    print("Odd Numbers:", odd_numbers)
    print("Sum Even:", sum_even)
    print("Sum Odd:", sum_odd)
#task 3
# Correct credentials
username = "admin"
password = "admin123"

attempts = 3   # total login attempts allowed

for i in range(attempts):
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == username and pwd == password:
        print("Login Successful")
        break
    else:
        print("Invalid credentials")

    # if last attempt failed
    if i == attempts - 1:
        print("Account Locked")

# Task 4 -Website Response Time Analyzer

response_times = [120, 200, 150, 90, 300, 250]

# Fastest response
fastest = min(response_times)

# Slowest response
slowest = max(response_times)

# Average response time
average = sum(response_times) / len(response_times)

# Find responses greater than 200ms
slow_responses = []

for time in response_times:
    if time > 200:
        slow_responses.append(time)

# Output
print("Fastest Response:", fastest)
print("Slowest Response:", slowest)
print("Average Response:", int(average))
print("Slow Responses:", slow_responses)
#task-5
users = ["admin", "qa", "dev", "admin", "tester", "qa"]

seen = set()
duplicates = set()

for user in users:
    if user in seen:
        duplicates.add(user)
    else:
        seen.add(user)

print("Duplicate Users:")
for user in duplicates:
    print(user)

def validate_email(email):
    if "@" in email and ".com" in email and " " not in email:
        print("Valid Email")
    else:
        print("Invalid Email")

# Input from user
email = input("Enter email: ")

validate_email(email)

# task 6-User database
users = {
    "admin": "admin123",
    "qa": "qa123",
    "tester": "test123"
}

# Ask for username
username = input("Enter username: ")

# Check if user exists
if username in users:
    password = input("Enter password: ")

    if users[username] == password:
        print("Login Successful")
    else:
        print("Invalid Credentials")
else:
    print("Invalid Credentials")
#task 7
logs = [
    "INFO: Login successful",
    "ERROR: Page not found",
    "INFO: User logout",
    "ERROR: Timeout",
    "INFO: Dashboard loaded"
]

total_logs = len(logs)
error_count = 0
error_messages = []

for log in logs:
    parts = log.split(": ")

    if parts[0] == "ERROR":
        error_count += 1
        error_messages.append(parts[1])

print("Total Logs:", total_logs)
print("Total Errors:", error_count)
print("Errors:")

for error in error_messages:
    print(error)

test_results = ["Pass","Fail","Pass","Pass","Fail","Pass"]

total_tests = len(test_results)
passed_tests = test_results.count("Pass")
failed_tests = test_results.count("Fail")

pass_percentage = (passed_tests / total_tests) * 100

print("Total:", total_tests)
print("Passed:", passed_tests)
print("Failed:", failed_tests)
print("Pass %:", int(pass_percentage), "%")
