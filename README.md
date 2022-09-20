
## AidUI (Automatically Identifying Dark Patterns in UI)
This is the repository of project AidUI.
- List of examples and patterns for different DP categories: https://docs.google.com/spreadsheets/d/15PAtmx9d7Us9sj4vFq1_r_pQM8KDxhWUYWT3q6-RE-o/edit#gid=2050474263
- AidUI implementation source code: https://anonymous.4open.science/r/AidUI-ICSE2023/
- Evaluation Dataset for AidUI: https://anonymous.4open.science/r/AidUI-ICSE2023/evaluation/evaluation_dataset/
- Visual Cue Detection Model Notebooks: https://anonymous.4open.science/r/AidUI-ICSE2023/object_detection/object_detection_frcnn_mscoco_boilerplate/
- Training dataset for Visual Cue Detection model: https://www.dropbox.com/sh/4yrph99b4wwcbgg/AAAinL6O_8itZAhrtby4zEwMa?dl=0


**Directory structure of AidUI major components:**
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
