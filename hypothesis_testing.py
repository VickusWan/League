import numpy as np
from scipy import stats

def student_ttest(null, alt, test='less'):
    
    equal_var = levene_test(null, alt)
    if equal_var[1] >= 0.05:
        var = True
    else:
        var = False
        
    statistic, pvalue = stats.ttest_ind(a=null, b=alt, equal_var=var, alternative=test, random_state=0, nan_policy='omit')
    return statistic, pvalue

def levene_test(null, alt):
    statistic, pvalue = stats.levene(null, alt)
    return (statistic, pvalue)