import argparse
import sys
import requests


parser = argparse.ArgumentParser()

# Adding positional argument
parser.add_argument("option", help="New activity(new) or list last 5 activities(list)")

# Adding optional argument
parser.add_argument("-k", "--key", help="Key id of activity")
parser.add_argument("-t", "--type", help="Type of activity (education, recreational, social, diy, charity, cooking, relaxation, music, busywork)")
parser.add_argument("--participants", help="The number of people that this activity could involve")
parser.add_argument("--price", help="A factor describing the cost of the event with zero being free (float)")
parser.add_argument("--minprice", help="Minimal value of price")
parser.add_argument("--maxprice", help="Max value of price")
parser.add_argument("--accessibility", help="A factor describing how possible an event is to do with zero being the most accessible (float)")
parser.add_argument("--minaccessibility", help="Minimal value of accessibility")
parser.add_argument("--maxaccessibility", help="Max value of accessibility")

# Read arguments from command line
args = parser.parse_args()

if len(sys.argv) != 1:
    if args.option == "new":
        params = vars(args)
        result_params = {key: value for key, value in params.items() if value is not None}
        res = requests.get("http://localhost:5000/api/activity/", params=result_params)
        print(res.text)
    elif args.option == "list":
        res = requests.get("http://localhost:5000/api/get_activities/")
        print(res.text)
