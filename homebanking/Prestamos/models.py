from django.db import models

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True, blank=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        db_table = 'prestamo'
