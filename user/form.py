from django import forms
from .models import Account
from django.core.exceptions import ValidationError



class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={

        'placeholder':'Enter password',
        'class':'form-control',


    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'PASSWORD',
         'class':'form-control',
    }))

    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'ENTER FIRST NAME',
         'class':'form-control',
    }))
        
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'ENTER LAST NAME',
         'class':'form-control',
    }))
        
    phone_number=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'ENTER PHONE NUMBER',
         'class':'form-control',
    }))
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'ENTER USERNAME',
         'class':'form-control',
    }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'ENTER EMAIL ADDRESS',
         'class':'form-control',
    }))
        
        
    class Meta:
        model=Account
        fields={'first_name','last_name','username','phone_number','email','password',}


    
    def __int__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter First Name'
        self.fields['username'].widget.attrs['placeholder']='Enter Username'
        self.fields['last_name'].widget.attrs['placeholder']='Enter Last Name'
        self.fields['phone_number'].widget.attrs['placeholder']='Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder']='Enter Email Address'
        for field in self.fields:
            self.fields[field].widget.attrs['class']= 'form-control'
    

    def clean(self):
        cleaned_data=super(RegistrationForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')


        if password != confirm_password:
            raise forms.ValidationError(
                'password doesnot match'
            )

from.models import Address



class AddressForm(forms.ModelForm):

    class Meta:

        model = Address

        fields = ['house_name', 'landmark','city',  'pincode', 'district', 'state','country','name','phone_number','email_2']


        def clean_pincode(self):
            pincode = self.cleaned_data['pincode']
            if pincode < 0:
                raise ValidationError("Pincode must be a positive number")
            return pincode

        def clean_phone_number(self):
            phone_number = self.cleaned_data['phone_number']
            if not str(phone_number).isdigit():
                raise ValidationError("Phone number must contain only digits")
            return phone_number
        
        def clean_house_name(self):
            house_name = self.cleaned_data['house_name']
            if not house_name:
                raise forms.ValidationError('House name is required.')
            return house_name

        def clean_phone_number(self):
            phone_number = self.cleaned_data['phone_number']
            if not phone_number:
                raise forms.ValidationError('Phone number is required.')
            elif not str(phone_number).isdigit():
                raise forms.ValidationError('Phone number must contain only digits.')
            return phone_number

        def clean_city(self):
            city = self.cleaned_data['city']
            if not city:
                raise forms.ValidationError('City is required.')
            return city

        def clean_district(self):
            district = self.cleaned_data['district']
            if not district:
                raise forms.ValidationError('District is required.')
            return district

        def clean_country(self):
            country = self.cleaned_data['country']
            if not country:
                raise forms.ValidationError('Country is required.')
            return country



  

   
    
  
    
    def _init_(self, *args, **kwargs):

        super(AddressForm, self).__init__(*args, **kwargs )
        
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Your name'

        self.fields['email_2'].widget.attrs['placeholder'] = 'Enter Your Email '

        self.fields['house_name'].widget.attrs['placeholder'] = 'Enter House name'

        self.fields['landmark'].widget.attrs['placeholder'] = 'Enter Your Landmark'
        
        self.fields['pincode'].widget.attrs['placeholder'] = 'Enter Your Pincode'

        self.fields['city'].widget.attrs['placeholder'] = 'Enter Your City'

        self.fields['district'].widget.attrs['placeholder'] = 'Enter Your District'

        self.fields['state'].widget.attrs['placeholder'] = 'Enter Your State'

        self.fields['country'].widget.attrs['placeholder'] = 'Enter Your Country'
        
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Your phone number'

        

        
        

        for field in self.fields:

            self.fields[field].widget.attrs['class'] = ' form-control form-control-lg form-label ml-5'
