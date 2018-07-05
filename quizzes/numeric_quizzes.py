from nose.tools import assert_equal, assert_true
import math
import numbers

def numeric_quizz1(answer, tol=0.01):
    if not isinstance(answer,numbers.Number):
        return "Your answer needs to be a number. You provided the type %s"%type(answer)
    ref = (5*3**3-2)**2/(4*3+1)
    try:
        assert_true(math.fabs(answer-ref) < math.fabs(ref)*tol)
        return "You got the correct answer!"
    except Exception:
        return "You did not get the correct answer. Pay attention to parentheses and operator precedence"

def numeric_quizz2(answer):
    if not isinstance(answer,bool):
        return "Your answer needs to be the Python value True or False. You provided the type %s"%type(answer)
    try:
        assert_equal(answer, 7**(0.5)*(4/3) < (3**2*(3/4))/(1+2**2))
        return "You got the correct answer"
    except Exception as error:
        return "You did not get the correct answer. Pay attention to parentheses and operator precedence: %s"%error

def numeric_quizz3(answer, tol=0.01):
    
    if not isinstance(answer,numbers.Number):
        return "Your answer needs to be a number. You provided the type %s"%type(answer)
    ref = math.exp(-5**2*math.cos(3*math.pi/7))
    try:
        assert_true(math.fabs(answer-ref)< math.fabs(ref)*tol)
        return "You got the correct answer"
    except Exception: 
        return "You did not get the correct answer. Pay attention to parentheses and operator precedence."
 
