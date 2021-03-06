import DRE
from threading import Thread, Lock
# ['Common definitions for 'Code items generator'' begin (DON'T REMOVE THIS LINE!)]
# Generic code items' definitions
dre = DRE.DRE()

def obtainVarName( variable ):
    # ['<global>::obtainVarName' begin]
    for k, v in locals().items():
        if v is variable:
            a_as_str = k
    return a_as_str
    # ['<global>::obtainVarName' end]

def sendUntimelyResponse( resptosend ):
    # ['<global>::sendUntimelyResponse' begin]
    if not(dre.disable_untimely_resp):
        if not(dre.cte_use_socket):
            dre.ser.write(resptosend+chr(13)+chr(10))
        else:
            dre.ser.sendall(resptosend+chr(13)+chr(10))
    # ['<global>::sendUntimelyResponse' end]

# ['Common definitions for 'Code items generator'' end (DON'T REMOVE THIS LINE!)]
