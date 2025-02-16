import subprocess

def check_style(fp):
    """Check style using the PEP-8 Guidelines"""
    result = subprocess.run(["flake8", "--statistics",  fp], capture_output=True, text = True)
    print(result.stdout)



#check_style("C:\\Users\\voltr\\OneDrive\\Python\\projectVyas\\cra\\src\\analyzers\\demo.py")
#place_holder("C:\\Users\\voltr\\OneDrive\\Python\\projectVyas\\cra\\src\\analyzers\\demo.py")