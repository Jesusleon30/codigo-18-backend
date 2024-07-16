from django.db import models

# Create your models here.


class CategoriaModel(models.Model):
    # sino le meto el db_column con su nombre por defecto la colunna se va a llamar id
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=100, unique=True, null=False)

    # campos de auditoria
    # creados automaticamente por la base de datos en el cual el backend no interfiere en nada solo para visualizacion
    # en createdAt significa que se va a guardar la fecha y ora en la cual se creo esa categoria
    # aca le estamos diciendo que cambie de nombre poniendole el db_column='created_at'
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    # se modificara el valor cada vez que hagamos una modificacion a las otras columnas con la fecha hora actual
    updatedAt = models.DateTimeField(auto_now=True, db_column='updated_at')
    # auto_now= True su valor por defecto va hacer la actual

    class Meta:
        db_table = 'categorias'


class ProductoModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=100, null=False)
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)

    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    # relaciones
    categoria = models.ForeignKey(
        to=CategoriaModel, on_delete=models.CASCADE, db_column='categoria_id')
    # on_delete=CASCADE quando se elimine esta categoiria  este se elimine todos sus productos

    class Meta:
        db_table = 'productos'
