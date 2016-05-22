# ['Common imports' begin (DON'T REMOVE THIS LINE!)]
from FoV_CI import *
# ['Common imports' end (DON'T REMOVE THIS LINE!)]

# ['Common definitions for 'Hierarchical State Chart generator'' begin (DON'T REMOVE THIS LINE!)]
# Code items' definitions
def serialCharRead(  ):
    # ['<global>::serialCharRead' begin]
    if not(dre.cte_use_socket):
        dre.char_read=dre.ser.read(1) 
    else:
        readlen=0
        while(readlen<1):
            data = dre.ser.recv(1)
            readlen=len(data)
        dre.char_read=str(data)[0]
    # ['<global>::serialCharRead' end]

def decodeM1Cmd(  ):
    # ['<global>::decodeM1Cmd' begin]
    # Prepare common decoder with M1 values
    dre.mX=dre.m1
    
    # Call common decoder
    DecodeMotorCmd()
    # ['<global>::decodeM1Cmd' end]

def decodeM2Cmd(  ):
    # ['<global>::decodeM2Cmd' begin]
    # Prepare common decoder with M2 values
    dre.mX=dre.m2
    
    # Call common decoder
    DecodeMotorCmd()
    # ['<global>::decodeM2Cmd' end]

def decodeM3Cmd(  ):
    # ['<global>::decodeM3Cmd' begin]
    # Prepare common decoder with M3 values
    dre.mX=dre.m3
    
    # Call common decoder
    DecodeMotorCmd()
    # ['<global>::decodeM3Cmd' end]

def resetDecoder(  ):
    # ['<global>::resetDecoder' begin]
    # Flush commands from M1
    dre.mX.la=False
    dre.mX.np=False
    dre.mX.hosp=False
    dre.mX.goix=False
    dre.mX.apl=False
    dre.mX.gohoseq=False
    dre.mX.reqpos=False
    dre.mX.m=False
    dre.mX.spd=False
    # Flush arguments from M1
    dre.mX.spdarg=0
    dre.mX.posarg=0
    # Flush error
    dre.mX.error=False
    # ['<global>::resetDecoder' end]

def checkCharAtPos( idx, cToCheck, isEqual ):
    # ['<global>::checkCharAtPos' begin]
    if (isEqual):
        return (dre.mX.cmd[idx]==cToCheck)
    else:
        return (dre.mX.cmd[idx]!=cToCheck)
    # ['<global>::checkCharAtPos' end]

# ['Common definitions for 'Hierarchical State Chart generator'' end (DON'T REMOVE THIS LINE!)]

# ['Moving' begin (DON'T REMOVE THIS LINE!)]
# State IDs
ID_MOVING_INITIAL = 0
ID_MOVING_FINAL = 1
ID_MOVING_INTEGRATOR = 2

def Moving(  ):
    # set initial state
    state = ID_MOVING_INITIAL

    while( True ):
        # State ID: ID_MOVING_INITIAL
        if( state==ID_MOVING_INITIAL ):
            # Transition ID: ID_MOVING_TRANSITION_CONNECTION
            state = ID_MOVING_INTEGRATOR

        # State ID: ID_MOVING_INTEGRATOR
        elif( state==ID_MOVING_INTEGRATOR ):
            if( dre.m1setpoint > dre.m1pos ):
                # Transition ID: ID_MOVING_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::incrDelta' begin]
                tmp=dre.m1pos
                dre.m1pos+=1
                print obtainVarName(dre.m1pos)+":"+str(tmp)+"+"+str(1)+"="+str(dre.m1pos)
                # ['<global>::incrDelta' end]

            elif( dre.m1pos > dre.m1setpoint ):
                # Transition ID: ID_MOVING_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::incrDelta' begin]
                tmp=dre.m1pos
                dre.m1pos+=-1
                print obtainVarName(dre.m1pos)+":"+str(tmp)+"+"+str(-1)+"="+str(dre.m1pos)
                # ['<global>::incrDelta' end]

            else:
                # Transition ID: ID_MOVING_TRANSITION_CONNECTION
                state = ID_MOVING_FINAL

        # State ID: ID_MOVING_FINAL
        elif( state==ID_MOVING_FINAL ):
            return ID_MOVING_FINAL

