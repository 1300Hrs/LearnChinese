from django.shortcuts import render
from dotenv import load_dotenv
import openai, os
from .models import Quiz
from .forms import QuizForm

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)


# Create your views here.
def home(request):
    quizes = Quiz.objects.all()
    context = {'quizes': quizes}
    return render(request, 'features/home.html', context)


def user_reviews(request):
    return render(request, 'features/user_reviews.html')


def quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.question_set.all()

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = 0
            for question in questions:
                answer = form.cleaned_data[question.question_text]
                if answer == question.correct_answer:
                    score += 1
            return render(request, 'features/result.html', {'score': score, 'total': len(questions)})
    else:
        form = QuizForm(questions=questions)

    return render(request, 'features/quiz.html', {'quiz': quiz, 'form': form})


def chatGPT_bot(request):
    chatbot_response = None
    if api_key is not None and request.method == "POST":
        openai.api_key = api_key
        user_input = request.POST.get('user_input')

        # Check the selected use case
        use_case = request.POST.get('selected_use_case')
        if use_case == 'translation':
            prompt = f"Translate these texts from English to Chinese: {user_input}"
        elif use_case == 'language_practice':
            prompt = f"Can i practice my chinese with you? : {user_input}"
        elif use_case == 'vocabulary_building':
            prompt = f"I want to learn 5 vocabularies today: {user_input}"
        elif use_case == 'cultural_learning':
            prompt = f"I want to learn about chinese culture: {user_input}"
        elif use_case == 'travel_planning':
            prompt = f"I am planning to travel to China: {user_input}"
        else:
            prompt = user_input

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            temperature=0.5
        )
        chatbot_response = response["choices"][0]["text"]

    context = {"response": chatbot_response}
    return render(request, 'features/general_chatGPT.html', context)


def translation_bot(request):
    chatbot_response = None
    if api_key is not None and request.method == "POST":
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        # prompt = user_input
        prompt = f"Translate these texts from English to Chinese: {user_input}"
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            stop='.',
            temperature=0.5
        )
        print(response)

        chatbot_response = response["choices"][0]["text"]

    context = {"response": chatbot_response}
    return render(request, 'features/chatGPT.html', context)





def about(request):
    return render(request, 'features/about.html')
