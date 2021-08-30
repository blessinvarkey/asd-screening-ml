# ASD Screening 

## Autism Spectrum Quotient (AQ-10) | Q-CHAT

### About
The Autism-Spectrum Quotient publisehed by Baron-Cohen, Wheelwright, Skinner, Martin, & Clubley was developed to assess how adults with 'normal' intelligence has the traits associated with autism spectrum conditions. According to Wikia, "the test consists of fifty statements, each of which is in a forced-choice format. Each question allows the subject to indicate "Definitely agree", "Slightly agree", "Slightly disagree" or "Definitely disagree". Approximately half the questions are worded to elicit an "agree" response from normal individuals, and half to elicit a "disagree" response. The subject scores one point for each question which is answered "autistically" either slightly or definitely." The questions cover five different domains associated with the autism spectrum: social skills; communication skills; imagination; attention to detail; and attention switching/tolerance of change.

According to the dataset, 'Yes' indicates that the individual is on the Autism Spectum and 'No' is indicated when the final score is less than or equal to 7. You can refer the questions from [here](https://www.nice.org.uk/guidance/cg142/resources/autism-spectrum-quotient-aq10-test-pdf-186582493).

### AQ-10 questions
A1 I often notice small sounds when others do not.  
A2 I usually concentrate more on the whole picture, rather than the small details.   
A3 I find it easy to do more than one thing at once.    
A4 If there is an interruption, I can switch back to what I was doing very quickly.    
A5 I find it easy to ‘read between the lines’ when someone is talking to me.   
A6 I know how to tell if someone listening to me is getting bored.   
A7 When I’m reading a story I find it difficult to work out the characters’ intentions.    
A8 I like to collect information about categories of things (e.g. types of car, types of bird, types of train, types of plant etc).    
A9 I find it easy to work out what someone is thinking or feeling just by looking at their face. 
A10 I find it difficult to work out people’s intentions


## Dataset 

The Dataset can be downloaded from the UCI Repository which is publicly available [here](https://archive.ics.uci.edu/ml/datasets/Autism+Screening+Adult). 

## Algorithm Used
The project implements Logistic Regression.   

## Output 
Logistic Regression Accuracy 
Classification Report
The output is either a 1(YES, the individual is on the Spectrum) or 0(NO, the individual is not on the Spectrum)


# Installation

### 1. AQ-10 Screening 

Install [Jupiter Notebook](https://jupyter.org/install.html) to try the model.

Download the [Adult Autism](https://github.com/blessinvarkey/ASD-Screening/blob/main/Adult_dataset/autism-screening-project.ipynb) file with [Autism_Data.arff](https://github.com/blessinvarkey/ASD-Screening/blob/main/Energy_Consumption/Autism_Data.arff) to implement Logistic Regression on the Adult dataset. 


### 2. Energy Consumption of implementing Logistic Regression in ASD Screening project 
To see the **energy consumption** of the project download the [asd.py](https://github.com/blessinvarkey/ASD-Screening/blob/main/Energy_Consumption/asd.py) and the [Autism_Data.arff](https://github.com/blessinvarkey/ASD-Screening/blob/main/Energy_Consumption/Autism_Data.arff) file along with a code editor.

Use the terminal to navigate to the source folder. 

Create a virtual environment using `conda` for easier management of dependencies and packages. You can also follow the instructions on the [official conda website](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)

```
conda create --name codecarbon python=3.6
conda activate codecarbon
```

#### Install from PyPI repository
```
pip install codecarbon
```

#### Install from Conda repository

```
conda install -c codecarbon -c conda-forge codecarbon
```

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

You can install them using 

```
pip install <write the packagename you want to download>
```

To run the code
```
python run.py
```

[Back to top](https://github.com/blessinvarkey/ASD-Screening/blob/main/Adult_dataset/autism-screening-project.ipynb)