# ['Moving' end (DON'T REMOVE THIS LINE!)]

# ['M1' begin (DON'T REMOVE THIS LINE!)]
# State IDs
ID_M1_INITIAL = 4
ID_M1_FINAL = 5
ID_M1_WAITING = 6

def M1(  ):
    # set initial state
    state = ID_M1_INITIAL

    while( True ):
        # State ID: ID_M1_INITIAL
        if( state==ID_M1_INITIAL ):
            # Transition ID: ID_M1_TRANSITION_CONNECTION
            # Actions:
            # ['<global>::setM1Response' begin]
            dre.m1.resp="OK"
            # ['<global>::setM1Response' end]
            state = ID_M1_WAITING

        # State ID: ID_M1_WAITING
        elif( state==ID_M1_WAITING ):
            if( ((dre.m1.np)==(True)) ):
                # Transition ID: ID_M1_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::setFlag' begin]
                dre.m1.npflag=True
                # ['<global>::setFlag' end]
                state = ID_M1_FINAL

            elif( ((dre.m1.m)==(True)) ):
                # Transition ID: ID_M1_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::setFlag' begin]
                dre.m1.laflag=True
                # ['<global>::setFlag' end]
                state = ID_M1_FINAL

            elif( ((dre.m1.reqpos)==(True)) ):
                # Transition ID: ID_M1_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::setM1Response' begin]
                dre.m1.resp=str(dre.m1.pos)
                # ['<global>::setM1Response' end]
                state = ID_M1_FINAL

            elif( ((dre.m1.la)==(True)) ):
                # Transition ID: ID_M1_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::setVar' begin]
                dre.m1.setpoint=(dre.m1.posarg)
                # ['<global>::setVar' end]
                state = ID_M1_FINAL

            else:
                # Transition ID: ID_M1_TRANSITION_CONNECTION
                state = ID_M1_FINAL

        # State ID: ID_M1_FINAL
        elif( state==ID_M1_FINAL ):
            return ID_M1_FINAL

# ['M1' end (DON'T REMOVE THIS LINE!)]

# ['DecodeMotorCmd' begin (DON'T REMOVE THIS LINE!)]
# State IDs
ID_DECODEMOTORCMD_INITIAL = 7
ID_DECODEMOTORCMD_FINAL = 8
ID_DECODEMOTORCMD_ERROR = 9
ID_DECODEMOTORCMD_NRECEIVED = 10
ID_DECODEMOTORCMD_LRECEIVED = 11
ID_DECODEMOTORCMD_SRECEIVED = 12
ID_DECODEMOTORCMD_PRECEIVED = 13
ID_DECODEMOTORCMD_PORECEIVED = 14

