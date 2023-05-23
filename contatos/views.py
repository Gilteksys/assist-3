from django.shortcuts import render
from django.http import JsonResponse
from .models import Cliente, OrdemServico
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cliente_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        contato = request.POST.get('contato')
        documento = request.POST.get('documento')

        try:
            cliente = Cliente.objects.create(nome=nome, endereco=endereco,
                                             contato=contato, documento=documento)
            return JsonResponse({'success': True, 'cliente_id': cliente.id})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Método inválido'})


@csrf_exempt
def ordem_servico_create(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente_id')
        aparelho = request.POST.get('aparelho')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        serial = request.POST.get('serial')
        observacao = request.POST.get('observacao')

        try:
            cliente = Cliente.objects.get(id=cliente_id)
            ordem_servico = OrdemServico(
                nome=cliente,
                aparelho=aparelho,
                marca=marca,
                modelo=modelo,
                serial=serial,
                observacao=observacao
            )
            ordem_servico.save()
            return JsonResponse({'success': True})
        except Cliente.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Cliente não encontrado'})

    return JsonResponse({'success': False, 'message': 'Método inválido'})



def cliente_list(request):
    clientes = Cliente.objects.all()

    # Você pode retornar os dados em formato JSON para serem consumidos pelo PyQt5
    data = {
        'clientes': [
            {'nome': cliente.nome, 'endereco': cliente.endereco,
                'contato': cliente.contato, 'documento': cliente.documento}
            for cliente in clientes
        ]
    }
    return JsonResponse(data)


def buscar_cliente_por_nome(request):
    nome = request.GET.get('nome', '')

    clientes = Cliente.objects.filter(nome__icontains=nome)

    data = {
        'clientes': [
            {'nome': cliente.nome, 'endereco': cliente.endereco,
                'contato': cliente.contato, 'documento': cliente.documento}
            for cliente in clientes
        ]
    }

    return JsonResponse(data)
