def estimator(data):
  return data
def estimator(impact):
  monthWeeks = month * 4
  weekDays = week * 7
  totalDays = monthWeeks + weekDays + days
  currentlyInfected = reportedCases * 10
  factor = totalDays/3;
  infectionsByRequestedTime = currentlyInfected * 2^factor
  severeCasesByRequestedTime = 0.15 * infectionsByRequestedTime
  hospitalBedsByRequestedTime= totalHospitalBeds - severeCasesByRequestedTime
  casesForICUByRequestedTime = 0.05 * infectionsByRequestedTime
  casesForVentilatorsByRequestedTime = 0.02 * infectionsByRequestedTime
  dollarsInFlight = infectionsByRequestedTime * avgDailyIncomeInUSD * totalDays
 return impact

def estimator(severeImpact):
  monthWeeks = month * 4
  weekDays = week * 7
  totalDays = monthWeeks + weekDays + days
  currentlyInfected = reportedCases * 50
  factor = totalDays/3;
  infectionsByRequestedTime = currentlyInfected * 2^factor
  severeCasesByRequestedTime = 0.15 * infectionsByRequestedTime
  hospitalBedsByRequestedTime= totalHospitalBeds - severeCasesByRequestedTime
  casesForICUByRequestedTime = 0.05 * infectionsByRequestedTime
  casesForVentilatorsByRequestedTime = 0.02 * infectionsByRequestedTime
  dollarsInFlight = infectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD * totalDays
 return severeImpact
