<!-- vim-markdown-toc GFM -->

* [TODO](#todo)
* [Overview](#overview)
* [Programming](#programming)
* [Requirements](#requirements)
* [CSV table layout](#csv-table-layout)
    * [`episode_wins.csv`](#episode_winscsv)
    * [`points_per_race.csv`](#points_per_racecsv)
    * [`placements.csv` - placements by race in each episode of each season](#placementscsv---placements-by-race-in-each-episode-of-each-season)
    * [`items_pulled.csv` - items pulled](#items_pulledcsv---items-pulled)
    * [`itemplay.csv` - items used and blue/shock dodges by season, episode, and race](#itemplaycsv---items-used-and-blueshock-dodges-by-season-episode-and-race)
    * [`stage_hazards.csv` - fallen off the track, hit a cataquack/thwomp/cow/crab/goomba, fallen into water, fallen into lava, reskins of enemies count (e.g Fort Francis maids) by season, episode, and race](#stage_hazardscsv---fallen-off-the-track-hit-a-cataquackthwompcowcrabgoomba-fallen-into-water-fallen-into-lava-reskins-of-enemies-count-eg-fort-francis-maids-by-season-episode-and-race)
    * [`tracks_played` - tracks played](#tracks_played---tracks-played)

<!-- vim-markdown-toc -->

# TODO

- [ ] write a procedure for tracks_played that asks the user:
    - start id?
    - season?
    - episode?
    - is final episode of season?
    - date?
    - is tiebreak episode?
    - twd98 video title?
    - twd98 video link?
    - nmeade video link?
    - how many races?
    - *for as many races as there are, enter the track names on each race*
    - **the program automatically generates SQL statements for all of these operations and executes them**
    - **the first statement uses the start id, and after that increments the id on every new statement**
    - **the track counter starts at 1 and increments for each new race**
- [ ] make a 










# Overview 

- make a proram that allows the user to enter in data to track flounderfest episodes and:
    - their point totals/how points change over time
    - items
    - item usage
    - "stage" hazards
        - track placements
        - track wins
        - every time a win is counted, it increments a total_wins variable
        - plot graphs of points per episode
        - track point differential
        - pandas, matplotlib.pyplot, numpy, readline
        - make an analyser that looks at the item pulls within an episode/season range and says if that player tended to be at the front, middle, or back

# Programming

- data entry system that makes it easier and quicker to update the tables
    - READ
    - WRITE
    - UPDATE
    - DELETE
- `os.path.exists("file/path")` - check if file exists
- `with open("file.csv", "a") as f:` - open file
- `f.flush()` - resets buffer

# Requirements

matplotlib
pandas
numpy
sqlite3

- will write "idk" on tracks i can't identify and will try to later

# CSV table layout

## `episode_wins.csv`

| ID | Season | Episode | Final episode of season `bool` | Date `DATE` | Is tiebreak episode `bool` | Video title `string` | Video link `string` | Nmeade win `bool` | TWD98 win `bool` |
|----|--------|---------|--------------------------------|-------------|----------------------------|----------------------|---------------------|-------------------|------------------|
| 1  | 1      | 1       | false                          | ...         | false                      | ...                  | ...                 | true              | false            |

## `points_per_race.csv`

| ID | Season | Episode | Final episode of season `bool` | Date | Is tiebreak episode `bool` | Video title `string` | Video link `string` | Race | Nmeade points | Nmeade track win `bool` | TWD98 points | TWD98 track win `bool` |
|----|--------|---------|--------------------------------|------|----------------------------|----------------------|---------------------|------|---------------|-------------------------|--------------|------------------------|
| 1  | 1      | 1       | false                          | ...  | false                      | ...                  | ...                 | 1    | 5             | false                   | 15           | true                   |
| 2  | 1      | 1       | false                          | ...  | false                      | ...                  | ...                 | 2    | 15            | true                    | 0            | false                  |
                                                                                                   
## `placements.csv` - placements by race in each episode of each season

| ID | Season | Episode | Final episode of season `bool` | Date | Is tiebreak episode `bool` | Video title `string` | Video link `string` | Race | Nmeade placement | TWD98 placement |
|----|--------|---------|--------------------------------|------|----------------------------|----------------------|---------------------|------|------------------|-----------------|
| 1  | 1      | 1       | false                          | ...  | false                      | ...                  | ...                 | 1    | 1                | 12              |
| 2  | 1      | 1       | ...                            | ...  | false                      | ...                  | 2                   | 12   | 1                | 6               |
| 3  | 1      | 1       | ...                            | ...  | false                      | ...                  | 3                   | 3    | 5                | 1               |

## `items_pulled.csv` - items pulled

| ID | Season | Episode | Final episode of season `bool` | Date | Is tiebreak episode `bool` | Video title `string` | Video link `string` | Race | Nmeade Bananas | Nmeade Bloopers | Nmeade Bob-ombs | Nmeade Bullet Bills | Nmeade Fake Item Boxes | Nmeade Golden Mushrooms | Nmeade Green Shells | Nmeade Lightnings | Nmeade Mega Mushrooms | Nmeade Mushrooms | Nmeade POWs | Nmeade Red Shells | Nmeade Blue Shells | Nmeade Stars | Nmeade Thunder Clouds | Nmeade Triple Bananas | Nmeade Triple Green Shells | Nmeade Triple Mushrooms | Nmeade Triple Red Shells | TWD98 Bananas | TWD98 Bloopers | TWD98 Bob-ombs | TWD98 Bullet Bills | TWD98 Fake Item Boxes | TWD98 Golden Mushrooms | TWD98 Green Shells | TWD98 Lightnings | TWD98 Mega Mushrooms | TWD98 Mushrooms | TWD98 POWs | TWD98 Red Shells | TWD98 Blue Shells | TWD98 Stars | TWD98 Thunder Clouds | TWD98 Triple Green Shells | TWD98 Triple Mushrooms | TWD98 Triple Red Shells |
|----|--------|---------|--------------------------------|------|----------------------------|----------------------|---------------------|------|----------------|-----------------|-----------------|---------------------|------------------------|-------------------------|---------------------|-------------------|-----------------------|------------------|-------------|-------------------|--------------------|--------------|-----------------------|-----------------------|----------------------------|-------------------------|--------------------------|---------------|----------------|----------------|--------------------|-----------------------|------------------------|--------------------|------------------|----------------------|-----------------|------------|------------------|-------------------|-------------|----------------------|---------------------------|------------------------|-------------------------|
| 1  | 1      | 1       | false                          |      | false                      | ...                  | ...                 | 1    | 0              | 0               | 0               | 0                   | 0                      | 0                       | 0                   | 0                 | 0                     | 0                | 0           | 0                 | 0                  | 0            | 0                     | 0                     | 0                          | 0                       | 0                        | 0             | 0              | 0              | 0                  | 0                     | 0                      | 0                  | 0                | 0                    | 0               | 0          | 0                | 0                 | 0           | 0                    | 0                         | 0                      | 0                       |

## `itemplay.csv` - items used and blue/shock dodges by season, episode, and race

| ID | Season | Episode | Final episode of season `bool` | Date | Is tiebreak episode `bool` | Video title `string` | Video link `string` | Race | Nmeade Bananas | Nmeade Bloopers | Nmeade Bob-ombs | Nmeade Bullet Bills | Nmeade Fake Item Boxes | Nmeade Golden Mushrooms | Nmeade Green Shells | Nmeade Lightnings | Nmeade Mega Mushrooms | Nmeade Mushrooms | Nmeade POWs | Nmeade Red Shells | Nmeade Blue Shells | Nmeade Stars | Nmeade Thunder Clouds | Nmeade Triple Bananas | Nmeade Triple Green Shells | Nmeade Triple Mushrooms | Nmeade Triple Red Shells | Nmeade bullet shock dodges | Nmeade mega mushroom shock dodges | Nmeade scrub shock dodges | Nmeade star shock dodges | Nmeade star-mega shock dodges | Nmeade crossed line before shock | Nmeade bullet blue dodges | Nmeade golden mushroom blue dodges | Nmeade mega mushroom blue dodges | Nmeade mushroom blue dodges | Nmeade Triple mushroom blue dodges | Nmeade scrub blue dodges | Nmeade star blue dodges | Nmeade star-mega blue dodges | Nmeade crossed line before blue | TWD98 Bananas | TWD98 Bloopers | TWD98 Bob-ombs | TWD98 Bullet Bills | TWD98 Fake Item Boxes | TWD98 Golden Mushrooms | TWD98 Green Shells | TWD98 Lightnings | TWD98 Mega Mushrooms | TWD98 Mushrooms | TWD98 POWs | TWD98 Red Shells | TWD98 Blue Shells | TWD98 Stars | TWD98 Thunder Clouds | TWD98 Triple Green Shells | TWD98 Triple Mushrooms | TWD98 Triple Red Shells | TWD98 bullet shock dodges | TWD98 mega mushroom shock dodges | TWD98 scrub shock dodges | TWD98 star shock dodges | TWD98 star-mega shock dodges | TWD98 crossed line before shock | TWD98 bullet blue dodges | TWD98 golden mushroom blue dodges | TWD98 mega mushroom blue dodges | TWD98 mushroom blue dodges | TWD98 Triple mushroom blue dodges | TWD98 scrub blue dodges | TWD98 star blue dodges | TWD98 star-mega blue dodges | TWD98 crossed line before blue |
|----|--------|---------|--------------------------------|------|----------------------------|----------------------|---------------------|------|----------------|-----------------|-----------------|---------------------|------------------------|-------------------------|---------------------|-------------------|-----------------------|------------------|-------------|-------------------|--------------------|--------------|-----------------------|-----------------------|----------------------------|-------------------------|--------------------------|----------------------------|-----------------------------------|---------------------------|--------------------------|-------------------------------|----------------------------------|---------------------------|------------------------------------|----------------------------------|-----------------------------|------------------------------------|--------------------------|-------------------------|------------------------------|---------------------------------|---------------|----------------|----------------|--------------------|-----------------------|------------------------|--------------------|------------------|----------------------|-----------------|------------|------------------|-------------------|-------------|----------------------|---------------------------|------------------------|-------------------------|---------------------------|----------------------------------|--------------------------|-------------------------|------------------------------|---------------------------------|--------------------------|-----------------------------------|---------------------------------|----------------------------|-----------------------------------|-------------------------|------------------------|-----------------------------|--------------------------------|
| 1  | 1      | 1       | false                          |      | false                      | ...                  | ...                 | 1    | 0              | 0               | 0               | 0                   | 0                      | 0                       | 0                   | 0                 | 0                     | 0                | 0           | 0                 | 0                  | 0            | 0                     | 0                     | 0                          | 0                       | 0                        | 0                          | 0                                 | 0                         | 0                        | 0                             | 0                                | 0                         | 0                                  | 0                                | 0                           | 0                                  | 0                        | 0                       | 0                            | 0                               | 0             | 0              | 0              | 0                  | 0                     | 0                      | 0                  | 0                | 0                    | 0               | 0          | 0                | 0                 | 0           | 0                    | 0                         | 0                      | 0                       | 0                         | 0                                | 0                        | 0                       | 0                            | 0                               | 0                        | 0                                 | 0                               | 0                          | 0                                 | 0                       | 0                      | 0                           | 0                              |

## `stage_hazards.csv` - fallen off the track, hit a cataquack/thwomp/cow/crab/goomba, fallen into water, fallen into lava, reskins of enemies count (e.g Fort Francis maids) by season, episode, and race
abcdefghijklmnopqrstuvwxyz

| ID | Season | Episode | Final episode of season `bool` | Date | Is tiebreak episode `bool` | Video title `string` | Video link `string` | Race | Nmeade fallen off track | Nmeade fallen into lava | Nmeade fallen into water | Nmeade hit a cataquack | Nmeade hit a cow | Nmeade hit a crab | Nmeade hit a goomba | Nmeade hit by a thwomp | Nmeade hit by enemy reskin - can't tell what it is | TWD98 fallen off track | TWD98 fallen into lava | TWD98 fallen into water | TWD98 hit a cataquack | TWD98 hit a cow | TWD98 hit a crab | TWD98 hit a goomba | TWD98 hit by a thwomp | TWD98 hit by enemy reskin - can't tell what it is |
|----|--------|---------|--------------------------------|------|----------------------------|----------------------|---------------------|------|-------------------------|-------------------------|--------------------------|------------------------|------------------|-------------------|---------------------|------------------------|----------------------------------------------------|------------------------|------------------------|-------------------------|-----------------------|-----------------|------------------|--------------------|-----------------------|---------------------------------------------------|
| 1  | 1      | 1       | false                          |      | false                      | ...                  | ...                 | 1    | 0                       | 0                       | 0                        | 0                      | 0                | 0                 | 0                   | 0                      | 0                                                  | 0                      | 0                      | 0                       | 0                     | 0               | 0                | 0                  | 0                     | 0                                                 |

## `tracks_played` - tracks played
- will be in the format `MKgame_abbreviation_from_respective_game`
- e.g `mkwii_RR`
- or `custom_TRACK`

| ID | Season | Episode | Final episode of season `bool` | Date | Is tiebreak episode `bool` | Video title `string` | Video link `string` | Race | Track `string` |
|----|--------|---------|--------------------------------|------|----------------------------|----------------------|---------------------|------|----------------|
| 1  | 1      | 1       | false                          |      | false                      | ...                  | ...                 | 1    | LC             |
| 2  | 1      | 1       | false                          |      | false                      | ...                  | ...                 | 2    | DC             |