def DecodeMotorCmd(  ):
    # set initial state
    state = ID_DECODEMOTORCMD_INITIAL

    while( True ):
        # State ID: ID_DECODEMOTORCMD_INITIAL
        if( state==ID_DECODEMOTORCMD_INITIAL ):
            if( checkCharAtPos(0, 'N', True) ):
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                # Actions:
                resetDecoder()
                state = ID_DECODEMOTORCMD_NRECEIVED

            elif( checkCharAtPos(0, 'L', True) ):
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                # Actions:
                resetDecoder()
                state = ID_DECODEMOTORCMD_LRECEIVED

            elif( checkCharAtPos(0, 'P', True) ):
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                # Actions:
                resetDecoder()
                state = ID_DECODEMOTORCMD_PRECEIVED

            elif( checkCharAtPos(0, 'M', True) ):
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                # Actions:
                resetDecoder()
                # ['<global>::programM' begin]
                dre.mX.m = True
                # ['<global>::programM' end]
                state = ID_DECODEMOTORCMD_FINAL

            elif( checkCharAtPos(0, 'S', True) ):
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                # Actions:
                resetDecoder()
                state = ID_DECODEMOTORCMD_SRECEIVED

            else:
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                # Actions:
                resetDecoder()
                state = ID_DECODEMOTORCMD_ERROR

        # State ID: ID_DECODEMOTORCMD_NRECEIVED
        elif( state==ID_DECODEMOTORCMD_NRECEIVED ):
            if( checkCharAtPos(1, 'P', True) ):
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::programNP' begin]
                dre.mX.np=True
                # ['<global>::programNP' end]
                state = ID_DECODEMOTORCMD_FINAL

            else:
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                state = ID_DECODEMOTORCMD_ERROR

        # State ID: ID_DECODEMOTORCMD_ERROR
        elif( state==ID_DECODEMOTORCMD_ERROR ):
            # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
            # Actions:
            # ['<global>::decodeError' begin]
            dre.mX.error=True
            # ['<global>::decodeError' end]
            state = ID_DECODEMOTORCMD_FINAL

        # State ID: ID_DECODEMOTORCMD_FINAL
        elif( state==ID_DECODEMOTORCMD_FINAL ):
            return ID_DECODEMOTORCMD_FINAL

        # State ID: ID_DECODEMOTORCMD_LRECEIVED
        elif( state==ID_DECODEMOTORCMD_LRECEIVED ):
            if( checkCharAtPos(1, 'A', True) ):
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::programLA' begin]
                dre.mX.la=True
                dre.mX.posarg=int(dre.mX.cmd[2:])
                # ['<global>::programLA' end]
                state = ID_DECODEMOTORCMD_FINAL

            elif( checkCharAtPos(1, 'R', True) ):
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::programLR' begin]
                dre.mX.lr=True
                dre.mX.posarg=int(dre.mX.cmd[2:])
                # ['<global>::programLR' end]
                state = ID_DECODEMOTORCMD_FINAL

            else:
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                state = ID_DECODEMOTORCMD_ERROR

        # State ID: ID_DECODEMOTORCMD_PRECEIVED
        elif( state==ID_DECODEMOTORCMD_PRECEIVED ):
            if( checkCharAtPos(1, 'O', True) ):
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                state = ID_DECODEMOTORCMD_PORECEIVED

            else:
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                state = ID_DECODEMOTORCMD_ERROR

        # State ID: ID_DECODEMOTORCMD_PORECEIVED
        elif( state==ID_DECODEMOTORCMD_PORECEIVED ):
            if( checkCharAtPos(2, 'S', True) ):
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::programPOS' begin]
                dre.mX.reqpos=True
                # ['<global>::programPOS' end]
                state = ID_DECODEMOTORCMD_FINAL

            else:
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                state = ID_DECODEMOTORCMD_ERROR

        # State ID: ID_DECODEMOTORCMD_SRECEIVED
        elif( state==ID_DECODEMOTORCMD_SRECEIVED ):
            if( checkCharAtPos(1, 'P', True) ):
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::programSP' begin]
                dre.mX.spd = True
                dre.mX.spdarg = int(dre.mX.cmd[2:])
                # ['<global>::programSP' end]
                state = ID_DECODEMOTORCMD_FINAL

            else:
                # Transition ID: ID_DECODEMOTORCMD_TRANSITION_CONNECTION
                state = ID_DECODEMOTORCMD_ERROR

# ['DecodeMotorCmd' end (DON'T REMOVE THIS LINE!)]

# ['ProgramMotors' begin (DON'T REMOVE THIS LINE!)]
# State IDs
ID_PROGRAMMOTORS_INITIAL = 15
ID_PROGRAMMOTORS_FINAL = 16
ID_PROGRAMMOTORS_M2BYPASS = 17
ID_PROGRAMMOTORS_M1BYPASS = 18
ID_PROGRAMMOTORS_M2DECODED = 19
ID_PROGRAMMOTORS_M3DECODED = 20
ID_PROGRAMMOTORS_M1DECODED = 21

