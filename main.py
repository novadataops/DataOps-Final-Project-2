import logging
from extract import extract
from transform import transform
from load import load

# Логирование
logging.basicConfig(filename="pipeline.log", level=logging.INFO)

def notify_error(msg):
    print(f"[ALERT] {msg}")  # можно расширить через email/Slack

if __name__ == "__main__":
    try:
        logging.info("Pipeline started")
        df = extract()
        df_transformed = transform(df)
        load(df_transformed)
        logging.info("Pipeline finished successfully")
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
        notify_error(str(e))
