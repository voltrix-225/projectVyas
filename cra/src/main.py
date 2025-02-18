from analyzers.complexity_checker import calculateCyclomaticComplexity, countNestedLoops, recursionCounter
from analyzers.style_checker import check_code_style_issues
from analyzers.security_checker import analyze_security, Pwd_checker, check_subprocess
from analyzers.syntax_checker import check_syntax_errors

fp = input(eval())

syntax = check_syntax_errors(fp)
if not syntax:
    print("\n")
    exit()

print("CHECKING CODE SECURITY \n")
analyze_security(fp)
Pwd_checker(fp)
check_subprocess(fp)
print("\n")

print("CHECKING CODE DESIGN\n")
check_code_style_issues(fp)
print("\n")

print("RUNNING COMPLEXITY ANALYSIS \n")
cyclomatic_complexity = calculateCyclomaticComplexity(fp)
nested_loop = countNestedLoops(fp)
rec_name, rec_calls = recursionCounter(fp)
print(f"Found a Recursive Function '{rec_name}', with {rec_calls} calls\n")
print(f"The total complexity score is : {cyclomatic_complexity + nested_loop + rec_calls}")
