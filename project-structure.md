
my-ds-project/
├── data/
│   ├── raw/           # Never modify — git-ignored or DVC tracked
│   ├── processed/     # Cleaned, feature-engineered data
│   └── external/      # Third-party reference data
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_eng.ipynb
│   └── 03_modelling.ipynb
├── src/               # Importable Python package
│   ├── __init__.py
│   ├── data/          # Data loading & validation
│   ├── features/      # Feature engineering
│   ├── models/        # Model training & evaluation
│   └── utils/         # Shared utilities
├── tests/             # pytest tests
├── configs/           # YAML/JSON configs
├── outputs/
│   ├── models/        # Serialized models
│   ├── figures/       # Saved plots
│   └── reports/       # Generated reports
├── pyproject.toml
├── uv.lock
├── .gitignore
├── .env.example       # Never commit .env
└── README.md

