# dark pattern classes
class_dp = {
    "activity_message": "ACTIVITY MESSAGE"
    , "high_demand_message": "HIGH DEMAND MESSAGE"
    , "low_stock_message": "LOW STOCK MESSAGE"
    , "limited_time_message": "LIMITED TIME MESSAGE"
    , "countdown_timer": "COUNTDOWN TIMER"
    , "attention_distraction": "ATTENTION DISTRACTION"
    , "default_choice": "DEFAULT CHOICE"
    , "friend_spam": "FRIEND SPAM"
    # , "forced_enrollment": "FORCED ENROLLMENT"
    , "disguised_ads": "DISGUISED ADS"
    , "social_pyramid": "SOCIAL PYRAMID"
    , "privacy_zuckering": "PRIVACY ZUCKERING"
    , "intermediate_currency": "INTERMEDIATE CURRENCY"
    , "nagging": "NAGGING"
    , "gamification": "GAMIFICATION"
    , "roach_motel": "ROACH MOTEL"
    , "forced_continuity": "FORCED CONTINUITY"
    , "no_dp": "NO DP"
}

class_dp_bin_index = {
    "ACTIVITY MESSAGE": 0
    , "HIGH DEMAND MESSAGE": 1
    , "LOW STOCK MESSAGE": 2
    , "LIMITED TIME MESSAGE": 3
    , "COUNTDOWN TIMER": 4
    , "ATTENTION DISTRACTION": 5
    , "DEFAULT CHOICE": 6
    , "FRIEND SPAM": 7
    # , "FORCED ENROLLMENT": 8
    , "DISGUISED ADS": 8
    , "SOCIAL PYRAMID": 9
    , "PRIVACY ZUCKERING": 10
    , "INTERMEDIATE CURRENCY": 11
    , "NAGGING": 12
    , "GAMIFICATION": 13
    , "ROACH MOTEL": 14
    , "FORCED CONTINUITY": 15
    , "NO DP": 16
}

class_bin_index_to_dp = {
    "0": "ACTIVITY MESSAGE"
    , "1": "HIGH DEMAND MESSAGE"
    , "2": "LOW STOCK MESSAGE"
    , "3": "LIMITED TIME MESSAGE"
    , "4": "COUNTDOWN TIMER"
    , "5": "ATTENTION DISTRACTION"
    , "6": "DEFAULT CHOICE"
    , "7": "FRIEND SPAM"
    # , "8": "FORCED ENROLLMENT"
    , "8": "DISGUISED ADS"
    , "9": "SOCIAL PYRAMID"
    , "10": "PRIVACY ZUCKERING"
    , "11": "INTERMEDIATE CURRENCY"
    , "12": "NAGGING"
    , "13": "GAMIFICATION"
    , "14": "ROACH MOTEL"
    , "15": "FORCED CONTINUITY"
    , "16": "NO DP"
}

class_bin_index_to_dp_acronym = {
    "0": "AM"
    , "1": "HDM"
    , "2": "LSM"
    , "3": "LTM"
    , "4": "CT"
    , "5": "AD"
    , "6": "DC"
    , "7": "FS"
    # , "8": "FORCED ENROLLMENT"
    , "8": "DA"
    , "9": "SP"
    , "10": "PZ"
    , "11": "IC"
    , "12": "NAG"
    , "13": "GAM"
    , "14": "RM"
    , "15": "FC"
    , "16": "NO DP"
}

classes_excluded_in_report = ["FRIEND SPAM", "SOCIAL PYRAMID", "PRIVACY ZUCKERING", "INTERMEDIATE CURRENCY", "ROACH MOTEL", "FORCED CONTINUITY"]
classes_acronyms_excluded_in_report = ["FS", "SP", "PZ", "IC", "RM", "FC"]
