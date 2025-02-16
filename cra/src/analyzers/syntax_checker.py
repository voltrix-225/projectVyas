import subprocess
from pylint.lint import Run
import ast

def run_pylint(fp):
    result = subprocess.run(["pylint", fp], capture_output=True, text = True)
    print(result.stdout)
'''
def check_file(fp):
    """Checks error, warnings, style issues"""
    print(Run([fp]))'''

def check_complexity(fp):
    result = subprocess.run(["pylint",  "--enable=design", "--disable=all",  fp], capture_output = True, text = True)
    print(result.stdout)

def check_syntax_errors(fp):
    """
    Checks for syntax errors in a Python file using AST parsing.
    Returns True if syntax is correct, otherwise prints the error.
    """
     
    try:
        with open(fp, 'r', encoding='utf-8') as file:
            source_code = file.read()
        ast.parse(source_code)
        print(f"The syntax of {fp} is correct")
        return True
    except SyntaxError as e:
        print(f"Syntax error in {fp} at line {e.lineno} is {e.msg}")
        return False
    
check_syntax_errors("C:\\Users\\voltr\\OneDrive\\Python\\projectVyas\\cra\\src\\analyzers\\demo.py")

