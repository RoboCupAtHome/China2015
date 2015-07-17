import random
from copy import deepcopy

teamsA = """BahiaRT
Uchile Homebreakers
Sun@Home
WrightEagle
Bit@Home
Demura.net
KameRider
Pumas
Jiaolong""".split('\n')

teamsB = """Cesar Voxar
Tinker
Tobi
Homer
Erasers
TechUnited
aiRobots_NCKU
Skuba""".split('\n')

arenas = {"A":teamsA, "B":teamsB}

challenges = "Navigation    Person Recognition  Manipulation + Object recognition   Speech Recognition  GPSR".split("\t")


def interleave_teams(teams_, attempts=3):
    teams = deepcopy(teams_)
    while teams:
        for attempt in range(attempts):
            yield teams[0]
            if len(teams) > 1: 
                yield teams[1]
        del teams[0]
        if teams: del teams[0]

# for arena,teams in arenas.iteritems():
#     print arena
#     for challenge in challenges:
#         print challenge
#         random.shuffle(teams)
#         for team_attempt in interleave_teams(teams):
#             print team_attempt
#     print "-" * 20


# import ipdb; ipdb.set_trace()
random.shuffle(teamsA)

# for team in teamsA:
#     print team

gen = interleave_teams(teamsA)
while True:
    try:
        team_attempt = gen.next()
        print team_attempt
    except StopIteration:
        break
    except IndexError:
        break