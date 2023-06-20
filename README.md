# Project--1

## Capturing the Beat of America: A Comprehensive Study of Music Genres

### Most Popular Genres of Music for 2022
Matthew Henry, Amara Henry, Christina LaManna, Ifeanyi Ezugwu

### Project Description/Outline
#### Project Description:
This project aims to provide a comprehensive analysis of music genre popularity in 2022, identify the most influential artists within each popular genre during this period, and examine how certain demographics impact the distribution of music preferences.

##### Objective 1: Determining the Three Most Popular Music Genres
By analyzing various sources, including listening preferences, streaming data, and charts, this project will identify and rank the three most popular music genres in 2022. The analysis will consider factors such as streaming statistics and overall audience preference based on demographics to establish the genres that have resonated the most with listeners during this period.

##### Objective 2: Identifying Artists with the Most Significant Impact on Each Genre
Building upon the identified popular genres, this project will delve into the artists who have exerted the most significant influence within each genre. By examining various factors such as album sales, critical acclaim, streaming numbers, and cultural impact, we will identify and highlight the artists who have shaped and defined these genres during the specified time frame.

##### Objective 3: Investigating the Effects of Demographics on Music Distribution
This project will explore how certain demographics impact the popularity of different music genres. By leveraging available data, such as music streaming platforms, we will analyze the listening preferences of various demographic groups. We will examine which genres are more favored by different demographics, such as age groups, genders, and levels of income.

### Expected Outcome:
This project will result in a comprehensive analysis report that outlines the three most popular music genres of 2022, highlights the artists who have significantly influenced each genre, and examines the impact of demographics on music distribution. The findings will offer valuable insights into the current music landscape, enabling a better understanding of audience preferences and the cultural dynamics of music consumption.

### Research Questions
1) What are the three most popular genres of music in 2022?
2) What artist affected each genre the most in that year?
3) How do demographics affect the popularity of those genres?
    
### Rough Breakdown of Tasks
#### Christina LaManna - Managing GitHub, Analysis, Presentation
#### Amara Henry - Cleaning of Data, Visual
#### Matthew Henry - Cleaning of Data, Visual
#### Ifeanyi Ezugwu - Visual

### Datasets To Be Used
#### STATISTA
    https://www-statista-com.atxlibrary.idm.oclc.org/
#### DEVELOPER.SPOTIFY.COM
    developer.spotify.com
#### KAGGLE
    https://www.kaggle.com/datasets/pepepython/spotify-huge-database-daily-charts-over-3-years](https://www.kaggle.com/datasets/rakkesharv/spotify-top-10000-streamed-songs?resource=download

## Analysis
### Question #1
#### What are the three most popular genres of music in 2022?
Through thorough analysis of music preference surveys using Statista, we meticulously filtered the raw data based on key demographic factors such as age, gender identity, ethnicity, and state. Our dataset encompassed 59,934 respondents, intended to represent the 187.4 million internet users in the United States during the survey year of 2022.

To ensure data accuracy, we eliminated categories with a response rating of 2% or less, including ethnicities such as American Indian or Alaskan Native, as well as unresponsive states. With the cleaned CSV data in hand, we proceeded to calculate the percentages of music preferences across our specified filters.

Among the music genres, namely Classical, Country, Dance/Electronic, Folk, Jazz & Blues, Pop/Adult Contemporary, Religious, Hip Hop/R&B/Rap, World, Other, and Don't Know, we encountered certain limitations in our analysis. Notably, the prevailing preference across various demographics appeared to be the category of "don't know," indicating respondents either had difficulty deciding or lacked a specific preference.

Acknowledging this limitation, we expanded our top three genres until we obtained concrete music genre categories to consider. Accounting for this challenge, we identified the top genres within each audience segment, namely state, income, gender, ethnicity, and age. By leveraging Excel, we compared the ratings of each genre and established the following rankings: #1: Other, #2: Dance/Electronica, #3: Rock/Alternative, and #4: a tie between the Urban genre (Hip Hop/R&B/Rap) and Religious.

These findings provide valuable insights into the music preferences of different demographic groups, despite the aforementioned limitations. 

Furthermore, to validate the accuracy of our statistical calculations, we utilized the Spotipy library in Python to develop an algorithm that interacted with the Spotify platform. This algorithm allowed us to compare our calculated top genres with the actual top genres observed on Spotify during the months of 2022.

We cross-referenced our findings with the Spotify data and confirmed that our analysis aligned with the trends observed on the platform. Although our "Other" preference limitation occupied the top rank, our identification of dance/electronica, rock/alternative, and the urban genre (hip hop/R&B/rap) in the top three positions were indeed accurate.

This integration of statistical analysis and real-world data from Spotify serves as a robust validation of our findings, reinforcing the reliability of our methodology and results.
### Question #2
#### What artist affected each genre the most in that year?

### Question #3
#### How do demographics affect the popularity of those genres?
Utilizing the meticulously cleaned dataset, we conducted an in-depth analysis of music preferences based on various demographic factors, including Household Income, Gender, Ethnicity, Age, and residing State.

For the Household Income categories (low, medium, high), we observed that the dominance of the "other" and "don't know" categories necessitated expanding the top 3 genres to the top 4. Consequently, the top genres were ranked as follows: #1: don't know, #2: other, #3: urban, #4: religious, and #5: rock. The influence of the "other" and "don't know" categories posed limitations on determining the top 3 genres.

When considering Gender, we focused on the male and female categories due to limited data availability from the LGBTQ+ community. Within this subset, the top 3 genres emerged as follows: #1: pop, #2: a tie between don't know, urban, religious, and country, and #3: jazz. The reduction in gender categories resulted in more concentrated preferences, leading to a compromise in the second-place ranking due to a tie.

Analyzing preferences by Ethnicity, we examined categories such as Asian, Black/African American, Native Hawaiian, White/Caucasian, and Other (ethnicities with a share of less than 1%), while also accounting for respondents who preferred not to disclose their ethnicity. The top genres derived from this analysis were: #1: don't know, #2: world, #3: other, and #4: a tie between dance/electronica and urban (hip hop/R&B/rap).

Within the Age category, we divided respondents into three groups: 18-29 years, 30-49 years, and 50-64 years. After calculating preferences within each age group, we aggregated the data to determine the overall percentage distribution of preferences for each genre. The top genres based on this analysis were: #1: don't know, #2: other, #3: rock/alternative, #4: pop, and #5: jazz. The age-based analysis provided clearer rankings due to more focused age ranges.

Lastly, we considered the geographic dimension by analyzing music preferences across different states, including the District of Columbia. By removing states and districts that accounted for less than 2% of the votes, we obtained a refined dataset consisting of 23 states. The results showcased distinct and resounding preferences, with the top genres being: #1: other, #2: dance/electronic, #3: rock/alternative, and #4: urban (hip hop/R&B/rap).

Through our comprehensive statistical analysis across these various demographic factors, we gained valuable insights into the music preferences of the surveyed population. The rankings and trends observed in the data were further corroborated by cross-referencing with real-time data from the Spotify platform, ensuring the reliability and accuracy of our findings.

### Conclusion
