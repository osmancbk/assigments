age =  input('75 yasindan buyuk ve sigara mi iciyorsunuz? evet/hayir :\n')
    
chronic =  input('Kronik bir hastakiginiz var mi? evet/hayir :\n')

immune =  input('Bagisiklik sisteminiz zayif mi? evet/hayir :ln')
print()

if age.lower() == 'evet':
    age = True
else:
    age = False
    
if chronic.lower() == 'evet':
    chronic = True
else:
    chronic = False  

if immune.lower() == 'evet':
    immune = True
else:
    immune = False 

if age and chronic and immune:
    print('Yuksek risk grubundasiniz, disariya adiminizi dahi atmayin!!!')
elif (age and chronic) or (immune and chronic) or (age and immune):
    print('Ikinci risk grubundasiniz dikkat etmeniz tavsiye olunur!!!')
elif age or chronic or immune:
    print('Dusuk risk grubundasiniz dikkat etmeniz tavsiye olunur!!!')
else:
    print('Risk grubunda degilsiniz, gez, dolas, eglen...')
