# DS340W

Project summary and reproduction instructions.

## Project Organization

```
├── LICENSE
├── README.md          <- Project summary and reproduction instructions
├── data
│   ├── external       <- Data from third party sources
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- Final datasets for modeling
│   └── raw            <- The original, immutable data dump
├── docs               <- Project documentation
├── models             <- Trained and serialized models, model summaries
├── notebooks          <- Jupyter notebooks (naming: 1.0-initial-eda.ipynb)
├── pyproject.toml     <- Modern dependency and tool configuration
├── src                <- Source code for use in this project
│   ├── __init__.py    <- Makes src a Python module
│   ├── data           <- Scripts to download or generate data
│   ├── features       <- Scripts to turn raw data into features for modeling
│   ├── models         <- Scripts to train models and then use trained models
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
└── tests              <- Unit tests for your source code
```

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
pip install -e .
```

### Data

Raw data files are stored in `data/raw/`. Processed datasets for modeling go in `data/processed/`.
