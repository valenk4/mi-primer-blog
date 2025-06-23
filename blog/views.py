from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Pintor

def artistas(request):
    pintores = Pintor.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    return render(request, 'blog/artistas.html', {'pintores':pintores})

def detalle_pintor(request, pk):
    pintor = get_object_or_404(Pintor, pk=pk)
    return render(request, 'blog/detalle.html', {'pintor': pintor})