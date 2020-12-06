from google.cloud import bigquery

def predict_weight(ismale, gestation_weeks, mother_age, mother_race):
    client = bigquery.Client()
    query = """
    SELECT
    predicted_weight_pounds
    FROM
    ML.PREDICT(MODEL `msds-434-final-project.models.natality_model`,
        (
        SELECT
        CAST({} AS BOOLEAN) as is_male,
        {} as gestation_weeks,
        {} as mother_age,
        CAST({} AS STRING) AS mother_race
        ))
    """.format(ismale, gestation_weeks, mother_age, mother_race)
    results = client.query(query) 
    for result in results:
        prediction = round(result['predicted_weight_pounds'], 2)
    return(prediction)