<!-- This is the README file for DLDarkPatterns Project -->

## AidUI (Automatically Identifying Dark Patterns in UI)

**Overall code structure:**
```bash
├── DLDarkPatterns
│   ├── UIED (UI area(text/non text) extraction)
|   |
│   ├── object_detetion
│   │   ├── object_detection_frcnn_mscoco_boilerplate
│   │   ├── synthetic_data_generation
|   |
│   ├── text_analysis
│   │   ├── pattern_matching
│   │   
│   ├── visual_analysis
│   │   ├── histogram_analysis
|   |
│   ├── spatial_analysis
│   │   ├── size_analysis
│   │   ├── proximity_analysis
|   |
│   ├── dp_resolver
```

**sample Analysis Module output(text[pattern matching], visual[histogram] and spatial[proximity, size]):**
```json
{
  "9": {
    "segment_info": {
      "content": "CONTINUE",
      "column_max": 628,
      "row_max": 1290,
      "id": 9,
      "column_min": 452,
      "row_min": 1259,
      "width": 176,
      "height": 31
    },
    "text_analysis": {
      "patterns_false_hierarchy": {
        "doc": "CONTINUE",
        "span": "CONTINUE",
        "span_length": 8
      },
      "patterns_attention_distraction": {
        "doc": "CONTINUE",
        "span": "CONTINUE",
        "span_length": 8
      },
      "patterns_default_choice": {
        "doc": "CONTINUE",
        "span": "CONTINUE",
        "span_length": 8
      }
    },
    "visual_analysis": {
      "hist": [
        "0.87734836",
        "0.12265164"
      ],
      "opacity": "darker"
    },
    "proximity_analysis": {
      "neighborhood_coordinates": [
        1159,
        1390,
        352,
        728
      ],
      "neighbors": [
        "10"
      ]
    },
    "size_analysis": {
      "relative_height": {
        "9": 0.9117647058823529,
        "10": 1
      },
      "relative_width": {
        "9": 1,
        "10": 0.9147727272727273
      }
    }
  },
  "10": {
    "segment_info": {
      "content": "NOT NOW",
      "column_max": 621,
      "row_max": 1417,
      "id": 10,
      "column_min": 460,
      "row_min": 1383,
      "width": 161,
      "height": 34
    },
    "text_analysis": {
      "patterns_false_hierarchy": {
        "doc": "NOT NOW",
        "span": "NOT NOW",
        "span_length": 7
      },
      "patterns_attention_distraction": {
        "doc": "NOT NOW",
        "span": "NOT NOW",
        "span_length": 7
      },
      "patterns_default_choice": {
        "doc": "NOT NOW",
        "span": "NOT NOW",
        "span_length": 7
      }
    },
    "visual_analysis": {
      "hist": [
        "0.044517424",
        "0.9554826"
      ],
      "opacity": "brighter"
    },
    "proximity_analysis": {
      "neighborhood_coordinates": [
        1283,
        1517,
        360,
        721
      ],
      "neighbors": [
        "9"
      ]
    },
    "size_analysis": {
      "relative_height": {
        "9": 0.9117647058823529,
        "10": 1
      },
      "relative_width": {
        "9": 1,
        "10": 0.9147727272727273
      }
    }
  },
  "11": {
    "segment_info": {
      "content": "NEXT",
      "column_max": 585,
      "row_max": 1817,
      "id": 11,
      "column_min": 497,
      "row_min": 1786,
      "width": 88,
      "height": 31
    },
    "text_analysis": {
      "patterns_false_hierarchy": {
        "doc": "NEXT",
        "span": "NEXT",
        "span_length": 4
      },
      "patterns_attention_distraction": {
        "doc": "NEXT",
        "span": "NEXT",
        "span_length": 4
      },
      "patterns_default_choice": {
        "doc": "NEXT",
        "span": "NEXT",
        "span_length": 4
      }
    },
    "visual_analysis": {
      "hist": [
        "1.0",
        "0.0"
      ],
      "opacity": "darker"
    },
    "proximity_analysis": {
      "neighborhood_coordinates": [
        1686,
        1917,
        397,
        685
      ],
      "neighbors": []
    },
    "size_analysis": {
      "relative_height": {
        "11": 1
      },
      "relative_width": {
        "11": 1
      }
    }
  }
}
```

**sample Object Detection Module output**
```json
{"boxes": [74.51097869873047,
           1023.1127319335938,
           1023.6506958007812,
           1213.6737060546875],
 "labels": 4,
 "potential_dp_classes": ["nagging", "disguised_ads"],
 "scores": 0.11698809266090393}
```

