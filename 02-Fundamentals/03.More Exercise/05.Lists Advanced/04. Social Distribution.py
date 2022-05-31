population = [int(x) for x in input().split(', ')]
min_wealth = int(input())

if sum(population) < min_wealth * len(population):
    print('No equal distribution possible')
else:
    poorest = min(population)

    while poorest < min_wealth:
        richest = max(population)
        needed = min_wealth - poorest

        population[population.index(richest)] -= needed
        population[population.index(poorest)] += needed

        poorest = min(population)

    print(population)