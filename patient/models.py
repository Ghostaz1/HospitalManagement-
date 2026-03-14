from django.db import models

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=255)
    dateofbirth = models.DateField()
    age = models.IntegerField()

    class Meta:
        db_table = 'PATIENTS'

    def __str__(self):
        return self.patient_name