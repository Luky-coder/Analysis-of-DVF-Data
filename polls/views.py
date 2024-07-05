from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

from django.shortcuts import render
from io import BytesIO
import base64


import pandas as pd
import matplotlib.pyplot as plt


def index2(request):
    template = loader.get_template('template1.html')
    
    if(request.GET['model']=="Moyenne"):
        plot_html= Moy()
    if(request.GET['model']=="Minimum"):
        plot_html= Min()
    if(request.GET['model']=="Maximum"):
        plot_html= Max()
        
    context = {
        "plot_html": plot_html
    }
    return HttpResponse(template.render(context, request))
    return render(request, 'template1.html')


def index1(request):
    template = loader.get_template('template1.html')
    
    if(request.GET['model']=="Moyenne"):
        plot_html= Moy()
    elif(request.GET['model']=="Minimum"):
        plot_html= Min()
    elif(request.GET['model']=="Maximum"):
        plot_html= Max()
    elif(request.GET['model']=="Dep"):
        return render(request, 'template0.html')
        
    context = {
        "plot_html": plot_html
    }
    return HttpResponse(template.render(context, request))
    return render(request, 'template1.html')


def index(request):
    
    
    return render(request, 'template1.html')


def Moy():
    
    
    df = pd.read_csv('full.csv', sep=(","))

    df = df.dropna(axis=1, how='all')

    df = df.drop_duplicates()
    
    df_ev = df
    df_ev['date_mutation'] = pd.to_datetime(df_ev['date_mutation'])
    df_ev = df_ev.set_index("date_mutation").sort_index()
    df_Visu = df_ev[['valeur_fonciere']]
    df_Visu.resample('M').mean().plot()
    plt.title("Moyenne")
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    plot_html = base64.b64encode(buffer.read()).decode('utf-8')
    
    plt.close()
    
    return plot_html

def Min():
    
    
    df = pd.read_csv('full.csv', sep=(","))

    df = df.dropna(axis=1, how='all')

    df = df.drop_duplicates()
    
    df_ev = df
    df_ev['date_mutation'] = pd.to_datetime(df_ev['date_mutation'])
    df_ev = df_ev.set_index("date_mutation").sort_index()
    df_Visu = df_ev[['valeur_fonciere']]
    df_Visu.resample('M').min().plot()
    plt.title("Minimum")
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    plot_html = base64.b64encode(buffer.read()).decode('utf-8')
    
    plt.close()
    
    return plot_html


def Max():
    
    
    df = pd.read_csv('full.csv', sep=(","))

    df = df.dropna(axis=1, how='all')

    df = df.drop_duplicates()
    
    df_ev = df
    df_ev['date_mutation'] = pd.to_datetime(df_ev['date_mutation'])
    df_ev = df_ev.set_index("date_mutation").sort_index()
    df_Visu = df_ev[['valeur_fonciere']]
    df_Visu.resample('M').max().plot()
    plt.title("Maximum")
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    plot_html = base64.b64encode(buffer.read()).decode('utf-8')
    
    plt.close()
    
    return plot_html



def Dep(code_departement):
    
    
    df = pd.read_csv('full.csv', sep=(","))

    df = df.dropna(axis=1, how='all')

    df = df.drop_duplicates()
    
    df_ev = df
    df_ev['date_mutation'] = pd.to_datetime(df_ev['date_mutation'])
    df_ev = df_ev.set_index("date_mutation").sort_index()
    df_Visu = df_ev[df_ev['code_departement'].astype(str).str.startswith(code_departement)][['valeur_fonciere']]
    df_Visu.resample('M').mean().plot() 
    plt.title(f'Moyenne mensuelle de la valeur foncière pour le département du {code_departement}')
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    plot_html = base64.b64encode(buffer.read()).decode('utf-8')
    
    plt.close()
    
    return plot_html



def ma_vue_django(request):
    template = loader.get_template('template0.html')
    if request.method == 'POST':
        code_departement = request.POST.get('texte_utilisateur', '')
        plot_html = Dep(code_departement)
        
    
    context = {
        "plot_html": plot_html
    }
    return HttpResponse(template.render(context, request))


