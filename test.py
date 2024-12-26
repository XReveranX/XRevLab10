import paket.Lin
import paket.generator
import paket.sredn


print(paket.Lin.linearize_rec(([12,22,[1,[15]]])))

sred=paket.sredn.zamican()
sred(11)
sred(12)
sred(112)
print(sred(86))

'''
a=paket.generator.besk_posl(10)
for i in a:
    None
'''
