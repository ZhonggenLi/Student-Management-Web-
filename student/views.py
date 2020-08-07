from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from student.models import Student
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
# Create your views here.
@csrf_exempt
def insert(request):
   if request.POST:
      post = request.POST
      new_student = Student(
         num = post["num"],
         name = post["name"],
         chinese = post["chinese"],
         math = post["math"],
         english = post["english"],
         physics = post["physics"],
         chemistry = post["chemistry"],
         allscore = int(post["chinese"])+int(post["math"])+int(post["english"])+int(post["physics"])+int(post["chemistry"]))
      new_student.save()
   return render(request, 'insert.html')


def list(request):
    student_list = Student.objects.all()
    c = {"student_list": student_list, }
    return render(request, "list.html", c)


def delete(request):
   delete_num = request.GET.get('delete_num')
   Student.objects.get(num = delete_num).delete()
   return render(request, "delete.html")


def updateStudent(request):
   update_num = request.GET.get('update_num')
   update_student = Student.objects.get(num=update_num)
   a = {"update_student": update_student, }
   if request.POST:
      update_name = request.POST.get("name")
      update_chinese = request.POST.get("chinese")
      update_math = request.POST.get("math")
      update_english = request.POST.get("english")
      update_physics = request.POST.get("physics")
      update_chemistry = request.POST.get("chemistry")

      update_student.num = update_num
      update_student.name = update_name
      update_student.chinese = update_chinese
      update_student.math = update_math
      update_student.english = update_english
      update_student.physics = update_physics
      update_student.chemistry = update_chemistry
      update_student.allscore =int(update_chemistry)+int(update_physics)+int(update_english)+int(update_math)+int(update_chinese)
      update_student.save()
   return render(request, "update.html", a)

def questu(request):
    stu = {}
    if request.POST:
       quename = request.POST.get("name")
       quenum = request.POST.get("num")
       if quename:
          student_list = Student.objects.filter(name = quename)
          stu = {"student_list": student_list, }
       elif quenum:
          student_list = Student.objects.filter(num = quenum)
          stu = {"student_list":student_list, }
    return render(request, "questu.html", stu)

def sinsort(request):
   stu = {}
   if request.POST:
      proj = request.POST.get("proj")
      if proj == '1':
         stulist = Student.objects.order_by("-chinese")
         stu = {"stulist": stulist, "proj": proj, }
      elif proj == '2':
         stulist = Student.objects.order_by("-math")
         stu = {"stulist": stulist, "proj": proj, }
      elif proj == '3':
         stulist = Student.objects.order_by("-english")
         stu = {"stulist": stulist, "proj": proj, }
      elif proj == '4':
         stulist = Student.objects.order_by("-physics")
         stu = {"stulist": stulist, "proj": proj, }
      elif proj == '5':
         stulist = Student.objects.order_by("-chemistry")
         stu = {"stulist": stulist, "proj": proj, }
      elif proj == '6':
         stulist = Student.objects.order_by("-allscore")
         stu = {"stulist":stulist,"proj":proj, }
   return render(request, "sinsort.html", stu)

def fraction(request):
   stu = {}
   if request.POST:
      score = request.POST.get("score")
      if score == '1':
         stulist = Student.objects.filter(allscore__gte=600)
         stulist = sorted(stulist, key=lambda x:x.allscore, reverse=True)
         stu = {"stulist": stulist, }
      elif score == '2':
         stulist = Student.objects.filter(allscore__gte=500, allscore__lt=600)
         stulist = sorted(stulist, key=lambda x: x.allscore, reverse=True)
         stu = {"stulist": stulist, }
      elif score == '3':
         stulist = Student.objects.filter(allscore__gte=400, allscore__lt=500)
         stulist = sorted(stulist, key=lambda x: x.allscore, reverse=True)
         stu = {"stulist": stulist, }
      elif score == '4':
         stulist = Student.objects.filter(allscore__gte=300, allscore__lt=400)
         stulist = sorted(stulist, key=lambda x: x.allscore, reverse=True)
         stu = {"stulist": stulist, }
      elif score == '5':
         stulist = Student.objects.filter(allscore__lte=300)
         stulist = sorted(stulist, key=lambda x: x.allscore, reverse=True)
         stu = {"stulist":stulist, }
   return render(request, "fraction.html", stu)

