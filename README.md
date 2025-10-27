# python_emoji

Goal: Practice creating a clean project, setting up a virtual environment, installing/pinning
packages, writing a small Python script (not a notebook), timing code, and adding a smoke test.

## Setup (env creation, install from requirements)

1. Clone repository in your local system
```
git clone git@github.com:Jordid13/python_emoji.git
```

2. Create python virtual environment and activate it
```
python3 -m venv testenv
source testenv/bin/activate
```

3. Install requirements and dependencies
```
pip install -r requirements.txt
```

## Run

Example Command: 
```
python3 make_emoji.py --name ":rocket:" --msg "Lift off\!"
```

Example Output:
```
🚀 Lift off!
```

## Time it

Performance Results:
```
python3 -m timeit -n 1000 -s "from emoji import emojize" "emojize(':rocket:')"
1000 loops, best of 5: 1.05 usec per loop
```

## Test

To test the project run:
```
pytest -q
```
Note: Make sure you are in the project root  before running above command