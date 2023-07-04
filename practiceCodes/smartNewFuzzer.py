import numpy as np
from fuzzingbook.Coverage import Coverage
from fuzzingbook.MutationFuzzer import MutationFuzzer
import random

class Scheduler(object):
    def normalizedCoverage(self, population):
        """Normalize energy"""
        coverage = [item[1] for item in population.values()]
        overall_coverage = sum(coverage)  # Add up all values in energy
        norm_coverage = list(map(lambda nrg: nrg/overall_coverage, coverage))
        return norm_coverage

    def choose(self, population):
        """Choose weighted by normalized energy."""
        norm_coverage = self.normalizedCoverage(population)
        seed = np.random.choice(list(population.keys()), p=norm_coverage)
        return seed

class smartFuzzer(MutationFuzzer):
    def __init__(self, seeds):
        self.seeds = seeds

    def calculate_cumulative_coverage(self, seed, population, input_population, function):
        all_coverage = set()
        for inp in input_population:
            with Coverage() as cov:
                try:
                    function(inp)
                except:
                    pass
            all_coverage |= cov.coverage()
            if inp in list(population.keys()):
                if len(all_coverage) > population[inp][1]:
                    population[inp][0] =  (len(all_coverage)-population[inp][1])/population[inp][1]
                    population[inp][1] = len(all_coverage)
            else:
                increase_ratio = (len(all_coverage)-population[seed][1])/population[seed][1]
                if increase_ratio > 0:
                    population[inp] = [increase_ratio, len(all_coverage)]

        return population
            
    def fuzz(self):
        split_url = self.seeds[0].split('.')
        random_index = random.randrange(0, len(split_url))
        for i in range(0, len(split_url[random_index])):
            split_url[random_index] = split_url[random_index][::-1]
        change = ".".join(split_url)
        return change


# your answer starts here
from urllib.request import urlopen
from urllib.parse import urlparse

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

def http_program(url):
    supported_schemes = ["http", "https"]
    result = urlparse(url)
    if result.scheme not in supported_schemes:
        raise ValueError("Scheme must be one of " + repr(supported_schemes))
    if result.netloc == '':
        raise ValueError("Host must be non-empty")

    # Do something with the URL
    return True  

def is_valid_url(url):
    try:
        result = http_program(url)
        return True
    except ValueError:
        return False
    
def fetch_website_data(url):
    if is_valid_url(url):
        try:
            webUrl = urlopen(url)
            #data = webUrl.read()
            return webUrl
            #print(data)
        except Exception as e:
            return False
        
def perform_url_fuzzing(trials = 5):
        population = {
            "https://www.youtube.com" : [0.0, 1],
            "https://www.google.com" : [0.0, 1],
            "http://yahoo.com" : [0.0, 1],
            "http://www.facebook.com" : [0.0, 1]
        }
        seed_list = ["https://www.youtube.com", "https://www.google.com", "http://yahoo.com", "http://www.facebook.com"]

        scheduler = Scheduler()
        for i in range(trials):
            if i < len(seed_list):
                seed = seed_list[i]
            else:
                seed = scheduler.choose(population)
            fuzzer = smartFuzzer([seed])
            temp_population = []
            for j in range(trials):
                temp_population.append(fuzzer.fuzz())
            coverage_report = fuzzer.calculate_cumulative_coverage(seed, population, temp_population, fetch_website_data)

        print(coverage_report)


def perform_pallindrome_fuzzing(trials = 5):
        population = {
            "swetha" : [0.0, 1],
            "sweews" : [0.0, 1],
            "radar" : [0.0, 1],
            "sethu" : [0.0, 1]
        }
        seed_list = ["swetha", "sethu", "sweews", "radar"]

        scheduler = Scheduler()
        for i in range(trials):
            if i < len(seed_list):
                seed = seed_list[i]
            else:
                seed = scheduler.choose(population)
            fuzzer = smartFuzzer([seed])
            temp_population = []
            for j in range(trials):
                temp_population.append(fuzzer.fuzz())
            coverage_report = fuzzer.calculate_cumulative_coverage(seed, population, temp_population, isPallindrome)

        print(coverage_report)


def perform_strlen_fuzzing(trials = 5):
        population = {
            "swetha" : [0.0, 1],
            "sweews" : [0.0, 1],
            "radar" : [0.0, 1],
            "sethu" : [0.0, 1]
        }
        seed_list = ["swetha", "sethu", "sweews", "radar"]

        scheduler = Scheduler()
        for i in range(trials):
            if i < len(seed_list):
                seed = seed_list[i]
            else:
                seed = scheduler.choose(population)
            fuzzer = smartFuzzer([seed])
            temp_population = []
            for j in range(trials):
                temp_population.append(fuzzer.fuzz())
            coverage_report = fuzzer.calculate_cumulative_coverage(seed, population, temp_population, isStrLenOdd)

        print(coverage_report)

perform_url_fuzzing(8)
print("")
perform_pallindrome_fuzzing(40)
print()
perform_strlen_fuzzing(40)



