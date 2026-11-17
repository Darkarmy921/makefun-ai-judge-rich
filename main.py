# A working ai-judge-rich-01 entry (Python 3.13, standard library only): it writes one
# fixed plan, the plan an AI agent would follow to turn $100, a computer with internet access
# and 30 days into the most money, to /output/entry.txt. The plan sells same-day Etsy listing
# fixes: a service an agent can do entirely itself (site, payment link, forum outreach, code
# delivery), with a free first listing to remove the buyer's risk, explicit money math, a kill
# rule, and an edge (24/7, delivery in hours) no human freelancer matches.
# Entry text is 917 characters, inside the 1-1,000 gate; two local runs wrote byte-identical output.
#
# The gate takes UTF-8 text of 1 to 1,000 characters that is not only white space, and the judge
# reads exactly the bytes written, line ends included, so write no line end you do not mean to
# show. The program runs twice with no network, and both runs must write the same bytes.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with nothing installed.
# Only the standard library imports. This file keeps everything in itself.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Plan: sell same-day Etsy listing fixes to sellers losing sales to bad listings.",
        "Day 1: one-page site + payment link: rewrite 10 listings (titles, tags, descriptions) for $20, paid in advance, delivered in 24 hours. Post 3 before/after samples.",
        "Days 2-7: answer posts in Etsy seller forums and r/Etsy from sellers asking why their listings do not sell; offer the first listing free. Goal: 5 paying buyers.",
        "Days 8-30: deliver every order in under a day, ask each buyer for a review, raise the price to $25 after 10 five-star reviews. Spend at most $40 on Etsy Ads, only after 5 paid orders.",
        "Math: $100 start + 20 orders x $20 = $400 revenue; costs about $60; end near $440. Kill rule: no paying buyer by day 7, move the same offer to Amazon sellers. Never pay for ads before a sale.",
        "Edge: I work 24/7 and deliver in hours; human freelancers take days. Speed is the product, and the free sample removes the buyer's risk.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
