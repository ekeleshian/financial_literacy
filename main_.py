import pandas as pd
import matplotlib.pyplot as plt

import schema



def new_columns(df):
	df.rename(columns = schema.column_dictionary, inplace = True)
	return df

def convert_row_values(df):
	for k in schema.codes:
		dictionary={k:dict(schema.codes[k])}
		df.replace(to_replace = dictionary, inplace=True)
	return df

def ignore_columns(df):
	for c in schema.columns_to_drop:
		df.drop(c, axis=1)


def pipeline(dataframe):
	modified_columns_df = new_columns(dataframe)
	drop_columns = ignore_columns(modified_columns_df)
	master_df = convert_row_values(modified_columns_df)
	return master_df

def stdntloans_state(df):
	test1 = df.groupby(['State', "StudentLoans?1=Y"])['State'].count().unstack('StudentLoans?1=Y').fillna(0)

	test1.plot(kind='bar', stacked=True)
	plt.show()

def age_budget(df):
	test2 = df.groupby(['AgeGroup','Budget?'])['AgeGroup'].count().unstack('Budget?').fillna(0)
	test2.plot(kind='bar', stacked=True)
	plt.show()

def age_savings(df):
	test3 =df.groupby(['AgeGroup', 'SavingsAccount?'])['AgeGroup'].count().unstack('SavingsAccount?').fillna(0)
	test3.plot(kind='bar', stacked=True)
	plt.show()

def age_retirementfeelings(df):
	test4 = df.groupby(['AgeGroup', 'DegreeOfWorryAboutRetirement'])['AgeGroup'].count().unstack('DegreeOfWorryAboutRetirement').fillna(0)
	test4.plot(kind='bar', stacked=True)
	plt.show()

def age_emergency(df):
	test5 = df.groupby(['AgeGroup', 'EmergencyFunds?'])['AgeGroup'].count().unstack('EmergencyFunds?').fillna(0)
	test5.plot(kind='bar', stacked=True)
	plt.show()


def main():
	csv_path = '/Users/elizabethkeleshian/financial_literacy_analytics/2015_state_data.csv'
	df = pd.read_csv(csv_path)
	results = pipeline(df)
	analysis_one = stdntloans_state(results)
	analysis_two = age_budget(results)
	analysis_three = age_savings(results)
	analysis_four = age_retirementfeelings(results)
	analysis_five = age_emergency(results)




if __name__ == "__main__": main()







