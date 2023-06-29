import re
import string

def standardise_column_names(df, remove_punct=True):
    """ Converts all DataFrame column names to lower case replacing
    whitespace of any length with a single underscore. Can also strip
    all punctuation from column names.
    
    Parameters
    ----------
    df: pandas.DataFrame
        DataFrame with non-standardised column names.
    remove_punct: bool (default True)
        If True will remove all punctuation from column names.
    
    Returns
    -------
    df: pandas.DataFrame
        DataFrame with standardised column names.
    Example
    -------
    >>> df = pd.DataFrame({'Column With Spaces': [1,2,3,4,5],
                           'Column-With-Hyphens&Others/': [6,7,8,9,10],
                           'Too    Many Spaces': [11,12,13,14,15],
                           })
    >>> df = standardise_column_names(df)
    >>> print(df.columns)
    Index(['column_with_spaces',
           'column_with_hyphens_others',
           'too_many_spaces'], dtype='object')
    """
    
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))

    for c in df.columns:
        c_mod = c.lower()
        if remove_punct:            
            c_mod = c_mod.translate(translator)
        c_mod = '_'.join(c_mod.split(' '))
        if c_mod[-1] == '_':
            c_mod = c_mod[:-1]
        c_mod = re.sub(r'\_+', '_', c_mod)
        df.rename({c: c_mod}, inplace=True, axis=1)
    return df