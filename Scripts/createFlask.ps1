Write-output 'SCRIPT WRITTEN BY KALIBER'
Write-output 'Running script....'

Write-output ' '
Write-Progress -Activity 'Creating flask environment, please wait...' -Status 'In progress' -PercentComplete 0
python -m venv venv | Out-Null
Write-Progress -Activity 'Creating flask environment, please wait...' -Status 'In progress' -PercentComplete 20

Write-Output "Creating flask environment: DONE"

Write-Progress -Activity 'Creating app.py file, please wait...' -Status 'In progress' -PercentComplete 20
New-item app.py | Out-Null
Write-Progress -Activity 'Creating app.py file' -Status 'In progress' -PercentComplete 35

Write-Output "Creating app.py: DONE"

Write-Progress -Activity 'Setting content of app.py, please wait...' -Status 'In progress' -PercentComplete 35

Set-content app.py 'from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"' | Out-Null

Write-Progress -Activity 'Setting content of app.py, please wait...' -Status 'In progress' -PercentComplete 50
Write-Output "Setting content of app.py: DONE"

Write-Progress -Activity 'Activating venv script' -Status 'In progress' -PercentComplete 50
venv\scripts\activate | Out-Null
Write-Progress -Activity 'Activating venv script' -Status 'In progress' -PercentComplete 75

Write-output "Activating venv script: DONE"

Write-Progress -Activity 'Running pip install flask' -Status 'In progress' -PercentComplete 75
pip install flask | Out-Null
Write-Progress -Activity 'Running pip install flask' -Status 'In progress' -PercentComplete 90

Write-Output "Running pip install flask: DONE"

Write-output 'All done!'
Write-Progress -Activity 'Running flask in debug' -Status 'Complete' -PercentComplete 90

flask run --debug | Out-Null
Write-Progress -Activity 'Running flask in debug' -Status 'Complete' -PercentComplete 100
