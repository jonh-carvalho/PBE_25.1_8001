from django.db import models
from enum import Enum

class TipoEsgoto(models.TextChoices):
    REDE_PUBLICA = 'RP', 'Rede Pública'
    FOSSA = 'FS', 'Fossa'
    NENHUM = 'NN', 'Nenhum'

class Sexo(models.TextChoices):
    FEMININO = 'F', 'Feminino'
    MASCULINO = 'M', 'Masculino'
    OUTRO = 'O', 'Outro'

class RacaCor(models.TextChoices):
    BRANCA = 'B', 'Branca'
    PRETA = 'P', 'Preta'
    PARDA = 'PA', 'Parda'
    INDIGENA = 'I', 'Indígena'
    AMARELA = 'A', 'Amarela'

class Entrevistador(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    area_cobertura = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nome} ({self.matricula})"

class Domicilio(models.Model):
    endereco = models.CharField(max_length=200)
    coordenadas = models.JSONField()  # Ou usar PointField do GeoDjango
    tem_agua_encanada = models.BooleanField()
    tem_energia = models.BooleanField()
    tipo_esgoto = models.CharField(
        max_length=2,
        choices=TipoEsgoto.choices
    )
    
    class Meta:
        verbose_name_plural = "Domicílios"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=Sexo.choices)
    raca_cor = models.CharField(max_length=2, choices=RacaCor.choices)
    escolaridade = models.CharField(max_length=50)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE, related_name='pessoas')
    
    def __str__(self):
        return self.nome

class Entrevista(models.Model):
    entrevistador = models.ForeignKey(Entrevistador, on_delete=models.PROTECT)
    domicilio = models.OneToOneField(Domicilio, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    sincronizada = models.BooleanField(default=False)
    
    def validar_dados(self):
        return self.domicilio and self.pessoas.exists()
    
    @property
    def pessoas(self):
        return self.domicilio.pessoas.all()

class Relatorio(models.Model):
    regiao = models.CharField(max_length=50)
    periodo = models.CharField(max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)
    entrevistas = models.ManyToManyField(Entrevista)
    
    def gerar_csv(self):
        # Implementação real geraria um arquivo físico
        import csv
        from io import StringIO
        
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(['Nome', 'Idade', 'Sexo', 'Renda'])
        
        for entrevista in self.entrevistas.all():
            for pessoa in entrevista.pessoas:
                writer.writerow([
                    pessoa.nome,
                    pessoa.idade,
                    pessoa.get_sexo_display(),
                    pessoa.renda
                ])
        
        return output.getvalue()