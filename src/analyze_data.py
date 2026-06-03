import numpy as np


def add_popularity_score(df):
    df["popularity_score"] = (
        (df["rating"] / 5)
        * np.log(df["review_count"] + 1)
    )

    return df


def calculate_kpi(df):
    total_spots = len(df)

    average_rating = round(
        df["rating"].mean(),
        2
    )

    total_reviews = df["review_count"].sum()

    top_spot_row = df.sort_values(
        by="popularity_score",
        ascending=False
    ).iloc[0]

    kpi = {
        "total_spots": total_spots,
        "average_rating": average_rating,
        "total_reviews": total_reviews,
        "top_spot": top_spot_row["spot_name"],
        "top_score": round(top_spot_row["popularity_score"], 2)
    }

    return kpi

def area_analysis(df):

    area_df = (
        df.groupby("area")
        .agg(
            spot_count=("spot_name", "count"),
            avg_rating=("rating", "mean"),
            total_reviews=("review_count", "sum")
        )
        .reset_index()
    )

    area_df["avg_rating"] = (
        area_df["avg_rating"]
        .round(2)
    )

    return area_df


def category_analysis(df):

    category_df = (
        df.groupby("category")
        .agg(
            spot_count=("spot_name", "count"),
            avg_rating=("rating", "mean"),
            total_reviews=("review_count", "sum"),
            avg_popularity_score=("popularity_score", "mean")
        )
        .reset_index()
    )

    category_df["avg_rating"] = (
        category_df["avg_rating"]
        .round(2)
    )

    category_df["avg_popularity_score"] = (
        category_df["avg_popularity_score"]
        .round(2)
    )

    return category_df


def top10_spots(df):

    top10_df = (
        df.sort_values(
            by="popularity_score",
            ascending=False
        )
        [["spot_name",
          "area",
          "category",
          "rating",
          "review_count",
          "popularity_score"]]
        .head(10)
    )

    top10_df["popularity_score"] = (
        top10_df["popularity_score"]
        .round(2)
    )

    return top10_df