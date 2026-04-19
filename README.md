```bash

cloud-data-pipeline/
├── README.md
├── pyproject.toml / requirements.txt
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── configs/
│   ├── dev.yaml
│   ├── staging.yaml
│   └── prod.yaml
├── pipelines/
│   ├── ingestion/
│   ├── transformation/
│   ├── training_data/
│   └── exports/
├── src/
│   ├── api_clients/
│   ├── extract/
│   ├── transform/
│   ├── load/
│   ├── validation/
│   ├── logging_utils/
│   ├── storage/
│   └── utils/
├── orchestration/
│   ├── airflow/
├── sql/
│   ├── staging/
│   ├── marts/
│   └── checks/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── data_quality/
├── infra/
│   ├── terraform/
│   ├── cloudformation/
│   └── iam/
├── notebooks/
│   └── exploration/
├── scripts/
│   ├── bootstrap.sh
│   ├── backfill.py
│   └── run_local.py
└── .github/workflows/
    ├── ci.yml
    └── deploy.yml

```
