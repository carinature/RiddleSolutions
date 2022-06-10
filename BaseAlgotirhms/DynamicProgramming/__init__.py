from BaseAlgotirhms.DynamicProgramming.Memoization import Fibonacci, GridTraveler, CanSum, HowSum, BestSum
# from BaseAlgotirhms.DynamicProgramming.Tabulation import Fibonacci, GridTraveler, CanSum, HowSum, BestSum

import timeit

# # # # # # # # # # # # # # # # # # # # #
# # # #    Memoization    # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #

# Fibonacci
print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(Memoization.Fibonacci.testing, number=10)))

# GreedTraveler
print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(Memoization.GridTraveler.testing, number=10)))

# CanSum
print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(Memoization.CanSum.testing, number=10)))

# HowSum
print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(Memoization.HowSum.testing, number=10)))

# BestSum
print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(Memoization.BestSum.testing, number=10)))

# # # # # # # # # # # # # # # # # # # # #
# # # #     Tabulation    # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #
