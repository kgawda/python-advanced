import cProfile
import pstats
from game import main  # uwaga, tu może być błąd

with cProfile.Profile() as pr:
   main.simulate()

pr = cProfile.Profile().run('main.simulate()')

pstats.Stats(pr).sort_stats(pstats.SortKey.TIME).print_stats()

# python -m cProfile -s tottime main.py

mem1 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
# kod alokujący pamięć
mem2 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
mem2 - mem1  # wzrost zaalokowanej pamięci w kB
