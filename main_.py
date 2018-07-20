import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import schema


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
    education_groups = df.groupby('HighestLevelEducation')

    print(education_groups['financialliteracyscore'].mean())

    df.hist(column = 'financialliteracyscore', by='HighestLevelEducation')
    df.hist(column = 'financialliteracyscore', by="Ethnicity")
    df.hist(column = 'financialliteracyscore', by='AgeGroup')
    df.hist(column = 'financialliteracyscore', by='CensusRegion')


    # mean = df['financialliteracyscore'].mean()
    # plt.text(80, 80, '\mu = ', mean)

    plt.show()

def financial_score_calculation(df, dictionary_of_parameters):

    for parameter in dictionary_of_parameters:
        index = df[df[parameter].isin(dictionary_of_parameters[parameter]['target'])].index
        df.loc[index, 'financialliteracyscore'] += dictionary_of_parameters[parameter]['score']
    df['financialliteracyscore'] = df['financialliteracyscore'] / 27.0 * 100
    print(df['financialliteracyscore'].head())

    return df


def main():
    csv_path = '/home/elizabeth/2018SummerProjects/financial_literacy/2015_state_data.csv'
    df = pd.read_csv(csv_path, index_col='NFCSID')
    results = pipeline(df)
    results['financialliteracyscore'] = 0
    time_0 = time.time()
    df = financial_score_calculation(df, schema.dictionary_of_parameters)
    # time_now = time.time() - time_0
    # print(time_now)
    # score_analysis(df)



    # analysis_one = stdntloans_state(results)
    # analysis_two = age_budget(results)
    # analysis_three = age_savings(results)
    # analysis_four = age_retirementfeelings(results)
    # analysis_five = age_emergency(results)


if __name__ == "__main__": main()
