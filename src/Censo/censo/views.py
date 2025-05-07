from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

class EntrevistadorViewSet(viewsets.ModelViewSet):
    queryset = Entrevistador.objects.all()
    serializer_class = EntrevistadorSerializer

class DomicilioViewSet(viewsets.ModelViewSet):
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer

class EntrevistaViewSet(viewsets.ModelViewSet):
    queryset = Entrevista.objects.select_related('entrevistador', 'domicilio')
    serializer_class = EntrevistaSerializer

class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.prefetch_related('entrevistas')
    serializer_class = RelatorioSerializer
    
    @action(detail=True, methods=['get'])
    def download_csv(self, request, pk=None):
        relatorio = self.get_object()
        csv_data = relatorio.gerar_csv()
        
        from django.http import HttpResponse
        response = HttpResponse(csv_data, content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="relatorio_{relatorio.id}.csv"'
        return response