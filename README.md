# pipeline-gen-ai

- Streamlit: Free , for creating dashboards
- Pydantic: for data quality and data contract
- MkDocks for documentation
- SQLAlchemy: for ORM

- Pydantic: data validation for objects and classes
- Pandera: data validation for dataframes (Spark, pandas, etc)

Activate the virtual environment:
```source .venv/Scripts/activate```

Install the requeriments:
```
pip install requirements.txt
```

Run the streamlit app:
```
streamlit run app.py
```

```
pip install mkdocs mkdocs-material mkdocstrings mkdocstrings-python
```

```
mkdocs new .
```

```
mkdocs serve
```

```
mkdocs build
```

```
mkdocs gh-deploy
```

Task 1:
Migrate db from render to AWS

Task2: 
Create medallion architecture: bronze, silver, and gold

Task 3:
dbt-core to create views

Task 4:
SQL and notebook in BRIEFER# pipeline-gen-ai-datawarehouse
