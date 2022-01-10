import yaml
import argparse
import pandas as pd


def read_params(config_path):
    """
    read parameters from the params.yaml file
    input: params.yaml location
    output: parameters as dictionary
    """
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def prep_data(data_path):
    """
    load original csv dataset from given path and make the first data cleaning
    input: csv path 
    output: pandas dataframe 
    """
    
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    
    # Add cleaning functions here
    # This should be customized for each project
    
    return df


def load_data(config_path):
    """
    load data from external/original location (data/external) to the raw folder (data/raw)  
    input: config_path 
    output: save train file in data/raw folder 
    """
    
    config = read_params(config_path)
    external_data_path = config["external_data_config"]["external_data_csv"]
    raw_data_path = config["raw_data_config"]["raw_data_csv"]
    
    df = prep_data(external_data_path)
    df.to_csv(raw_data_path, index=False)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_data(config_path=parsed_args.config)
