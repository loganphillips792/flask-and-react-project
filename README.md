# Running the frontend web app

The frontend web app is built using Vite, Typescript and React.

1. ```npm install```
2. ```npm run dev```

# Running the backend Flask app

## Installing Python depdencies

1. ```python3 -m venv ~/Desktop/FlaskEnv```
2. ```source ~/Desktop/FlaskEnv/bin/activate``` - this line activates the virtual environment so your Python will use an packages that are installed in it
3. ```which pip``` to verify what is being used (Should point to the one from the virtual environment)
4. ```~/Desktop/FlaskEnv/bin/python3 -m pip install --upgrade pip```
5. ```pip install -r requirements.txt```

## Running application

1. Go to project root
2. Create environment file (.env)
3. Enable virtual environment
4. python3 main.py