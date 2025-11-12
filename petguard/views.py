from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Animal, Especie, Raca


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Usuário ou senha inválidos")
    return render(request, "petguard/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def index(request):
    query = request.GET.get('q', '')
    especie_id = request.GET.get('especie')
    raca_id = request.GET.get('raca')
    status = request.GET.get('status')

    animais = Animal.objects.all()

    # Filtro por apelido
    if query:
        animais = animais.filter(apelido__icontains=query)

    # Filtro por espécie
    if especie_id and especie_id.lower() != 'todas as espécies':
        animais = animais.filter(especie_id=especie_id)

    # Filtro por raça (corrigido)
    if raca_id and raca_id.lower() != 'todas as raças':
        try:
            animais = animais.filter(raca_id=int(raca_id))
        except ValueError:
            pass  # caso venha algo inválido

    # Filtro por status
    if status and status.lower() != 'todos':
        animais = animais.filter(status=status)

    context = {
        'animais': animais,
        'especies': Especie.objects.all(),
        'racas': Raca.objects.all(),
        'is_admin': request.user.is_superuser,
    }

    return render(request, 'petguard/index.html', context)


@login_required(login_url="login")
def add_animal(request, id=None):
    animal = None
    if id:
        animal = get_object_or_404(Animal, id=id)

    especies = Especie.objects.all()
    racas = Raca.objects.all()

    if request.method == 'POST':
        anos = request.POST.get('anos')
        meses = request.POST.get('meses')
        apelido = request.POST.get('apelido')
        especie_id = request.POST.get('especie')
        raca_id = request.POST.get('raca')
        nova_raca_nome = request.POST.get('nova_raca')
        status = request.POST.get('status')
        observacoes = request.POST.get('observacoes')

        especie = get_object_or_404(Especie, id=especie_id)

        if nova_raca_nome:
            raca, _ = Raca.objects.get_or_create(nome=nova_raca_nome, especie=especie)
        elif raca_id:
            raca = get_object_or_404(Raca, id=raca_id)
        else:
            raca = None

        if animal:
            animal.anos = anos
            animal.meses = meses
            animal.apelido = apelido
            animal.especie = especie
            animal.raca = raca
            animal.status = status
            animal.observacoes = observacoes
            animal.save()
        else:
            Animal.objects.create(
                anos=anos,
                meses=meses,
                apelido=apelido,
                especie=especie,
                raca=raca,
                status=status,
                observacoes=observacoes,
            )

        return redirect('index')

    anos = range(0, 11)
    meses = range(0, 13)

    return render(request, 'petguard/addAnimal.html', {
        'animal': animal,
        'anos': anos,
        'meses': meses,
        'especies': especies,
        'racas': racas,
    })


def racas_por_especie(request, especie_id):
    racas = Raca.objects.filter(especie_id=especie_id).values('id', 'nome')
    return JsonResponse(list(racas), safe=False)


@login_required(login_url="login")
def detalhes(request, id):
    animal = get_object_or_404(Animal, id=id)
    return render(request, "petguard/detalhes.html", {"animal": animal})


@require_POST
@login_required(login_url="login")
def excluir_animal(request, animal_id):
    try:
        animal = Animal.objects.get(id=animal_id)
        animal.delete()
        return JsonResponse({"success": True})
    except Animal.DoesNotExist:
        return JsonResponse({"success": False, "error": "Animal não encontrado"})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})
