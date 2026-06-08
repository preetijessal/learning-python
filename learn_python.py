#!/usr/bin/env python3
"""
Interactive Python Learning Program
Learn Python step-by-step with 6 comprehensive lessons, examples, and quizzes
"""

def lesson_1_basics():
    """Lesson 1: Python Basics & Variables"""
    print("\n" + "="*60)
    print("LESSON 1: PYTHON BASICS & VARIABLES")
    print("="*60)
    
    print("""
WHAT IS A VARIABLE?
A variable stores a value you can use later.

Examples:
    name = "Alice"          # String (text)
    age = 25                # Integer (whole number)
    height = 5.9            # Float (decimal)
    is_active = True        # Boolean (True/False)
    
NAMING RULES:
    • Start with letter or underscore
    • Use lowercase with underscores
    • Be descriptive (user_age, not x)
    • Avoid Python keywords
    """)
    
    print("\n--- PRACTICE ---")
    country = "Canada"
    population = 40000000
    print(f"Country: {country}, Population: {population}")
    
    return input_quiz("What data type is 3.14? (1:int, 2:float, 3:str): ", "2")


def lesson_2_strings():
    """Lesson 2: Strings & Text"""
    print("\n" + "="*60)
    print("LESSON 2: STRINGS & TEXT MANIPULATION")
    print("="*60)
    
    print("""
WORKING WITH TEXT:

Concatenation (combining):
    first = "John"
    last = "Doe"
    full_name = first + " " + last    # "John Doe"

Length and indexing:
    word = "Python"
    len(word)               # 6
    word[0]                 # "P" (first character)
    word[-1]                # "n" (last character)
    word[0:3]               # "Pyt" (slicing)

String methods:
    text = "hello"
    text.upper()            # "HELLO"
    text.capitalize()       # "Hello"
    text.replace("l", "L")  # "heLLo"
    """)
    
    print("\n--- PRACTICE ---")
    sentence = "Python is awesome"
    print(f"Text: {sentence}")
    print(f"Uppercase: {sentence.upper()}")
    print(f"First char: {sentence[0]}")
    print(f"First word: {sentence[0:6]}")
    
    return input_quiz("What does 'hello'[1:4] return? (1:h, 2:ell, 3:llo): ", "2")


def lesson_3_lists():
    """Lesson 3: Lists & Collections"""
    print("\n" + "="*60)
    print("LESSON 3: LISTS & COLLECTIONS")
    print("="*60)
    
    print("""
LISTS - STORING MULTIPLE VALUES:

Creating lists:
    fruits = ["apple", "banana", "orange"]
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]

Accessing elements (indexing):
    fruits[0]               # "apple"
    fruits[-1]              # "orange" (last item)

Common operations:
    len(fruits)             # 3 (length)
    fruits.append("grape")  # Add to end
    fruits.remove("banana") # Remove by value
    fruits.pop(0)           # Remove by index
    fruits.sort()           # Sort the list
    "apple" in fruits       # Check if exists (True/False)

Looping through a list:
    for fruit in fruits:
        print(fruit)
    """)
    
    print("\n--- PRACTICE ---")
    colors = ["red", "green", "blue"]
    print(f"List: {colors}")
    colors.append("yellow")
    print(f"After append: {colors}")
    colors.remove("green")
    print(f"After remove: {colors}")
    
    return input_quiz("What does lst.pop(0) do? (1:remove at 0, 2:remove value 0, 3:return 0): ", "1")


def lesson_4_conditionals():
    """Lesson 4: If/Else Statements"""
    print("\n" + "="*60)
    print("LESSON 4: CONDITIONAL STATEMENTS (IF/ELSE)")
    print("="*60)
    
    print("""
MAKING DECISIONS:

IF statement:
    age = 18
    if age >= 18:
        print("You are an adult")

IF/ELSE:
    age = 15
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")

IF/ELIF/ELSE (multiple choices):
    score = 75
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    else:
        print("Grade: C")

COMPARISON OPERATORS:
    ==  Equal to            >=  Greater or equal
    !=  Not equal           <=  Less or equal
    >   Greater than        <   Less than

LOGICAL OPERATORS:
    and    Both True        or     At least one True
    not    Reverses result
    """)
    
    print("\n--- PRACTICE ---")
    temperature = 25
    if temperature > 30:
        result = "It's hot!"
    elif temperature > 20:
        result = "It's warm"
    else:
        result = "It's cool"
    print(f"Temperature: {temperature}°C → {result}")
    
    return input_quiz("What prints for x=10? if x>5 and x<15: print('yes') (1:yes, 2:no, 3:nothing): ", "1")


