This is the README file for DLDarkPatterns Project

Overall code structure:
```bash
├── DLDarkPatterns
│   ├── UIED (UI area(text/non text) extraction)
|   |
│   ├── text_analysis
│   │   ├── pattern_matching
│   │   │   ├── matching (matching patterns)
│   │   │   ├── patterns (definition of patterns)
│   │   │   
│   │   ├── sentiment_analysis (TBD)
|   │   │   ├── nlp_model
│   │   
│   ├── visual_analysis (TBD)
│   │   ├── histogram_analysis
│   │   ├── object_detetion
|   |
│   ├── spatial_analysis (TBD)
│   │   ├── size_analysis
│   │   ├── proximity_analysis
```

sample output after text(pattern matching), visual(histogram) and spatial(proximity, size) analysis:
```json
{
  "9": {
    "segment_info": {
      "height": 31,
      "width": 176,
      "column_max": 628,
      "content": "CONTINUE",
      "column_min": 452,
      "id": 9,
      "row_max": 1290,
      "row_min": 1259
    },
    "text_analysis": {
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
      "height": 34,
      "width": 161,
      "column_max": 621,
      "content": "NOT NOW",
      "column_min": 460,
      "id": 10,
      "row_max": 1417,
      "row_min": 1383
    },
    "text_analysis": {
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
      "height": 31,
      "width": 88,
      "column_max": 585,
      "content": "NEXT",
      "column_min": 497,
      "id": 11,
      "row_max": 1817,
      "row_min": 1786
    },
    "text_analysis": {
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

