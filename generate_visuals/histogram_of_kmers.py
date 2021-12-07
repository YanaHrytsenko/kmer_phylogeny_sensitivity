import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

name = sys.argv[1]
histName = sys.argv[2]

freq = []
with open(name, "r") as f:
    for line in f:
        vals = int(line.split(" ",1)[1])
        freq.append(vals)
f.close()

bins = [10,100,1000,10000,100000,1000000,10000000]


plt.xscale('log')
plt.yscale('log')
plt.hist(freq, bins)
plt.savefig(histName, bbox_inches='tight')

'''
plt.xscale('log')
#hist(pop, bins='freedman')
#plt.savefig('unsorted_freedman.pdf', bbox_inches='tight')
#hist(pop, bins='blocks')
#plt.savefig('blocks.pdf', bbox_inches='tight')
#hist(pop, bins='knuth')
#plt.savefig('knuth.pdf', bbox_inches='tight')
hist(pop, bins='scott')
plt.savefig('scott.pdf', bbox_inches='tight')
'''
