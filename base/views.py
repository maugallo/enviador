from django.shortcuts import render, redirect
from .forms import EmailForm
from django.core.mail import EmailMessage
from django.conf import settings

lista_receptores = []

# Create your views here.
def index(request):
    context = {}
    return render(request, "base/index.html", context)


# Function-based view que conecta con un form:
def emailView(request):
    if request.method == "POST":
        form = EmailForm(request.POST, request.FILES)
        if "agregar" in request.POST:
            receptor = request.POST.get("receptor")
            if (
                not any(receptores == receptor for receptores in lista_receptores)
                and receptor != ""
            ):
                lista_receptores.append(receptor)
        if "limpiar" in request.POST:
            lista_receptores.clear()
        if "enviar" in request.POST:
            if form.is_valid():
                nombre = form.cleaned_data["nombre"]
                emisor = form.cleaned_data["emisor"]
                mensaje = f"{nombre}, con el mail {emisor} le ha enviado el siguiente mensaje:\n\n"
                titulo = form.cleaned_data["titulo"]
                contenido = form.cleaned_data["contenido"]
                contenido = mensaje + contenido
                archivos = request.FILES.getlist("archivo")
                try:
                    mail = EmailMessage(
                        titulo, contenido, settings.EMAIL_HOST_USER, lista_receptores
                    )
                    for archivo in archivos:
                        mail.attach(archivo.name, archivo.read(), archivo.content_type)
                    if len(lista_receptores) == 0:
                        return redirect("failed")
                    else:
                        mail.send()
                        return redirect("success")
                except:
                    return redirect("failed")
    else:
        form = EmailForm()
    context = {"form": form, "lista_receptores": lista_receptores}
    return render(request, "base/enviar.html", context)


def emailSuccess(request):
    context = {}
    return render(request, "base/sucess.html", context)


def emailFailed(request):
    context = {}
    return render(request, "base/failed.html", context)
