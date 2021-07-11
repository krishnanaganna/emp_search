from django.shortcuts import render
from django.db import connection       

def index(request):
    return render(request,"index.html")

def search(request):
    inputID=request.POST.get('inputID')
    with connection.cursor() as cursor:
        cursor.execute('select e1.empName as empName, d1.depName as depName from employee e1 left JOIN department d1 ON e1.depID=d1.depID where e1.empID = "'+inputID+'"')
          
        if cursor.rowcount==1:
         results = cursor.fetchone()
         return render(request,"result.html",  {'Id': inputID, 'name': results[0], 'department': results[1]}) 
        else:
         return render(request,"index.html", {'text': "No results were available for a given employee ID"})