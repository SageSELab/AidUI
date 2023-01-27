<h2 align="center"> AidUI: Toward Automated Recognition of Dark Patterns in User Interfaces </h2>

## Overview
This repository contains the replication package of our **ICSE'23** paper:
> S M Hasan Mansur, Sabiha Salma, Damilola Awofisayo, and Kevin Moran, “_**AidUI: Toward Automated Recognition of Dark Patterns in User Interfaces**_,” in Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE 2023), 2023, to appear

This replication package includes three main parts which we discuss in details in later sections: 
- Part1: Our proposed unified taxonomy of UI Dark Patterns 
- Part2: Source code and setup instructions of AidUI, our developed research prototype to detect UI Dark Patterns
- Part3: CONTEXTDP, the evaluation dataset for AidUI

## Part1: Unified Taxonomy of UI Dark Patterns
There has been a wealth of work from the general HCI community that has constructed Dark Pattern taxonomies. Given the somewhat complementary, yet disparate nature of existing taxonomies of Dark Patterns, we aimed to create a unified taxonomy that merges together similar categories and provides a larger landscape of patterns for mobile and web apps toward which we can design and evaluate our automated detection approach. Our unified taxonomy is primarily a fusing of the various categories and subcategories derived by Gray et al. [1], Mathur et al. [2] and Brignull et al. [3]. Our final unified taxonomy, illustrated in the following figure, spans 7 parent categories which organize a total of 27 classes that describe different Dark Patterns.

<p align="center"> <img src="docs_images/test.jpg" width="300"></p>

We aimed to prioritize the detection strategy of AidUI toward certain patterns that carry with them distinct visual and textual cues which both manifest on a single screen. Thus, we identified a final set of 10 target Dark Patterns, toward which we oriented AidUI’S analysis. The targeted Dark Pattern categories are marked with a <img src="docs_images/check.png" width="18"> in the above figure. However, we provide descriptions and examples of each Dark Pattern in this [document](docs_images/dp_taxonomy.pdf).

## Part2: Source code and setup instructions of AidUI
Based on the observations gained during taxonomy study, we developed AidUI, the research prototype of our proposed automated approach to detect UI dark pattens. Following subsections present the directory structure of the source code of AidUI as well as the instructions to set it up.
### Source Code Directory structure
```bash
├── AidUI
│   ├── UIED --> module to extract UI area segments(text/non text)
|   |
│   ├── object_detetion --> DL model to detect visual cue(i.e., icons)
│   │   ├── object_detection_frcnn_mscoco_boilerplate 
|   |
│   ├── text_analysis --> module to detect lexical patterns
│   │   ├── pattern_matching
│   │   
│   ├── visual_analysis --> module to analyze brightness of neighbor UI segments
│   │   ├── histogram_analysis
|   |
│   ├── spatial_analysis --> module to analyze relative size and proximity of neighbor UI segments
│   │   ├── size_analysis
│   │   ├── proximity_analysis
|   |
│   ├── dp_resolver --> module to identify potential underlying dark patterns in UIs
```
### Setup AidUI





<!-- # AidUI (Automatically Identifying Dark Patterns in UI)
This is the repository of project AidUI.
- List of examples and patterns for different DP categories: https://docs.google.com/spreadsheets/d/1Sgu1o4aSdxa9QMJCU8yNJtVo0X7A8zRf/edit?usp=sharing&ouid=104998694462888676969&rtpof=true&sd=true
- AidUI implementation source code: https://anonymous.4open.science/r/AidUI-ICSE2023/
- Evaluation Dataset for AidUI: https://anonymous.4open.science/r/AidUI-ICSE2023/evaluation/evaluation_dataset/
- Visual Cue Detection Model Notebooks: https://anonymous.4open.science/r/AidUI-ICSE2023/object_detection/object_detection_frcnn_mscoco_boilerplate/
- Training dataset for Visual Cue Detection model: https://drive.google.com/file/d/1UIJIcZCAXeltrsyS63Wu55IcMLTJv3-X/view?usp=sharing


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
 -->
