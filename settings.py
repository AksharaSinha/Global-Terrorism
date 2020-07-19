TRACK_TERMS = ["terrorist", "terrorist attacks", "bomb blast", "explosions", "armed assault", "hijacking", "hostage taking", "taliban", "ISIS", "Islamic State", "Boko haram", "Al-Shabaab", "Shining Path", "Al-Qaeda", "Irish Republic Army", "Liberation Tigers of Tamil EELAM", "maoists", "New People's Army"]
CSV_NAME = "tweets.csv"
TABLE_NAME = "terrortweets"

try:
    from private import *
except Exception:
    pass