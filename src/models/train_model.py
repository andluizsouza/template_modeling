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


def class_model(train_data_path, target, exp_name, model_dir):

    from pycaret.classification import setup, compare_models, save_model

    train = pd.read_csv(train_data_path, sep=",")
    setup_model = setup(data=train, target=target, preprocess=True,
                        log_experiment=True, experiment_name=exp_name,
                        log_plots=True, log_profile=True, log_data=True)

    best_model = compare_models(n_select=1)
    save_model(best_model, model_dir+exp_name)

    return


def regression_model():

    return


def training(config_path):

    config = read_params(config_path)
    train_data_path = config["processed_data_config"]["train_data_csv"]
    target = config["processed_data_config"]["target"]

    mode = config["modeling_config"]["mode"]
    exp_name = config["modeling_config"]["exp_name"]
    model_dir = config["modeling_config"]["model_dir"]

    if mode == 'classification':
        class_model(train_data_path, target, exp_name, model_dir)
    elif mode == 'regression':
        regression_model()

    return


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    training(config_path=parsed_args.config)



