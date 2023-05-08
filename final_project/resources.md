# [Final Project](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project.html) resources

## Open data portals

There are countless places to get data, notably:

- Local:
   - [NYC OpenData](https://opendata.cityofnewyork.us/)
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
- Lists of open data portals:
   - [DataPortals](https://dataportals.org/)
   - [Open Data Network](https://www.opendatanetwork.com/)

{% if school_slug == "columbia" -%}
## Counting lines of code

To count the number of lines of code in a notebook:

1. Download the notebook as a Python file.
    1. With the notebook open in {{coding_env_name}}, go to `File`->`Download`->`Download .py`.
1. Upload the Python file to [{{coding_env_name}}]({{coding_env_url}}).
1. Put the following in a code cell and run it.

    ```sh
    !apt-get install -y cloc > /dev/null
    !cloc --hide-rate --by-file *.py
    ```
{%- endif %}