def ProgramMotors(  ):
    # set initial state
    state = ID_PROGRAMMOTORS_INITIAL

    while( True ):
        # State ID: ID_PROGRAMMOTORS_INITIAL
        if( state==ID_PROGRAMMOTORS_INITIAL ):
            if( dre.m1.req==True ):
                # Transition ID: ID_PROGRAMMOTORS_TRANSITION_CONNECTION
                # Actions:
                decodeM1Cmd()
                state = ID_PROGRAMMOTORS_M1DECODED

            elif( dre.m1.req==False ):
                # Transition ID: ID_PROGRAMMOTORS_TRANSITION_CONNECTION
                state = ID_PROGRAMMOTORS_M1BYPASS

        # State ID: ID_PROGRAMMOTORS_M1DECODED
        elif( state==ID_PROGRAMMOTORS_M1DECODED ):
            if( dre.m2.req==True ):
                # Transition ID: ID_PROGRAMMOTORS_TRANSITION_CONNECTION
                # Actions:
                decodeM2Cmd()
                state = ID_PROGRAMMOTORS_M2DECODED

            elif( dre.m2.req==False ):
                # Transition ID: ID_PROGRAMMOTORS_TRANSITION_CONNECTION
                state = ID_PROGRAMMOTORS_M2BYPASS

        # State ID: ID_PROGRAMMOTORS_M2DECODED
        elif( state==ID_PROGRAMMOTORS_M2DECODED ):
            if( dre.m3.req==False ):
                # Transition ID: ID_PROGRAMMOTORS_TRANSITION_CONNECTION
                state = ID_PROGRAMMOTORS_FINAL

            elif( dre.m3.req==True ):
                # Transition ID: ID_PROGRAMMOTORS_TRANSITION_CONNECTION
                # Actions:
                decodeM3Cmd()
                state = ID_PROGRAMMOTORS_M3DECODED

        # State ID: ID_PROGRAMMOTORS_FINAL
        elif( state==ID_PROGRAMMOTORS_FINAL ):
            return ID_PROGRAMMOTORS_FINAL

        # State ID: ID_PROGRAMMOTORS_M3DECODED
        elif( state==ID_PROGRAMMOTORS_M3DECODED ):
            # Transition ID: ID_PROGRAMMOTORS_TRANSITION_CONNECTION
            state = ID_PROGRAMMOTORS_FINAL

        # State ID: ID_PROGRAMMOTORS_M2BYPASS
        elif( state==ID_PROGRAMMOTORS_M2BYPASS ):
            if( dre.m3.req==True ):
                # Transition ID: ID_PROGRAMMOTORS_TRANSITION_CONNECTION
                # Actions:
                decodeM3Cmd()
                state = ID_PROGRAMMOTORS_M3DECODED

            elif( dre.m3.req==False ):
                # Transition ID: ID_PROGRAMMOTORS_TRANSITION_CONNECTION
                state = ID_PROGRAMMOTORS_FINAL

        # State ID: ID_PROGRAMMOTORS_M1BYPASS
        elif( state==ID_PROGRAMMOTORS_M1BYPASS ):
            if( dre.m2.req==False ):
                # Transition ID: ID_PROGRAMMOTORS_TRANSITION_CONNECTION
                state = ID_PROGRAMMOTORS_M2BYPASS

            elif( dre.m2.req==True ):
                # Transition ID: ID_PROGRAMMOTORS_TRANSITION_CONNECTION
                # Actions:
                decodeM2Cmd()
                state = ID_PROGRAMMOTORS_M2DECODED

# ['ProgramMotors' end (DON'T REMOVE THIS LINE!)]

# ['CmdDispatcher' begin (DON'T REMOVE THIS LINE!)]
# State IDs
ID_CMDDISPATCHER_INITIAL = 22
ID_CMDDISPATCHER_FINAL = 23
ID_CMDDISPATCHER_DECODEENGINE = 24
ID_CMDDISPATCHER_PROGRAMMOTORS = 25

