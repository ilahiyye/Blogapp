from django import forms

#Login formu
class LoginForm(forms.Form):
    username = forms.CharField(label="Istifadəçi adı")
    password = forms.CharField(label="Parol", widget=forms.PasswordInput)


#register formu
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15, label="İstifadəçi adı")
    password = forms.CharField(max_length=20, label="Parol", widget=forms.PasswordInput)  #yazilan parolun gorunmemesi ucun widget=forms.PasswordInput yazilir
    confirm  = forms.CharField(max_length=20, label="Parolu təkrar et", widget=forms.PasswordInput)

    def clean(self):   #clean djangonun bir metodudur. Tekrar yazilan parolla evvelki parolun eyniliyini yoxlamaq ucun yaziriq
        username = self.cleaned_data.get("username")        #username icine yazilani goturur
        password = self.cleaned_data.get("password")
        confirm  = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:    # password and confirm bu sahenin doldurulub-doldurulmadigini yoxlayir
            raise forms.ValidationError("Parollar fərqlidir")

        #Hec bir problem yoxdursa

        values = {                                           #dictioary(sozluk).den istifade edib onlari diger fayllara otururuk
            "username": username,
            "password": password

                 }
        return values

        