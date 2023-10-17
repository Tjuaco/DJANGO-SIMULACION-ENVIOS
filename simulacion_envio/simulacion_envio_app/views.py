from django.shortcuts import render
from .models import Simulacion
from .forms import SimulacionForm
from django.views.generic import ListView
from django.http import Http404
from decimal import Decimal

# RENDERIZAR PAGINA DE INICIO
def inicio(request):
    return render(request, 'html/inicio.html')

#RENDERIZA FORMULARIO
def crear_simulacion_form(request):
    form = SimulacionForm()
    return render(request, 'html/formulario.html', {'form': form})

#PROCESA SIMULACION Y LA GUARDA
def enviar_simulacion_form(request):
    form = SimulacionForm()
    simulacion = None

    if request.method == 'POST':
        form = SimulacionForm(request.POST)
        if form.is_valid():
            simulacion = form.save(commit=False)

            unidades = form.cleaned_data['cantidad_unidades']
            costo_unitario = form.cleaned_data['costo_unitario']
            envio = Decimal(form.cleaned_data['costo_envio'])
            
            valor_pedido_usd = unidades * costo_unitario
            costo_envio_clp = int(envio * 890)
            valor_cif_clp = int((valor_pedido_usd + envio) * 890)
            tasa_aduana_clp = int(valor_cif_clp * 0.06)
            iva_clp = int(valor_cif_clp * 0.19)
            impuesto_aduana_clp = tasa_aduana_clp + iva_clp
            costo_total_clp = valor_cif_clp + impuesto_aduana_clp
            costo_total_usd = costo_total_clp / 890
            
            simulacion.total_pedido = valor_pedido_usd*890
            simulacion.costo_envio = costo_envio_clp
            simulacion.tasa_aduana = tasa_aduana_clp
            simulacion.iva = iva_clp
            simulacion.impuesto_aduana = impuesto_aduana_clp
            simulacion.costo_total = costo_total_clp

            simulacion.save()

             #CONVERTIR VALORES A CLP
            simulacion.total_pedido_usd = valor_pedido_usd / 890
            simulacion.costo_envio_usd = costo_envio_clp / 890
            simulacion.tasa_aduana_usd = tasa_aduana_clp / 890
            simulacion.iva_usd = iva_clp / 890
            simulacion.impuesto_aduana_usd = impuesto_aduana_clp / 890
            simulacion.costo_total_usd = costo_total_usd

            simulacion.save()

            return render(request, 'html/resultados.html', {'simulacion': simulacion})

#VISTA BASADA EN CLASE(PARA MOSTRAR LA LISTA)
class ListaSimulacionesView(ListView):
    model = Simulacion
    template_name = 'html/lista_simulaciones.html'
    context_object_name = 'simulaciones'


#ELIMINAR SIMULACIONES
def eliminar_simulacion(request, id):
    try:
        simulacion = Simulacion.objects.get(pk=id)
        simulacion.delete()
        mensaje = "Simulación eliminada con éxito."
    except Simulacion.DoesNotExist:
        raise Http404("La simulación no existe")

    simulaciones = Simulacion.objects.all()
    data = {'simulaciones': simulaciones, 'mensaje': mensaje}
    return render(request, 'html/lista_simulaciones.html', data)
