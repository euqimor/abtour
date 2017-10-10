from django import forms
from .models import TouristRequest

class RequestForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-lg', 'id':'id_name', 'maxlength':'100', 'name':'name', 'placeholder':'Ваше имя', 'type':'text'}), label= 'Ваше имя', max_length=100)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control input-lg', 'id':'id_startdate', 'maxlength':'30', 'name':'name', 'placeholder':'С', 'type':'text'}), label='С', input_formats=['%d.%m.%Y'])
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control input-lg', 'id':'id_enddate', 'maxlength':'30', 'name':'name', 'placeholder':'По', 'type':'text'}),label='По', input_formats=['%d.%m.%Y'])
    num_adults = forms.IntegerField(label='Взрослых', widget=forms.NumberInput(attrs={'class':'form-persons form-control input-lg', 'id':'id_adults', 'name':'name', 'placeholder':'Взрослых'}), min_value=1, max_value=30)
    num_kids = forms.IntegerField(label='Детей', widget=forms.NumberInput(attrs={'class':'form-persons form-control input-lg', 'id':'id_kids', 'name':'name', 'placeholder':'Детей'}), min_value=1, max_value=30)
    where = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-lg', 'id':'id_where', 'maxlength':'100', 'name':'name', 'placeholder':'Куда', 'type':'text'}), label='Куда', max_length=100)
    budget = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-budget form-control input-lg', 'id':'id_budget', 'name':'name', 'placeholder':'Ваш бюджет'}),label='Ваш бюджет')
    currency = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-currency form-control input-lg', 'id':'id_currency'}), label='Валюта', choices=[('RUB', '₽'),('EUR', '€'), ('USD','$')])
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control input-lg', 'id':'id_comment', 'placeholder':'Комментарии и пожелания'}), label='Комментарии и пожелания', max_length=1000)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control input-lg', 'id':'id_email', 'placeholder':'address@yourmail.ru'}), label='Ваша почта')
    phone = forms.RegexField(widget=forms.TextInput(attrs={'class':'form-control input-lg', 'id':'id_phone', 'maxlength':'15', 'name':'name', 'placeholder':'89671234567', 'type':'text'}), label='Телефон (только цифры)', strip=True, regex=r'^(?:(?:\+?7)|8)?\d{9,15}$')
                                    # error_message=(
                                    # "Номер телефона должен быть введён без скобок, тире и пробелов. Допускается использование +7, например: '+74954151734', '84954151734' или '4954151734'. Максимальная длина 15 символов. Это не обязательное поле."))
    def save(self):
        obj = TouristRequest()
        obj.name = self.cleaned_data['name']
        obj.start_date = self.cleaned_data['start_date']
        obj.end_date = self.cleaned_data['end_date']
        obj.num_adults = self.cleaned_data['num_adults']
        obj.num_kids = self.cleaned_data['num_kids']
        obj.where = self.cleaned_data['where']
        obj.budget = self.cleaned_data['budget']
        obj.currency = self.cleaned_data['currency']
        obj.comment = self.cleaned_data['comment']
        obj.email = self.cleaned_data['email']
        obj.phone = self.cleaned_data['phone']
        obj.save()