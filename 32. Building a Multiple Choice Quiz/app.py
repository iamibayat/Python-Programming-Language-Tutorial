from question import Question

question_prompts = \
    [
        "What is the color of sky? \n\n(a) Yellow \n(b) Violet \n(c) Blue \n",
        "What is the color of water? \n\n(a) White \n(b) Colorless \n(c) Pink \n",
        "What is the color of Leaf? \n\n(a) Orange \n(b) Black \n(c) Green \n",
    ]

question_obj = \
    [
        Question(question_prompts[0], "c"),
        Question(question_prompts[1], "b"),
        Question(question_prompts[2], "c")
    ]


def run_test(question_obj):
    score = 0
    for question in question_obj:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(question_obj)) + " correct")


run_test(question_obj)
