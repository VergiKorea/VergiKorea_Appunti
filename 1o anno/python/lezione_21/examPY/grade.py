# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
DEBUG = True
# DEBUG = False
#############################################################################

def error_message(res, expected, msg=None):
    msg_std = f"Valore NON corretto! [NOT OK]\n TUO RISULTATO = {res} \n ma e' ATTESO = {expected}"
    if msg is None:
        msg = msg_std
    else:
        msg = msg + msg_std
    print('*'*50)
    print(msg)

def test_personal_data_entry():
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', "ERROR: Please assign the 'name' variable with YOUR NAME in program.py"
        assert program.surname    != 'SURNAME', "ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py"
        assert program.student_id != 'MATRICULATION NUMBER', "ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py"
    else:
        assert program.nome      != 'NOME', "ERRORE: Indica il tuo NOME in program.py"
        assert program.cognome   != 'COGNOME', "ERRORE: Indica il tuo COGNOME in program.py"
        assert program.matricola != 'MATRICOLA', "ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py"
    return 0

###############################################################################

# ----------------------------------- EX.3 ----------------------------------- #
from tree import BinaryTree as BinTree


def do_test_ex3(root, j, k, expected, expectednum):
    if not DEBUG:
        try:
            root1 = BinTree.fromList(root)
            isrecursive.decorate_module(program)
            program.ex3(root1, j, k)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    root2 = BinTree.fromList(root)
    res   = program.ex3(root2, j, k)
    expected2 = BinTree.fromList(expected)
    testlib.check(root2, expected2,   None, f"Wrong tree! Returned=\n{root}, expected=\n{expected}")
    try:
        assert res == expectednum, f"Wrong number of nodes! Returned={res}, expected={expectednum}"
    except Exception as e:
        print(e)
        return 2
    return 3

def test_ex3_1():
    root     = [ 1, [  2, [3, [4, None, None], None],
                          [5, None, [6, None, None]]],
                    [  7, [8, None, [9, None, None]], None]]
    expected = [ 1, [ 10, [3, [4, None, None], None],
                          [5, None, [6, None, None]]],
                    [ 15, [8, None, [9, None, None]], None]]
    j, k = 1, 2
    expectednum = 5
    return do_test_ex3(root, j, k, expected, expectednum)


def test_ex3_2():
    root     = [220689, [701526, None, [843044, [997976, [795464, None, [230911, None, None]], None], None]], 
                        [17746, [364108, [283446, None, None], 
                                         [605042, [236082, [948668, None, None], 
                                                           [339782, None, None]], 
                                                  [787038, None, None]]], 
                                [35091, [786618, [836211, [57783, None, None], 
                                                          [984361, None, None]], 
                                                 [982305, None, [258344, None, None]]], 
                                        [94428, [791648, [961306, None, None], 
                                                         [348550, [527385, None, None], None]], 
                                                [818090, [124878, None, None], None]]]]]
    expected = [220689, [701526, None, [2867395, [997976, [795464, None, [230911, None, None]], None], None]], 
                        [17746, [3564166, [283446, None, None], 
                                          [605042, [236082, [948668, None, None], 
                                                            [339782, None, None]], 
                                                   [787038, None, None]]], 
                                [7079613, [786618, [836211, [57783, None, None], 
                                                            [984361, None, None]], 
                                                   [982305, None, [258344, None, None]]], 
                                          [94428, [791648, [961306, None, None], 
                                                           [348550, [527385, None, None], None]], 
                                                  [818090, [124878, None, None], None]]]]]
    j, k = 2, 5
    expectednum = 24
    return do_test_ex3(root, j, k, expected, expectednum)

def test_ex3_3():
    root = [753939, [424882, None, [936878, [960205, [153596, [168465, None, None], [448329, None, None]], [786073, None, [665776, [666603, None, None], [220793, None, [833643, None, None]]]]], [725451, [583121, [436361, None, None], [6015, [174847, None, None], [881981, None, None]]], [257257, [918102, None, [220908, None, None]], [902429, [307919, None, None], None]]]]], None]

    expected = [753939, [424882, None, [936878, [960205, [153596, [168465, None, None], [448329, None, None]], [786073, None, [665776, [666603, None, None], [1054436, None, [833643, None, None]]]]], [725451, [583121, [436361, None, None], [6015, [174847, None, None], [881981, None, None]]], [257257, [918102, None, [220908, None, None]], [902429, [307919, None, None], None]]]]], None]
    j, k = 6, 8
    expectednum = 7
    return do_test_ex3(root, j, k, expected, expectednum)
# ----------------------------------- EX.4 ----------------------------------- #


