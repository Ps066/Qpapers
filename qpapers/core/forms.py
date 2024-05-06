from django import forms
from .models import *

# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Questions  # Link to the Song model
#         fields = ['questions', 'image', 'song_file', 'genre', 'language']  # Include all required fields
#         # You can customize widgets if needed
#         widgets = {
#             'genre': forms.Select(attrs={'class': 'form-control'}),  # Using dropdown
#             'language': forms.Select(attrs={'class': 'form-control'}),  # Using dropdown
#         }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['questions', 'course', 'subject', 'marks', 'rbt_level']
        
        # Custom widgets for the fields
        # widgets = {
        #     'questions': forms.Textarea(attrs={
        #         'placeholder': 'Start typing your question....',
        #         'rows': 5,
        #     }),
        #     'course': forms.Select(
        #         choices=[('', 'Please select a course')] + [(course.id, course.title) for course in Course.objects.all()],
        #         attrs={'class': 'nice-form-group'}
        #     ),
        #     'subject': forms.Select(
        #         choices=[('', 'Please select a subject')] + [(subject.id, subject.title) for subject in Subject.objects.all()],
        #         attrs={'class': 'nice-form-group'}
        #     ),
        #     'marks': forms.Select(
        #         choices=[('', 'Please select marks')] + [(mark.id, str(mark.marks) + " marks") for mark in Marks.objects.all()],
        #         attrs={'class': 'nice-form-group'}
        #     ),
        #     'rbt_level': forms.Select(
        #         choices=[('', 'Please select RBT level')] + [(rbt.id, rbt.rbt_level) for rbt in Rbt.objects.all()],
        #         attrs={'class': 'nice-form-group'}
        #     ),
        # }
        widgets = {
            'questions': forms.Textarea(attrs={
                'placeholder': 'Start typing your question....',
                'rows': 5,
            }),
            'course': forms.Select(attrs={
                'class': 'nice-form-group',
                'label': 'Course',
            }),
            'subject': forms.Select(attrs={
                'class': 'nice-form-group',
                'label': 'Subject code',
            }),
            'marks': forms.Select(attrs={
                'class': 'nice-form-group',
                'label': 'Marks',
            }),
            'rbt_level': forms.Select(attrs={
                'class': 'nice-form-group',
                'label': 'RBT level',
            }),
        }