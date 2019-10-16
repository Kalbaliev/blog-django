from django import forms


class LoginForm(forms.Form):

    username=forms.CharField(max_length=20,label="İstifadəçi adı")
    password=forms.CharField(max_length=16,label="Şifrə",widget=forms.PasswordInput)



class RegisterForm(forms.Form):

    username=forms.CharField(max_length=20,label="İstifadəçi adı")
    password=forms.CharField(max_length=16,min_length=6,label="Şifrə",widget=forms.PasswordInput) # password area ucun widget
    confirm=forms.CharField(max_length=16,min_length=6,label="Şifrə Təkrar",widget=forms.PasswordInput)
    
    def clean(self):

        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")

        if password and confirm and password!=confirm:
            raise forms.ValidationError("Şifrə uyğun gəlmir!")
        values={
            "username":username,
            "password":password
        }

        return values
