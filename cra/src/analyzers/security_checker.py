import subprocess

def security_check(fp):
    result = subprocess.run(['bandit', '-r', fp], capture_output=True, text = True)
    print(result.stdout)



security_check("C:\\Users\\voltr\\OneDrive\\Python\\projectVyas\\cra\\src\\analyzers\\demo.py")