import _init_

  _init_.estimator(data):
  return data

  _init_.estimator(impact):
    impact.currentlyInfected = reportedCases * 10
    factor = int(totalDays/3)
    impact.infectionsByRequestedTime = currentlyInfected * 2^factor
    impact.severeCasesByRequestedTime = 0.15 * infectionsByRequestedTime
    impact.hospitalBedsByRequestedTime= totalHospitalBeds - severeCasesByRequestedTime
    impact.casesForICUByRequestedTime = 0.05 * infectionsByRequestedTime
    impact.casesForVentilatorsByRequestedTime = 0.02 * infectionsByRequestedTime
    impact.dollarsInFlight = infectionsByRequestedTime * avgDailyIncomeInUSD * totalDays
  return impact

 _init_.estimator(severeImpact):
   severeImpact.currentlyInfected = reportedCases * 50
   severeImpact.infectionsByRequestedTime = currentlyInfected * 2^factor
   severeImpact.severeCasesByRequestedTime = 0.15 * infectionsByRequestedTime
   severeImpact.hospitalBedsByRequestedTime= totalHospitalBeds - severeCasesByRequestedTime
   severeImpact.casesForICUByRequestedTime = 0.05 * infectionsByRequestedTime
   severeImpact.casesForVentilatorsByRequestedTime = 0.02 * infectionsByRequestedTime
   severeImpact.dollarsInFlight = infectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD * totalDays
 return severeImpact
