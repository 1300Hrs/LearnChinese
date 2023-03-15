from django import forms
from .models import Question, Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['question_text'].widget.attrs['readonly'] = True


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']


class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)
        for question in questions:
            self.fields[question.question_text] = forms.ChoiceField(
                choices=[(choice.choice_text, choice.choice_text) for choice in question.choice_set.all()],
                widget=forms.RadioSelect, required=True)
            self.fields[question.question_text].question_id = question.id
            self.fields[question.question_text].widget.attrs.update({'class': 'form-check-input'})

            question_form = QuestionForm(instance=question)
            self.fields[question.question_text].label = question_form['question_text'].value()
            self.fields[question.question_text].label_suffix = ''
