import re

def check_password_complexity(password):
    # Define the complexity criteria
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Check if all criteria are met
    if all([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_criteria]):
        return True
    else:
        return False

def get_password_feedback(password):
    feedback = []
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    if re.search(r'[a-z]', password) is None:
        feedback.append("Password should include at least one lowercase letter.")
    if re.search(r'[A-Z]', password) is None:
        feedback.append("Password should include at least one uppercase letter.")
    if re.search(r'\d', password) is None:
        feedback.append("Password should include at least one digit.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is None:
        feedback.append("Password should include at least one special character.")
    
    return feedback

def main():
    password = input("Enter your password: ")
    if check_password_complexity(password):
        print("Password is complex.")
    else:
        print("Password is not complex enough.")
        feedback = get_password_feedback(password)
        for item in feedback:
            print(item)

if __name__ == "__main__":
    main()
