class em:
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language


l = em("loha", 20000, "hindi")

print(l.name, l.salary, l.language)