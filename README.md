## alura-intro-datascience

I'm trying Alura's [Intro to Data Science Course](https://cursos.alura.com.br/formacao-data-science) using Python with Pandas. Here's the code I created for every class lesson.
The lessons are in Jupyter and Anaconda, but I'm running it using plain Python env and VS Code.

#### repeated-code
You'll note every source file begins with a little hack, to load dataset files based on source-file location, instead of shell/terminal location.

```py
filedir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(filedir, '..', 'datasets/filtered.csv')

data = pd.read_csv(csv_path)
```
This code is repeated all over the Python files. As this is just study code, I don't have plans to change it :-)

#### Courses progress

As I'm still taking the classes, it's not complete yet. Here's the current status:

- [x] Course 1 - First Steps
- [x] Course 2 - Intro to Pandas
- [ ] Course 3 - Intro to Time-series and analysis
- [ ] Course 4 - Model and Linear regression 
- [ ] Course 5 - Linear regression and statsmodel
- [ ] Course 6 - Intro to charts design
- [ ] Course 7 - Choosing the right chart
- [ ] Course 8 - Intro to statistical tests with Python
