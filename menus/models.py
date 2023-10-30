from django.db import models

class Restaurant(models.Model):
    """ Um objeto classe Restaurant armazena informações
    sobre um restaurante """

    name = models.CharField(max_length=45)

    def __str__(self):
        """ Retorna uma representação em string do objeto """

        return f"[Restaurant] name: {self.name}"
