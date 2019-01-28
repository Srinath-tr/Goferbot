import facerec_model

load = facerec_model.facerec()
mod = load[0]
camid = load[1]
filename = load[2]

facerec_model.startapp(mod,camid,filename)  
