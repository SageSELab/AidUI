############################ nagging ###########################################
# ==============================================================================
# keywords: Rate, Rating, Star, Like, Upvote etc.

pattern1_nagging = [
    # {"LEMMA": {"IN": ["rate", "like", "upvote"]}},
    {"LEMMA": {"IN": ["rate", "upvote"]}},
    {"LOWER": {"IN": ["this"]}, "OP": "?"},
    # {"LOWER": {"IN": ["us", "app", "it", "now", "image", "picture", "video", "feature"]}},
    {"LOWER": {"IN": ["us", "app", "now", "image", "picture", "video", "feature"]}},
    {"LOWER": {"IN": ["now"]}, "OP": "?"}
]

pattern2_nagging = [
    {"LOWER": {"IN": ["ad", "adchoices"]}}
]

pattern3_nagging = [
    # {"LOWER": {"IN": ["install", "download"]}},
    {"LOWER": {"IN": ["install"]}},
    {"LOWER": {"IN": ["now"]}, "OP": "?"}
]

pattern4_nagging = [
    {"LOWER": {"IN": ["watch"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["ad", "session"]}},
    {"LOWER": {"IN": ["to"]}},
    {"LOWER": {"IN": ["unlock", "earn", "get", "collect", "gain", "access"]}, "OP": "?"}
]

pattern5_nagging = [
    {"LOWER": {"IN": ["unlock", "earn", "get", "collect", "gain", "access"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["by"]}},
    {"LEMMA": {"IN": ["watch"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["ad", "session"]}}
]

pattern6_nagging = [
    {"LEMMA": {"IN": ["give"]}},
    {"LOWER": {"IN": ["this"]}, "OP": "?"},
    {"LOWER": {"IN": ["us", "app", "it"]}},
    {"LOWER": {"IN": ["five", "5"]}, "OP": "?"},
    {"LEMMA": {"IN": ["star"]}},
    {"LOWER": {"IN": ["rate", "review"]}}
]

pattern7_nagging = [
    {"LEMMA": {"IN": ["star"]}},
    {"LEMMA": {"IN": ["rate", "review"]}}
]

pattern8_nagging = [
    {"POS": "ADJ", "OP": "?"},
    {"LOWER": {"IN": ["sponsored"]}},
    {"LOWER": {"IN": ["session"]}}
]

pattern9_nagging = [
    {"LOWER": {"IN": ["do"]}},
    {"LOWER": {"IN": ["you"]}},
    {"LOWER": {"IN": ["like", "love"]}}
]

patterns_nagging = [pattern1_nagging, pattern2_nagging, pattern3_nagging
, pattern4_nagging, pattern5_nagging, pattern6_nagging, pattern7_nagging
, pattern8_nagging, pattern9_nagging]

############################# bait and switch ##################################
# ==============================================================================
# keywords: free trial, auto renew, subscription, cancel anytime, skip (smaller text)
# button text: start/continue etc. (bigger text)
# keywords: AdChoices, Install

pattern1_bait_and_switch = [
    {"LOWER": {"IN": ["free", "auto", "cancel"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["trial", "renew", "anytime"]}}
]

pattern2_bait_and_switch = [
    {"LOWER": {"IN": ["start", "turn", "add", "yes", "next", "sign", "ok", "continue", "unlock", "subscribe", "confirm", "setup"]}},
    {"LOWER": {"IN": ["on", "in", "up", "off"]}, "OP": "*"}
]

pattern3_bait_and_switch = [
    {"LOWER": {"IN": ["ad", "adchoices"]}},
]

pattern4_bait_and_switch = [
    {"LOWER": {"IN": ["install", "download"]}},
    {"LOWER": {"IN": ["now"]}, "OP": "?"}
]

patterns_bait_and_switch = [pattern1_bait_and_switch, pattern2_bait_and_switch, pattern3_bait_and_switch, pattern4_bait_and_switch]

############################# forced continuity ################################
# ==============================================================================
# - keyword/sentence pattern: 'automatically renew/renewal', 'subscription', 'cancel anytime', 'by calling'
# - 'call us', 'call', 'phone', 'by phone only', 'contact agent', 'to unsubscribe', 'to discontinue' etc.

pattern1_forced_continuity = [
    {"LOWER": {"IN": ["cancel", "unsubscribe", "discontinue"]}, "OP": "?"},
    # {"LEMMA": {"IN": ["cancel", "unsubscribe", "discontinue"]}, "OP": "?"},
    {"LOWER": {"IN": ["anytime"]}, "OP": "?"},
    {"LOWER": {"IN": ["by"]}},
    {"LEMMA": {"IN": ["call", "give", "phone", "contact"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["call", "only"]}, "OP": "?"}
]

pattern2_forced_continuity = [
    {"LOWER": {"IN": ["call", "give", "contact"]}},
    {"LOWER": {"IN": ["us", "agent"]}, "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["to"]}},
    {"LOWER": {"IN": ["cancel", "unsubscribe", "discontinue"]}}
]

pattern3_forced_continuity = [
    {"LEMMA": {"IN": ["cancel", "unsubscribe", "discontinue"]}},
    {"IS_ALPHA": True, "OP": "*"},
    {"LOWER": {"IN": ["by"]}},
    {"LEMMA": {"IN": ["call", "give", "phone", "contact"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["call", "only"]}, "OP": "?"}
]

patterns_forced_continuity = [pattern1_forced_continuity, pattern2_forced_continuity]

############################# roach motel ######################################
# ==============================================================================
# - keywords: free trial, auto renew, subscription, cancel anytime, skip (smaller text)
# - button text: start/continue etc. (bigger text)
# - I decline/don't want/opt out/refuse...to...

pattern1_roach_motel = [
    {"LOWER": {"IN": ["free", "auto", "cancel"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["trial", "renew", "anytime"]}}
]

# pattern2_roach_motel = [
#     {"LOWER": {"IN": ["start", "turn", "add", "yes", "next", "sign", "ok", "continue", "unlock", "subscribe", "confirm", "setup"]}},
#     {"LOWER": {"IN": ["on", "in", "up", "off"]}, "OP": "*"}
# ]

pattern3_roach_motel = [
    {"LOWER": {"IN": ["decline", "refuse", "don't", "opt"]}},
    {"LOWER": {"IN": ["want", "out"]}, "OP": "?"},
    {"LOWER": {"IN": ["to"]}}
]

patterns_roach_motel = [pattern1_roach_motel, pattern3_roach_motel]

############################# price comparison prevention ######################
# ==============================================================================
# 'per kg', '/kg', '/ea', 'for each'

pattern1_price_comparison_prevention = [
    {},
    {"LOWER": {"IN": ["unit", "kg", "each", "ea", "lb", "pound", "kilogram"]}}
]

patterns_price_comparison_prevention = [pattern1_price_comparison_prevention]

############################# intermediate currency ############################
# ==============================================================================
# Buy/get/collect x credits/Badge/reward/token/points/stars'

pattern1_intermediate_currency = [
    # {"LOWER": {"IN": ["buy", "get", "collect", "earn", "gain", "unlock"]}},
    {"LOWER": {"IN": ["buy", "get", "collect"]}},
    {"POS": "NUM"},
    {"IS_ALPHA": True, "OP": "?"},
    # {"LEMMA": {"IN": ["credit", "reward", "point", "token", "badge", "star"]}}
    {"LEMMA": {"IN": ["credit", "badge", "star"]}}
]

patterns_intermediate_currency = [pattern1_intermediate_currency]

############################# privacy zuckering ################################
# ==============================================================================
# upload/sync/share/invite/add....friends/contacts/location....'

pattern1_privacy_zuckering = [
    {"LOWER": {"IN": ["upload", "sync", "share", "add", "invite"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["friends", "contacts", "location"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["to"]}, "OP": "?"}
]

# pattern2_privacy_zuckering = [
#     {"LOWER": {"IN": ["no", "not", "later", "cancel", "skip"]}},
#     {"LOWER": {"IN": ["now", "thanks"]}, "OP": "*"}
# ]

patterns_privacy_zuckering = [pattern1_privacy_zuckering]

############################ social pyramid ####################################
# ==============================================================================
# ask/invite/refer/signup
# contacts/friends...to...'
# 'unlock/earn/get/collect .... credits/rewards/points/tokens ....for....signup....

pattern1_social_pyramid = [
    {"LOWER": {"IN": ["ask", "invite", "refer", "add", "signup"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["friends", "contacts", "neighbors"]}},
    {"LOWER": {"IN": ["to"]}, "OP": "?"},
    {"LOWER": {"IN": ["unlock", "earn", "get", "collect", "gain"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["credits", "rewards", "points", "tokens"]}, "OP": "?"}
]

pattern2_social_pyramid = [
    {"LOWER": {"IN": ["unlock", "earn", "get", "collect", "gain"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["credits", "rewards", "points", "tokens"]}},
    {"LOWER": {"IN": ["by"]}, "OP": "?"},
    {"LEMMA": {"IN": ["ask", "invite", "refer", "add", "sign"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["friends", "contacts", "neighbors"]}}
]

patterns_social_pyramid = [pattern1_social_pyramid, pattern2_social_pyramid]

############################ gamification ######################################
# ==============================================================================
# ask/invite/refer/signup
# contacts/friends...to...'
# 'unlock/earn/get/collect .... credits/rewards/points/tokens ....for....signup....

pattern1_gamification = [
    {"LOWER": {"IN": ["ask", "invite", "refer", "add", "signup"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["friends", "contacts", "neighbors"]}},
    {"LOWER": {"IN": ["to"]}, "OP": "?"},
    {"LOWER": {"IN": ["unlock", "earn", "get", "collect", "gain", "access"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["credits", "rewards", "points", "tokens"]}, "OP": "?"}
]

pattern2_gamification = [
    {"LOWER": {"IN": ["unlock", "earn", "get", "collect", "gain", "access"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["credits", "rewards", "points", "tokens"]}},
    {"LOWER": {"IN": ["by", "for"]}, "OP": "?"},
    {"LEMMA": {"IN": ["ask", "invite", "refer", "add", "signup"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["friends", "contacts", "neighbors"]}}
]

pattern3_gamification = [
    {"LOWER": {"IN": ["watch"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["ad", "session"]}},
    {"LOWER": {"IN": ["to"]}},
    {"LOWER": {"IN": ["unlock", "earn", "get", "collect", "gain", "access"]}, "OP": "?"}
]

pattern4_gamification = [
    {"LOWER": {"IN": ["unlock", "earn", "get", "collect", "gain", "access"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["by", "for"]}},
    {"LEMMA": {"IN": ["watch"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["ad", "session"]}}
]

pattern5_gamification = [
    {"POS": "ADJ", "OP": "?"},
    {"LOWER": {"IN": ["sponsored"]}},
    {"LOWER": {"IN": ["session"]}}
]

pattern6_gamification = [
    {"LOWER": {"IN": ["unlock", "earn", "get", "collect", "gain", "access"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["credits", "rewards", "points", "tokens"]}},
    {"LOWER": {"IN": ["by", "for"]}}
]

patterns_gamification = [pattern1_gamification, pattern2_gamification
, pattern3_gamification, pattern4_gamification, pattern5_gamification, pattern6_gamification]

############################# forced enrollment ################################
# ==============================================================================
# want/like to join/subscribe to ... and ..... terms and conditions ... [usually appears inline]

pattern1_forced_enrollment = [
    {"LOWER": {"IN": ["want", "like", "would"]}},
    {"LOWER": {"IN": ["like"]}, "OP": "?"},
    {"LOWER": {"IN": ["to"]}, "OP": "?"},
    {"LOWER": {"IN": ["join", "subscribe"]}},
    {"IS_ALPHA": True, "OP": "*"},
    {"LOWER": {"IN": ["terms", "policies"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["conditions", "policies"]}}
]

pattern2_forced_enrollment = [
    {"LOWER": {"IN": ["terms", "policies"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["conditions", "policies"]}}
]

patterns_forced_enrollment = [pattern1_forced_enrollment, pattern2_forced_enrollment]

############################# default choice ###################################
# ==============================================================================
# - keywords (bigger size): start, turn, add, yes,next, sign in/up, ok, continue, unlock, subscribe, confirm,setup etc.
# - keywords (smaller size):  no, not now, later, cancel, skip, exit etc.

#  notify/notification

# I agree/consent to ...', 'I give permission to ...'
# by giving us permission/consent ...'
# by clicking/pressing .....agree/consent to ....'
# by subscribing ....agree/consent to ....

pattern1_default_choice = [
    {"LOWER": {"IN": ["start", "turn", "yes", "next", "sign", "ok", "continue", "unlock", "confirm", "setup", "set"]}},
    {"LOWER": {"IN": ["on", "in", "up", "off"]}, "OP": "?"}
]

pattern2_default_choice = [
    {"LOWER": {"IN": ["no", "later", "cancel", "skip", "exit"]}},
    {"LOWER": {"IN": ["now", "thanks", "up", "later", "anytime"]}, "OP": "?"}
]

pattern3_default_choice = [
    # {"LOWER": {"IN": ["notify", "notification", "notifications"]}}
    {"LOWER": {"IN": ["notification", "notifications"]}}
]

# pattern4_default_choice = [
#     {"LEMMA": {"IN": ["click", "press", "subscribe", "use"]}, "OP": "?"},
#     {"IS_ALPHA": True, "OP": "*"},
#     {"LEMMA": {"IN": ["agree", "consent", "give"]}},
#     {"IS_ALPHA": True, "OP": "?"},
#     {"LOWER": {"IN": ["permission", "consent"]}, "OP": "?"},
#     {"LOWER": {"IN": ["to"]}, "OP": "?"}
# ]

patterns_default_choice = [
    pattern1_default_choice, pattern2_default_choice,
    pattern3_default_choice
]

############################# attention distraction ############################
# ==============================================================================
# - keywords (bigger size): start, turn, add, yes,next, sign in/up, ok, continue, unlock, subscribe, confirm,setup etc.
# - keywords (smaller size):  no, not now, later, cancel, skip, exit etc.
# - I decline/don't want/opt out/refuse...to...

# pattern1_attention_distraction = [
#     {"LOWER": {"IN": ["start", "turn", "add", "yes", "next", "sign", "ok", "continue", "unlock", "subscribe", "confirm", "setup"]}},
#     {"LOWER": {"IN": ["on", "in", "up", "off"]}, "OP": "?"}
# ]
#
# pattern2_attention_distraction = [
#     {"LOWER": {"IN": ["no", "not", "later", "cancel", "skip", "exit"]}},
#     {"LOWER": {"IN": ["now", "thanks", "up", "later", "anytime"]}, "OP": "?"}
# ]
#
# pattern3_attention_distraction = [
#     {"LOWER": {"IN": ["decline", "refuse", "don't", "opt"]}},
#     {"LOWER": {"IN": ["want", "out"]}, "OP": "?"},
#     {"LOWER": {"IN": ["to"]}}
# ]

# patterns_attention_distraction = [pattern1_attention_distraction, pattern2_attention_distraction, pattern3_attention_distraction]

pattern1_attention_distraction = [
    {"LOWER": {"IN": ["yes", "no", "maybe", "may"]}},
    {"POS": "PUNCT", "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["agree", "thank", "thanks", "later"]}}
]

patterns_attention_distraction = [pattern1_attention_distraction]

############################# disguised ads ####################################
# ==============================================================================
# AdChoices, ad

pattern1_disguised_ads = [
    {"LOWER": {"IN": ["ad", "adchoices"]}},
]

patterns_disguised_ads = [pattern1_disguised_ads]

############################# friend spam ######################################
# ==============================================================================
# upload/sync/share....contacts....',
# invite/add friends...

pattern1_friend_spam = [
    {"LOWER": {"IN": ["upload", "sync", "share", "add", "invite"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["friends", "contacts"]}},
    {"IS_ALPHA": True, "OP": "?"},
    {"LOWER": {"IN": ["to"]}}
]

patterns_friend_spam = [pattern1_friend_spam]

############################# false hierarchy ##################################
# ==============================================================================
# - keywords (bigger size): start, turn, add, yes,next, sign in/up, ok, continue, unlock, subscribe, confirm,setup etc.
# - keywords (smaller size):  no, not now, later, cancel, skip, exit etc.

pattern1_false_hierarchy = [
    {"LOWER": {"IN": ["start", "turn", "add", "yes", "next", "sign", "ok", "continue", "unlock", "subscribe", "confirm", "setup"]}},
    {"LOWER": {"IN": ["on", "in", "up", "off"]}, "OP": "?"}
]

pattern2_false_hierarchy = [
    {"LOWER": {"IN": ["no", "not", "later", "cancel", "skip", "exit"]}},
    {"LOWER": {"IN": ["now", "thanks", "up", "later", "anytime"]}, "OP": "?"}
]

patterns_false_hierarchy = [pattern1_false_hierarchy, pattern2_false_hierarchy]

############################# countdown timer ##################################
# ==============================================================================
# sale ends, deal ends
# shop now, clearance, order within
# time remaining, , sale countdown,
# number in the counter
# day/hour/min/sec

# pattern1_countdown_timer = [
#     {"LOWER": {"IN": ["sale", "offer", "deal", "apply", "order"]}},
#     {"LOWER": {"IN": ["ends", "by", "valid", "open", "available"]}},
#     {"LOWER": "soon", "OP": "?"},
#     {"LOWER": {"IN": ["by", "for", "in", "on", "at", "within"]}},
#     {"POS": "PUNCT", "OP": "*"},
#     {"POS": "NUM", "OP": "*"}
# ]

# pattern2_countdown_timer = [
#     {"LOWER": {"IN": ["ends", "valid", "open", "available", "order"]}},
#     {"LOWER": {"IN": ["by", "for", "in", "on", "at", "within"]}},
#     {"POS": "PUNCT", "OP": "*"},
#     {"POS": "NUM", "OP": "*"}
# ]

# pattern3_countdown_timer = [
#     {"LOWER": {"IN": ['shop', "order", "time", "sale"]}},
#     {"LOWER": {"IN": ["by", "within", "remaining", "countdown"]}},
#     {"POS": "PUNCT", "OP": "*"},
#     {"POS": "NUM", "OP": "*"}
# ]

# pattern4_countdown_timer = [
#     {"POS": "NUM"},
#     {"LOWER": {"IN": ["remaining", "left"]}}
# ]

pattern5_countdown_timer = [
    {"POS": "NUM"},
    {"LOWER": {"IN": [":"]}},
    {"POS": "NUM"},
    {"LOWER": {"IN": [":"]}},
    {"POS": "NUM"},
    {"LOWER": {"IN": [":"]}, "OP": "?"},
    {"POS": "NUM", "OP": "?"}
]

pattern6_countdown_timer = [
    {"LOWER": {"IN": ["hrs", "mins", "secs"]}}
]

pattern7_countdown_timer = [{"TEXT": {"REGEX": "[0-9]{2}:[0-9]{2}:[0-9]{2}"}}]

pattern8_countdown_timer = [
    {"POS": "NUM", "OP": "?"},
    {"LOWER": {"IN": ["hrs", "mins", "secs", "hours", "minutes", "seconds", "hr", "min", "sec"]}},
    {"LOWER": {"IN": [":"]}, "OP": "?"},
    {"POS": "NUM", "OP": "?"},
    {"LOWER": {"IN": ["hrs", "mins", "secs", "hours", "minutes", "seconds", "hr", "min", "sec"]}},
    {"LOWER": {"IN": [":"]}, "OP": "?"},
    {"POS": "NUM", "OP": "?"},
    {"LOWER": {"IN": ["hrs", "mins", "secs", "hours", "minutes", "seconds", "hr", "min", "sec"]}}
]


# tba: only timer
# - time remaing in one ocr, counter in anther ocr
# - sale countdown in one ocr, counter in another ocr
# - days/hrs/mins/secs below or above the counter

# tba: days/hrs/mins/secs
# tba: time remaining

patterns_countdown_timer = [pattern5_countdown_timer, pattern6_countdown_timer, pattern7_countdown_timer, pattern8_countdown_timer]

############################# limited time message #############################
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
    # {"POS": "PUNCT", "OP": "*"},
    # {"POS": "NUM", "OP": "*"}
    {"POS": "NUM"}
]

# pattern ENDS JULY 31st (TBA)
# expires soon (TBA)

patterns_limited_time_message = [pattern1_limited_time_message, pattern2_limited_time_message, pattern3_limited_time_message]

############################# low stock message ################################
# ==============================================================================
# only X [items] [available, left] in stock
# limited stock/quantity/quantities/availability at this price
pattern1_low_stock_message = [
    {"LOWER": {"IN": ["limited", "low"]}},
    {"LOWER": {"IN": ["supply", "stock", "quantity", "availability"]}}
]

pattern2_low_stock_message = [
    {"LOWER": "only", "OP": "?"},
    {"POS": "NUM"},
    {"POS": "NOUN", "OP": "?"},
    {"LOWER": {"IN": ["left", "available"]}},
    {"POS": "ADP", "OP": "?"},
    {"LEMMA": {"IN": ["stock"]}, "OP": "?"}
]

pattern3_low_stock_message = [
    {"LOWER": {"IN": ["left", "available"]}},
    {"POS": "ADP", "OP": "?"},
    {"LEMMA": {"IN": ["stock"]}}
]

patterns_low_stock_message = [pattern1_low_stock_message, pattern2_low_stock_message, pattern3_low_stock_message]

############################# high demand message ##############################
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
    {"LEMMA": {"IN": ["sell", "finish"]}},
    {"LOWER": {"IN": ["fast", "quick"]}}
]

patterns_high_demand_message = [pattern1_high_demand_message, pattern2_high_demand_message, pattern3_high_demand_message]

############################# activity message #################################
# ==============================================================================
# X people/person/visitors/users ordered/purchased/subscribed/viewed/booked in last 24 hours'
# 8 people ordered in last 24 hours
# 8 people are looking right now
# people booked 78 times in last 24 hours
# jack just saved 52$ on his order
# X items sold in Y time/this hour

# pattern_generic_activity_message = [
#     {"POS": "NUM", "OP": "?"},
#     {"POS": {"IN": ["NOUN", "PROPN"]}},
#     {"POS": "AUX", "OP": "?"},
#     {"POS": "ADV", "OP": "?"},
#     {"POS": "VERB"},
#     {"POS": "NUM", "OP": "?"},
#     {"POS": "NOUN", "OP": "?"},
#     {"POS": "ADP", "OP": "?"},
#     {"POS": "DET", "OP": "?"},
#     {"POS": "ADJ", "OP": "?"},
#     {"POS": "ADV", "OP": "?"},
#     {"POS": "ADV", "OP": "?"},
#     {"POS": "NUM", "OP": "?"},
#     {"POS": "NOUN", "OP": "?"},
# ]

# pattern1_activity_message = [
#     {"POS": "NUM", "OP": "?"},
#     {"POS": {"IN": ["NOUN", "PROPN"]}},
#     {"POS": "AUX", "OP": "?"},
#     {"POS": "ADV", "OP": "?"},
#     {"LEMMA": {"IN": ["order", "purchase", "subscribe", "view", "book", "visit", "sell", "save", "look"]}},
#     {"POS": "ADP", "OP": "?"},
#     {"POS": "ADJ", "OP": "?"},
#     {"POS": "NUM", "OP": "?"}
# ]

pattern2_activity_message = [
    {"POS": "NUM"},
    # {"POS": {"IN": ["NOUN", "PROPN"]}, "OP": "?"},
    {"LOWER": {"IN": ["items"]}, "OP": "?"},
    {"POS": "AUX", "OP": "?"},
    {"POS": "ADV", "OP": "?"},
    {"LEMMA": {"IN": ["order", "purchase", "subscribe", "view", "book", "visit", "sell", "save", "look"]}},
    {"LOWER": {"IN": ["by", "in"]}}
]

pattern3_activity_message = [
    {"POS": "NUM", "OP": "?"},
    {"LEMMA": {"IN": ["people", "person", "visitor", "user"]}},
    {"POS": "AUX", "OP": "?"},
    {"POS": "ADV", "OP": "?"},
    {"LEMMA": {"IN": ["order", "purchase", "subscribe", "view", "book", "visit", "sell", "save", "look"]}},
    {"POS": "ADP", "OP": "?"},
    {"POS": "ADJ", "OP": "?"},
    {"POS": "NUM", "OP": "?"}
]

patterns_activity_message = [pattern2_activity_message, pattern3_activity_message]
