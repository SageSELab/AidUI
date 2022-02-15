# activity message:
# ==============================================================================
# X people/person/visitors/users ordered/purchased/subscribed/viewed/booked in last 24 hours'
# 8 people ordered in last 24 hours
# 8 people are looking right now
# people booked 78 times in last 24 hours
# jack just saved 52$ on his order
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

# false hierarchy
# ==============================================================================
# - keywords (bigger size): start, turn, add, yes,next, sign in/up, ok, continue, unlock, subscribe, confirm,setup etc.
# - keywords (smaller size):  no, not now, later, cancel, skip, exit etc.

pattern1_false_hierarchy = [
    {"LOWER": {"IN": ["start", "turn", "add", "yes", "next", "sign", "ok", "continue", "unlock", "subscribe", "confirm", "setup"]}},
    {"LOWER": {"IN": ["on", "in", "up", "off"]}, "OP": "*"}
]

pattern2_false_hierarchy = [
    {"LOWER": {"IN": ["no", "not", "later", "cancel", "skip", "exit"]}},
    {"LOWER": {"IN": ["now", "thanks", "up", "later", "anytime"]}, "OP": "*"}
]

patterns_false_hierarchy = [pattern1_false_hierarchy, pattern2_false_hierarchy]


# attention distraction
# ==============================================================================
# - keywords (bigger size): start, turn, add, yes,next, sign in/up, ok, continue, unlock, subscribe, confirm,setup etc.
# - keywords (smaller size):  no, not now, later, cancel, skip, exit etc.
# - I decline/don't want/opt out/refuse...to...

pattern1_attention_distraction = [
    {"LOWER": {"IN": ["start", "turn", "add", "yes", "next", "sign", "ok", "continue", "unlock", "subscribe", "confirm", "setup"]}},
    {"LOWER": {"IN": ["on", "in", "up", "off"]}, "OP": "*"}
]

pattern2_attention_distraction = [
    {"LOWER": {"IN": ["no", "not", "later", "cancel", "skip", "exit"]}},
    {"LOWER": {"IN": ["now", "thanks", "up", "later", "anytime"]}, "OP": "*"}
]

pattern3_attention_distraction = [
    {"LOWER": {"IN": ["decline", "refuse", "don't", "opt"]}},
    {"LOWER": {"IN": ["want", "out"]}, "OP": "?"}
]

patterns_attention_distraction = [pattern1_attention_distraction, pattern2_attention_distraction, pattern3_attention_distraction]

# default choice
# ==============================================================================
# - keywords (bigger size): start, turn, add, yes,next, sign in/up, ok, continue, unlock, subscribe, confirm,setup etc.
# - keywords (smaller size):  no, not now, later, cancel, skip, exit etc.

#  notify/notification

# I agree/consent to ...', 'I give permission to ...'
# by giving us permission/consent ...'
# by clicking/pressing .....agree/consent to ....'
# by subscribing ....agree/consent to ....

pattern1_default_choice = [
    {"LOWER": {"IN": ["start", "turn", "add", "yes", "next", "sign", "ok", "continue", "unlock", "subscribe", "confirm", "setup"]}},
    {"LOWER": {"IN": ["on", "in", "up", "off"]}, "OP": "*"}
]

pattern2_default_choice = [
    {"LOWER": {"IN": ["no", "not", "later", "cancel", "skip", "exit"]}},
    {"LOWER": {"IN": ["now", "thanks", "up", "later", "anytime"]}, "OP": "*"}
]

pattern3_default_choice = [
    {"LOWER": {"IN": ["notify", "notification"]}}
]

pattern4_default_choice = [
    {"LOWER": {"IN": ["agree", "consent"]}},
    {"LOWER": {"IN": ["permission", "consent"]}, "OP": "?"}
]

pattern5_default_choice = [
    {"LEMMA": {"IN": ["give"]}},
    {"IS_ALPHA": True, "OP": "*"},
    {"LEMMA": {"IN": ["permission", "consent"]}}
]

pattern6_default_choice = [
    {"LEMMA": {"IN": ["click", "press", "subscribe", "use"]}},
    {"IS_ALPHA": True, "OP": "*"},
    {"LEMMA": {"IN": ["agree", "consent", "give"]}},
    {"IS_ALPHA": True, "OP": "*"},
    {"LEMMA": {"IN": ["permission", "consent"]}, "OP": "?"}
]

