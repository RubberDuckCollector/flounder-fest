import os
import csv
import numpy
import pprint
import readline
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore


# if it a file isn't found, the program will will create the file and the table's fields
# this is in global scope because i want it to happen every time the program runs
# and the field names should be accessible to every part of the program
episode_wins_field_names = ["season", "episode", "final_episode_of_season", "is_tiebreak", "video_title", "video_link", "nmeade_win", "twd98_win"]
if not os.path.exists("data/episode_wins.csv"):
    with open("data/episode_wins.csv", "w") as f:
        episode_wins_writer = csv.DictWriter(f, fieldnames=episode_wins_field_names)  # initialise field names
        episode_wins_writer.writeheader()  # write field names


points_per_race_field_names = ["season", "episode", "final_episode_of_season", "is_tiebreak", "video_title", "video_link", "race", "nmeade_placement", "twd98_placement"]
if not os.path.exists("data/points_per_race.csv"):
    with open("data/points_per_race.csv", "w") as f:
        points_per_race_writer = csv.DictWriter(f, fieldnames=points_per_race_field_names)
        points_per_race_writer.writeheader()


items_pulled_field_names = ["season", "episode", "final_episode_of_season", "is_tiebreak", "video_title", "video_link", "race", "nmeade_bananas", "nmeade_bloopers", "nmeade_bob-ombs", "nmeade_bullet_bills", "nmeade_fake_item_boxes", "nmeade_golden_mushrooms", "nmeade_green_shells", "nmeade_lightnings", "nmeade_mega_mushrooms", "nmeade_mushrooms", "nmeade_pows", "nmeade_red_shells", "nmeade_blue_shells", "nmeade_stars", "nmeade_thunder_clouds", "nmeade_triple_bananas", "nmeade_triple_green_shells", "nmeade_triple_mushrooms", "nmeade_triple_red_shells", "twd98_bananas", "twd98_bloopers", "twd98_bob-ombs", "twd98_bullet_bills", "twd98_fake_item_boxes", "twd98_golden_mushrooms", "twd98_green_shells", "twd98_lightnings", "twd98_mega_mushrooms", "twd98_mushrooms", "twd98_pows", "twd98_red_shells", "twd98_blue_shells", "twd98_stars", "twd98_thunder_clouds", "twd98_triple_green_shells", "twd98_triple_mushrooms", "twd98_triple_red_shells"]
if not os.path.exists("data/items_pulled.csv"):
    with open("data/items_pulled.csv", "w") as f:
        items_pulled_writer = csv.DictWriter(f, fieldnames=items_pulled_field_names)
        items_pulled_writer.writeheader()


itemplay_field_names = ["season", "episode", "final_episode_of_season", "is_tiebreak", "video_title", "video_link", "race", "nmeade_bananas", "nmeade_bloopers", "nmeade_bob-ombs", "nmeade_bullet_bills", "nmeade_fake_item_boxes", "nmeade_golden_mushrooms", "nmeade_green_shells", "nmeade_lightnings", "nmeade_mega_mushrooms", "nmeade_mushrooms", "nmeade_pows", "nmeade_red_shells", "nmeade_blue_shells", "nmeade_stars", "nmeade_thunder_clouds", "nmeade_triple_bananas", "nmeade_triple_green_shells", "nmeade_triple_mushrooms", "nmeade_triple_red_shells", "nmeade_bullet_shock_dodges", "nmeade_mega_mushroom_shock_dodges", "nmeade_scrub_shock_dodges", "nmeade_star_shock_dodges", "nmeade_star_mega_shock_dodges", "nmeade_crossed_line_before_shock", "nmeade_bullet_blue_dodges", "nmeade_golden_mushroom_blue_dodges", "nmeade_mega_mushroom_blue_dodges", "nmeade_mushroom_blue_dodges", "nmeade_triple_mushroom_blue_dodges", "nmeade_scrub_blue_dodges", "nmeade_star_blue_dodges", "nmeade_star_mega_blue_dodges", "nmeade_crossed_line_before_blue", "twd98_bananas", "twd98_bloopers", "twd98_bob-ombs", "twd98_bullet_bills", "twd98_fake_item_boxes", "twd98_golden_mushrooms", "twd98_green_shells", "twd98_lightnings", "twd98_mega_mushrooms", "twd98_mushrooms", "twd98_pows", "twd98_red_shells", "twd98_blue_shells", "twd98_stars", "twd98_thunder_clouds", "twd98_triple_green_shells", "twd98_triple_mushrooms", "twd98_triple_red_shells", "twd98_bullet_shock_dodges", "twd98_mega_mushroom_shock_dodges", "twd98_scrub_shock_dodges", "twd98_star_shock_dodges", "twd98_star_mega_shock_dodges", "twd98_crossed_line_before_shock", "twd98_bullet_blue_dodges", "twd98_golden_mushroom_blue_dodges", "twd98_mega_mushroom_blue_dodges", "twd98_mushroom_blue_dodges", "twd98_triple_mushroom_blue_dodges", "twd98_scrub_blue_dodges", "twd98_star_blue_dodges", "twd98_star_mega_blue_dodges", "twd98_crossed_line_before_blue"]
if not os.path.exists("data/itemplay.csv"):
    with open("data/itemplay.csv", "w") as f:
        itemplay_writer = csv.DictWriter(f, fieldnames=itemplay_field_names)
        itemplay_writer.writeheader()


stage_hazard_field_names = ["season", "episode", "final_episode_of_season", "is_tiebreak", "video_title", "video_link", "race", "nmeade_fallen_off_track", "nmeade_fallen_into_lava", "nmeade_fallen_into_water", "nmeade_hit_cataquack", "nmeade_hit_cow", "nmeade_hit_crab", "nmeade_hit_goomba", "nmeade_hit_by_thwomp", "nmeade_hit_by_enemy_reskin", "twd98_fallen_off_track", "twd98_fallen_into_lava", "twd98_fallen_into_water", "twd98_hit_cataquack", "twd98_hit_cow", "twd98_hit_crab", "twd98_hit_goomba", "twd98_hit_by_thwomp", "twd98_hit_by_enemy_reskin"]
if not os.path.exists("data/stage_hazards.csv"):
    with open("data/stage_hazards.csv", "w") as f:
        stage_hazard_writer = csv.DictWriter(f, fieldnames=stage_hazard_field_names)
        stage_hazard_writer.writeheader()


def main():
    dataframe = pd.read_csv("data/stage_hazards.csv")
    print(dataframe)


if __name__ == "__main__":
    main()
