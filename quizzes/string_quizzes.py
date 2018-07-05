from nose.tools import assert_true, assert_equal

mystring = """Termination of Swan-Ganz catheter within the proximal right main pulmonary."""

def string_index1_quiz(value):
    try:
        assert_equal(value, mystring[19])
        print("%s is the correct value"%value)
    except:
        print("%s is NOT the correct value for mystring[19]"%value)

def string_index2_quiz(value):
    try: 
        assert_equal(value, mystring[-4])
        print("%s is the correct value"%value)
    except:
        print("%s is NOT the correct value for mystring[-4]"%value)

