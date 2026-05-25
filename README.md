# Decoding the 2026 Tamil Nadu Assembly Election
## Project Overview
This project analyzes Tamil Nadu Assembly Elections 2026 results and presents insights to a fictional news network Atliq Media.

--- 

### Problem Statement
AtliQ Media is a national news network making a one-hour TV show on the 2026 Tamil Nadu Assembly election results.  Our job is to find the most interesting stories in the 2026 results, build clear charts for each story, and pitch them to AtliQ in a way that helps them plan the show.

---

### ✨Features

1. Seats distribution across 6 Tamil Nadu regions — AIADMK's heartlands South and Kongu fell.
2. Flip Story - 163 of 234 constituencies (70% changed the winning party)
3. Story behind TVK's 1.72 crore votes in the election.

---

### 💡 Key Insights

| TVK seats won on debut | **108 / 234** |\
| Constituencies flipped | **163 (70%)** |\
| DMK vote share drop | **37.7% → 24.2% (−13.7 pts)** |\
| AIADMK vote share drop | **33.3% → 21.2% (−13.7 pts)** |\
| AIADMK fell from | ** 21 to 8 ** | seats in Kongu, and from | ** 18 to 5 ** | in South|\
| Chennai Metro sweep | **46.6% vote share → TVK** |

---

### 📽️ Presentation Slides  
_[TN_Elections_2026_Findings](https://github.com/Mythili24/Tamil-Nadu-Assembly-Elections-2026/blob/main/TN_Election_2026_Findings.pptx)_

---

### 📊 Power BI Dashboard
_[Tamil Nadu Elections 2026.pbix](https://github.com/Mythili24/Tamil-Nadu-Assembly-Elections-2026/blob/main/Tamil%20Nadu%20Elections%202026.pbix)_

---

### 🎬 Video Presentation
_[TN_Elections_2026_Findings](https://github.com/Mythili24/Tamil-Nadu-Assembly-Elections-2026/blob/main/TN_Election_2026_Findings.pptx)_

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| 🐍 Python (Pandas) | Data cleaning and analysis |
| 📊 Power BI | Interactive dashboard |
| 🎨 Claude | Slide deck design |
| 🐙 GitHub | Version control and hosting |
| 📹 VEED | Video Recording |

---

## ⚙️ Installation

### Prerequisites
- Python 3.8+
- `pip` package manager
- or Google Colab

## 📂 Steps for scraping 2026 turnout values from results.eci.gov.in 

### Extract voter turnout per candidate for 2026 for all 234 constituencies from eci.gov.in
_[scrapping_with_zenrows.py](https://github.com/Mythili24/Tamil-Nadu-Assembly-Elections-2026/blob/main/scrapping_with_zenrows.py)_\
python scrapping_with_zenrows.py --election_turnout.csv 

### Calculate electorate base from 2021 values
_[calculate_electorate.py](https://github.com/Mythili24/Tamil-Nadu-Assembly-Elections-2026/blob/main/calculate_electorate.py)_\
python calculate_electorate.py --input tn_2021_results.csv --output tn_2021_electorate.csv

### Calculate voter turnout for 2026 and adding it to existing tn_2026_results.csv
_[calculate_turnout_2026.py](https://github.com/Mythili24/Tamil-Nadu-Assembly-Elections-2026/blob/main/calculate_turnout_2026.py)_\
python calculate_turnout_2026.py --input tn_2026_results.csv -- input tn_2021_electorate.csv --output election_turnout_with_2026pct.csv

---

## 📂 Data Sources

- 🏛️ **Election Commission of India** — [results.eci.gov.in](https://results.eci.gov.in)

---

## 👤 Author

**Mythili Subramanian**
- 📍 Bengaluru, Karnataka, India
- 🔗 [LinkedIn](#) ← *www.linkedin.com/in/mythili-subramanian*

---

## 🏆 Submitted For

**Codebasics Resume Project Challenge**
Tamil Nadu 2026 Assembly Election Analysis

---

⚠️ **Disclaimer:** This project takes no political position. All analysis is based solely on publicly available ECI data. This is a non-partisan data analysis exercise.





