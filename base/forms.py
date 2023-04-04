from django import forms


class EmailForm(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder": "Ingrese su nombre"}),
    )
    emisor = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Ingrese su mail"}),
    )
    titulo = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder": "Ingrese un título"}),
    )
    contenido = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "Ingrese el contenido del mensaje"}
        ),
    )
    # attrs=multiple me permite poder cargar más de un archivo:
    archivo = forms.FileField(
        widget=forms.FileInput(attrs={"multiple": True}), required=False
    )