def do_ex4_test(path, testID, expected):
    outfile = f"ex4{testID}_out.txt"
    expfile = f"ex4{testID}_exp.txt"
    try:
        os.unlink(outfile)
    except: pass
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex4(path, outfile)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)
    try:
        os.unlink(outfile)
    except: pass
    res = program.ex4(path, outfile)
    testlib.check(res, expected, None, f"Dictionaries differs!\nUnexpected item(s): {set(res.items()).difference(expected.items())}\nMissing items: {set(expected.items()).difference(res.items())}")
    p=2
    if os.path.isfile(outfile):
        try:
            testlib.check_text_file(outfile, expfile)
        except: 
            print("Output file differs! (-1)", end=' ')
        else:         
            print("Output file matches", end=' ')
            p=3
    return p

def test_ex4_1():
    '''
    path = 'ex4/honchos'
    outfile = 'ex41_out.txt'
    expected = {'ex4/honchos/finny.txt': 9481,
                'ex4/honchos/analysable.txt': 1919,
                'ex4/honchos/interlineation.txt': 3295,
                'ex4/honchos/crescendos/sensitisation.txt': 6212}
    '''
    path = 'ex4/honchos'
    testID = 1
    expected = {'ex4/honchos/finny.txt': 9481,
     'ex4/honchos/analysable.txt': 1919,
     'ex4/honchos/interlineation.txt': 3295,
     'ex4/honchos/crescendos/sensitisation.txt': 6212}
    return do_ex4_test(path, testID, expected)

def test_ex4_2():
    '''
    path = 'ex4/cabals'
    outfile = 'ex42_out.txt'
    expected = {'ex4/cabals/results.txt': 8684,
     'ex4/cabals/angering/flatter.txt': 3419,
     'ex4/cabals/angering/lineaments/palaeocene.txt': 2083,
     'ex4/cabals/angering/lineaments/utilization.txt': 4507,
     'ex4/cabals/angering/lineaments/plainclothes.txt': 10155,
     'ex4/cabals/angering/homeostatic.txt': 5537,
     'ex4/cabals/angering/accesses.txt': 2784,
     'ex4/cabals/angering/iberia/erred.txt': 3982,
     'ex4/cabals/angering/iberia/forbear.txt': 7460,
     'ex4/cabals/angering/iberia/sebaceous.txt': 2873,
     'ex4/cabals/angering/iberia/mastering.txt': 6503,
     'ex4/cabals/angering/fingerprinting.txt': 2388,
     'ex4/cabals/angering/bismuth.txt': 7374,
     'ex4/cabals/angering/endive/detains.txt': 9415,
     'ex4/cabals/angering/endive/rebating.txt': 2614,
     'ex4/cabals/angering/endive/rover.txt': 1220,
     'ex4/cabals/angering/endive/sec.txt': 6485,
     'ex4/cabals/angering/proficiency.txt': 2925,
     'ex4/cabals/angering/moulds.txt': 7091,
     'ex4/cabals/vivisect.txt': 9061,
     'ex4/cabals/titanium.txt': 6503,
     'ex4/cabals/ruts.txt': 3885,
     'ex4/cabals/phosphoresces.txt': 3557,
     'ex4/cabals/heartaches.txt': 9147,
     'ex4/cabals/sprague.txt': 6503}
    '''
    path = 'ex4/cabals'
    testID = 2
    expected = {'ex4/cabals/results.txt': 8684,
     'ex4/cabals/angering/flatter.txt': 3419,
     'ex4/cabals/angering/lineaments/palaeocene.txt': 2083,
     'ex4/cabals/angering/lineaments/utilization.txt': 4507,
     'ex4/cabals/angering/lineaments/plainclothes.txt': 10155,
     'ex4/cabals/angering/homeostatic.txt': 5537,
     'ex4/cabals/angering/accesses.txt': 2784,
     'ex4/cabals/angering/iberia/erred.txt': 3982,
     'ex4/cabals/angering/iberia/forbear.txt': 7460,
     'ex4/cabals/angering/iberia/sebaceous.txt': 2873,
     'ex4/cabals/angering/iberia/mastering.txt': 6503,
     'ex4/cabals/angering/fingerprinting.txt': 2388,
     'ex4/cabals/angering/bismuth.txt': 7374,
     'ex4/cabals/angering/endive/detains.txt': 9415,
     'ex4/cabals/angering/endive/rebating.txt': 2614,
     'ex4/cabals/angering/endive/rover.txt': 1220,
     'ex4/cabals/angering/endive/sec.txt': 6485,
     'ex4/cabals/angering/proficiency.txt': 2925,
     'ex4/cabals/angering/moulds.txt': 7091,
     'ex4/cabals/vivisect.txt': 9061,
     'ex4/cabals/titanium.txt': 6503,
     'ex4/cabals/ruts.txt': 3885,
     'ex4/cabals/phosphoresces.txt': 3557,
     'ex4/cabals/heartaches.txt': 9147,
     'ex4/cabals/sprague.txt': 6503}
    return do_ex4_test(path, testID, expected)

