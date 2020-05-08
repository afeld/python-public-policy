import csv
import itertools
import requests
import sys

if len(sys.argv) != 2:
    print(
        """Usage:

    python reg_comments.py <DocketID>

Example:

    python reg_comments.py DOT-OST-2018-0068-12959

Writes to <DocketID>.csv."""
    )
    exit(1)

DOCKET_ID = sys.argv[1]
FILENAME = f"{DOCKET_ID}.csv"


# curl 'https://beta.regulations.gov/api/comments?filter%5BcommentOnId%5D=090000648432b7e1&page%5Bnumber%5D=1'
def get_comments(docket_obj_id, page):
    params = {"filter[commentOnId]": docket_obj_id, "page[number]": page}
    response = requests.get("https://beta.regulations.gov/api/comments", params=params)
    return response.json()


def get_document(id):
    response = requests.get("https://beta.regulations.gov/api/documentdetails/" + id)
    data = response.json()["data"]

    # collect all the attributes
    attrs = data["attributes"]
    attrs["id"] = data["id"]
    attrs["type"] = data["type"]
    # TODO handle attachments, e.g. from
    # https://beta.regulations.gov/api/documentdetails/DOT-OST-2018-0068-14971

    return attrs


print(
    f"Reading comments from https://beta.regulations.gov/document/{DOCKET_ID}/comment ..."
)

docket = get_document(DOCKET_ID)
docket_obj_id = docket["objectId"]

with open(FILENAME, "w") as csvfile:
    writer = None

    for page in itertools.count(start=1):
        print("Page", page)
        response = get_comments(docket_obj_id, page)

        for comment_summary in response["data"]:
            id = comment_summary["id"]
            print(" ", id)
            comment = get_document(id)

            if not writer:
                # initialize
                writer = csv.DictWriter(csvfile, fieldnames=comment.keys())
                writer.writeheader()

            writer.writerow(comment)

        if response["meta"]["lastPage"]:
            break

print("COMPLETE")
