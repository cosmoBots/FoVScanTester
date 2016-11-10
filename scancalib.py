# Tolerances for deciding if the movement has to be commanded or not.
# If the distance to be covered is less than this ones, the movement will be skipped
cte_tol_x = 5      # minimum distance in motor encoder to command a movement in X direction
cte_tol_y = 7      # minimum distance in motor encoder to command a movement in Y direction
cte_tol_comp = 5   # minimum distance in motor encoder to command a movement in compensation direction

# Time to wait between steps, apart from motors and camera ones
cte_waitTime = 1
cte_stepTime = cte_waitTime * 1000

########### WINDOW TO MOTORS DEFINITIONS ################

# Mx = x
cte_lsx_min = 0  # End of LS travel in lower units
cte_lsx_scale = (1000 * 1000)  # LS units / mm * 1000 mm / 1 m
cte_lsx_max = 26900  # End of LS travel in upper units
#cte_lsx_zero = 13100  # LS units coincidence with 0 mm (center)
cte_lsx_zero = 11100  # Primer alineado en GREGOR

# My = y
cte_lsy_min = 0  # End of LS travel in lower units
cte_lsy_scale = - (2000 * 1000)  # LS units / mm * 1000 mm / 1 m
cte_lsy_max = 39401  # End of LS travel in upper units
#cte_lsy_zero = 18400  # LS units coincidence with 0 mm (center)
cte_lsy_zero = 16400  # Primer alineado en GREGOR

# Mcomp = compensaTion
cte_lscomp_min = 0  # End of LS travel in lower units
cte_lscomp_scale = (2000 * 1000)  # LS units / mm * 1000 mm / 1 m
cte_lscomp_max = 39800  # End of LS travel in upper units
#cte_lscomp_zero = 25800  # LS units coincidence with 0 mm (center)
#cte_lscomp_zero = 15000  # LS units coincidence with 0 mm (center)
#cte_lscomp_zero = 20350# LS units coincidence with 0 mm (center) #CARLOS
cte_lscomp_zero = 19500 # Primer alineado en GREGOR
#bien 20250 antes de tcar SM1 y RS1
#Calculado con RS1 19500 ver excel
#Calculado con Oct_BancoFocoSW 19650 ver excel
# Con mascara A kapton F_silica en visible(550nm) aumentar 1mm x (2000)/2 = 1000 entonces quedaria en 20650
# Con mascara A kapton F_silica en NIR(1um) aumentar 0.7mm x (2000)/2 = 700 entonces quedaria en 20350
#Calculado en visible con Oct_BancoFocomascaraSW 20500 ver excel
#TXINTO 19350 # Primer alineado en GREGOR
#19500 #  Alineado en GREGOR IR

# Home speeds
cte_vhx = 100
cte_vhy = 100
cte_vhcomp = 100

# Index speeds
cte_vix = 30
cte_viy = 30
cte_vicomp = 30

# Movement speeds
cte_vx = 100
cte_vy = 100
cte_vcomp = 100

###################### COMPENSATION ALGORITHM PARAMETERS ######################
# Original function ---> lscomp = (x + y) / 2
# Tunable function ---> lscomp = ((cte_comp_factor_x * x) + (cte_comp_factor_x * y)) / cte_comp_divisor
cte_comp_factor_x = 1
cte_comp_factor_y = 1
cte_comp_divisor = 2