"""
Data collection script for Premier League forwards statistics (2025/26 season).

This script uses the ScraperFC library to scrape player statistics from
Sofascore and export the collected data to an Excel file for further analysis.
"""

import pandas as pd
import ScraperFC as sfc


def collect_forwards_stats(
    year: str = "25/26",
    league: str = "England Premier League",
    accumulation: str = "total",
    output_path: str = "premier_league_25_26_forwards.xlsx",
) -> pd.DataFrame:
    """
    Scrape forward players' statistics for a given league/season from Sofascore
    and save the resulting dataset to an Excel file.

    Args:
        year: Season to scrape (e.g. "25/26").
        league: League name as expected by ScraperFC.
        accumulation: Stat accumulation type ("total", "per90", etc.).
        output_path: File path where the resulting Excel file will be saved.

    Returns:
        A pandas DataFrame containing the scraped statistics.
    """
    # Initialize the Sofascore scraper
    sofa = sfc.Sofascore()

    # Scrape statistics for forwards in the specified league/season
    df = sofa.scrape_player_league_stats(
        year=year,
        league=league,
        accumulation=accumulation,
        selected_positions=["Forwards"],
    )

    # Display basic info about the collected dataset
    print("Shape:", df.shape)
    print("\nAvailable columns:\n")
    print(df.columns.tolist())

    # Show a preview of the data (all columns visible)
    pd.set_option("display.max_columns", None)
    print("\nFirst rows:\n")
    print(df.head())

    # Save the dataset to an Excel file
    df.to_excel(output_path, index=False)
    print(f"\nFile saved to '{output_path}'!")

    return df


if __name__ == "__main__":
    collect_forwards_stats()