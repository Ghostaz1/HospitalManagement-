from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient

# List all patients
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient/patient_list.html', {'patients': patients})

# View single patient
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient/patient_detail.html', {'patient': patient})

# Add new patient
def patient_create(request):
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        dateofbirth = request.POST['dateofbirth']
        age = request.POST['age']
        Patient.objects.create(patient_name=patient_name, dateofbirth=dateofbirth, age=age)
        return redirect('patient_list')
    return render(request, 'patient/patient_form.html')

# Edit patient
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.patient_name = request.POST['patient_name']
        patient.dateofbirth = request.POST['dateofbirth']
        patient.age = request.POST['age']
        patient.save()
        return redirect('patient_list')
    return render(request, 'patient/patient_form.html', {'patient': patient})

# Delete patient
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patient/patient_confirm_delete.html', {'patient': patient})