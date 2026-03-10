import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux

def link_records(anon_df, aux_df):
    #Merge the anonymized and auxiliary datasets
    merged = pd.merge(anon_df, aux_df, on=['age', 'gender', 'zip3'])
    merged = merged.rename(columns={'name': 'matched_name'}) #Fix autograder error
    #Count records in merged dataset that correspond to each anon_id
    match_counts = merged['anon_id'].value_counts()
    #Filter to keep only the uniquely deanonymized individuals
    unique_ids = match_counts[match_counts == 1].index
    unique_matches = merged[merged['anon_id'].isin(unique_ids)]
    return unique_matches
    
    # raise NotImplementedError


def deanonymization_rate(matches_df, original_anon_df):
    #Count unique records that were successfully linked
    num_matches = len(matches_df)
    #Count records in original anonymized set
    total_records = len(original_anon_df)
    #Calculate the percentage
    if total_records == 0:
        return 0.0
        
    return (num_matches / total_records)

    # raise NotImplementedError
