import requests
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
import numpy as np

def get_data(ticker, function,key):

    url = 'https://www.alphavantage.co/query'
    params = {'function': function,
          'symbol': ticker,
          'apikey':key
    }

    return requests.get(url,params = params).json()

def merge_data (ticker):

    df = pd.read_csv('data/stocks_quarterly.csv')
    tickers = list(df.symbol.unique())

    if ticker in tickers :
        df = df[df['symbol']== ticker]

    else:

        df = pd.DataFrame()

        r = get_data(ticker,'INCOME_STATEMENT','RE7IZFZJVQHVS0FP')
        response = pd.DataFrame(r['quarterlyReports'])
        response.drop(columns = 'reportedCurrency',inplace = True)
        df = pd.concat([df,response], axis= 1)

        r = get_data(ticker,'BALANCE_SHEET','M4JMED658AGMIEXK')
        response = pd.DataFrame(r['quarterlyReports'])
        response.drop(columns = 'reportedCurrency',inplace = True)
        df = df.merge(response, on = 'fiscalDateEnding')

        r = get_data(ticker,'CASH_FLOW','9Q6MRAOS3OPYVK3R')
        response = pd.DataFrame(r['quarterlyReports'])
        response.drop(columns = 'reportedCurrency',inplace = True)
        df = df.merge(response, on = 'fiscalDateEnding')

        r = get_data(ticker,'EARNINGS','W6ASJZ1LC2DTIE1T')
        response = pd.DataFrame(r['quarterlyEarnings'])
        df = df.merge(response, on = 'fiscalDateEnding')

    return df.head(1)


def  clean_data(df):
    cols = ['grossProfit', 'totalRevenue', 'costOfRevenue',
       'costofGoodsAndServicesSold', 'operatingIncome',
       'sellingGeneralAndAdministrative', 'operatingExpenses',
       'interestExpense', 'depreciationAndAmortization', 'incomeBeforeTax',
       'incomeTaxExpense', 'netIncomeFromContinuingOperations',
       'comprehensiveIncomeNetOfTax', 'ebit', 'ebitda', 'netIncome_x',
       'totalAssets', 'totalCurrentAssets',
       'cashAndCashEquivalentsAtCarryingValue', 'cashAndShortTermInvestments',
       'totalNonCurrentAssets', 'propertyPlantEquipment', 'otherCurrentAssets',
       'otherNonCurrrentAssets', 'totalLiabilities', 'totalCurrentLiabilities',
       'totalNonCurrentLiabilities', 'shortLongTermDebtTotal',
       'otherCurrentLiabilities', 'totalShareholderEquity', 'retainedEarnings',
       'commonStock', 'commonStockSharesOutstanding', 'operatingCashflow',
       'depreciationDepletionAndAmortization', 'capitalExpenditures',
       'profitLoss', 'cashflowFromInvestment', 'cashflowFromFinancing',
       'proceedsFromRepurchaseOfEquity', 'changeInCashAndCashEquivalents',
       'netIncome_y', 'reportedEPS', 'estimatedEPS', 'surprise',
       'surprisePercentage']

    preproc_data = pd.read_csv('data/preproc_data.csv')

    df = df.replace('None',np.nan)
    column_transformer = make_column_transformer((SimpleImputer(strategy='median'),cols),
                                            remainder="passthrough")

    column_transformer.fit(preproc_data)
    df  = column_transformer.transform(df)

    return df

import requests
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
import numpy as np

def get_data(ticker, function,key):

    url = 'https://www.alphavantage.co/query'
    params = {'function': function,
          'symbol': ticker,
          'apikey':key
    }

    return requests.get(url,params = params).json()

def merge_data (ticker):

    df = pd.read_csv('data/stocks_quarterly.csv')
    tickers = list(df.symbol.unique())

    if ticker in tickers :
        df = df[df['symbol']== ticker]

    else:

        df = pd.DataFrame()

        r = get_data(ticker,'INCOME_STATEMENT','RE7IZFZJVQHVS0FP')
        response = pd.DataFrame(r['quarterlyReports'])
        response.drop(columns = 'reportedCurrency',inplace = True)
        df = pd.concat([df,response], axis= 1)

        r = get_data(ticker,'BALANCE_SHEET','M4JMED658AGMIEXK')
        response = pd.DataFrame(r['quarterlyReports'])
        response.drop(columns = 'reportedCurrency',inplace = True)
        df = df.merge(response, on = 'fiscalDateEnding')

        r = get_data(ticker,'CASH_FLOW','9Q6MRAOS3OPYVK3R')
        response = pd.DataFrame(r['quarterlyReports'])
        response.drop(columns = 'reportedCurrency',inplace = True)
        df = df.merge(response, on = 'fiscalDateEnding')

        r = get_data(ticker,'EARNINGS','W6ASJZ1LC2DTIE1T')
        response = pd.DataFrame(r['quarterlyEarnings'])
        df = df.merge(response, on = 'fiscalDateEnding')

    return df.head(1)


def  clean_data(df):
    cols = ['grossProfit', 'totalRevenue', 'costOfRevenue',
       'costofGoodsAndServicesSold', 'operatingIncome',
       'sellingGeneralAndAdministrative', 'operatingExpenses',
       'interestExpense', 'depreciationAndAmortization', 'incomeBeforeTax',
       'incomeTaxExpense', 'netIncomeFromContinuingOperations',
       'comprehensiveIncomeNetOfTax', 'ebit', 'ebitda', 'netIncome_x',
       'totalAssets', 'totalCurrentAssets',
       'cashAndCashEquivalentsAtCarryingValue', 'cashAndShortTermInvestments',
       'totalNonCurrentAssets', 'propertyPlantEquipment', 'otherCurrentAssets',
       'otherNonCurrrentAssets', 'totalLiabilities', 'totalCurrentLiabilities',
       'totalNonCurrentLiabilities', 'shortLongTermDebtTotal',
       'otherCurrentLiabilities', 'totalShareholderEquity', 'retainedEarnings',
       'commonStock', 'commonStockSharesOutstanding', 'operatingCashflow',
       'depreciationDepletionAndAmortization', 'capitalExpenditures',
       'profitLoss', 'cashflowFromInvestment', 'cashflowFromFinancing',
       'proceedsFromRepurchaseOfEquity', 'changeInCashAndCashEquivalents',
       'netIncome_y', 'reportedEPS', 'estimatedEPS', 'surprise',
       'surprisePercentage']

    preproc_data = pd.read_csv('data/preproc_data.csv')

    df = df.replace('None',np.nan)
    column_transformer = make_column_transformer((SimpleImputer(strategy='median'),cols),
                                            remainder="passthrough")

    column_transformer.fit(preproc_data)
    df  = column_transformer.transform(df)

    return df

