import pandas as pd

def excel_diff(df_OLD, df_NEW):
    # 차이점 나타내기
    dfDiff = df_NEW.copy()
    newRows = []

    cols_OLD = df_OLD.columns
    cols_NEW = df_NEW.columns
    sharedCols = list(set(cols_OLD).intersection(cols_NEW))

    for row in dfDiff.index:
        if (row in df_OLD.index) and (row in df_NEW.index):
            for col in sharedCols:
                value_OLD = df_OLD.loc[row, col]
                value_NEW = df_NEW.loc[row, col]
                if value_OLD == value_NEW:
                    dfDiff.loc[row, col] = df_NEW.loc[row, col]
                else:
                    dfDiff.loc[row, col] = ('{}→{}').format(value_OLD, value_NEW)
        else:
            newRows.append(row)

    return dfDiff