 yarn import
import json

data = {
 "region": {
  "name" : "Africa",
  "avgAge": 19.75,
  "avgIncomeInUSD": 4,
  "avgDailyIncomePopulationInUSD": 0.71
 },
 "periodType" : "days",
 "timeToElapse": 58,
 "reportedCases": 674,
 "population": 66622705,  
 "totalHospitalBeds": 1380614
}

for x in data:
 print(x)
 

def estimator(data):
 days = 365
 factor = int(days/3)
 estimate = {
  "impact": {
     "currentlyInfected" : "reportedCases" * 10,
     "infectionsByRequestedTime" : "currentlyInfected" * 2^factor,
     "severeCasesByRequestedTime" : 0.15 * "infectionsByRequestedTime",
     "hospitalBedsByRequestedTime" : "totalHospitalBeds" - "severeCasesByRequestedTime",
     "casesForICUByRequestedTime" : 0.05 * "infectionsByRequestedTime",
     "casesForVentilatorsByRequestedTime" : 0.02 * "infectionsByRequestedTime",
     "dollarsInFlight" : "infectionsByRequestedTime" * "avgDailyIncomeInUSD" * days
  },
  "severeImpact": {
    "currentlyInfected" : "reportedCases" * 50,
    "infectionsByRequestedTime" : "currentlyInfected" * 2^factor,
    "severeCasesByRequestedTime" : 0.15 * "infectionsByRequestedTime",
    "hospitalBedsByRequestedTime" : "totalHospitalBeds" - "severeCasesByRequestedTime",
    "casesForICUByRequestedTime" : 0.05 * "infectionsByRequestedTime",
    "casesForVentilatorsByRequestedTime" : 0.02 * "infectionsByRequestedTime",
    "dollarsInFlight" : "infectionsByRequestedTime" * "avgDailyIncomeInUSD" * days
  }
 }
 return data
 for x,y in estimate:
  print(x,y)
  
  
estimator()

yarn run test  





