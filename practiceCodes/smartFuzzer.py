import numpy as np
from fuzzingbook.Coverage import Coverage
from fuzzingbook.MutationFuzzer import MutationFuzzer
class smartFuzzer:
    def __init__(self):
        self.mutators = [
            self.delete_random_character,
            self.insert_random_character,
            self.flip_random_character
        ]
    
    def insert_random_character(self,s):
        """Returns s with a random character inserted"""
        pos = random.randint(0, len(s))
        random_character = chr(random.randrange(32, 127))
        return s[:pos] + random_character + s[pos:]
    
    def delete_random_character(self,s):
        """Returns s with a random character deleted"""
        if s == "":
            return self.insert_random_character(s)

        pos = random.randint(0, len(s) - 1)
        return s[:pos] + s[pos + 1:]
    
    def flip_random_character(self,s):
        """Returns s with a random bit flipped in a random position"""
        if s == "":
            return self.insert_random_character(s)

        pos = random.randint(0, len(s) - 1)
        c = s[pos]
        bit = 1 << random.randint(0, 6)
        new_c = chr(ord(c) ^ bit)
        return s[:pos] + new_c + s[pos + 1:]

    def mutate(self, inp):
        """Return s with a random mutation applied"""
        mutator = random.choice(self.mutators)
        return mutator(inp)

class Seed(object):    
    def __init__(self, data):
        """Set seed data"""
        self.data = data

    def __str__(self):
        """Returns data as string representation of the seed"""
        return self.data
    __repr__ = __str__

class PowerSchedule(object):

    def normalizedCoverage(self, population):
        """Normalize energy"""
        coverage = [item[1] for item in population.values()]
        overall_coverage = sum(coverage)  # Add up all values in energy
        norm_coverage = list(map(lambda nrg: nrg/overall_coverage, coverage))
        return norm_coverage

    def choose(self, population):
        """Choose weighted by normalized energy."""
        #self.assignEnergy(population)
        norm_coverage = self.normalizedCoverage(population)
        seed = np.random.choice(list(population.keys()), p=norm_coverage)
        return seed

def isPallindrome(my_str):
    new_string = my_str.casefold()
    rev_string = reversed(new_string)
    if list(new_string) == list(rev_string):
        return True
    else:
        return False

def isStrLenOdd(my_str):
    length = len(my_str)
    if length%2 == 0:
        return False
    else:
        return True

def calculate_cumulative_coverage(seed, population, input_population, function):
    all_coverage = set()
    
    for inp in population.keys():
        with Coverage() as cov:
            try:
                function(inp)
            except:
                # we ignore exceptions for the purpose of this code, but some exceptions may be interesting
                pass
        # set union
        all_coverage |= cov.coverage()
        if len(all_coverage) > population[seed][1]: 
            population[seed][0] = (len(all_coverage)-population[seed][1])/population[seed][1]
            population[seed][1] = len(all_coverage)
    return population

schedule = PowerSchedule()
population = {
    "dinesh" : [0.0, 1],
    "dineenid" : [0.0, 1],
    "radar" : [0.0, 1],
    "ganesh" : [0.0, 1]
}

trials = 100

for i in range(trials):
        seed = schedule.choose(population)
        fuzzer = MutationFuzzer([seed])
        temp_population = []
        for j in range(trials):
            temp_population.append(fuzzer.fuzz())
        coverage_report = calculate_cumulative_coverage(seed, population, temp_population, isPallindrome)


print(coverage_report)


population = {
    "dinesh" : [0.0, 1],
    "dineenid" : [0.0, 1],
    "radar" : [0.0, 1],
    "ganesh" : [0.0, 1]
}
for i in range(trials):
        seed = schedule.choose(population)
        fuzzer = MutationFuzzer([seed])
        temp_population = []
        for j in range(trials):
            temp_population.append(fuzzer.fuzz())
        coverage_report = calculate_cumulative_coverage(seed, population, temp_population, isStrLenOdd)

print(coverage_report)
