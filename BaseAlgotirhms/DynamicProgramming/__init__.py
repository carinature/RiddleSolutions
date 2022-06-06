from BaseAlgotirhms.DynamicProgramming import Fibonacci, GridTraveler

import timeit

# Fibonacci
print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(Fibonacci.testing, number=10)))

# GreedTraveler
print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(GridTraveler.testing, number=10)))