def CmdDispatcher(  ):
    # set initial state
    state = ID_CMDDISPATCHER_INITIAL

    while( True ):
        # State ID: ID_CMDDISPATCHER_INITIAL
        if( state==ID_CMDDISPATCHER_INITIAL ):
            # Transition ID: ID_CMDDISPATCHER_TRANSITION_CONNECTION
            # Actions:
            # ['<global>::resetDispatcher' begin]
            dre.dispatcher_idx=0
            dre.m1.cmd=""
            dre.m2.cmd=""
            dre.m2.cmd=""
            dre.m1.req=False
            dre.m2.req=False
            dre.m3.req=False
            # ['<global>::resetDispatcher' end]
            state = ID_CMDDISPATCHER_DECODEENGINE

        # State ID: ID_CMDDISPATCHER_DECODEENGINE
        elif( state==ID_CMDDISPATCHER_DECODEENGINE ):
            if( str(1)[0]==dre.command_rx_buf[0] ):
                # Transition ID: ID_CMDDISPATCHER_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::setM1Cmd' begin]
                dre.m1.req=True
                dre.m1.cmd=dre.command_rx_buf[1:]
                # ['<global>::setM1Cmd' end]
                state = ID_CMDDISPATCHER_PROGRAMMOTORS

            elif( str(2)[0]==dre.command_rx_buf[0] ):
                # Transition ID: ID_CMDDISPATCHER_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::setM2Cmd' begin]
                dre.m2.req=True
                dre.m2.cmd=dre.command_rx_buf[1:]
                # ['<global>::setM2Cmd' end]
                state = ID_CMDDISPATCHER_PROGRAMMOTORS

            elif( str(3)[0]==dre.command_rx_buf[0] ):
                # Transition ID: ID_CMDDISPATCHER_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::setM3Cmd' begin]
                dre.m3.req=True
                dre.m3.cmd=dre.command_rx_buf[1:]
                # ['<global>::setM3Cmd' end]
                state = ID_CMDDISPATCHER_PROGRAMMOTORS

            else:
                # Transition ID: ID_CMDDISPATCHER_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::setAllMotorsCmd' begin]
                dre.m1.req=True
                dre.m2.req=True
                dre.m3.req=True
                dre.m1.cmd=dre.command_rx_buf
                dre.m2.cmd=dre.command_rx_buf
                dre.m3.cmd=dre.command_rx_buf
                # ['<global>::setAllMotorsCmd' end]
                state = ID_CMDDISPATCHER_PROGRAMMOTORS

        # State ID: ID_CMDDISPATCHER_PROGRAMMOTORS
        elif( state==ID_CMDDISPATCHER_PROGRAMMOTORS ):
            # call substate function
            programmotors_retval = ProgramMotors(  )
            # Transition ID: ID_CMDDISPATCHER_TRANSITION_CONNECTION
            state = ID_CMDDISPATCHER_FINAL

        # State ID: ID_CMDDISPATCHER_FINAL
        elif( state==ID_CMDDISPATCHER_FINAL ):
            return ID_CMDDISPATCHER_FINAL

# ['CmdDispatcher' end (DON'T REMOVE THIS LINE!)]

# ['sendCtrlResponse' begin (DON'T REMOVE THIS LINE!)]
# State IDs
ID_SENDCTRLRESPONSE_INITIAL = 26
ID_SENDCTRLRESPONSE_FINAL = 27

def sendCtrlResponse(  ):
    # set initial state
    state = ID_SENDCTRLRESPONSE_INITIAL

    while( True ):
        # State ID: ID_SENDCTRLRESPONSE_INITIAL
        if( state==ID_SENDCTRLRESPONSE_INITIAL ):
            # Transition ID: ID_SENDCTRLRESPONSE_TRANSITION_CONNECTION
            # Actions:
            # ['<global>::serialResposeWrite' begin]
            if not(dre.cte_use_socket):
                dre.ser.write(dre.command_tx_buf+'\13'+'\10')
            else:
                dre.ser.sendall(dre.command_tx_buf+'\13'+'\10')
            # ['<global>::serialResposeWrite' end]
            state = ID_SENDCTRLRESPONSE_FINAL

        # State ID: ID_SENDCTRLRESPONSE_FINAL
        elif( state==ID_SENDCTRLRESPONSE_FINAL ):
            return ID_SENDCTRLRESPONSE_FINAL

# ['sendCtrlResponse' end (DON'T REMOVE THIS LINE!)]

# ['getCtrlCommand' begin (DON'T REMOVE THIS LINE!)]
# State IDs
ID_GETCTRLCOMMAND_INITIAL = 28
ID_GETCTRLCOMMAND_FINAL = 29
ID_GETCTRLCOMMAND_READING = 30
ID_GETCTRLCOMMAND_PREVBUF = 31

