import random
used_pairs = set()
# Define dictionary of country-capitals pairs
capitalsEasy = {
    "France": "Paris",
    "Russia": "Moscow",
    "Japan": "Tokyo",
    "USA": "New York",
    "Spain": "Madrid",
    "Greece": "Athens",
    "Bulgaria": "Sofia",
    "England": "London",
    "Afghanistan": "Kabul",
    "Austria": "Vienna",
    "Germany": "Berlin",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "China": "Beijing",
    "Chile": "Santiago",
    "Colombia": "Bogota",
    "Cuba": "Havana",
    "Croatia": "Zagreb",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Egypt": "Cairo",
    "Finland": "Helsinki",
    "Hungary": "Budapest",
    "India": "New Delhi",
    "Ireland": "Dublin",
    "Israel": "Jerusalem",
    "Italy": "Rome",
    "Argentina": "Buenos Aires"
}

capitalsHard = {
    "Angola": "Luanda",
    "Antigua and Barbuda": "Saint John's",
    "Armenia": "Yerevan",
    "Azerbaijan": "Baku",
    "Bahamas": "Nasau",
    "Bahrain": "Manama",
    "Bagladesh": "Dhaka",
    "Barbados": "Bridgetown",
    "Belize": "Belmopan",
    "Benin": "Porto Novo",
    "Bhutan": "Thimphu",
    "Botswana": "Gaborone",
    "Brunei": "Bandar Seri Begawan",
    "Burkina Faso": "Ouagadougou",
    "Burundi": "Gitega",
    "Cabo Verde": "Praia",
    "Cambodia": "Phnom Penh",
    "Cameroon": "Yaounde",
    "Canada": "Ottawa",
    "Central African Republic": "Bangui",
    "Chad": "N'Djamena",
    "Comoros": "Moroni",
    "Congo": "Brazzaville",
    "Costa Rica": "San Jose",
    "Cote d'Ivoire": "Yamoussoukro",
    "Dominica": "Roseau",
    "Dominican Republic": "Santo Domingo",
    "Ecuador": "Quito",
    "El Salvador": "San Salvador",
    "Equatorial Guinea": "Malabo",
    "Eritrea": "Asmara",
}

# Function to generate a random question
def generate_question(difficulty):
    global used_pairs
    capitals = capitalsEasy if difficulty == "easy" else capitalsHard
    while True:
        country = random.choice(list(capitals.keys()))
        correct_answer = capitals[country]
        pair = (country, correct_answer)
        if pair not in used_pairs:
            used_pairs.add(pair)
            break

    # Generate wrong answers excluding the correct answer
    wrong_answers = random.sample([value for key, value in capitals.items() if value != correct_answer], 3)

    # Shuffle options
    options = [correct_answer] + wrong_answers
    random.shuffle(options)

    return country, options, correct_answer


# Function to display a question and get user's answer
def ask_question(country, options):
    print(f"What is the capital of {country}?")
    print(f"1. {options[0]}")
    print(f"2. {options[1]}")
    print(f"3. {options[2]}")
    print(f"4. {options[3]}")
    while True:
        try:
            answer = input("Your answer (enter the capital): ").capitalize()
            if answer in options:
                break
            elif answer == "Break":
                quit()
            else:
                print("Invalid input.")
        except ValueError:
            print("Invalid input.")
    return answer

# Function to check if the answer is correct
def check_answer(answer, correct_answer):
    if answer == correct_answer:
        print("\nCorrect!\n")
        return True
    else:
        print("\nIncorrect!\n")
        return False

# Ask User if he wants Easy or Hard mode
def check_difficulty():
    while True:
        difficulty = input("Chose Difficulty (Easy / Hard): ").lower()
        if difficulty == "easy" or difficulty == "hard":
            break
        else:
            print("Invalid Input")
    return difficulty


# Main quiz loop
def quiz():
    global used_pairs
    score = 0
    difficulty = check_difficulty()
    used_pairs.clear()
    while True:
        country, options, correct_answer = generate_question(difficulty)
        answer = ask_question(country, options)
        if check_answer(answer, correct_answer):
            score += 1
        else:
            print("Game Over!")
            print(f"Score: {score}")
            break

# Start the quiz
if __name__ == "__main__":
    quiz()
