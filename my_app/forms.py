from django import forms
from my_app.models import Contact,Checkout,Comment,SignUp

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'mesage','subject')

    def __init__(self, *args, **kwargs):
        super(ContactForm , self).__init__(*args, **kwargs)
        for field in self.fields:

            self.fields[field].widget.attrs.update({'class':'form-control'})
            self.fields[field].required = True

            self.fields['name'].widget.attrs.update({'placeholder':'adiniz'})
            self.fields['name'].label='adiniz'
            self.fields['email'].widget.attrs.update({'placeholder':'E-mailiniz'})
            self.fields['subject'].widget.attrs.update({'placeholder':'metn'})
            self.fields['mesage'].widget.attrs.update({'placeholder':'mesajlariniz','class':'message-box form-control','style':'height:300px'})
            self.fields['mesage'].label='mesaj'


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ('name', 'surname', 'email', 'phone','adress1','adress2','country','city','state','zipcode')

    def __init__(self, *args, **kwargs):
        super(CheckoutForm , self).__init__(*args, **kwargs)
        for field in self.fields:

            self.fields[field].widget.attrs.update({'class':'form-control'})
            self.fields[field].required = True

            self.fields['name'].widget.attrs.update({'placeholder':'adiniz'})
            self.fields['name'].label='adiniz'
            self.fields['surname'].widget.attrs.update({'placeholder':'soyadiniz'})
            self.fields['surname'].label='soyad'
            self.fields['email'].widget.attrs.update({'placeholder':'E-mailiniz'})
            self.fields['phone'].widget.attrs.update({'placeholder':'telefon'})
            self.fields['phone'].label='telefon'
            self.fields['adress1'].widget.attrs.update({'placeholder':'adress 1'})
            self.fields['adress1'].label='adress1'
            self.fields['adress2'].widget.attrs.update({'placeholder':'adress 2'})
            self.fields['adress2'].label='adress2'
            self.fields['country'].widget.attrs.update({'placeholder':'country'})
            self.fields['country'].label='country'
            self.fields['city'].widget.attrs.update({'placeholder':'sheher'})
            self.fields['city'].label='sheher'
            self.fields['state'].widget.attrs.update({'placeholder':'state'})
            self.fields['state'].label='state'
            self.fields['zipcode'].widget.attrs.update({'placeholder':'zipcode'})
            self.fields['zipcode'].label='zipcode'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text','user','products')

    def __init__(self, *args, **kwargs):
        super(CommentForm , self).__init__(*args, **kwargs)
        for field in self.fields:
         self.fields['text'].widget.attrs.update({'placeholder':'text'})
         self.fields['text'].label='text'

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ('email',) 

    def __init__(self, *args, **kwargs):
        super(SignUpForm , self).__init__(*args, **kwargs)
        for field in self.fields:
         self.fields['email'].widget.attrs.update({'placeholder':'enter your email'})
         self.fields['email'].label='email'