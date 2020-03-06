class  Athlete:
    def __init__(self, sport, practice = 'Yes', running = 'Yes'):
        self.sport = sport
        self.practice = practice
        self.running = running
    
    def Runner(self):
        return 'This Athlete runs'

    def Lifting(self):
        return "This Athlete Lifts Weights"

class  DistanceRunner(Athlete):
    marathon_runner = "Runs 26.2 Miles. No one can beat them in distance."
    def __str__(self):
        return 'This guy definitely runs too much'

    def __repr__(self):
        return f'''
        Runs: Daily
        For: {self.sport}
        '''

    def tenk(self):
        return "This Athele can complete 10Ks"

    def lifting(self):
        return "This Athlete does not Lift Weights"

class  SoccerPlayer:

    def __str__(self):
        return "This guy definitely runs too much, but there's a ball involved"
    
    def __repr__(self):
        return f'''
        Runs: Daily
        For: {self.sport}
        '''

charlie.SoccerPlayer()