def test_ex4_3():
    '''
    path = 'ex4'
    outfile = 'ex43_out.txt'
    expected = {'ex4/cabals/results.txt': 8684,
     'ex4/cabals/angering/flatter.txt': 3419,
     'ex4/cabals/angering/lineaments/palaeocene.txt': 2083,
     'ex4/cabals/angering/lineaments/utilization.txt': 4507,
     'ex4/cabals/angering/lineaments/plainclothes.txt': 10155,
     'ex4/cabals/angering/homeostatic.txt': 5537,
     'ex4/cabals/angering/accesses.txt': 2784,
     'ex4/cabals/angering/iberia/erred.txt': 3982,
     'ex4/cabals/angering/iberia/forbear.txt': 7460,
     'ex4/cabals/angering/iberia/sebaceous.txt': 2873,
     'ex4/cabals/angering/iberia/mastering.txt': 6503,
     'ex4/cabals/angering/fingerprinting.txt': 2388,
     'ex4/cabals/angering/bismuth.txt': 7374,
     'ex4/cabals/angering/endive/detains.txt': 9415,
     'ex4/cabals/angering/endive/rebating.txt': 2614,
     'ex4/cabals/angering/endive/rover.txt': 1220,
     'ex4/cabals/angering/endive/sec.txt': 6485,
     'ex4/cabals/angering/proficiency.txt': 2925,
     'ex4/cabals/angering/moulds.txt': 7091,
     'ex4/cabals/vivisect.txt': 9061,
     'ex4/cabals/titanium.txt': 6503,
     'ex4/cabals/ruts.txt': 3885,
     'ex4/cabals/phosphoresces.txt': 3557,
     'ex4/cabals/heartaches.txt': 9147,
     'ex4/cabals/sprague.txt': 6503,
     'ex4/mermaids.txt': 4307,
     'ex4/anoint.txt': 5894,
     'ex4/bedpan.txt': 2786,
     'ex4/galantines.txt': 4748,
     'ex4/honchos/finny.txt': 9481,
     'ex4/honchos/analysable.txt': 1919,
     'ex4/honchos/interlineation.txt': 3295,
     'ex4/honchos/crescendos/sensitisation.txt': 6212}
    '''
    path = 'ex4'
    testID = 3
    expected = {'ex4/cabals/results.txt': 8684,
     'ex4/cabals/angering/flatter.txt': 3419,
     'ex4/cabals/angering/lineaments/palaeocene.txt': 2083,
     'ex4/cabals/angering/lineaments/utilization.txt': 4507,
     'ex4/cabals/angering/lineaments/plainclothes.txt': 10155,
     'ex4/cabals/angering/homeostatic.txt': 5537,
     'ex4/cabals/angering/accesses.txt': 2784,
     'ex4/cabals/angering/iberia/erred.txt': 3982,
     'ex4/cabals/angering/iberia/forbear.txt': 7460,
     'ex4/cabals/angering/iberia/sebaceous.txt': 2873,
     'ex4/cabals/angering/iberia/mastering.txt': 6503,
     'ex4/cabals/angering/fingerprinting.txt': 2388,
     'ex4/cabals/angering/bismuth.txt': 7374,
     'ex4/cabals/angering/endive/detains.txt': 9415,
     'ex4/cabals/angering/endive/rebating.txt': 2614,
     'ex4/cabals/angering/endive/rover.txt': 1220,
     'ex4/cabals/angering/endive/sec.txt': 6485,
     'ex4/cabals/angering/proficiency.txt': 2925,
     'ex4/cabals/angering/moulds.txt': 7091,
     'ex4/cabals/vivisect.txt': 9061,
     'ex4/cabals/titanium.txt': 6503,
     'ex4/cabals/ruts.txt': 3885,
     'ex4/cabals/phosphoresces.txt': 3557,
     'ex4/cabals/heartaches.txt': 9147,
     'ex4/cabals/sprague.txt': 6503,
     'ex4/mermaids.txt': 4307,
     'ex4/anoint.txt': 5894,
     'ex4/bedpan.txt': 2786,
     'ex4/galantines.txt': 4748,
     'ex4/honchos/finny.txt': 9481,
     'ex4/honchos/analysable.txt': 1919,
     'ex4/honchos/interlineation.txt': 3295,
     'ex4/honchos/crescendos/sensitisation.txt': 6212}
    return do_ex4_test(path, testID, expected)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    #test_ex1_1,   test_ex1_2,  test_ex1_3,           # sort rows and then list
    #test_ex2_1,  test_ex2_2, test_ex2_3,             # disegna quadrati conc.
    test_ex3_1,  test_ex3_2, test_ex3_3,             # tree to count and modify
    #test_ex4_1,  test_ex4_2, test_ex4_3,             # parse tree text and write
    #test_personal_data_entry,
]


if __name__ == '__main__':
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
################################################################################
