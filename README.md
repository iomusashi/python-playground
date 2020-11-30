# python-playground
A brief history of snakes and ladders.

## What's this about?
Nothing. Nothing here.

## Getting started

### Python3

Install python3 via homebrew, apt, or pkg.

If you just want to play games, or explore python, that's all you need.

### Jupyter Notebook / Caffe2
If you want to play using jupyter notebook and caffe2, continue:

#### Play safe, use virtual environments

When playing with Jupyter and Caffe, it is advisable to work on a virtual environment to install dependencies without affecting your personal computing environment.

To do so, use the Python3-env to manage virtual environments. See some useful python3-env commands below.

Create a new virtual environment
```bash
python -m venv ~/env
```

Activate the virtual environment
```bash
source ~/env/bin/activate
```

Deactivate the virtual environment
```bash
deactivate
```

#### Install
Install pip3, and setuptools.

Create and activate your virtual environment, and continue installation on the following pip packages:
```bash
pip install
    future \
    numpy \
    protobuf \
    pyyaml \
    six \
    graphviz \
    hypothesis \
    ipython \
    jupyter \
    matplotlib \
    notebook \
    pydot \
    python-nvd3 \
    pyyaml \
    requests \
    scikit-image \
    scipy
```

I recommend installing pip packages over a virtual environment to avoid conflicting packages with your personal computing environment.

### /boring-stuff
Collection of stuff about learning the language.

Nothing cool here.

### /caffe
Learning caffe2 and stuff.

### /games
The only stuff you care about that's why you came here.

Recommended if you're totally bored:

(0) An Android Phone w/ Google Play

(1) Download termux (root or not root)

(2) In termux, install curl, git, zsh, oh-my-termux (Optional)

(3) Using git, clone this repo by either HTTPS or SSH (requires additional setup)

(4) Install python.

(5) Go to games, and play the game you want.

(6) Add more text games you like.

### /jupyter  

Contains some handy notebook for learning how to code maths.

NN+ML Review materials for maths:
Linear Algebra and Multivariate Calc

/tensorflow - Stuff relating to learning tensorflow.

### 100-days of Python

Just some practice of python awesomeness in 100 days.
