import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import schema
import csv
from pdb import set_trace


def new_columns(df):
    df.rename(columns=schema.column_dictionary, inplace=True)
    return df


def convert_row_values(df):
    for k in schema.codes:
        dictionary = {k: dict(schema.codes[k])}
        df.replace(to_replace=dictionary, inplace=True)
    return df


def ignore_columns(df):
    for c in schema.columns_to_drop:
        df.drop(c, axis=1)

def idk_metric(df):
    for k in schema.idk_columns:
        dictionary = {k: dict(schema.idk_score)}
        df.replace(to_replace = dictionary, inplace=True)
    return df

def pipeline(dataframe):
    modified_columns_df = new_columns(dataframe)
    drop_columns = ignore_columns(modified_columns_df)
    master_df = convert_row_values(modified_columns_df)
    master_master_df = idk_metric(master_df)
    return master_master_df


def stdntloans_state(df):
    test1 = df.groupby(['State', "StudentLoans?1=Y"])['State'].count().unstack('StudentLoans?1=Y').fillna(0)
    test1.plot(kind='bar', stacked=True)
    plt.show()


def age_budget(df):
    test2 = df.groupby(['AgeGroup', 'Budget?'])['AgeGroup'].count().unstack('Budget?').fillna(0)
    test2.plot(kind='bar', stacked=True)
    plt.show()


def age_savings(df):
    test3 = df.groupby(['AgeGroup', 'SavingsAccount?'])['AgeGroup'].count().unstack('SavingsAccount?').fillna(0)
    test3.plot(kind='bar', stacked=True)
    plt.show()


def age_retirementfeelings(df):
    data = df.loc[df['DegreeOfWorryAboutRetirement'] <= 7]
    data.boxplot(column='DegreeOfWorryAboutRetirement', by="AgeGroup", showmeans=True)
    plt.show()
    data.boxplot(column='DegreeOfWorryAboutRetirement', by='HighestLevelEducation', showmeans=True)
    plt.show()


def age_emergency(df):
    test5 = df.groupby(['AgeGroup', 'EmergencyFunds?'])['AgeGroup']
    plt.show()

def score_analysis(df):
    # education_groups = df.groupby('HighestLevelEducation')
    #
    print(df['financialliteracyscore'].describe())
    #
    df.hist(column = 'financialliteracyscore')
    # # df.hist(column = 'financialliteracyscore', by="Ethnicity")
    # # df.hist(column = 'financialliteracyscore', by=df.loc[df['AgeGroup'].isin(['18-24'])])
    # # df.hist(column = 'financialliteracyscore', by='CensusRegion')
    # df.hist(column='financialliteracyscore', by='AgeGroup')
    # er_funds = df.loc[df["EmergencyFunds?"].isin([1,2])]
    # er_funds.hist(column = 'EmergencyFunds?')
    # print(er_funds['financialliteracyscore'].describe())
    # fin_know = df.loc[df['FinancialKnowledge?'].isin([1,2,3,4,5,6,7])]
    # fin_know.hist(column = 'FinancialKnowledge?')
    # print(fin_know['FinancialKnowledge?'].describe())


    # younger_adults = df.loc[df['AgeGroup'].isin(['18-24','25-34'])]
    # older_adults = df.loc[df['AgeGroup'].isin(['35-44', '45-54', '55-64', "65+"])]
    # younger_adults.hist(column = 'financialliteracyscore')
    # older_adults.hist(column = 'financialliteracyscore')
    # print(younger_adults['financialliteracyscore'].describe())
    #
    # print(older_adults['financialliteracyscore'].describe())

    # mean = df['financialliteracyscore'].mean()
    # plt.text(80, 80, '\mu = ', mean)
    #
    plt.show()

def financial_score_calculation(df, dictionary_of_parameters):

    for parameter in dictionary_of_parameters:
        index = df[df[parameter].isin(dictionary_of_parameters[parameter]['target'])].index
        df.loc[index, 'financialliteracyscore'] += dictionary_of_parameters[parameter]['score']
    df['financialliteracyscore'] = df['financialliteracyscore'] / 27.0* 100
    print(df['financialliteracyscore'].head())

    df['financialliteracyscore'] = (df['financialliteracyscore']+2)/27.0 *100
    return df


def main():
    csv_path = './2015_state_data.csv'
    df = pd.read_csv(csv_path, index_col='NFCSID')
    results = pipeline(df)

    results['financialliteracyscore'] = 0
    df = financial_score_calculation(results, schema.dictionary_of_parameters)
    # time_now = time.time() - time_0
    # print(time_now)
    score_analysis(df)


    df.to_csv('correct_data.csv')
    # with open('correct_data.csv', "w") as csv_file:
    #     writer = csv.writer(csv_file, delimiter = ',')
    #     for line in df:
    #     #     set_trace()
    #         writer.writerow([line])
    # analysis_one = stdntloans_state(results)
    # analysis_two = age_budget(results)
    # analysis_three = age_savings(results)
    # analysis_four = age_retirementfeelings(results)
    # analysis_five = age_emergency(results)


if __name__ == "__main__": main()
