from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Route for the home page
@app.get('/')
def home(request: Request):
    background_color = '#f2f2f2'  # Default background color
    return templates.TemplateResponse("home.html", {"request": request, "background_color": background_color})

# Route for the second page
@app.route('/database')
def database():
    # Retrieve your database data here and pass it to the template
    # Example data
    database_data = [
        {'datetime': 'datadb'},
        {'temperature': 'tempdb'},
        {'soilhumidity': 'shdb'},
        {'ambienthumidity': 'ahdb'}
    ]
    return render_template('database.html', data=database_data)

if __name__ == '__main__':
    app.run(debug=True)


INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