**sample DP Resolver Module output**
```json
{"attention_distraction": {"score": 1.0, "votes": 4.0},
 "default_choice": {"score": 0.75, "votes": 3.0},
 "privacy_zuckering": {"score": 0.5, "votes": 3.0}}

```

**sample Evaluation(all data points) output**
```json
{
  "num_data_points": "185",
  "num_total_dp_instances": "206",
  "category_info": {
    "ACTIVITY MESSAGE": {
      "num_instances": "1",
      "conf_mat": [
        [
          184,
          0
        ],
        [
          1,
          0
        ]
      ],
      "precision": "0.0",
      "recall": "0.0"
    },
    "HIGH DEMAND MESSAGE": {
      "num_instances": "2",
      "conf_mat": [
        [
          183,
          0
        ],
        [
          1,
          1
        ]
      ],
      "precision": "1.0",
      "recall": "0.5"
    },
    "LOW STOCK MESSAGE": {
      "num_instances": "10",
      "conf_mat": [
        [
          174,
          1
        ],
        [
          3,
          7
        ]
      ],
      "precision": "0.875",
      "recall": "0.7"
    },
    "LIMITED TIME MESSAGE": {
      "num_instances": "17",
      "conf_mat": [
        [
          168,
          0
        ],
        [
          7,
          10
        ]
      ],
      "precision": "1.0",
      "recall": "0.5882352941176471"
    },
    "COUNTDOWN TIMER": {
      "num_instances": "12",
      "conf_mat": [
        [
          171,
          2
        ],
        [
          7,
          5
        ]
      ],
      "precision": "0.7142857142857143",
      "recall": "0.4166666666666667"
    },
    "ATTENTION DISTRACTION": {
      "num_instances": "10",
      "conf_mat": [
        [
          132,
          43
        ],
        [
          5,
          5
        ]
      ],
      "precision": "0.10416666666666667",
      "recall": "0.5"
    },
    "DEFAULT CHOICE": {
      "num_instances": "80",
      "conf_mat": [
        [
          83,
          22
        ],
        [
          47,
          33
        ]
      ],
      "precision": "0.6",
      "recall": "0.4125"
    },
    "FRIEND SPAM": {
      "num_instances": "2",
      "conf_mat": [
        [
          183,
          0
        ],
        [
          2,
          0
        ]
      ],
      "precision": "0.0",
      "recall": "0.0"
    },
    "DISGUISED ADS": {
      "num_instances": "11",
      "conf_mat": [
        [
          167,
          7
        ],
        [
          6,
          5
        ]
      ],
      "precision": "0.4166666666666667",
      "recall": "0.45454545454545453"
    },
    "SOCIAL PYRAMID": {
      "num_instances": "1",
      "conf_mat": [
        [
          184,
          0
        ],
        [
          0,
          1
        ]
      ],
      "precision": "1.0",
      "recall": "1.0"
    },
    "PRIVACY ZUCKERING": {
      "num_instances": "2",
      "conf_mat": [
        [
          183,
          0
        ],
        [
          2,
          0
        ]
      ],
      "precision": "0.0",
      "recall": "0.0"
    },
    "INTERMEDIATE CURRENCY": {
      "num_instances": "1",
      "conf_mat": [
        [
          184,
          0
        ],
        [
          0,
          1
        ]
      ],
      "precision": "1.0",
      "recall": "1.0"
    },
    "NAGGING": {
      "num_instances": "42",
      "conf_mat": [
        [
          126,
          17
        ],
        [
          15,
          27
        ]
      ],
      "precision": "0.6136363636363636",
      "recall": "0.6428571428571429"
    },
    "GAMIFICATION": {
      "num_instances": "12",
      "conf_mat": [
        [
          172,
          1
        ],
        [
          9,
          3
        ]
      ],
      "precision": "0.75",
      "recall": "0.25"
    },
    "ROACH MOTEL": {
      "num_instances": "1",
      "conf_mat": [
        [
          184,
          0
        ],
        [
          1,
          0
        ]
      ],
      "precision": "0.0",
      "recall": "0.0"
    },
    "FORCED CONTINUITY": {
      "num_instances": "2",
      "conf_mat": [
        [
          183,
          0
        ],
        [
          2,
          0
        ]
      ],
      "precision": "0.0",
      "recall": "0.0"
    }
  },
  "macro_avg_precision": "0.5046097132034632",
  "macro_avg_recall": "0.40405028488668193",
  "weighted_avg_precision": "0.6151415332240574",
  "weighted_avg_recall": "0.47572815533980584"
}
```