patterns_default_choice = [
    pattern1_default_choice, pattern2_default_choice, pattern3_default_choice,
    pattern4_default_choice, pattern5_default_choice, pattern6_default_choice
]

# friend spam
# ==============================================================================
# upload/sync/share....contacts....',
# invite/add friends...

pattern1_friend_spam = [
    {"LOWER": {"IN": ["upload", "sync", "share", "add", "invite"]}},
    {"LOWER": {"IN": ["friends", "contacts"]}}
]

patterns_friend_spam = [pattern1_friend_spam]

# forced enrollment
# ==============================================================================
# want/like to join/subscribe to ... and ..... terms and conditions ... [usually appears inline]

pattern1_forced_enrollment = [
    {"LOWER": {"IN": ["want", "like", "would"]}},
    {"IS_ALPHA": True, "OP": "*"},
    {"LOWER": {"IN": ["join", "subscribe"]}}
]

pattern2_forced_enrollment = [
    {"LOWER": {"IN": ["terms"]}},
    {"IS_ALPHA": True, "OP": "*"},
    {"LOWER": {"IN": ["conditions"]}}
]

patterns_forced_enrollment = [pattern1_forced_enrollment, pattern2_forced_enrollment]

# disguised ads
# ==============================================================================
# AdChoices, Install now, Download now

pattern1_disguised_ads = [
    {"LOWER": {"IN": ["ad", "adchoices"]}},
]

pattern2_disguised_ads = [
    {"LOWER": {"IN": ["install", "download"]}},
    {"LOWER": {"IN": ["now"]}},
]

patterns_disguised_ads = [pattern1_disguised_ads, pattern2_disguised_ads]

# # social pyramid
# # ==============================================================================
# ask/invite/refer/signup
# contacts/friends...to...'
# 'unlock/earn/get/collect .... credits/rewards/points/tokens ....for....signup....

pattern1_social_pyramid = [
    {"LOWER": {"IN": ["ask", "invite", "refer", "add", "sign"]}},
    {"IS_ALPHA": True, "OP": "*"},
    {"LOWER": {"IN": ["friends", "contacts", "neighbors"]}},
    {"IS_ALPHA": True, "OP": "*"},
    {"LOWER": {"IN": ["unlock", "earn", "get", "collect", "gain"]}},
    {"IS_ALPHA": True, "OP": "*"},
    {"LOWER": {"IN": ["credits", "rewards", "points", "tokens"]}, "OP": "*"}
]

pattern2_social_pyramid = [
    {"LOWER": {"IN": ["unlock", "earn", "get", "collect", "gain"]}},
    {"IS_ALPHA": True, "OP": "*"},
    {"LOWER": {"IN": ["credits", "rewards", "points", "tokens"]}}
]

patterns_social_pyramid = [pattern1_social_pyramid, pattern2_social_pyramid]

# privacy zuckering
# ==============================================================================
# upload/sync/share/invite/add....friends/contacts/location....'

pattern1_privacy_zuckering = [
    {"LOWER": {"IN": ["upload", "sync", "share", "add", "invite"]}, "OP": "?"},
    {"LOWER": {"IN": ["friends", "contacts", "location"]}, "OP": "?"}
]

patterns_privacy_zuckering = [pattern1_privacy_zuckering]

# intermediate currency
# ==============================================================================
# Buy/get/collect x credits/Badge/reward/token/points/stars'

pattern1_intermediate_currency = [
    {"LOWER": {"IN": ["buy", "get", "collect", "earn", "gain", "unlock"]}},
    {"IS_ALPHA": True, "OP": "*"},
    {"LEMMA": {"IN": ["credit", "reward", "point", "token", "badge", "star"]}}
]

patterns_intermediate_currency = [pattern1_intermediate_currency]

# price comparison prevention
# ==============================================================================
# 'per kg', '/kg', '/ea', 'for each'

pattern1_price_comparison_prevention = [
    {},
    {"LOWER": {"IN": ["unit", "kg", "each", "ea", "lb", "pound", "kilogram"]}}
]

patterns_price_comparison_prevention = [pattern1_price_comparison_prevention]
