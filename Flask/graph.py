from flask import Flask,redirect,url_for,render_template,request,Response
import pandas as pd
import openpyxl
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('sample.html') 

@app.route('/<name>')
def user(name):
    return f"Hello {name}!"

@app.route('/login')
def admin():
    return redirect(url_for("hello_world"))

@app.route('/admin', methods = ['GET', 'POST'])
def plot_png():
    path = r"C:\Users\palani\Documents\flask\Indian_States_consolidated_1.xlsx"
    sheet1=index()
    fig = create_figure(path,sheet1)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def index():
    if request.method == 'POST':
        path = r"C:\Users\palani\Documents\flask\Indian_States_consolidated_1.xlsx"
        wb=openpyxl.load_workbook(path)
        sheet = request.form.get('sheet')
        date = request.form.get('date')
        TT = request.form.get('TT')
        MH = request.form.get('MH')
        TN = request.form.get('TN')
        DL = request.form.get('DL')
        GJ = request.form.get('GJ')
        RJ = request.form.get('RJ')
        UP = request.form.get('UP')
        MP = request.form.get('MP')
        AP = request.form.get('AP')
        TG = request.form.get('TG')
        KA = request.form.get('KA')
        KL = request.form.get('KL')
        ws=wb[sheet]
        ws.append([date,TT,MH,TN,DL,GJ,RJ,UP,MP,AP,TG,KA,KL])
        wb.save(path)
        return sheet

def create_figure(path,sheet1):
    fig = Figure()
    df = pd.read_excel(path,sheet_name=sheet1)
    axis = fig.add_subplot()
    df.plot('Date',ax=axis,linewidth=2,figsize=(15,15))

    return fig

           
     
    
    

      
    



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80)
