class Tournament:
    def __init__(self, distance, *runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        for runner in self.runners:
            runner.distance = 0
        for i in range(self.distance):
            for runner in self.runners:
                runner.run()
        sorted_runners = sorted(self.runners, key=lambda r: r.distance, reverse=True)
        for place, runner in enumerate(sorted_runners, start=1):
            results[place] = runner.name
        return results