# Food Nutritional Component API

This is a RESTful API that provides access to a food nutritional component database. The API allows users to search for food items based on various parameters such as food name, research year, maker name, and food code.

## Getting Started

### Prerequisites

- Python 3.x
- SQLite

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Finbek/Food-Nutrient-Component.git
cd Food-Nutrient-Component
```

2. Install the required packages:

pip install -r requirements.txt

3. Initialize the database (if not already done) and run the api server:

python app.py

## API Documentation

Base URL: http://localhost:4999/api/v1, you may change the port number in config.py

### Endpoints

Search Food

URL: /search
Method: GET

Parameters:

- food_name (optional) - Search for food items with a specific name or partial name.
- research_year (optional) - Filter food items by the year of research.
- maker_name (optional) - Search for food items produced by a specific maker or in a particular region.
- food_code (optional) - Search for food items by their unique food code.

Example Request:

GET /api/v1/food_nutrient_search?research_year=2023

Example Response:

[
[
{
"1회 제공량": 150,
"나트륨(mg)(1회제공량당)": "560.71",
"단백질(g)(1회제공량당)": "34.4",
"번호": 7,
"식품군": "음식",
"식품이름": "불고기",
"식품코드": "D000016",
"열량(kcal)(1회제공량당)": "395.29",
"자료출처": "품목대표",
"조사년도": 2019,
"지방(g)(1회제공량당)": "25.2",
"지역/제조사": "광양",
"총당류(g)(1회제공량당)": "7.9",
"콜레스테롤(mg)(1회제공량당)": "68.85",
"탄수화물(g)(1회제공량당)": "7.8",
"트랜스지방(g)(1회제공량당)": "0.4",
"포화지방산(g)(1회제공량당)": "6.6"
}
]
]