def getCtrlCommand(  ):
    # set initial state
    state = ID_GETCTRLCOMMAND_INITIAL

    while( True ):
        # State ID: ID_GETCTRLCOMMAND_INITIAL
        if( state==ID_GETCTRLCOMMAND_INITIAL ):
            if( len(dre.rx_buffer)<1 ):
                # Transition ID: ID_GETCTRLCOMMAND_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::resetRxTask' begin]
                dre.command_rx_buf=""
                # ['<global>::resetRxTask' end]
                serialCharRead()
                state = ID_GETCTRLCOMMAND_READING

            else:
                # Transition ID: ID_GETCTRLCOMMAND_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::resetRxTask' begin]
                dre.command_rx_buf=""
                # ['<global>::resetRxTask' end]
                # ['<global>::bufferCharRead' begin]
                dre.char_read=dre.rx_buffer[0]
                dre.rx_buffer=dre.rx_buffer[1:]
                # ['<global>::bufferCharRead' end]
                state = ID_GETCTRLCOMMAND_PREVBUF

        # State ID: ID_GETCTRLCOMMAND_READING
        elif( state==ID_GETCTRLCOMMAND_READING ):
            if( (dre.char_read != '\10') and (dre.char_read != '\13') ):
                # Transition ID: ID_GETCTRLCOMMAND_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::appendCharToRxBuf' begin]
                dre.command_rx_buf+=dre.char_read
                # ['<global>::appendCharToRxBuf' end]
                serialCharRead()

            elif( dre.char_read=='\10' or dre.char_read=='\13' ):
                # Transition ID: ID_GETCTRLCOMMAND_TRANSITION_CONNECTION
                state = ID_GETCTRLCOMMAND_FINAL

        # State ID: ID_GETCTRLCOMMAND_FINAL
        elif( state==ID_GETCTRLCOMMAND_FINAL ):
            return ID_GETCTRLCOMMAND_FINAL

        # State ID: ID_GETCTRLCOMMAND_PREVBUF
        elif( state==ID_GETCTRLCOMMAND_PREVBUF ):
            if( dre.char_read=='\10' or dre.char_read=='\13' ):
                # Transition ID: ID_GETCTRLCOMMAND_TRANSITION_CONNECTION
                state = ID_GETCTRLCOMMAND_FINAL

            elif( len(dre.rx_buffer)<1 ):
                # Transition ID: ID_GETCTRLCOMMAND_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::appendCharToRxBuf' begin]
                dre.command_rx_buf+=dre.char_read
                # ['<global>::appendCharToRxBuf' end]
                serialCharRead()
                state = ID_GETCTRLCOMMAND_READING

            else:
                # Transition ID: ID_GETCTRLCOMMAND_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::bufferCharRead' begin]
                dre.char_read=dre.rx_buffer[0]
                dre.rx_buffer=dre.rx_buffer[1:]
                # ['<global>::bufferCharRead' end]
                # ['<global>::appendCharToRxBuf' begin]
                dre.command_rx_buf+=dre.char_read
                # ['<global>::appendCharToRxBuf' end]

# ['getCtrlCommand' end (DON'T REMOVE THIS LINE!)]

# ['sendCtrlCommand' begin (DON'T REMOVE THIS LINE!)]
# State IDs
ID_SENDCTRLCOMMAND_INITIAL = 32
ID_SENDCTRLCOMMAND_FINAL = 33

def sendCtrlCommand(  ):
    # set initial state
    state = ID_SENDCTRLCOMMAND_INITIAL

    while( True ):
        # State ID: ID_SENDCTRLCOMMAND_INITIAL
        if( state==ID_SENDCTRLCOMMAND_INITIAL ):
            # Transition ID: ID_SENDCTRLCOMMAND_TRANSITION_CONNECTION
            # Actions:
            # ['<global>::serialCommandWrite' begin]
            if not(dre.cte_use_socket):
                dre.ser.write(dre.command_tx_buf+'\13')
            else:
                dre.ser.sendall(dre.command_tx_buf+'\13')
            # ['<global>::serialCommandWrite' end]
            state = ID_SENDCTRLCOMMAND_FINAL

        # State ID: ID_SENDCTRLCOMMAND_FINAL
        elif( state==ID_SENDCTRLCOMMAND_FINAL ):
            return ID_SENDCTRLCOMMAND_FINAL

