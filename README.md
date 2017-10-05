# Predictive Maintenance

Experimenting with predictive maintenance models.

Source data: https://ti.arc.nasa.gov/tech/dash/pcoe/prognostic-data-repository/#turbofan

# Getting Started

## Data

To generate necessary train/test data, execute the following command:

```sh
make data
```
We will have `train.csv`, `test.csv` and `RUL.csv` in `data/processed/` folder.

The `test.csv` and `train.csv` files are in the following format:

| Column     | Description                                                      |
|------------|------------------------------------------------------------------|
| dataset_id | id of the dataset where this instance is found                   |
| unit_id    | id of engine (unique in each dataset)                            |
| cycle      | number of operational cycles since beginning of engine operation |
| setting 1  | value of operational setting 1                                   |
| setting 2  | value of operational setting 2                                   |
| setting 3  | value of operational setting 3                                   |
| sensor 1   | value of sensor 1                                                |
| ...        | ...                                                              |
| sensor 21  | value of sensor 21                                               |

The `RUL.csv` file is in the following format:

| Column     | Description                                                                         |
|------------|-------------------------------------------------------------------------------------|
| dataset_id | id of the original dataset of this instance                                         |
| unit_id    | id of engine (unique in each dataset)                                               |
| rul        | the remaining useful life of this unit, after its maximum cycle in the test dataset |
