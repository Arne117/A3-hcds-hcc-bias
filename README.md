# A3-hcds-hcc-bias

## Project goal
The goal of this project is to explore the concept of bias through data on Wikipedia articles - specifically, articles on political figures from a variety of countries. We combine a dataset of Wikipedia articles with a dataset of country populations, and use ORES to estimate the quality of each article.

## Data sources
There are three data sources: (1) Wikipedia articles of politicians, (2) world population data and (3) the ORES data.

(1) **Wikipedia articles -**
The Wikipedia articles can be found on [Figshare](https://figshare.com/articles/Untitled_Item/5513449). It contains politicians by country from the English-language wikipedia within the category "Category:Politicians by nationality" and subcategories.
The data file `page_data.csv` is the extracted from the folder `country/data` of the downloaded `.zip` file.

**License:**
This data is released under the [CC-BY-SA 4.0 license](https://creativecommons.org/licenses/by/4.0/)


| Property | Description |
|---|---|
| country | The sanitised country name, extracted from the category name |
| page | The unsanitised page title |
| last_edit | The edit ID of the last edit to the page |


(2) **Population data -**
The population data is available in a `.csv` file format in the `data_raw` folder. The file is named `export_2019.csv`. This dataset is drawn from the [world population datasheet](https://www.prb.org/international/indicator/population/table/) published by the Population Reference Bureau (downloaded 2020-11-13 10:14 AM). The dataset was edited to make it easier to use in this project. The population per country is given in millions!

| Property | Description |
|---|---|
| country | The country name |
| population | The population count in millions |
| region | The region where the country is in |

(3) **ORES data -**
[ORES](https://ores.wikimedia.org/) is a web service that provides machine learning as a service for Wikimedia Projects, like Wikipedia and Wikidata. The system is designed to help human editors perform critical wiki-work and to increase their productivity by automating tasks like detecting vandalism and removing edits made in bad faith. ORES provides a `scores APIs` where we use the `v3` version in this project. You'll find the documentation [here](https://ores.wikimedia.org/v3/).

**License:**
Rights in Wikidata are waived using the [Creative Commons Zero public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).

## Special considerations
The Data source for the Wikipedia articles has inconsistent country codes. Where possible, they have been modified to match the country names found in the [PRB dataset](http://www.prb.org/DataFinder/Topic/Rankings.aspx?ind=14) - but it contains nations not found in Wikipedia, and vice versa.
Also, the actual recursion for the Wikipedia articles only went 2 levels deep into the category tree: someone listed as an Antiguan politician, say, is included - someone exclusively listed as an Antiguan politician who was assassinated is not.

## Results
In the `data_clean` folder you'll find three `.csv` files. 
1. The [Politicians by country](data_clean/politicians_by_country.csv)

| Property | Description |
|---|---|
| article_name | The name of the article about a politician |
| country | The country where the politician is in |
| region | The region where the politician is in |
| rev_id | The revision IDs for the ORES score |
| article_quality | The ORES prediction about the article's quality |
| population | The population of the country |

2. The [ORES no score](data_clean/ORES_no_scores.csv) file, where ORES had not found a score for a give `rev_id`.

| Property | Description |
|---|---|
| page | the name of the politician / article |
| country | The country where the politician is in |
| rev_id | The revision IDs for the ORES score |
| score | The returned ORES response as a json string |

3. The [Countries with no match](data_clean/countries_no_match.csv) found to compare it with the ORES score

| Property | Description |
|---|---|
| article_name | The name of the article about a politician |
| country | The country where the politician is in |
| region | The region where the politician is in |
| rev_id | The revision IDs for the ORES score |
| article_quality | The ORES prediction about the article's quality |
| population | The population of the country |

---
In the `results` folder you'll find six `.csv` files, which are described in the jupyter notebook in the `3. Analysis` section.

## Replication
### Getting started

We use the  "Amazing Python Data Workflow with Poetry, Pandas, and Jupyter"<sup>[1]</sup> to make sure everyone in the course uses the same environment and we don't run into any dependency hell.

### Prerequisites

Ensure that you have a Python version greater or equal to `3.9`, a working installation of Poetry and git installed.
### Setup

```sh
# 1. Clone this repository (or use SSH) and move it into the repo root
git clone https://github.com/Arne117/A3-hcds-hcc-bias.git
cd A3-hcds-hcc-bias

# 2. Install the dependencies in the repo root
poetry install

# 3. Create a subshell within the virtual environment by running:
poetry shell

# 4. Open the project with Jupyter in your browser.
jupyter notebook
```

---
## Licence
This project is licensed with the [MIT License](LICENSE).