# ['sendCtrlCommand' end (DON'T REMOVE THIS LINE!)]

# ['getCtrlResponse' begin (DON'T REMOVE THIS LINE!)]
# State IDs
ID_GETCTRLRESPONSE_INITIAL = 34
ID_GETCTRLRESPONSE_FINAL = 35
ID_GETCTRLRESPONSE_READING = 36
ID_GETCTRLRESPONSE_FINISHING = 37

def getCtrlResponse(  ):
    # set initial state
    state = ID_GETCTRLRESPONSE_INITIAL

    while( True ):
        # State ID: ID_GETCTRLRESPONSE_INITIAL
        if( state==ID_GETCTRLRESPONSE_INITIAL ):
            # Transition ID: ID_GETCTRLRESPONSE_TRANSITION_CONNECTION
            # Actions:
            # ['<global>::resetRxTask' begin]
            dre.command_rx_buf=""
            # ['<global>::resetRxTask' end]
            serialCharRead()
            state = ID_GETCTRLRESPONSE_READING

        # State ID: ID_GETCTRLRESPONSE_READING
        elif( state==ID_GETCTRLRESPONSE_READING ):
            if( (dre.char_read != '\10') and (dre.char_read != '\13') ):
                # Transition ID: ID_GETCTRLRESPONSE_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::appendCharToRxBuf' begin]
                dre.command_rx_buf+=dre.char_read
                # ['<global>::appendCharToRxBuf' end]
                serialCharRead()

            elif( dre.char_read=='\10' or dre.char_read=='\13' ):
                # Transition ID: ID_GETCTRLRESPONSE_TRANSITION_CONNECTION
                # Actions:
                serialCharRead()
                state = ID_GETCTRLRESPONSE_FINISHING

        # State ID: ID_GETCTRLRESPONSE_FINISHING
        elif( state==ID_GETCTRLRESPONSE_FINISHING ):
            if( (dre.char_read != '\10') and (dre.char_read != '\13') ):
                # Transition ID: ID_GETCTRLRESPONSE_TRANSITION_CONNECTION
                # Actions:
                serialCharRead()

            elif( dre.char_read=='\10' or dre.char_read=='\13' ):
                # Transition ID: ID_GETCTRLRESPONSE_TRANSITION_CONNECTION
                state = ID_GETCTRLRESPONSE_FINAL

        # State ID: ID_GETCTRLRESPONSE_FINAL
        elif( state==ID_GETCTRLRESPONSE_FINAL ):
            return ID_GETCTRLRESPONSE_FINAL

# ['getCtrlResponse' end (DON'T REMOVE THIS LINE!)]

# ['M1Movement' begin (DON'T REMOVE THIS LINE!)]
# State IDs
ID_M1MOVEMENT_INITIAL = 4
ID_M1MOVEMENT_FINAL = 5
ID_M1MOVEMENT_STEPDONE = 6
ID_M1MOVEMENT_ENABLE = 7

