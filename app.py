from flask import Flask, request, jsonify
import sqlite3
from config import FILE_PATH, DB_NAME, TABLE_NAME, PORT, HOST
from parser import parse_xlsx_and_save_to_db
import os
app = Flask(__name__)

@app.route("/api/v1/food_nutrient_search", methods=["GET"])
def search_food():

    food_name = request.args.get("food_name")
    research_year = request.args.get("research_year")
    maker_name = request.args.get("maker_name")
    food_code = request.args.get("food_code")


    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()


    sql_query = f"SELECT * FROM {TABLE_NAME} WHERE 1"
    if food_name:
        sql_query += f" AND food_name LIKE '%{food_name}%'"
    if research_year:
        sql_query += f" AND research_year = '{research_year}'"
    if maker_name:
        sql_query += f" AND maker_name LIKE '%{maker_name}%'"
    if food_code:
        sql_query += f" AND food_cd = '{food_code}'"


    cursor.execute(sql_query)
    search_results = cursor.fetchall()
    conn.close()
    response_items = []
    for result in search_results:
        response_item = {
            "번호": result[0],
            "식품코드": result[1],
            "식품군": result[2],
            "식품이름": result[3],
            "조사년도": result[4],
            "지역/제조사": result[5],
            "자료출처": result[6],
            "1회 제공량": result[7],
            "열량(kcal)(1회제공량당)": result[8],
            "탄수화물(g)(1회제공량당)": result[9],
            "단백질(g)(1회제공량당)": result[10],
            "지방(g)(1회제공량당)": result[11],
            "총당류(g)(1회제공량당)": result[12],
            "나트륨(mg)(1회제공량당)": result[13],
            "콜레스테롤(mg)(1회제공량당)": result[14],
            "포화지방산(g)(1회제공량당)": result[15],
            "트랜스지방(g)(1회제공량당)": result[16],
        }

        response_items.append(response_item)

    response = jsonify(response_items)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'

    return response

@app.after_request
def add_header(response):
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

if __name__ == "__main__":
    if os.path.exists(DB_NAME)==False:
      parse_xlsx_and_save_to_db()
    app.run(host=HOST, port=PORT)
