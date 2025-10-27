from django.db import models

class Animal(models.Model):
    STATUS_CHOICES = [
        ('Disponível', 'Disponível'),
        ('Em tratamento', 'Em tratamento'),
        ('Adotado', 'Adotado'),
    ]

    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    idade = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Disponível')
    foto = models.ImageField(upload_to='fotos_animais/', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.especie} - {self.raca} (ID {self.id})"
