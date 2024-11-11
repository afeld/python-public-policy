# [Final Project](../final_project.md) resources

## Open data portals

There are countless places to get data, notably:

- Local:
   - [NYC Open Data](https://opendata.cityofnewyork.us/)
      - [Scout](https://scout.tsdataclinic.com/explore/NYC) can be used to find datasets with certain columns
   - [BetaNYC](https://data.beta.nyc/)
- U.S. Federal:
   - [data.gov](https://www.data.gov/)
   - [Census Bureau](https://data.census.gov/)
- [United Nations](https://data.un.org/)
- [World Bank](https://data.worldbank.org/)
- [World Health Organization (WHO)](https://www.who.int/data)
- [Economic Policy Institute](https://www.epi.org/data/)
- [Kaggle](https://www.kaggle.com/datasets)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [Black Wealth Data](https://blackwealthdata.org/)
- Lists of open data portals:
   - [DataPortals](https://dataportals.org/)
   - [Open Data Network](https://www.opendatanetwork.com/)

## Inspiration

For starters, see the [examples from past semesters](examples.md).

Probably not realistic to make visualizations that are as fancy as these ones made by professionals, but they may give you ideas. Some also include links/downloads of the source data.

- [FiveThirtyEight Interactives](https://projects.fivethirtyeight.com/)
- [The Guardian Visual Journalism](https://www.theguardian.com/interactive)
- [New York Times Graphics](https://www.nytimes.com/spotlight/graphics)
- [Our World in Data](https://ourworldindata.org/)
- [ProPublica News Apps](https://www.propublica.org/newsapps/)
- [Visual Capitalist](https://www.visualcapitalist.com/)

## Counting lines of code

To count the number of lines of code in a notebook:

1. Download the notebook.
1. Upload the notebook to [Google Colab](https://colab.research.google.com/).
1. Download the notebook as a Python file.
    1. With the notebook open in JupyterHub, go to `File`->`Download`->`Download .py`.
1. Upload the Python file to Google Colab.
    1. Click the `Files` icon in the sidebar.
    1. Click the `Upload to session storage` button.
    1. Select the `.py` file.
1. Put the following in a code cell and run it.

    ```sh
    !apt-get install -y cloc > /dev/null
    !cloc --hide-rate --by-file *.py
    ```