def lesson_5_loops():
    """Lesson 5: For and While Loops"""
    print("\n" + "="*60)
    print("LESSON 5: LOOPS (FOR & WHILE)")
    print("="*60)
    
    print("""
REPEATING CODE:

FOR LOOP (repeat a set number of times):
    for i in range(5):
        print(i)           # Prints 0, 1, 2, 3, 4
    
    for fruit in ["apple", "banana", "orange"]:
        print(fruit)       # Prints each fruit

WHILE LOOP (repeat while condition is True):
    count = 0
    while count < 5:
        print(count)
        count += 1         # Increment

RANGE FUNCTION:
    range(5)           # 0, 1, 2, 3, 4
    range(1, 6)        # 1, 2, 3, 4, 5
    range(0, 10, 2)    # 0, 2, 4, 6, 8 (step by 2)

LOOP CONTROL:
    break              # Exit the loop
    continue           # Skip to next iteration
    """)
    
    print("\n--- PRACTICE ---")
    print("FOR loop - Counting:")
    for i in range(1, 4):
        print(f"  Number: {i}")
    
    print("FOR loop - Through list:")
    animals = ["cat", "dog", "bird"]
    for animal in animals:
        print(f"  {animal}")
    
    print("WHILE loop - Countdown:")
    count = 3
    while count > 0:
        print(f"  {count}...")
        count -= 1
    
    return input_quiz("What does range(3) give? (1:1,2,3  2:0,1,2  3:0,1,2,3): ", "2")


def lesson_6_functions():
    """Lesson 6: Functions"""
    print("\n" + "="*60)
    print("LESSON 6: FUNCTIONS - REUSABLE CODE")
    print("="*60)
    
    print("""
WHAT ARE FUNCTIONS?
Functions are reusable blocks of code that do a task.

BASIC FUNCTION:
    def greet():
        print("Hello!")
    
    greet()            # Call the function

FUNCTION WITH PARAMETERS:
    def greet(name):
        print(f"Hello, {name}!")
    
    greet("Alice")     # Output: Hello, Alice!

FUNCTION WITH RETURN VALUE:
    def add(a, b):
        return a + b
    
    result = add(5, 3)
    print(result)      # 8

MULTIPLE PARAMETERS:
    def describe(name, age):
        return f"{name} is {age} years old"
    
    print(describe("Alice", 25))

DEFAULT PARAMETERS:
    def greet(name="Friend"):
        print(f"Hello, {name}!")
    
    greet()            # Hello, Friend!
    greet("Bob")       # Hello, Bob!
    """)
    
    print("\n--- PRACTICE ---")
    def square(n):
        """Returns n squared"""
        return n * n
    
    def multiply(a, b):
        """Multiplies two numbers"""
        return a * b
    
    print(f"Square of 5: {square(5)}")
    print(f"5 × 3 = {multiply(5, 3)}")
    
    def welcome(name, city="Toronto"):
        return f"Welcome {name} from {city}!"
    
    print(welcome("Alice"))
    print(welcome("Bob", "Vancouver"))
    
    return input_quiz("What does return do in a function? (1:exits, 2:sends value back, 3:prints): ", "2")


def input_quiz(question, correct_answer):
    """Display quiz question and check answer"""
    answer = input(f"\n{question} ").strip()
    if answer == correct_answer:
        print("✅ Correct!")
        return 1
    else:
        print(f"❌ Incorrect. The correct answer is {correct_answer}")
        return 0


def display_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("PYTHON LEARNING PROGRAM")
    print("="*60)
    print("""
Choose a lesson to start:
    1) Basics & Variables
    2) Strings & Text
    3) Lists & Collections
    4) Conditionals (If/Else)
    5) Loops (For/While)
    6) Functions
    7) Run all lessons
    0) Exit
    """)


def main():
    """Main program"""
    scores = {}
    lessons = [
        ("Basics & Variables", lesson_1_basics),
        ("Strings & Text", lesson_2_strings),
        ("Lists & Collections", lesson_3_lists),
        ("Conditionals", lesson_4_conditionals),
        ("Loops", lesson_5_loops),
        ("Functions", lesson_6_functions),
    ]
    
    print("\n" + "🐍 "*10)
    print("Welcome to the Python Learning Program!".center(60))
    print("🐍 "*10)
    
    while True:
        display_menu()
        choice = input("Enter your choice (0-7): ").strip()
        
        if choice == "0":
            print("\nThank you for learning Python! Keep practicing! 👋\n")
            break
        elif choice in ["1", "2", "3", "4", "5", "6"]:
            idx = int(choice) - 1
            lesson_name, lesson_func = lessons[idx]
            score = lesson_func()
            scores[lesson_name] = score
            print(f"\n✓ Lesson complete! Score: {score}/1")
        elif choice == "7":
            print("\n⏳ Running all lessons...\n")
            for lesson_name, lesson_func in lessons:
                score = lesson_func()
                scores[lesson_name] = score
            print("\n" + "="*60)
            print("FINAL RESULTS")
            print("="*60)
            total = sum(scores.values())
            max_score = len(scores)
            for lesson, score in scores.items():
                print(f"  {lesson}: {score}/1")
            print(f"\nTotal Score: {total}/{max_score}")
            percentage = (total / max_score * 100) if max_score > 0 else 0
            print(f"Percentage: {percentage:.1f}%")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
