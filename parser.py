import pandas as pd
import sqlite3
from config import FILE_PATH, DB_NAME, TABLE_NAME

def parse_xlsx_and_save_to_db():
    column_mappings = {
        "NO": "NO",
        "식품코드": "food_cd",
        "DB군": "group_name",
        "식품명": "food_name",
        "연도": "research_year",
        "지역 / 제조사": "maker_name",
        "상용제품": "ref_name",
        "1회제공량": "serving_size",
        "에너지(㎉)": "calorie",
        "탄수화물(g)": "carbohydrate",
        "단백질(g)": "protein",
        "지방(g)": "province",
        "총당류(g)": "sugars",
        "나트륨(㎎)": "salt",
        "콜레스테롤(㎎)": "cholesterol",
        "총 포화 지방산(g)": "saturated_fatty_acids",
        "트랜스 지방산(g)": "trans_fat"
    }

    df = pd.read_excel(FILE_PATH)

    df.rename(columns=column_mappings, inplace=True)

    desired_columns = list(column_mappings.values())
    df = df[desired_columns]

    conn = sqlite3.connect(DB_NAME)
    df.to_sql(TABLE_NAME, conn, if_exists='replace', index=False)
    conn.close()
