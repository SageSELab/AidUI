# activity message:
# ==============================================================================
# pattern1
# X people/person/visitors/users ordered/purchased/subscribed/viewed/booked in last 24 hours'
# 8 people ordered in last 24 hours
# 8 people are looking right now

# people booked 78 times in last 24 hours

#
# pattern2
# jack just saved 52$ on his order
#
# pattern3
# X items sold in Y time/this hour

pattern_generic_activity_message = [
    {"POS": "NUM", "OP": "?"},
    {"POS": {"IN": ["NOUN", "PROPN"]}},
    {"POS": "AUX", "OP": "?"},
    {"POS": "ADV", "OP": "?"},
    {"POS": "VERB"},
    {"POS": "NUM", "OP": "?"},
    {"POS": "NOUN", "OP": "?"},
    {"POS": "ADP", "OP": "?"},
    {"POS": "DET", "OP": "?"},
    {"POS": "ADJ", "OP": "?"},
    {"POS": "ADV", "OP": "?"},
    {"POS": "ADV", "OP": "?"},
    {"POS": "NUM", "OP": "?"},
    {"POS": "NOUN", "OP": "?"},
]

pattern1_activity_message = [
    {"POS": "NUM", "OP": "?"},
    {"POS": {"IN": ["NOUN", "PROPN"]}},
    {"POS": "AUX", "OP": "?"},
    {"POS": "ADV", "OP": "?"},
    {"LEMMA": {"IN": ["order", "purchase", "subscribe", "view", "book", "visit", "sell", "save", "look"]}},
    {"POS": "NUM", "OP": "?"},
]

pattern2_activity_message = [
    {"POS": "NUM"},
    {"POS": {"IN": ["NOUN", "PROPN"]}, "OP": "?"},
    {"POS": "AUX", "OP": "?"},
    {"POS": "ADV", "OP": "?"},
    {"LEMMA": {"IN": ["order", "purchase", "subscribe", "view", "book", "visit", "sell", "save", "look"]}}
]

patterns_activity_message = [pattern1_activity_message, pattern2_activity_message]


# high demand message:
# ==============================================================================
# .... in high demand ....
# .... reserved for [time] .....

pattern1_high_demand_message = [
    {},
    {"POS": "ADP", "OP": "?"},
    {"LOWER": "high"},
    {"LOWER": "demand"}, {}
]
pattern2_high_demand_message = [
    {},
    {"LEMMA": {"IN": ["order", "book"]}, "OP": "?"},
    {"POS": "AUX", "OP": "?"},
    {"LEMMA": {"IN": ["reserve"]}},
    {"LOWER": "for"},
    {"POS": "NUM"},
    {}
]
pattern3_high_demand_message = [
    {"LEMMA": {"IN": ["sell"]}},
    {"LOWER": "fast"},
    {}
]

patterns_high_demand_message = [pattern1_high_demand_message, pattern2_high_demand_message, pattern3_high_demand_message]

# low stock message:
# ==============================================================================
# only X [items] [available, left] in stock
# limited stock/quantity/quantities/availability at this price
pattern1_low_stock_message = [
    {"LOWER": "limited"},
    {"LOWER": {"IN": ["supply", "stock", "quantity", "availability"]}}
]

pattern2_low_stock_message = [
    {"LOWER": "only", "OP": "?"},
    {"POS": "NUM", "OP": "?"},
    {"POS": "NOUN", "OP": "?"},
    {"LOWER": {"IN": ["left", "available"]}},
    {"POS": "ADP", "OP": "?"},
    {"LEMMA": {"IN": ["stock"]}, "OP": "?"}
]

patterns_low_stock_message = [pattern1_low_stock_message, pattern2_low_stock_message]

# limited time message:
# ==============================================================================
# sale ends soon, hurry,
# apply/order by,
# valid/open/available for X days/hours,
# ends in X days/hours,
# limited time only'

pattern1_limited_time_message = [
    {"LOWER": {"IN": ["sale", "offer", "deal", "apply", "order"]}},
    {"LOWER": {"IN": ["ends", "by", "valid", "open", "available"]}},
    {"LOWER": "soon", "OP": "?"},
    {"LOWER": {"IN": ["by", "for", "in", "on", "at", "within"]}},
    {"POS": "PUNCT", "OP": "*"},
    {"POS": "NUM", "OP": "*"}
]

pattern2_limited_time_message = [
    {"LOWER": "limited"},
    {"LOWER": "time"},
    {"LOWER": "only", "OP": "?"}
]

pattern3_limited_time_message = [
    {"LOWER": {"IN": ["ends", "valid", "open", "available", "order"]}},
    {"LOWER": {"IN": ["by", "for", "in", "on", "at", "within"]}},
    {"POS": "PUNCT", "OP": "*"},
    {"POS": "NUM", "OP": "*"}
]

# pattern ENDS JULY 31st (TBA)
# expires soon (TBA)

patterns_limited_time_message = [pattern1_limited_time_message, pattern2_limited_time_message, pattern3_limited_time_message]

# countdown timer:
# ==============================================================================
# sale ends, deal ends
# shop now, clearance, order within
# time remaining, , sale countdown,
# number in the counter
# day/hour/min/sec

pattern1_countdown_timer = [
    {"LOWER": {"IN": ["sale", "offer", "deal", "apply", "order"]}},
    {"LOWER": {"IN": ["ends", "by", "valid", "open", "available"]}},
    {"LOWER": "soon", "OP": "?"},
    {"LOWER": {"IN": ["by", "for", "in", "on", "at", "within"]}},
    {"POS": "PUNCT", "OP": "*"},
    {"POS": "NUM", "OP": "*"}
]

pattern2_countdown_timer = [
    {"LOWER": {"IN": ["ends", "valid", "open", "available", "order"]}},
    {"LOWER": {"IN": ["by", "for", "in", "on", "at", "within"]}},
    {"POS": "PUNCT", "OP": "*"},
    {"POS": "NUM", "OP": "*"}
]

pattern3_countdown_timer = [
    {"LOWER": {"IN": ['shop', "order", "time", "sale"]}},
    {"LOWER": {"IN": ["by", "within", "remaining", "countdown"]}},
    {"POS": "PUNCT", "OP": "*"},
    {"POS": "NUM"}
]

pattern4_countdown_timer = [
    {"POS": "NUM", "OP": "*"},
    {"LOWER": {"IN": ["remaining", "left"]}}
]

# tba: only timer
# - time remaing in one ocr, counter in anther ocr
# - sale countdown in one ocr, counter in another ocr
# - days/hrs/mins/secs below or above the counter

# tba: days/hrs/mins/secs
# tba: time remaining

patterns_countdown_timer = [pattern1_countdown_timer, pattern2_countdown_timer, pattern3_countdown_timer, pattern4_countdown_timer]
