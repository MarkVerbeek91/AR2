

class kinetics():

  def __init__():
    self.B = []
    self.C = []
    self.D = []
    self.E = []
    self.F = []
    self.F = []
    self.F = []


  def ForwardKinetics(self, joints)
    for joint in joints:
      if joint.CurrentAngle == 0:
        joint.CureentAngle == 0.001

    ## CONVERT TO RADIANS
    
      self.C[4,13] = math.radians(float(joint.CureentAngle)+DHt1)
      self.C[5,14] = math.radians(float(J2AngCur)+DHt2)
    C6 = math.radians(float(J3AngCur)+DHt3)
    C7 = math.radians(float(J4AngCur)+DHt4)
    C8 = math.radians(float(J5AngCur)+DHt5)
    C9 = math.radians(float(J6AngCur)+DHt6)
    ## DH TABLE
    C13 = C4
    C14 = C5
    C15 = C6
    C16 = C7
    C17 = C8
    C18 = C9
    D13 = math.radians(DHr1)
    D14 = math.radians(DHr2)
    D15 = math.radians(DHr3)
    D16 = math.radians(DHr4)
    D17 = math.radians(DHr5)
    D18 = math.radians(DHr6)
    E13 = DHd1
    E14 = DHd2
    E15 = DHd3
    E16 = DHd4
    E17 = DHd5
    E18 = DHd6
    F13 = DHa1
    F14 = DHa2
    F15 = DHa3
    F16 = DHa4
    F17 = DHa5
    F18 = DHa6
    ## WORK FRAME INPUT
    H13 = float(UFxEntryField.get()) 
    H14 = float(UFyEntryField.get())  
    H15 = float(UFzEntryField.get())
    H16 = float(UFrxEntryField.get()) 
    H17 = float(UFryEntryField.get()) 
    H18 = float(UFrzEntryField.get()) 
    ## TOOL FRAME INPUT
    J13 = float(TFxEntryField.get()) 
    J14 = float(TFyEntryField.get())  
    J15 = float(TFzEntryField.get())
    J16 = float(TFrxEntryField.get()) 
    J17 = float(TFryEntryField.get()) 
    J18 = float(TFrzEntryField.get())
    ## WORK FRAME TABLE
    B21 = math.cos(math.radians(H18))*math.cos(math.radians(H17))
    B22 = math.sin(math.radians(H18))*math.cos(math.radians(H17))
    B23 = -math.sin(math.radians(H18))
    B24 = 0
    C21 = -math.sin(math.radians(H18))*math.cos(math.radians(H16))+math.cos(math.radians(H18))*math.sin(math.radians(H17))*math.sin(math.radians(H16))
    C22 = math.cos(math.radians(H18))*math.cos(math.radians(H16))+math.sin(math.radians(H18))*math.sin(math.radians(H17))*math.sin(math.radians(H16))
    C23 = math.cos(math.radians(H17))*math.sin(math.radians(H16))
    C24 = 0
    D21 = math.sin(math.radians(H18))*math.sin(math.radians(H16))+math.cos(math.radians(H18))*math.sin(math.radians(H17))*math.cos(math.radians(H16))
    D22 = -math.cos(math.radians(H18))*math.sin(math.radians(H16))+math.sin(math.radians(H18))*math.sin(math.radians(H17))*math.cos(math.radians(H16))
    D23 = math.cos(math.radians(H17))*math.cos(math.radians(H16))
    D24 = 0
    E21 = H13
    E22 = H14
    E23 = H15
    E24 = 1 
    ## J1 FRAME
    B27 = math.cos(C13)
    B28 = math.sin(C13)
    B29 = 0
    B30 = 0
    C27 = -math.sin(C13)*math.cos(D13)
    C28 = math.cos(C13)*math.cos(D13)
    C29 = math.sin(D13)
    C30 = 0  
    D27 = math.sin(C13)*math.sin(D13)
    D28 = -math.cos(C13)*math.sin(D13)
    D29 = math.cos(D13)
    D30 = 0 
    E27 = F13*math.cos(C13)
    E28 = F13*math.sin(C13)
    E29 = E13
    E30 = 1
    ## J2 FRAME
    B33 = math.cos(C14)
    B34 = math.sin(C14)
    B35 = 0
    B36 = 0
    C33 = -math.sin(C14)*math.cos(D14)
    C34 = math.cos(C14)*math.cos(D14)
    C35 = math.sin(D14)
    C36 = 0
    D33 = math.sin(C14)*math.sin(D14)
    D34 = -math.cos(C14)*math.sin(D14)
    D35 = math.cos(D14)
    D36 = 0
    E33 = F14*math.cos(C14)
    E34 = F14*math.sin(C14)
    E35 = E14
    E36 = 1
    ## J3 FRAME 
    B39 = math.cos(C15)
    B40 = math.sin(C15)
    B41 = 0
    B42 = 0
    C39 = -math.sin(C15)*math.cos(D15)
    C40 = math.cos(C15)*math.cos(D15)
    C41 = math.sin(D15)
    C42 = 0
    D39 = math.sin(C15)*math.sin(D15)
    D40 = -math.cos(C15)*math.sin(D15)
    D41 = math.cos(D15)
    D42 = 0
    E39 = F15*math.cos(C15)
    E40 = F15*math.sin(C15)
    E41 = 0
    E42 = 1
    ## J4 FRAME 
    B45 = math.cos(C16)
    B46 = math.sin(C16)
    B47 = 0
    B48 = 0
    C45 = -math.sin(C16)*math.cos(D16)
    C46 = math.cos(C16)*math.cos(D16)
    C47 = math.sin(D16)
    C48 = 0
    D45 = math.sin(C16)*math.sin(D16)
    D46 = -math.cos(C16)*math.sin(D16)
    D47 = math.cos(D16)
    D48 = 0
    E45 = F16*math.cos(C16)
    E46 = F16*math.sin(C16)
    E47 = E16
    E48 = 1
    ## J5 FRAME 
    B51 = math.cos(C17)
    B52 = math.sin(C17)
    B53 = 0
    B54 = 0
    C51 = -math.sin(C17)*math.cos(D17)
    C52 = math.cos(C17)*math.cos(D17)
    C53 = math.sin(D17)
    C54 = 0 
    D51 = math.sin(C17)*math.sin(D17)
    D52 = -math.cos(C17)*math.sin(D17)
    D53 = math.cos(D17)
    D54 = 0
    E51 = F17*math.cos(C17)
    E52 = F17*math.sin(C17)
    E53 = E17
    E54 = 1
    ## J6 FRAME
    B57 = math.cos(C18)
    B58 = math.sin(C18)
    B59 = 0
    B60 = 0
    C57 = -math.sin(C18)*math.cos(D18)
    C58 = math.cos(C18)*math.cos(D18)
    C59 = math.sin(D18)
    C60 = 0
    D57 = math.sin(C18)*math.sin(D18)
    D58 = -math.cos(C18)*math.sin(D18)
    D59 = math.cos(D18)
    D60 = 0
    E57 = F18*math.cos(C18)
    E58 = F18*math.sin(C18)
    E59 = E18
    E60 = 1
    ## TOOL FRAME
    B63 = math.cos(math.radians(J18))*math.cos(math.radians(J17))
    B64 = math.sin(math.radians(J18))*math.cos(math.radians(J17))
    B65 = -math.sin(math.radians(J18))
    B66 = 0
    C63 = -math.sin(math.radians(J18))*math.cos(math.radians(J16))+math.cos(math.radians(J18))*math.sin(math.radians(J17))*math.sin(math.radians(J16))
    C64 = math.cos(math.radians(J18))*math.cos(math.radians(J16))+math.sin(math.radians(J18))*math.sin(math.radians(J17))*math.sin(math.radians(J16))
    C65 = math.cos(math.radians(J17))*math.sin(math.radians(J16))
    C66 = 0
    D63 = math.sin(math.radians(J18))*math.sin(math.radians(J16))+math.cos(math.radians(J18))*math.sin(math.radians(J17))*math.cos(math.radians(J16))
    D64 = -math.cos(math.radians(J18))*math.sin(math.radians(J16))+math.sin(math.radians(J18))*math.sin(math.radians(J17))*math.cos(math.radians(J16))
    D65 = math.cos(math.radians(J17))*math.cos(math.radians(J16))
    D66 = 0
    E63 = J13
    E64 = J14
    E65 = J15
    E66 = 1
    ## WF*J1
    G24 = (B21*B27)+(C21*B28)+(D21*B29)+(E21*B30)
    G25 = (B22*B27)+(C22*B28)+(D22*B29)+(E22*B30)
    G26 = (B23*B27)+(C23*B28)+(D23*B29)+(E23*B30)
    G27 = (B24*B27)+(C24*B28)+(D24*B29)+(E24*B30)
    H24 = (B21*C27)+(C21*C28)+(D21*C29)+(E21*C30)
    H25 = (B22*C27)+(C22*C28)+(D22*C29)+(E22*C30)
    H26 = (B23*C27)+(C23*C28)+(D23*C29)+(E23*C30)
    H27 = (B24*C27)+(C24*C28)+(D24*C29)+(E24*C30)
    I24 = (B21*D27)+(C21*D28)+(D21*D29)+(E21*D30)
    I25 = (B22*D27)+(C22*D28)+(D22*D29)+(E22*D30)
    I26 = (B23*D27)+(C23*D28)+(D23*D29)+(E23*D30)
    I27 = (B24*D27)+(C24*D28)+(D24*D29)+(E24*D30)
    J24 = (B21*E27)+(C21*E28)+(D21*E29)+(E21*E30)
    J25 = (B22*E27)+(C22*E28)+(D22*E29)+(E22*E30)
    J26 = (B23*E27)+(C23*E28)+(D23*E29)+(E23*E30)
    J27 = (B24*E27)+(C24*E28)+(D24*E29)+(E24*E30)
    ## (WF*J1)*J2
    G30 = (G24*B33)+(H24*B34)+(I24*B35)+(J24*B36)
    G31 = (G25*B33)+(H25*B34)+(I25*B35)+(J25*B36)
    G32 = (G26*B33)+(H26*B34)+(I26*B35)+(J26*B36)
    G33 = (G27*B33)+(H27*B34)+(I27*B35)+(J27*B36)
    H30 = (G24*C33)+(H24*C34)+(I24*C35)+(J24*C36)
    H31 = (G25*C33)+(H25*C34)+(I25*C35)+(J25*C36)
    H32 = (G26*C33)+(H26*C34)+(I26*C35)+(J26*C36)
    H33 = (G27*C33)+(H27*C34)+(I27*C35)+(J27*C36)
    I30 = (G24*D33)+(H24*D34)+(I24*D35)+(J24*D36)
    I31 = (G25*D33)+(H25*D34)+(I25*D35)+(J25*D36)
    I32 = (G26*D33)+(H26*D34)+(I26*D35)+(J26*D36)
    I33 = (G27*D33)+(H27*D34)+(I27*D35)+(J27*D36)
    J30 = (G24*E33)+(H24*E34)+(I24*E35)+(J24*E36)
    J31 = (G25*E33)+(H25*E34)+(I25*E35)+(J25*E36)
    J32 = (G26*E33)+(H26*E34)+(I26*E35)+(J26*E36)
    J33 = (G27*E33)+(H27*E34)+(I27*E35)+(J27*E36)
    ## (WF*J1*J2)*J3
    G36 = (G30*B39)+(H30*B40)+(I30*B41)+(J30*B42) 
    G37 = (G31*B39)+(H31*B40)+(I31*B41)+(J31*B42)  
    G38 = (G32*B39)+(H32*B40)+(I32*B41)+(J32*B42)  
    G39 = (G33*B39)+(H33*B40)+(I33*B41)+(J33*B42)  
    H36 = (G30*C39)+(H30*C40)+(I30*C41)+(J30*C42)  
    H37 = (G31*C39)+(H31*C40)+(I31*C41)+(J31*C42)  
    H38 = (G32*C39)+(H32*C40)+(I32*C41)+(J32*C42)  
    H39 = (G33*C39)+(H33*C40)+(I33*C41)+(J33*C42)  
    I36 = (G30*D39)+(H30*D40)+(I30*D41)+(J30*D42)  
    I37 = (G31*D39)+(H31*D40)+(I31*D41)+(J31*D42)  
    I38 = (G32*D39)+(H32*D40)+(I32*D41)+(J32*D42)  
    I39 = (G33*D39)+(H33*D40)+(I33*D41)+(J33*D42)  
    J36 = (G30*E39)+(H30*E40)+(I30*E41)+(J30*E42)  
    J37 = (G31*E39)+(H31*E40)+(I31*E41)+(J31*E42)  
    J38 = (G32*E39)+(H32*E40)+(I32*E41)+(J32*E42)  
    J39 = (G33*E39)+(H33*E40)+(I33*E41)+(J33*E42)
    ## (WF*J1*J2*J3)*J4
    G42 = (G36*B45)+(H36*B46)+(I36*B47)+(J36*B48)  
    G43 = (G37*B45)+(H37*B46)+(I37*B47)+(J37*B48) 
    G44 = (G38*B45)+(H38*B46)+(I38*B47)+(J38*B48) 
    G45 = (G39*B45)+(H39*B46)+(I39*B47)+(J39*B48) 
    H42 = (G36*C45)+(H36*C46)+(I36*C47)+(J36*C48)  
    H43 = (G37*C45)+(H37*C46)+(I37*C47)+(J37*C48) 
    H44 = (G38*C45)+(H38*C46)+(I38*C47)+(J38*C48) 
    H45 = (G39*C45)+(H39*C46)+(I39*C47)+(J39*C48) 
    I42 = (G36*D45)+(H36*D46)+(I36*D47)+(J36*D48)  
    I43 = (G37*D45)+(H37*D46)+(I37*D47)+(J37*D48) 
    I44 = (G38*D45)+(H38*D46)+(I38*D47)+(J38*D48) 
    I45 = (G39*D45)+(H39*D46)+(I39*D47)+(J39*D48) 
    J42 = (G36*E45)+(H36*E46)+(I36*E47)+(J36*E48)  
    J43 = (G37*E45)+(H37*E46)+(I37*E47)+(J37*E48) 
    J44 = (G38*E45)+(H38*E46)+(I38*E47)+(J38*E48) 
    J45 = (G39*E45)+(H39*E46)+(I39*E47)+(J39*E48)
    ## (WF*J1*J2*J3*J4)*J5
    G48 = (G42*B51)+(H42*B52)+(I42*B53)+(J42*B54)
    G49 = (G43*B51)+(H43*B52)+(I43*B53)+(J43*B54)
    G50 = (G44*B51)+(H44*B52)+(I44*B53)+(J44*B54)
    G51 = (G45*B51)+(H45*B52)+(I45*B53)+(J45*B54)
    H48 = (G42*C51)+(H42*C52)+(I42*C53)+(J42*C54)
    H49 = (G43*C51)+(H43*C52)+(I43*C53)+(J43*C54)
    H50 = (G44*C51)+(H44*C52)+(I44*C53)+(J44*C54)
    H51 = (G45*C51)+(H45*C52)+(I45*C53)+(J45*C54)
    I48 = (G42*D51)+(H42*D52)+(I42*D53)+(J42*D54)
    I49 = (G43*D51)+(H43*D52)+(I43*D53)+(J43*D54)
    I50 = (G44*D51)+(H44*D52)+(I44*D53)+(J44*D54)
    I51 = (G45*D51)+(H45*D52)+(I45*D53)+(J45*D54)
    J48 = (G42*E51)+(H42*E52)+(I42*E53)+(J42*E54)
    J49 = (G43*E51)+(H43*E52)+(I43*E53)+(J43*E54)
    J50 = (G44*E51)+(H44*E52)+(I44*E53)+(J44*E54)
    J51 = (G45*E51)+(H45*E52)+(I45*E53)+(J45*E54)
    ## (WF*J1*J2*J3*J4*J5)*J6 
    G54 = (G48*B57)+(H48*B58)+(I48*B59)+(J48*B60)
    G55 = (G49*B57)+(H49*B58)+(I49*B59)+(J49*B60)
    G56 = (G50*B57)+(H50*B58)+(I50*B59)+(J50*B60)
    G57 = (G51*B57)+(H51*B58)+(I51*B59)+(J51*B60)
    H54 = (G48*C57)+(H48*C58)+(I48*C59)+(J48*C60)
    H55 = (G49*C57)+(H49*C58)+(I49*C59)+(J49*C60)
    H56 = (G50*C57)+(H50*C58)+(I50*C59)+(J50*C60)
    H57 = (G51*C57)+(H51*C58)+(I51*C59)+(J51*C60)
    I54 = (G48*D57)+(H48*D58)+(I48*D59)+(J48*D60)
    I55 = (G49*D57)+(H49*D58)+(I49*D59)+(J49*D60)
    I56 = (G50*D57)+(H50*D58)+(I50*D59)+(J50*D60)
    I57 = (G51*D57)+(H51*D58)+(I51*D59)+(J51*D60)
    J54 = (G48*E57)+(H48*E58)+(I48*E59)+(J48*E60)
    J55 = (G49*E57)+(H49*E58)+(I49*E59)+(J49*E60)
    J56 = (G50*E57)+(H50*E58)+(I50*E59)+(J50*E60)
    J57 = (G51*E57)+(H51*E58)+(I51*E59)+(J51*E60)
    ## (WF*J1*J2*J3*J4*J5*J6)*TF
    G60 = (G54*B63)+(H54*B64)+(I54*B65)+(J54*B66)
    G61 = (G55*B63)+(H55*B64)+(I55*B65)+(J55*B66)
    G62 = (G56*B63)+(H56*B64)+(I56*B65)+(J56*B66)
    G63 = (G57*B63)+(H57*B64)+(I57*B65)+(J57*B66)
    H60 = (G54*C63)+(H54*C64)+(I54*C65)+(J54*C66)
    H61 = (G55*C63)+(H55*C64)+(I55*C65)+(J55*C66)
    H62 = (G56*C63)+(H56*C64)+(I56*C65)+(J56*C66)
    H63 = (G57*C63)+(H57*C64)+(I57*C65)+(J57*C66)
    I60 = (G54*D63)+(H54*D64)+(I54*D65)+(J54*D66)
    I61 = (G55*D63)+(H55*D64)+(I55*D65)+(J55*D66)
    I62 = (G56*D63)+(H56*D64)+(I56*D65)+(J56*D66)
    I63 = (G57*D63)+(H57*D64)+(I57*D65)+(J57*D66)
    J60 = (G54*E63)+(H54*E64)+(I54*E65)+(J54*E66)
    J61 = (G55*E63)+(H55*E64)+(I55*E65)+(J55*E66)
    J62 = (G56*E63)+(H56*E64)+(I56*E65)+(J56*E66)
    J63 = (G57*E63)+(H57*E64)+(I57*E65)+(J57*E66)
    ## SET ORIENTATION MARKERS
    if E28 < 0:
      if E27 < 0:
        E7 = 1
      else: E7 = 2
    else:
      if E27 < 0:
        E7 = 4
      else: E7 = 3
    ##
    if J49 < 0:
      if J48 < 0:
        E8 = 1
      else:
        E8 = 2
    else:
      if J48 < 0:
        E8 = 4
      else:
        E8 = 3
    ## GET YPR
    I8 = math.atan2(math.sqrt((I60**2)+(I61**2)),-I62)  
    I7 = math.atan2((G62/I8),(H62/I8))  
    I9 = math.atan2((I60/I8),(I61/I8))
    H4 = J48
    H5 = J49
    H6 = J50
    H7 = math.degrees(I7)
    H8 = math.degrees(I8)
    H9 = math.degrees(I9)  
    XcurPos = J48
    YcurPos = J49
    ZcurPos = J50
    RxcurPos = H7
    RycurPos = H8
    RzcurPos = H9
    
  def ReversKinetics(self, joints)
    
    P13 = math.atan((H5+CY)/(H4+CX))
    if E7 == 1:
      Q13 = (math.degrees(P13)-90)-90
    else:
      if E7 == 2:
        Q13 = math.degrees(P13)
      else:
        if E7 == 3:
          Q13 = math.degrees(P13)
        else:
          Q13 = 90+math.degrees(P13)+90
    P14 = math.sqrt(((H5+CY)**2)+((H4+CX)**2))+DHa1
    P15 = math.sqrt(((H5+CY)**2)+((H4+CX)**2))
    P16 = abs(P15-DHa1)
    Q16 = P15-DHa1
    P17 = (H6+CZ)-DHd1
    if E7 == E8:
      P19 = math.sqrt((P16**2)+(P17**2))
    else:
      P19 = math.sqrt((P14**2)+(P17**2))
    P22 = math.atan(P17/P16)
    Q22 = math.degrees(P22)
    P23 = math.atan(P16/P17)
    Q23 = math.degrees(P23)
    P24 = math.sqrt((DHa3**2)+((abs(DHd4)**2)))
    P25 = math.atan(P17/P14)
    Q25 = math.degrees(P25)
    P26 = math.acos(((DHa2**2)+(P19**2)-(P24**2))/(2*DHa2*P19))
    Q26 = math.degrees(P26)
    P27 = math.atan2(math.sqrt(1-((((DHa2**2)+(P19**2)-(P24**2))/(2*DHa2*P19)))**2),(((DHa2**2)+(P19**2)-(P24**2))/(2*DHa2*P19)))
    Q27 = math.degrees(P27)
    if Q16>0 and E7==E8:
      Q28 = -(Q22+Q26)
    else:
      if Q16>0 and E7!=E8:
        Q28 = -(180-Q25+Q26)
      else:
        if Q16<0 and E7!=E8:
          Q28 = -(180-Q25+Q26)
        else:
          Q28 = -(Q26+Q23+90)
    P30 = math.acos(((P24**2)+(abs(DHd4)**2)-(DHa3**2))/(2*P24*abs(DHd4)))
    Q30 = math.degrees(P30)
    P32 = math.acos(((P24**2)+(DHa2**2)-(P19**2))/(2*P24*DHa2))
    Q32 = 180-math.degrees(P32)+Q30
    Q4 = Q13
    Q5 = Q28
    Q6 = Q32
    P37 = math.radians(Q4)
    P38 = math.radians(Q5)
    P39 = math.radians(Q6-90)
    Q37 = math.radians(-90)
    Q38 = math.radians(0)
    Q39 = math.radians(90)
    R37 = DHd1
    R38 = DHd2
    R39 = DHd3
    S37 = DHa1
    S38 = DHa2
    S39 = DHa3
    ## WORK FRAME INPUT
    H13 = float(UFxEntryField.get()) 
    H14 = float(UFyEntryField.get())  
    H15 = float(UFzEntryField.get())
    H16 = float(UFrxEntryField.get()) 
    H17 = float(UFryEntryField.get()) 
    H18 = float(UFrzEntryField.get()) 
    ## WORK FRAME TABLE
    O45 = math.cos(math.radians(H18))*math.cos(math.radians(H17))
    O46 = math.sin(math.radians(H18))*math.cos(math.radians(H17))
    O47 = -math.sin(math.radians(H18))
    O48 = 0
    P45 = -math.sin(math.radians(H18))*math.cos(math.radians(H16))+math.cos(math.radians(H18))*math.sin(math.radians(H17))*math.sin(math.radians(H16))
    P46 = math.cos(math.radians(H18))*math.cos(math.radians(H16))+math.sin(math.radians(H18))*math.sin(math.radians(H17))*math.sin(math.radians(H16))
    P47 = math.cos(math.radians(H17))*math.sin(math.radians(H16))
    P48 = 0
    Q45 = math.sin(math.radians(H18))*math.sin(math.radians(H16))+math.cos(math.radians(H18))*math.sin(math.radians(H17))*math.cos(math.radians(H16))
    Q46 = -math.cos(math.radians(H18))*math.sin(math.radians(H16))+math.sin(math.radians(H18))*math.sin(math.radians(H17))*math.cos(math.radians(H16))
    Q47 = math.cos(math.radians(H17))*math.cos(math.radians(H16))
    Q48 = 0
    R45 = H13
    R46 = H14
    R47 = H15
    R48 = 1 
    ## J1 FRAME
    O51 = math.cos(P37)
    O52 = math.sin(P37)
    O53 = 0
    O54 = 0
    P51 = -math.sin(P37)*math.cos(Q37)
    P52 = math.cos(P37)*math.cos(Q37)
    P53 = math.sin(Q37)
    P54 = 0  
    Q51 = math.sin(P37)*math.sin(Q37)
    Q52 = -math.cos(P37)*math.sin(Q37)
    Q53 = math.cos(Q37)
    Q54 = 0 
    R51 = S37*math.cos(P37)
    R52 = S37*math.sin(P37)
    R53 = R37
    R54 = 1
    ## J2 FRAME
    O57 = math.cos(P38)
    O58 = math.sin(P38)
    O59 = 0
    O60 = 0
    P57 = -math.sin(P38)*math.cos(Q38)
    P58 = math.cos(P38)*math.cos(Q38)
    P59 = math.sin(Q38)
    P60 = 0
    Q57 = math.sin(P38)*math.sin(Q38)
    Q58 = -math.cos(P38)*math.sin(Q38)
    Q59 = math.cos(Q38)
    Q60 = 0
    R57 = S38*math.cos(P38)
    R58 = S38*math.sin(P38)
    R59 = R38
    R60 = 1
    ## J3 FRAME 
    O63 = math.cos(P39)
    O64 = math.sin(P39)
    O65 = 0
    O66 = 0
    P63 = -math.sin(P39)*math.cos(Q39)
    P64 = math.cos(P39)*math.cos(Q39)
    P65 = math.sin(Q39)
    P66 = 0
    Q63 = math.sin(P39)*math.sin(Q39)
    Q64 = -math.cos(P39)*math.sin(Q39)
    Q65 = math.cos(Q39)
    Q66 = 0
    R63 = S39*math.cos(P39)
    R64 = S39*math.sin(P39)
    R65 = 0
    R66 = 1
    #WF*J1
    T48 = (O45*O51)+(P45*O52)+(Q45*O53)+(R45*O54)
    T49 = (O46*O51)+(P46*O52)+(Q46*O53)+(R46*O54)
    T50 = (O47*O51)+(P47*O52)+(Q47*O53)+(R47*O54)
    T51 = (O48*O51)+(P48*O52)+(Q48*O53)+(R48*O54) 
    U48 = (O45*P51)+(P45*P52)+(Q45*P53)+(R45*P54)
    U49 = (O46*P51)+(P46*P52)+(Q46*P53)+(R46*P54)
    U50 = (O47*P51)+(P47*P52)+(Q47*P53)+(R47*P54)
    U51 = (O48*P51)+(P48*P52)+(Q48*P53)+(R48*P54)
    V48 = (O45*Q51)+(P45*Q52)+(Q45*Q53)+(R45*Q54)
    V49 = (O46*Q51)+(P46*Q52)+(Q46*Q53)+(R46*Q54)
    V50 = (O47*Q51)+(P47*Q52)+(Q47*Q53)+(R47*Q54)
    V51 = (O48*Q51)+(P48*Q52)+(Q48*Q53)+(R48*Q54)
    W48 = (O45*R51)+(P45*R52)+(Q45*R53)+(R45*R54)
    W49 = (O46*R51)+(P46*R52)+(Q46*R53)+(R46*R54)
    W50 = (O47*R51)+(P47*R52)+(Q47*R53)+(R47*R54)
    W51 = (O48*R51)+(P48*R52)+(Q48*R53)+(R48*R54) 
    #(WF*J1)*J2
    T54 = (T48*O57)+(U48*O58)+(V48*O59)+(W48*O60)
    T55 = (T49*O57)+(U49*O58)+(V49*O59)+(W49*O60)
    T56 = (T50*O57)+(U50*O58)+(V50*O59)+(W50*O60)
    T57 = (T51*O57)+(U51*O58)+(V51*O59)+(W51*O60)
    U54 = (T48*P57)+(U48*P58)+(V48*P59)+(W48*P60)
    U55 = (T49*P57)+(U49*P58)+(V49*P59)+(W49*P60)
    U56 = (T50*P57)+(U50*P58)+(V50*P59)+(W50*P60)
    U57 = (T51*P57)+(U51*P58)+(V51*P59)+(W51*P60)
    V54 = (T48*Q57)+(U48*Q58)+(V48*Q59)+(W48*Q60)
    V55 = (T49*Q57)+(U49*Q58)+(V49*Q59)+(W49*Q60)
    V56 = (T50*Q57)+(U50*Q58)+(V50*Q59)+(W50*Q60)
    V57 = (T51*Q57)+(U51*Q58)+(V51*Q59)+(W51*Q60)
    W54 = (T48*R57)+(U48*R58)+(V48*R59)+(W48*R60)
    W55 = (T49*R57)+(U49*R58)+(V49*R59)+(W49*R60)
    W56 = (T50*R57)+(U50*R58)+(V50*R59)+(W50*R60)
    W57 = (T51*R57)+(U51*R58)+(V51*R59)+(W51*R60) 
    #(WF*J1*J2)*J3
    T60 = (T54*O63)+(U54*O64)+(V54*O65)+(W54*O66)
    T61 = (T55*O63)+(U55*O64)+(V55*O65)+(W55*O66)
    T62 = (T56*O63)+(U56*O64)+(V56*O65)+(W56*O66)
    T63 = (T57*O63)+(U57*O64)+(V57*O65)+(W57*O66)
    U60 = (T54*P63)+(U54*P64)+(V54*P65)+(W54*P66)
    U61 = (T55*P63)+(U55*P64)+(V55*P65)+(W55*P66)
    U62 = (T56*P63)+(U56*P64)+(V56*P65)+(W56*P66)
    U63 = (T57*P63)+(U57*P64)+(V57*P65)+(W57*P66)
    V60 = (T54*Q63)+(U54*Q64)+(V54*Q65)+(W54*Q66)
    V61 = (T55*Q63)+(U55*Q64)+(V55*Q65)+(W55*Q66)
    V62 = (T56*Q63)+(U56*Q64)+(V56*Q65)+(W56*Q66)
    V63 = (T57*Q63)+(U57*Q64)+(V57*Q65)+(W57*Q66)
    W60 = (T54*R63)+(U54*R64)+(V54*R65)+(W54*R66)
    W61 = (T55*R63)+(U55*R64)+(V55*R65)+(W55*R66)
    W62 = (T56*R63)+(U56*R64)+(V56*R65)+(W56*R66)
    W63 = (T57*R63)+(U57*R64)+(V57*R65)+(W57*R66)
    #INVERSE OF (WF*J1*J2)*J3
    Y48 = U61
    Y49 = U62
    Z48 = V61
    Z49 = V62
    AA48 = T61
    AA49 = T62
    AB48 = V61
    AB49 = V62
    AC48 = T61
    AC49 = T62
    AD48 = U61
    AD49 = U62
    Y50 = U60
    Y51 = U62
    Z50 = V60
    Z51 = V62
    AA50 = T60
    AA51 = T62
    AB50 = V60
    AB51 = V62
    AC50 = T60
    AC51 = T62
    AD50 = U60
    AD51 = U62
    Y52 = U60
    Y53 = U61
    Z52 = V60
    Z53 = V61
    AA52 = T60
    AA53 = T61
    AB52 = V60
    AB53 = V61
    AC52 = T60
    AC53 = T61
    AD52 = U60
    AD53 = U61
    #minors determinant
    Y56 = (Y48*Z49)-(Y49*Z48)
    Y57 = (Y50*Z51)-(Y51*Z50)
    Y58 = (Y52*Z53)-(Y53*Z52)
    Z56 = (AA48*AB49)-(AA49*AB48)
    Z57 = (AA50*AB51)-(AA51*AB50)
    Z58 = (AA52*AB53)-(AA53*AB52)
    AA56 = (AC48*AD49)-(AC49*AD48)
    AA57 = (AC50*AD51)-(AC51*AD50)
    AA58 = (AC52*AD53)-(AC53*AD52)
    #cofactors
    Y61 = 1
    Y62 = -1
    Y63 = 1
    Z61 = -1
    Z62 = 1
    Z63 = -1
    AA61 = 1
    AA62 = -1
    AA63 = 1
    #cofactors*determinant
    AC61 = Y56*Y61
    AC62 = Y57*Y62
    AC63 = Y58*Y63
    AD61 = Z56*Z61
    AD62 = Z57*Z62
    AD63 = Z58*Z63
    AE61 = AA56*AA61
    AE62 = AA57*AA62
    AE63 = AA58*AA63
    #adjugate
    Y66 = AC61
    Y67 = AD61
    Y68 = AE61
    Z66 = AC62
    Z67 = AD62
    Z68 = AE62
    AA66 = AC63
    AA67 = AD63
    AA68 = AE63
    #determinant
    Y71 = (T60*AC61)+(U60*AD61)+(V60*AE61)
    #inverse (WF*J1*J2)*J3 
    AA71 = 1/Y71*Y66
    AA72 = 1/Y71*Y67
    AA73 = 1/Y71*Y68
    AB71 = 1/Y71*Z66
    AB72 = 1/Y71*Z67
    AB73 = 1/Y71*Z68
    AC71 = 1/Y71*AA66
    AC72 = 1/Y71*AA67
    AC73 = 1/Y71*AA68
    #Z change
    O69 = math.cos(math.radians(N9))
    O70 = math.sin(math.radians(N9))
    O71 = 0
    P69 = -math.sin(math.radians(N9))
    P70 = math.cos(math.radians(N9))
    P71 = 0
    Q69 = 0
    Q70 = 0
    Q71 = 1
    #Y change
    O74 = math.cos(math.radians(N8))
    O75 = 0
    O76 = -math.sin(math.radians(N8))
    P74 = 0
    P75 = 1
    P76 = 0
    Q74 = math.sin(math.radians(N8))
    Q75 = 0
    Q76 = math.cos(math.radians(N8))
    #X change
    O79 = 1
    O80 = 0
    O81 = 0
    P79 = 0
    P80 = math.cos(math.radians(N7))
    P81 = math.sin(math.radians(N7))
    Q79 = 0
    Q80 = -math.sin(math.radians(N7))
    Q81 = math.cos(math.radians(N7))
    #Current R 0-T
    O84 = G60
    O85 = G61
    O86 = G62
    P84 = H60
    P85 = H61
    P86 = H62
    Q84 = I60
    Q85 = I61
    Q86 = I62
    #Z*Y
    S72 = (O69*O74)+(P69*O75)+(Q69*O76)
    S73 = (O70*O74)+(P70*O75)+(Q70*O76)
    S74 = (O71*O74)+(P71*O75)+(Q71*O76)
    T72 = (O69*P74)+(P69*P75)+(Q69*P76)
    T73 = (O70*P74)+(P70*P75)+(Q70*P76)
    T74 = (O71*P74)+(P71*P75)+(Q71*P76)
    U72 = (O69*Q74)+(P69*Q75)+(Q69*Q76)
    U73 = (O70*Q74)+(P70*Q75)+(Q70*Q76)
    U74 = (O71*Q74)+(P71*Q75)+(Q71*Q76)
    #Z*Y*X
    S77 = (S72*O79)+(T72*O80)+(U72*O81)
    S78 = (S73*O79)+(T73*O80)+(U73*O81)
    S79 = (S74*O79)+(T74*O80)+(U74*O81)
    T77 = (S72*P79)+(T72*P80)+(U72*P81)
    T78 = (S73*P79)+(T73*P80)+(U73*P81)
    T79 = (S74*P79)+(T74*P80)+(U74*P81)
    U77 = (S72*Q79)+(T72*Q80)+(U72*Q81)
    U78 = (S73*Q79)+(T73*Q80)+(U73*Q81)
    U79 = (S74*Q79)+(T74*Q80)+(U74*Q81)
    #Z*Y*X*0-T
    S82 = (S77*O84)+(T77*O85)+(U77*O86)
    S83 = (S78*O84)+(T78*O85)+(U78*O86)
    S84 = (S79*O84)+(T79*O85)+(U79*O86)
    T82 = (S77*P84)+(T77*P85)+(U77*P86)
    T83 = (S78*P84)+(T78*P85)+(U78*P86)
    T84 = (S79*P84)+(T79*P85)+(U79*P86)
    U82 = (S77*Q84)+(T77*Q85)+(U77*Q86)
    U83 = (S78*Q84)+(T78*Q85)+(U78*Q86)
    U84 = (S79*Q84)+(T79*Q85)+(U79*Q86)
    #R,3-6
    O89 = (AA71*S82)+(AB71*S83)+(AC71*S84)
    O90 = (AA72*S82)+(AB72*S83)+(AC72*S84)
    O91 = (AA73*S82)+(AB73*S83)+(AC73*S84)
    P89 = (AA71*T82)+(AB71*T83)+(AC71*T84)
    P90 = (AA72*T82)+(AB72*T83)+(AC72*T84)
    P91 = (AA73*T82)+(AB73*T83)+(AC73*T84)
    Q89 = (AA71*U82)+(AB71*U83)+(AC71*U84)
    Q90 = (AA72*U82)+(AB72*U83)+(AC72*U84)
    Q91 = (AA73*U82)+(AB73*U83)+(AC73*U84) 
    #calc 456
    R7 = math.degrees(math.atan2(Q90,Q89))
    R8 = math.degrees(math.atan2(+math.sqrt(1-Q91**2),Q91))
    if (P91<0):
      R9 = math.degrees(math.atan2(P91,-O91))+180
    else:
      R9 = math.degrees(math.atan2(P91,-O91))-180
    S7 = math.degrees(math.atan2(-Q90,-Q89))
    S8 = math.degrees(math.atan2(-math.sqrt(1-Q91**2),Q91))  
    if (P91<0):
      S9 = math.degrees(math.atan2(-P91,O91))-180
    else:
      S9 = math.degrees(math.atan2(-P91,O91))+180  
    if (J5AngCur>0 and R8>0):
      Q8 = R8
    else:
      Q8 = S8
    if (Q8>0):
      Q7 = R7
    else:
      Q7 = S7
    if (Q8<0):
      Q9 = S9
    else:
      Q9 = R9