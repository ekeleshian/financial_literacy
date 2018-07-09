
column_dictionary = {"NFCSID": "RespondentID",
                     "STATEQ": "State",
                     "CENSUSDIV": "CensusDivision",
                     "CENSUSREG": "CensusRegion",
                     "A3": "Gender",
                     "A3Ar_w": "AgeGroup",
                     "A3B": "Gender/AgeNet",
                     "A4A_new_w": "Ethnicity",
                     "A5_2015": "HighestLevelEducation",
                     "A6": "MaritalStatus",
                     "A7": "LivingArrangements",
                     "A7A": "MaritalStatusVariable",
                     "A11": "Dependents", "A8": "HouseholdIncome",
                     "AM21": "USVeteran?",
                     "AM30": "EndOfMilitaryService",
                     "AM31": "RetireFromMilitary?",
                     "AM22": "SpouseUSVeteran?",
                     "A9": "CurrentWorkStatus",
                     "A10": "SpouseCurrentWorkStatus",
                     "A10A": "HouseholdRetirementStatus",
                     "A21_2015": "PartTimeStudent?",
                     "A22_2015": "TypeSchool",
                     "A14": "WhoExpertInFinances",
                     "J1": "SatisfactionLevelCurrentFinances",
                     "J2": "WillingnessFinancialRisk",
                     "J3": "SpendingVsIncome",
                     "J4": "DifficultyLevelPayingBills",
                     "J5": "EmergencyFunds?",
                     "J6": "SavingsChildCollegeEducation?",
                     "J8": "RetirementFundCalculationsAtAll?",
                     "J9": "RetirementFundCalculationsBeforeRetired?",
                     "J10": "IncomeDropPastYear?",
                     "J20": "ConfidenceLevelToEarn2000WithinMonth",
                     "J30": "ImportantTimePeriodsForBudgeting",
                     "J31": "Budget?",
                     "J32": "CreditRating",
                     "J33_1": "DegreeOfWorryAboutRetirement",
                     "J33_2": "HaveFinancialGoals?",
                     'B1': "CheckingAccount?",
                     "B2": "SavingsAccount?",
                     "B4": "OverdrawOccasionally?",
                     "B30": "FrequencyOfPayingBillsWithDebitCard",
                     "B31": "FrequencyPhoneToPay",
                     "C1_2012": "PensionPlanFromEmployer?",
                     "C2_2012": "WhoseEmployerForRetirementPlans?",
                     "C3_2012": "CanYouChooseHowRetirementPlans?",
                     "C4_2012": "RetirementsAccountNotFromWork?",
                     "C5_2012": "RegularlyContributeToRetirement?",
                     "C10_2012": "LoanPastYearFromRetirement?",
                     "C11_2012": "HardshipWithdrawalFromRetirement?",
                     "B14": "OtherInvestments?",
                     "D20_1": "IncomeFromWorkingPastYear?",
                     "D20_2": "IncomeFromPensionPastYear?",
                     "D20_3": "IncomeFromRetirementAccountsPastYear?",
                     "D20_4": "IncomeFromSocialSecurityPastYear?",
                     "D20_5": "IncomeFromOtherFedOrStateBenefitsPastYear?",
                     "D20_6": "IncomeFromBusinessPastYear?",
                     "D20_7": "IncomeFromFamilyPastYear?",
                     "EA_1": "OwnHome?",
                     "E4A_2015": "YearBoughtHome",
                     "E5_2015": "Downpayment",
                     "E7": "CurrentlyMortgages?",
                     "E8": "EquityLoans?",
                     "E20": "MortgageDebtVsValue",
                     "E15_2015": "FrequencyLateMortgagePastYear",
                     "F1": "HowManyCreditCards",
                     "F2_1": "PayCreditCardsInFullAlways?",
                     "F2_2": "CreditCardChargedInterest?",
                     "F2_3": "CreditCardMinPaymentOnly?",
                     "F2_4": "CreditCardLateFee?",
                     "F2_5": "CreditCardExceedCreditLine?",
                     "F2_6": "CreditCardCashAdvance?",
                     "F10": "ResearchBeforeCreditCard?",
                     "G1": "AutoLoan?",
                     "G20": "UnpaidMedical?",
                     "G30_1": "StudentLoans?1=Y",
                     "G30_2": "StudentLoansFromPartner?",
                     "G30_3": "StudentLoansFromChild?",
                     "G30_4": "StudentLoansFromGrandchild?",
                     "G30_5": "StudentLoansFromOther?",
                     "G30_97": "NoStudentLoans",
                     "G30_98": "DontKnowStudentLoans",
                     "G30_99": "NoAnswerStudentLoans",
                     "G31": "FedVsPrivateLoans?",
                     "G32": "StudentLoanPaymentDeterminedByIncome?",
                     "G33": "StudentLoansCalculations?",
                     "G34": "CompleteEducationalProgram?",
                     "G35": "FrequencyLateStudentLoanPayment",
                     "G22_2015": "StudentLoansWorried?",
                     "G36": "StudentLoansProcessDoItAgain?",
                     "G25_1": "Past5YearsAutoTitleLoan?",
                     "G25_2": "Past5YearsPayDayLoan?",
                     "G25_4": "Past5YearsPawnShop",
                     "G25_5": "Past5YearsRentToOwnStore?",
                     "G37_1": "BoughtAtPawnShop?",
                     "G37_2": "SoldAtPawnShop?",
                     "G37_3": "PawnedAtPawnShop?",
                     "G37_98": "DontKnowAtPawnShop?",
                     "G37_99": "NoAnswerAtPawnShop",
                     "G38": "DebtCollection?",
                     "G23": "TooMuchDebt?",
                     "H1": "HealthInsurance?",
                     "H30_1": "NoMedicineBecauseCost?",
                     "H30_2": "SkippedMedicalTestBecauseCost?",
                     "H30_3": "IgnoreMedicalProblemBecauseCost?",
                     "M1_1": "GoodWithYourMoney?",
                     "M1_2": "GoodAtMath?",
                     "M4": "FinancialKnowledge?",
                     "M20": "FinancialEducationOfferedAtSchoolOrWork?",
                     "M21_1": "ReceiveFinancialEducationInHighSchool?",
                     "M21_2_2015": "ReceiveFinancialEducationInCollege?",
                     "M21_3": "ReceiveFinancialEducationFromWork?",
                     "M21_4": "ReceiveFinancialEducationFromMilitary?",
                     "M30": "ParentsTeachYouAboutFinance?",
                     "M6": "FinancialTestQ1",
                     "M7": "FinancialTestQ2",
                     "M8": "FinancialTestQ3",
                     "M31": "FinancialTestQ4",
                     "M9": "FinancialTestQ5",
                     "M10": "FinancialTestQ6",
                     "wgt_n2": "NationalWeightByAgeGenderEthnicityEducationCensusDivision",
                     "wgt_d2": "DivisionalWeightByAgeGenderEthnicityEducationState",
                     "wgt_s3": "StateWeightByAgeGenderEthnicityEducation"
                     }
