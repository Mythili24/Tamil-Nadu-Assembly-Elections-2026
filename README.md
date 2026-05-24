# Decoding the 2026 Tamil Nadu Assembly Election
## Project Overview
This project analyzes Tamil Nadu Assembly Elections 2026 results and presents insights to a fictional news network Atliq Media.

### Problem Statement
AtliQ Media is a national news network making a one-hour TV show on the 2026 Tamil Nadu Assembly election results.  Our job is to find the most interesting stories in the 2026 results, build clear charts for each story, and pitch them to AtliQ in a way that helps them plan the show.

### ✨Features

1. Seats distribution across 6 Tamil Nadu regions — AIADMK's heartlands South and Kongu fell.
2. Flip Story - 163 of 234 constituencies (70% changed the winning party)
3. Story behind TVK's 1.72 crore votes in the election.

### 💡 Key Insights

| TVK seats won on debut | **108 / 234** |
| Constituencies flipped | **163 (70%)** |
| DMK vote share drop | **37.7% → 24.2% (−13.7 pts)** |
| AIADMK vote share drop | **33.3% → 21.2% (−13.7 pts)** |
| AIADMK fell from | ** 21 to 8 ** | seats in Kongu, and from | ** 18 to 5 ** | in South
| Chennai Metro sweep | **46.6% vote share → TVK** |

### 📽️ Presentation Slides

![Front Page]<img width="960" height="540" alt="TN_Election_2026_Findings" src="https://github.com/user-attachments/assets/b17ba0f9-d899-4be3-89e5-4090f27bc9c4" />

### 📊 Power BI Dashboard
![Landing Page]<img width="1427" height="797" alt="Power BI Front Page" src="https://github.com/user-attachments/assets/d34e3953-c36f-407f-ba53-a06c902e4d5e" />

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| 🐍 Python (Pandas) | Data cleaning and analysis |
| 📊 Power BI | Interactive dashboard |
| 🎨 Claude | Slide deck design |
| 🐙 GitHub | Version control and hosting |
| 🐙 VEED | Video Recording |

## 📂 Scrapping 2026 turnout from results.eci.gov.in 

       1) execute scrapping_with_zenrows.py to extract candidate wise turnout figures for all 234 constituencies
       2) execute calculate_electorate.py to calculate electorate 2021 = turnout 2021 / total votes 2021
       3) execute calculate_turnout_2026.py to calculate final turnout figures for 2026
## 📂 Data Sources

- 🏛️ **Election Commission of India** — [results.eci.gov.in](https://results.eci.gov.in)

⚠️ **Disclaimer:** This project takes no political position. All analysis is based solely on publicly available ECI data. This is a non-partisan data analysis exercise.

## 👤 Author

**Mythili Subramanian**
- 📍 Bengaluru, Karnataka, India
- 🔗 [LinkedIn](#) ← *www.linkedin.com/in/mythili-subramanian*




