print("""
Note from the author: This is quite inefficient because it's based on a not-currently-working build of the ranked voting system.
It's essentially the ranked voting program with some functionality (and the lack of it functioning correctly) removed.
""")

#function to add "Message to operators: " before operator messages
def opmessage(message):
    print("Message to operators: \n" +str(message))

#creates the ballot out of the votes
def voting():
    morevoters = 1
    while morevoters != 0:
        voterlist = []
        y = 1
        print("CAUTION: if the candidate's name is entered incorrectly (including capitalization), the vote will not be counted.")
        choice = input("choice: ")
        if choice != "voting complete":
            voterlist.append(choice)
            ballotlist.append(voterlist)
        else:
            morevoters = 0

#counts the votes and assigns the amount of votes to the respective candidates
def calculate():
    thevoter = 0
    for i in range(0, len(ballotlist)):
        thechoice = 0
        # != was <
        while thechoice < numberofcandidates:
            if candidate_list.index(ballotlist[thevoter][thechoice])+1 != -1:
                candidate_list[int(candidate_list.index(ballotlist[thevoter][thechoice]))+1] = candidate_list[int(candidate_list.index(ballotlist[thevoter][thechoice]))+1]+1
                thechoice = numberofcandidates
            else:
                thechoice += 1
            thevoter += 1

#finds the candidate with the most votes
def winner():
    v = 1
    justnumberscandidatelist = []
    for i in range(0, int(len(candidate_list) / 2)):
        justnumberscandidatelist.append(candidate_list[v])
        v += 2
    print('\n')
    if justnumberscandidatelist.count(max(justnumberscandidatelist)) == 1:
        print(candidate_list[candidate_list.index(max(justnumberscandidatelist))-1]+" is the winner!")
    elif justnumberscandidatelist.count(max(justnumberscandidatelist)) > 1:
        print("There's a tie!")
    if input("Would you like additional information? ") != "no":
        print('\n')
        print("Number of votes per candidate: " + str(candidate_list))

#Main code begins
print('\n')
print("Welcome to the automated voting system.")
candidate_list = []
morecandidates = 1
numberofcandidates = 0
print('\n')
opmessage("If it is likely a candidate's name will be misspelled or otherwise entered incorrectly, \nit is recommended to enter an alternate name instead, such as a nickname or number.")
while morecandidates == 1:
    candidate_list.append(input("Enter candidate: "))
    candidate_list.append(0)
    numberofcandidates += 1
    if input("Are there more candidates? Type 'no' to stop adding candidates. ") == "no":
        morecandidates = 0
print('\n')

opmessage("When there are no additional voters remaining, enter 'voting complete' in the 'choice' field.")
opmessage("It is recommended to create a line of voters at this time.")
print('\n')
print("Voting begins now.")
ballotlist = []
voting()
calculate()
winner()
print('\n')
print("Created by Kaveer Gera")