codes = {'State':
             {1: "Alabama", 2: "Alaska",
              3: "Arizona",
              4: "Arkansas",
              5: "California",
              6: "Colorado",
              7: "Connecticut",
              9: "District of Columbia",
              8: "Delaware",
              10: "Florida",
              11: "Georgia",
              12: "Hawaii",
              13: "Idaho",
              14: "Illinois",
              15: "Indiana",
              16: "Iowa",
              17: "Kansas",
              18: "Kentucky",
              19: "Louisiana",
              20: "Maine",
              21: "Maryland",
              22: "Massachusetts",
              23: "Michigan",
              24: "Minnesota",
              25: "Mississippi",
              26: "Missouri",
              27: "Montana",
              28: "Nebraska",
              29: "Nevada",
              30: "New Hampshire",
              31: "New Jersey",
              32: "New Mexico",
              33: "New York",
              34: "North Carolina",
              35: "North Dakota",
              36: "Ohio",
              37: "Oklohoma",
              38: "Oregon",
              39: "Pennsylvania",
              40: "Rhode Island",
              41: "South Carolina",
              42: "South Dakota",
              43: "Tennessee",
              44: "Texas",
              45: "Utah",
              46: "Vermont",
              47: "Virginia",
              48: "Washington",
              49: "West Virginia",
              50: "Wisconsin",
              51: "Wyoming"
              },
         "CensusDivision": {
             1: "New England",
             2: "Middle Atlantic",
             3: "East North Central",
             4: "West North Central",
             5: "South Atlantic",
             6: "East South Central",
             7: "West South Central",
             8: "Mountain",
             9: "Pacific"
         },
         "CensusDivision": {
             1: "New England",
             2: "Middle Atlantic",
             3: "East North Central",
             4: "West North Central",
             5: "South Atlantic",
             6: "East South Central",
             7: "West South Central",
             8: "Mountain",
             9: "Pacific"
         },
         "CensusRegion": {
             1: "Northeast",
             2: "Midwest",
             3: "South",
             4: "West"
         },
         "Gender": {
             1: "Male",
             2: "Female"
         },
         "AgeGroup": {
             1: '18-24',
             2: '25-34',
             3: '35-44',
             4: '45-54',
             5: '55-64',
             6: '65+'
         },
         "Ethnicity": {
             1: "White",
             2: "Non-White"
         },
         "HighestLevelEducation": {
             1: "Did not complete HS",
             2: "HS diploma",
             3: "GED or alternative",
             4: "College, no degree",
             5: "Associate's",
             6: "Bachelor's",
             7: "Post Graduate",
             99: "No Answer"
         },
         "MaritalStatus": {
             1: "Married",
             2: "Single",
             3: "Separated",
             4: "Divorced",
             5: "Widowed/Widower",
             99: "No Answer"
         },
         "LivingArrangements": {
             1: "Only adult",
             2: "Live with spouse",
             3: "Live with parents",
             4: "Live with other",
             99: "No Answer"
         },
         "HouseholdIncome": {
             1: "[0, 15K)",
             2: "[15k, 25k)",
             3: "[25k, 35k)",
             4: "[35k, 50k)",
             5: "[50k, 75k)",
             6: "[70k, 100k)",
             7: "[100k, 150k)",
             8: "150k+",
             98: "Don't know",
             99: "No Answer"
         },
         "CurrentWorkStatus": {
             1: "Self employed",
             2: "Work full-time",
             3: "Work part-time",
             4: "Homemaker",
             5: "Full-time student",
             6: "Permanently disabled",
             7: "Unemployed",
             8: "Retired",
             99: "No Answer"
         },
         "SpouseCurrentWorkStatus": {
             1: "Self employed",
             2: "Work full-time",
             3: "Work part-time",
             4: "Homemaker",
             5: "Full-time student",
             6: "Permanently disabled",
             7: "Unemployed",
             8: "Retired",
             99: "No Answer"
         },
         "WhoExpertInFinances": {
             1: "You",
             2: "Someone else",
             3: "You and someone else are equally knowledgeable",
             98: "Don't know"
         },
        }

wealth_metric = ['SavingsAccount?', "CheckingAccount?", "ConfidenceLevelToEarn2000WithinMonth", "EmregencyFunds?",
                 "SpendingVsIncome",
                 "OtherInvestments?", "OwnHome?", "CurrentlyMortgages?", "TooMuchDebt?"]

columns_to_drop = ["Gender/AgeNet", "EndOfMilitaryService", "RetireFromMilitary?", "SpouseUSVeteran?"]