def M1Movement(  ):
    # set initial state
    state = ID_M1MOVEMENT_INITIAL

    while( True ):
        # State ID: ID_M1MOVEMENT_INITIAL
        if( state==ID_M1MOVEMENT_INITIAL ):
            if( ((dre.m1.laflag)==(True)) ):
                # Transition ID: ID_M1MOVEMENT_TRANSITION_CONNECTION
                state = ID_M1MOVEMENT_ENABLE

            else:
                # Transition ID: ID_M1MOVEMENT_TRANSITION_CONNECTION
                state = ID_M1MOVEMENT_FINAL

        # State ID: ID_M1MOVEMENT_ENABLE
        elif( state==ID_M1MOVEMENT_ENABLE ):
            if( dre.m1.setpoint > dre.m1.pos ):
                # Transition ID: ID_M1MOVEMENT_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::incrDelta' begin]
                tmp=dre.m1.pos
                dre.m1.pos+=+1
                #print obtainVarName(dre.m1.pos)+":"+str(tmp)+"+"+str(+1)+"="+str(dre.m1.pos)
                # ['<global>::incrDelta' end]
                state = ID_M1MOVEMENT_STEPDONE

            elif( dre.m1.pos > dre.m1.setpoint ):
                # Transition ID: ID_M1MOVEMENT_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::incrDelta' begin]
                tmp=dre.m1.pos
                dre.m1.pos+=-1
                #print obtainVarName(dre.m1.pos)+":"+str(tmp)+"+"+str(-1)+"="+str(dre.m1.pos)
                # ['<global>::incrDelta' end]
                state = ID_M1MOVEMENT_STEPDONE

            else:
                # Transition ID: ID_M1MOVEMENT_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::notifyEndMv' begin]
                if (dre.m1.npflag):
                    sendUntimelyResponse("p")
                # ['<global>::notifyEndMv' end]
                # ['<global>::setFlag' begin]
                dre.m1.npflag=False
                # ['<global>::setFlag' end]
                # ['<global>::setFlag' begin]
                dre.m1.laflag=False
                # ['<global>::setFlag' end]
                state = ID_M1MOVEMENT_FINAL

        # State ID: ID_M1MOVEMENT_STEPDONE
        elif( state==ID_M1MOVEMENT_STEPDONE ):
            # Transition ID: ID_M1MOVEMENT_TRANSITION_CONNECTION
            state = ID_M1MOVEMENT_FINAL

        # State ID: ID_M1MOVEMENT_FINAL
        elif( state==ID_M1MOVEMENT_FINAL ):
            return ID_M1MOVEMENT_FINAL

# ['M1Movement' end (DON'T REMOVE THIS LINE!)]

# ['M1Sim' begin (DON'T REMOVE THIS LINE!)]
# State IDs
ID_M1SIM_INITIAL = 0
ID_M1SIM_FINAL = 1
ID_M1SIM_IDLE = 2
ID_M1SIM_MOVING = 3

def M1Sim(  ):
    # set initial state
    state = ID_M1SIM_INITIAL

    while( True ):
        # State ID: ID_M1SIM_INITIAL
        if( state==ID_M1SIM_INITIAL ):
            # Transition ID: ID_M1SIM_TRANSITION_CONNECTION
            state = ID_M1SIM_IDLE

        # State ID: ID_M1SIM_IDLE
        elif( state==ID_M1SIM_IDLE ):
            if( ((dre.m1.laflag)==(True)) ):
                # Transition ID: ID_M1SIM_TRANSITION_CONNECTION
                state = ID_M1SIM_MOVING

            elif( ((dre.m1.simstop)==(True)) ):
                # Transition ID: ID_M1SIM_TRANSITION_CONNECTION
                state = ID_M1SIM_FINAL

        # State ID: ID_M1SIM_MOVING
        elif( state==ID_M1SIM_MOVING ):
            if( dre.m1.pos > dre.m1.setpoint ):
                # Transition ID: ID_M1SIM_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::incrDelta' begin]
                tmp=dre.m1.pos
                dre.m1.pos+=-1
                #print obtainVarName(dre.m1.pos)+":"+str(tmp)+"+"+str(-1)+"="+str(dre.m1.pos)
                # ['<global>::incrDelta' end]

            elif( dre.m1.setpoint > dre.m1.pos ):
                # Transition ID: ID_M1SIM_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::incrDelta' begin]
                tmp=dre.m1.pos
                dre.m1.pos+=1
                #print obtainVarName(dre.m1.pos)+":"+str(tmp)+"+"+str(1)+"="+str(dre.m1.pos)
                # ['<global>::incrDelta' end]

            else:
                # Transition ID: ID_M1SIM_TRANSITION_CONNECTION
                # Actions:
                # ['<global>::notifyEndMv' begin]
                if (dre.m1.npflag):
                    sendUntimelyResponse("p")
                # ['<global>::notifyEndMv' end]
                # ['<global>::setFlag' begin]
                dre.m1.npflag=False
                # ['<global>::setFlag' end]
                # ['<global>::setFlag' begin]
                dre.m1.laflag=False
                # ['<global>::setFlag' end]
                state = ID_M1SIM_IDLE

        # State ID: ID_M1SIM_FINAL
        elif( state==ID_M1SIM_FINAL ):
            return ID_M1SIM_FINAL

# ['M1Sim' end (DON'T REMOVE THIS LINE!)]
