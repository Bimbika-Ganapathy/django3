from django.shortcuts import render

# Create your views here.
def fruit_student(request):
    fruitList=['Mango','Apple','Banana','Orange','Berry']
    studentList=['Rama','Devi','Ramesh','Geetha','Jam']
    return render (request,'fruit_student.html',{'fruitList':fruitList,'studentList':sorted(studentList)})