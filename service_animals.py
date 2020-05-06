import csv
import itertools
import requests

# https://beta.regulations.gov/document/DOT-OST-2018-0068-12959/comment
REG_OBJ_ID = "090000648432b7e1"
FILENAME = "service_animals.csv"


# curl 'https://beta.regulations.gov/api/comments?filter%5BcommentOnId%5D=090000648432b7e1&page%5Bnumber%5D=1'
def get_comments(page):
    params = {"filter[commentOnId]": REG_OBJ_ID, "page[number]": page}
    response = requests.get("https://beta.regulations.gov/api/comments", params=params)
    return response.json()


def get_comment(id):
    response = requests.get("https://beta.regulations.gov/api/documentdetails/" + id)
    data = response.json()["data"]

    # collect all the attributes
    attrs = data["attributes"]
    attrs["id"] = data["id"]
    attrs["type"] = data["type"]
    # TODO handle attachments, e.g. from
    # https://beta.regulations.gov/api/documentdetails/DOT-OST-2018-0068-14971

    return attrs


with open(FILENAME, "w") as csvfile:
    writer = None

    for page in itertools.count(start=1):
        print("Page", page)
        response = get_comments(page)

        for comment_summary in response["data"]:
            id = comment_summary["id"]
            print(" ", id)
            comment = get_comment(id)

            if not writer:
                # initialize
                writer = csv.DictWriter(csvfile, fieldnames=comment.keys())
                writer.writeheader()

            writer.writerow(comment)

        if response["meta"]["lastPage"]:
            break
