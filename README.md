<!-- This is the README file for DLDarkPatterns Project -->

**Overall code structure:**
```bash
├── DLDarkPatterns
│   ├── UIED (UI area(text/non text) extraction)
|   |
│   ├── object_detetion (TBD)
|   |
│   ├── text_analysis
│   │   ├── pattern_matching
│   │   │   ├── matching (matching patterns)
│   │   │   ├── patterns (definition of patterns)
│   │   │   
│   │   ├── sentiment_analysis (SKIP)
|   │   │   ├── nlp_model
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

**sample output after text(pattern matching), visual(histogram) and spatial(proximity, size) analysis:**
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

*** sample DP Resolver output (to be modified) ***
```json
{
 'patterns_attention_distraction': 8.0,
 'patterns_default_choice': 8.0,
 'patterns_false_hierarchy': 8.0
}
```
