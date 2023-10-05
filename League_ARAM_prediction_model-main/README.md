![](https://github.com/VickusWan/League_ARAM_prediction_model/blob/EDA/images/league.jpg)

# League_ARAM_prediction_model

League of Legends is team-based game where players form a team of five and assume the role of a champion, characters with unique abilities, generally varying around a type of class, and battle against another team of five players. ARAM (all random, all mid) is a game mode where the champions are randomly selected (rather than picked).

## Goal/Hypothesis
Since the champions of each players are randomly selected, the goal of this data analysis is to find whether certain parameters affected the winning rate of games. Several factors that are included in the data set are: 
- Team kills
- Team deaths
- Total Damage Dealt
- Total Damage Taken
- Total Time CC'ed (how long is the champion stunned/unable to move)
- Total Gold Earned
- First turret
- Champion Tag

## Data Scrapping/Collection
Since there were no available dataset on the specific hypothesis, the data had to be collected through the RIOT developed API (https://developer.riotgames.com/apis) (note: users need a personal API key in order to access the API). The steps to obtain the dataset were:
1. Obtain a summoner's encrypted ID, which can be found using a summoner's name.
2. Using the summoner's encrypted ID, obtain the match history for the past 100 games.
3. Obtain each match's ID and filter out games that are ARAM game modes only.
4. Using the matchID, extract the information mentioned above.

The final dataset contains approximately 2000 points, which is found under (Match_history.csv) https://github.com/VickusWan/League_ARAM_prediction_model/blob/EDA/Match_history.csv

## Exploratory Data Analysis (EDA)

After the data is cleaned up, parameters were visualized against each other to find trends or patterns. Below is a histogram for the total damage dealt, damage taken and total gold earned for each individual games. The blue color represents the winning team, and the red, for the losing team.

![](https://github.com/VickusWan/League_ARAM_prediction_model/blob/EDA/images/damage.png)

For the damage dealt, the blue team apepars to be slightly more skewed to the right. For the damage taken, the blue team appears to have a higher frequency in the lower portion of the bin ranges. Finally, the blue team seems to have a trend that is more skewed to the red, compared to the red team.

Next, we have the kill-death-assist ratio for each team, 

![](https://github.com/VickusWan/League_ARAM_prediction_model/blob/EDA/images/kda.png)

As shown, it can be seen that the blue team (winning team) has a greater assist score for a lower death. On the other hand, the orange team (losing team) has a greater death to assist ratio.

Finally, an original conclusion was that certain champion classes were more effective in the ARAM gameplay. For example, it is hypothesized that mages were better performers than supports.

![](https://github.com/VickusWan/League_ARAM_prediction_model/blob/EDA/images/dist.png)

AS shown, it can be seen that the blue team (winning team) has a greater average mages and tanks in their team composition, while the red team (losing team) carries a team composition with more assassins and fighters. All other classes seem to have the same disparity.

## Data Modelling

Having a cleaned up dataset, the next step would be to use Machine Learning Algorithms to predict if a team would win based on the listed factors. 

The first step would be to numerize the label WIN/LOSS. In this case, the WIN would be equivalent to "1" and the LOSS would be represented by "0". Afterwards, we drop the "MatchID" feature since it does not provide any effect on the final score. 

For this dataset, both the Naives-Bayes and the K-Nearest Neighbours were used as Machine Learning Algorithms. 

![](https://github.com/VickusWan/League_ARAM_prediction_model/blob/main/images/setup.PNG)

Using the sci-kit module, the F1 prediction score of the K-Nearest Neighbours was found to be,

![](https://github.com/VickusWan/League_ARAM_prediction_model/blob/main/images/KN.PNG)

Finally, the F1 prediction score of Naive Bayes was found to be,

![](https://github.com/VickusWan/League_ARAM_prediction_model/blob/main/images/NB.PNG)

## Conclusion

Thus, with certain parameters before-game (champion classes), and during game factors (kills, death, gold, damage), we can use the Naives Bayes algorithms to predict whether a team will win or lose, with a F1 score of 78%.
