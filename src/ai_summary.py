from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_ai_summary(
    kpi,
    area_df,
    category_df
):

    top_area = area_df.loc[
        area_df["spot_count"].idxmax(),
        "area"
    ]

    top_category = category_df.loc[
        category_df["avg_popularity_score"].idxmax(),
        "category"
    ]

    prompt = f"""
あなたは観光データ分析レポートを作成するアシスタントです。

以下の神戸観光データをもとに、PDFレポート用の分析サマリーを日本語で作成してください。

条件：
- 3文以内
- 丁寧で自然な日本語
- 数値から読み取れる内容だけを書く
- 過度な推測はしない

データ：
総スポット数：{kpi["total_spots"]}
平均評価：{kpi["average_rating"]}
総レビュー数：{kpi["total_reviews"]}
最も人気の高いスポット：{kpi["top_spot"]}
人気指数：{kpi["top_score"]}
スポット数が最も多いエリア：{top_area}
平均人気指数が最も高いカテゴリ：{top_category}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as error:
        print(error)

        return (
            f"神戸市内の観光スポット{kpi['total_spots']}件を分析した結果、"
            f"最も人気の高いスポットは{kpi['top_spot']}でした。"
            f"{top_area}はスポット数が最も多く、観光資源が集中しているエリアです。"
            f"また、{top_category}カテゴリは平均人気指数が最も高く、"
            f"観光客から高い関心を集めていると考えられます。"
        )