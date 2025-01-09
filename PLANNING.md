# Overview 

- make a proram that allows the user to enter in data to track all flounderfest episodes and their point totals/how points change over time
    - track placements
    - track wins
    - every time a win is counted, it increments a total_wins variable
    - plot graphs of points per episode
    - track point differential
    - pandas, matplotlib.pyplot, numpy, readline

# Requirements

matplotlib
pandas
numpy

# CSV table layout

`points.csv`
| Season | Video title `string` | Video link `string` | Nmeade points after each race `[[len(int n)], [len(int n)]]` | Nmeade win `bool` | TWD98 points after each race `[[len(int n)], [len(int n)]]` | TWD98 win `bool` |
|--------|----------------------|---------------------|--------------------------------------------------------------|-------------------|-------------------------------------------------------------|------------------|
| 1      | ...                  | ...                 | [[15, 20, 21, 21...], [1, 2, 3, 4...]]                       | true              | [[15, 20, 21, 21...], [1, 2, 3, 4...]]                      | false            |

`items.csv`
| Season | Video title `string` | Video link `string` | Nmeade Bananas | Nmeade Bloopers | Nmeade Bob-ombs | Nmeade Bullet Bills | Nmeade Fake Item Boxes | Nmeade Golden Mushrooms | Nmeade Green Shells | Nmeade Lightnings | Nmeade Mega Mushrooms | Nmeade Mushrooms | Nmeade POWs | Nmeade Red Shells | Nmeade Blue Shells | Nmeade Stars | Nmeade Thunder Clouds | Nmeade Triple Bananas | Nmeade Triple Green Shells | Nmeade Triple Mushrooms | Nmeade Triple Red Shells | TWD98 Bananas | TWD98 Bloopers | TWD98 Bob-ombs | TWD98 Bullet Bills | TWD98 Fake Item Boxes | TWD98 Golden Mushrooms | TWD98 Green Shells | TWD98 Lightnings | TWD98 Mega Mushrooms | TWD98 Mushrooms | TWD98 POWs | TWD98 Red Shells | TWD98 Blue Shells | TWD98 Stars | TWD98 Thunder Clouds | TWD98 Triple Green Shells | TWD98 Triple Mushrooms | TWD98 Triple Red Shells |
|--------|----------------------|---------------------|----------------|-----------------|-----------------|---------------------|------------------------|-------------------------|---------------------|-------------------|-----------------------|------------------|-------------|-------------------|--------------------|--------------|-----------------------|-----------------------|----------------------------|-------------------------|--------------------------|---------------|----------------|----------------|--------------------|-----------------------|------------------------|--------------------|------------------|----------------------|-----------------|------------|------------------|-------------------|-------------|----------------------|---------------------------|------------------------|-------------------------|
| 1      | ...                  | ...                 | 0              | 0               | 0               | 0                   | 0                      | 0                       | 0                   | 0                 | 0                     | 0                | 0           | 0                 | 0                  | 0            | 0                     | 0                     | 0                          | 0                       | 0                        | 0             | 0              | 0              | 0                  | 0                     | 0                      | 0                  | 0                | 0                    | 0               | 0          | 0                | 0                 | 0           | 0                    | 0                         | 0                      | 0                       |