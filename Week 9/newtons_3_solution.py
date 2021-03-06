def f(x):
    y = round(exp(0.05*x)*(0.05*x)-5,5)
    return(y)
    
def fdash(x):
    d = round(exp(0.05*x)*(0.0025*x+0.05),5)
    return(d)
    
def onestep(x):
    newguess = round(x - f(x)/fdash(x),5)
    return(newguess)
    
def newtons_nsteps(x, n):
    currentStep = 1
    while currentStep <= n:
        x = onestep(x)
        currentStep = currentStep + 1
    return(x)
