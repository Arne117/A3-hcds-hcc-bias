# A3-hcds-hcc-bias

## Project goal

## Results
In the `data_clean` folder you'll find the  ... [file](data_clean/xy.csv)

| Property | Description |
|---|---|
| X | abc |
| Y | def |

## Data sources
There are two data sources: (1) Wikipedia articles of politicians and (2) world population data.

**Wikipedia articles -**
The Wikipedia articles can be found on [Figshare](https://figshare.com/articles/Untitled_Item/5513449). It contains politicians by country from the English-language wikipedia within the category "Category:Politicians by nationality" and subcategories.
The data file `page_data.csv` is the extracted from the folder `country/data` of downloaded `.zip` file.

**License:**
This data is released under the [CC-BY-SA 4.0 license](https://creativecommons.org/licenses/by/4.0/)


| Property | Description |
|---|---|
| country | The sanitised country name, extracted from the category name |
| page | The unsanitised page title |
| last_edit | The edit ID of the last edit to the page |


**Population data -**
The population data is available in a `.csv` file format in the `data_raw` folder. The file is named `export_2019.csv`. This dataset is drawn from the [world population datasheet](https://www.prb.org/international/indicator/population/table/) published by the Population Reference Bureau (downloaded 2020-11-13 10:14 AM). The dataset was edited to make it easier to use in this project. The population per country is given in millions!

## Special considerations
The Data source for the Wikipedia articles has inconsistent country codes. Where possible, they have been modified to match the country names found in the [PRB dataset](http://www.prb.org/DataFinder/Topic/Rankings.aspx?ind=14) - but it contains nations not found in Wikipedia, and vice versa.
Also, the actual recursion for the Wikipedia articles only went 2 levels deep into the category tree: someone listed as an Antiguan politician, say, is included - someone exclusively listed as an Antiguan politician who was assassinated is not.

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