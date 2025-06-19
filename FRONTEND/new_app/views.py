from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from .models import predict


def read_file(file_name):
    opened_file = open(file_name, 'r')
    lines_list = []
    for line in opened_file:
        line = line.split()
        lines_list.append(line)
    #print(lines_list)
    return lines_list



# Create your views here.
# Create your views here.  
def home(request):
	return render(request,'index.html')


def input(request):
    file_name = 'account.txt'
    name = request.POST.get('name')
    password = request.POST.get('password')
    account_list = read_file(file_name)
    print(name)
    print(password)
    for i in account_list:

        if i[0] == name  and i[1] == password:
            print(i[0])
            print(i[1])
            return render(request,'input.html')
        else:
            return HttpResponse('Wrong Password or Name', content_type='text/plain')


import numpy as np

def output(request):
    algo = request.POST.get('algo')  # Get selected algorithm
    text = [str(request.POST.get('text'))]  # Get input text
    
    out = predict(text, algo)  # Predict class index
    
    # Ensure the output is converted to float
    out = np.float32(out)  # Fix for LightGBM expected type

    # Emotion classes mapping
    class_names = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']
    
    # Get predicted class name
    class_name = class_names[int(out)]  
    
    print('Output:', out)
    print('Predicted Emotion:', class_name)
    
    return render(request, 'output.html', {'out': class_name})
