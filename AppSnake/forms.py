from django import forms
class form_medicos(forms.Form):
    nombre= forms.CharField(label='nombre',max_length=20)
    apellido=forms.CharField()
    credencial= forms.IntegerField(min_value=4)
    interno=forms.IntegerField(min_value=6)

class form_cientificos(forms.Form):
    nombre= forms.CharField(label='nombre',max_length=20)
    apellido=forms.CharField()
    comision= forms.IntegerField(min_value=4)

class form_proyecto(forms.Form):
    nombre=forms.CharField(label='nombre',max_length=20)
    creado= forms.DateTimeField()
    