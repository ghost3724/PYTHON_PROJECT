
# Quiz na badha questions, options ane correct answers store kariye chhiye
questions = [
    {
        "question": "1. Sun upar kon gayu che?",
        "options": [
            "A. Sukra charya",
            "B. A.P.J. Kalam",
            "C. Sunita Williams",
            "D. Koi nahi"
        ],
        "answer": "D"  # Aa question no correct answer D che
    },
    {
        "question": "2. Bharat no National Animal kon che?",
        "options": [
            "A. Hathi",
            "B. Sher",
            "C. Tiger",
            "D. Lion"
        ],
        "answer": "C"
    },
    {
        "question": "3. Pehlo grah kayo che?",
        "options": [
            "A. Budh",
            "B. Mangal",
            "C. Sukra",
            "D. Shani"
        ],
        "answer": "A"
    },
    {
        "question": "4. Bharat na vartaman Rashtrapati kon che?",
        "options": [
            "A. Dr. A.P.J. Abdul Kalam",
            "B. Pandit Jawaharlal Nehru",
            "C. Droupadi Murmu",
            "D. Sardar Patel"
        ],
        "answer": "C"
    },
    {
        "question": "5. Human body ma ketli bones hoy che?",
        "options": [
            "A. 201",
            "B. 206",
            "C. 208",
            "D. 210"
        ],
        "answer": "B"
    },
    {
        "question": "6. Bharat ni rajdhani kai che?",
        "options": [
            "A. Mumbai",
            "B. New Delhi",
            "C. Kolkata",
            "D. Chennai"
        ],
        "answer": "B"
    },
    {
        "question": "7. Computer nu brain shu che?",
        "options": [
            "A. RAM",
            "B. Hard Disk",
            "C. CPU",
            "D. Monitor"
        ],
        "answer": "C"
    },
    {
        "question": "8. Bharat ne aazadi kyare mali hati?",
        "options": [
            "A. 26 January 1950",
            "B. 15 August 1947",
            "C. 2 October 1869",
            "D. 15 August 1950"
        ],
        "answer": "B"
    },
    {
        "question": "9. Bharat ni aazadi ni ladai ma pramukh neta kon hata?",
        "options": [
            "A. Rudra",
            "B. Mahatma Gandhi",
            "C. Mayur",
            "D. Rahuk"
        ],
        "answer": "B"
    },
    {
        "question": "10. Men's ODI Cricket World Cup sauthi vadhu vaar kone jityo che?",
        "options": [
            "A. India",
            "B. Australia",
            "C. West Indies",
            "D. England"
        ],
        "answer": "B"
    },
    {
        "question": "11. Taj Mahal Bharat ma kya aavelu che?",
        "options": [
            "A. Delhi",
            "B. Jaipur",
            "C. Agra",
            "D. Lucknow"
        ],
        "answer": "C"
    }
]


# Quiz chalava mate function banaviye chhiye
def run_quiz():

    score = 0  # Starting score 0 rakhyo che

    total = len(questions)  # Total questions ni sankhya count kare che

    # Quiz nu welcome message print kare che
    print("\n" + "=" * 45)
    print("       WELCOME TO PYTHON QUIZ APP")
    print("=" * 45)

    # Darek question ne ek-ek kari ne access kare che
    for i, item in enumerate(questions):

        # Current question screen par batave che
        print(f"\n{item['question']}")

        # Current question na badha options print kare che
        for option in item["options"]:
            print(f"  {option}")

        # User pase thi sacho option letter le che
        while True:

            user_ans = input(
                "\nTamaro answer chuno (A/B/C/D): "
            ).strip().upper()

            # Check kare che ke user e valid option lakhyo che ke nahi
            if user_ans in ["A", "B", "C", "D"]:
                break  # Valid answer hoy to loop mathi bahar nikle che

            # Invalid answer hoy to aa message batave che
            print("Invalid input! Please A, B, C athva D lakho.")

        # User no answer correct answer sathe compare kare che
        if user_ans == item["answer"]:

            print("Sacho jawab! Well done!")

            score += 1  # Correct answer mate score ma 1 add kare che

        else:

            # Khoto jawab hoy to options mathi aakho sacho option shodhe che
            correct_answer = next(
                option
                for option in item["options"]
                if option.startswith(item["answer"] + ".")
            )

            # Khoto jawab hovani information batave che
            print("Khoto jawab!")

            # Correct option letter sathe aakho jawab batave che
            print(f"Sacho jawab: {correct_answer}")

        # Last question na hoy tyare next question mate wait kare che
        if i < total - 1:

            input("\nBijo question jovva Enter dabavo...")

            # Questions vachche separator print kare che
            print("-" * 45)

    # Badha questions pura thay pachi percentage calculate kare che
    percentage = (score / total) * 100

    # Final result ni heading print kare che
    print("\n" + "*" * 45)
    print("              QUIZ NU RESULT")
    print("*" * 45)

    # Total questions, correct ane wrong answers batave che
    print(f"Total Questions : {total}")
    print(f"Correct Answers : {score}")
    print(f"Wrong Answers   : {total - score}")

    # User no final score batave che
    print(f"Total Score     : {score}/{total}")

    # Percentage decimal pachhi ek digit sathe batave che
    print(f"Percentage      : {percentage:.1f}%")

    # Percentage pramane feedback aape che
    if percentage >= 80:
        print("Feedback: Excellent! Tame quiz ma saras score karyo!")

    elif percentage >= 50:
        print("Feedback: Good try! Haju practice karo.")

    else:
        print("Feedback: Koi vaat nahi! Farithi try karo.")

    # Quiz no ending message print kare che
    print("*" * 45)
    print("Quiz ramva badal aabhar!")


# Aa file direct run thay tyare quiz start kare che
if __name__ == "__main__":
    run_quiz()
