from django.db import models

class Especie(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Raca(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, related_name='racas')

    def __str__(self):
        return f"{self.nome} ({self.especie.nome})"


class Animal(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('em_tratamento', 'Em tratamento'),
        ('adotado', 'Adotado'),
    ]
    apelido = models.CharField(max_length=100)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    anos = models.PositiveIntegerField(default=0)
    meses = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=30,choices=STATUS_CHOICES, default="disponivel")
    observacoes = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='animais/', null=True, blank=True)

    def __str__(self):
        return f"{self.apelido} ({self.especie})"
