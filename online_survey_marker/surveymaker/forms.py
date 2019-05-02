from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Survey Name', max_length=100)

class NumberForm(forms.Form):
    your_number = forms.IntegerField(label="How Many Choices Does Your New Question have",min_value=1,max_value=100)

class MCMakerForm(forms.Form):
    
    def __init__(self,num_of_choice, *args,**kwargs):
        super(MCMakerForm, self).__init__(*args, **kwargs)
        for idx in range(num_of_choice):
            self.fields['choice_'+str(idx)] = forms.CharField(label=str(idx+1)+' Choice ', max_length=100)

    question_text = forms.CharField(label='Your Question Text', max_length=100)
