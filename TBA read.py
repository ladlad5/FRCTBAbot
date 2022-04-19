import requests



serverLocation = "https://www.thebluealliance.com/api/v3"
headers = {
    'accept': 'application/json'
}
with open("Tokens.txt") as x: #read TBA token
    headers['X-TBA-Auth-Key'] = x.readlines()[1]

def getTeamInfo(teamNumber): #gives short summary of a team TODO: maybe make formatting nicer but not a priority
    keys = ["nickname", "city", "state_prov", "country", "school_name", "rookie_year"]
    requestLocation = serverLocation + "/team/" + str(teamNumber)
    information = requests.get(requestLocation, headers=headers).json()
    teamSummary = []
    for x in keys:
        if(information[x] != None):
            teamSummary = teamSummary + [x + ': ' + str(information[x])]
    return teamSummary

print(getTeamInfo("frc2877"))