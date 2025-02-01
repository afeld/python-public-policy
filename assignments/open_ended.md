# Open-ended assignments

In [Homework 1](../hw_1.md) and the [Final Project](../final_project.md), you will pick your own dataset(s).

- Use at least one dataset that you aren't familiar with.
   - Using data from a primary source is preferred.
- Finding a dataset available in CSV or JSON is recommended, though [pandas can read other formats](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html).
- If you'd be interested in working with [SIPA alumni employment data](https://www.sipa.columbia.edu/pathways-careers/employment-statistics), [reach out to the instructor](../syllabus.md#instructor-information).

## Open data portals

There are countless places to get data, notably:

- Local:
   - [NYC Open Data](https://opendata.cityofnewyork.us/)
      - [Scout](https://scout.tsdataclinic.com/explore/NYC) can be used to find datasets with certain columns
   - [BetaNYC](https://data.beta.nyc/)
- U.S. Federal:
   - [data.gov](https://www.data.gov/)
   - [Census Bureau](https://data.census.gov/)
   - [Federal Reserve Economic Data (FRED)](https://fred.stlouisfed.org/)
- [United Nations](https://data.un.org/)
- [World Bank](https://data.worldbank.org/)
- [World Health Organization (WHO)](https://www.who.int/data)
- [HealthData.gov](https://healthdata.gov/)
- [Economic Policy Institute](https://www.epi.org/data/)
- [Kaggle](https://www.kaggle.com/datasets)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [Black Wealth Data](https://blackwealthdata.org/)
- [DataHub](https://datahub.io/collections)
- Lists of open data portals:
   - [DataPortals](https://dataportals.org/)
   - [Open Data Network](https://www.opendatanetwork.com/)

## Inspiration

For starters, see the [Final Project examples from past semesters](../final_project/examples.md).

Probably not realistic to make visualizations that are as fancy as these ones made by professionals, but they may give you ideas. Some also include links/downloads of the source data.

- [Climate & Economic Justice Screening Tool](https://screeningtool.geoplatform.gov/)
- [FiveThirtyEight Interactives](https://projects.fivethirtyeight.com/)
- [The Guardian Visual Journalism](https://www.theguardian.com/interactive)
- [New York Times Graphics](https://www.nytimes.com/spotlight/graphics)
- [Our World in Data](https://ourworldindata.org/)
- [ProPublica News Apps](https://www.propublica.org/newsapps/)
- [Statista](https://clio.columbia.edu/catalog/11329105)
- [Visual Capitalist](https://www.visualcapitalist.com/)

## Storing data

To keep data between sessions in Google Colab, you'll probably want to store it in Google Drive.

1. Upload the file(s) somewhere in Drive.
1. In the Google Colab sidebar, click the `Files` icon.
1. Click the `Mount Drive` icon.
   - Think of this as attaching your Drive to your Google Colab instance, as if you were plugging in a USB flash drive.
1. Navigate to the file.
1. Next to the filename, click the three dots.
1. Click `Copy path`.
   - The value should be something like `/content/drive/My Drive/...`.
1. Use this path with `read_csv()`.


## Reducing data size

You can make data smaller _before_ uploading by filtering it through:

- The data portal, if it supports it
  - This makes the download faster, including only the data you need.
  - [Instructions for Socrata-based portals](https://support.socrata.com/hc/en-us/articles/202950808-Creating-a-Filtered-View)
- In a spreadsheet program
