<h2 align="center"> AidUI: Toward Automated Recognition of Dark Patterns in User Interfaces </h2>

[![DOI](https://zenodo.org/badge/342777003.svg)](https://zenodo.org/badge/latestdoi/342777003) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Overview
This repository contains the replication package of our **ICSE'23** paper:
> S M Hasan Mansur, Sabiha Salma, Damilola Awofisayo, and Kevin Moran, “_**AidUI: Toward Automated Recognition of Dark Patterns in User Interfaces**_,” in Proceedings of the 45th IEEE/ACM International Conference on Software Engineering (ICSE 2023), 2023, to appear

This replication package includes three main parts which we discuss in details in later sections: 
- Part1: Our proposed unified taxonomy of UI Dark Patterns 
- Part2: Source code and setup instructions of AidUI, our developed research prototype to detect UI Dark Patterns
- Part3: Datasets for AidUI

## Part1: Unified Taxonomy of UI Dark Patterns
There has been a wealth of work from the general HCI community that has constructed Dark Pattern taxonomies. Given the somewhat complementary, yet disparate nature of existing taxonomies of Dark Patterns, we aimed to create a unified taxonomy that merges together similar categories and provides a larger landscape of patterns for mobile and web apps toward which we can design and evaluate our automated detection approach. Our unified taxonomy is primarily a fusing of the various categories and subcategories derived by Gray et al. [1], Mathur et al. [2] and Brignull et al. [3]. Our final unified taxonomy, illustrated in the following figure, spans 7 parent categories which organize a total of 27 classes that describe different Dark Patterns.

<p align="center"> <img src="docs_images/dp-taxonomy.pdf" width="500"></p>

We aimed to prioritize the detection strategy of AidUI toward certain patterns that carry with them distinct visual and textual cues which both manifest on a single screen. Thus, we identified a final set of 10 target Dark Patterns, toward which we oriented AidUI’S analysis. The targeted Dark Pattern categories are marked with a <img src="docs_images/check.png" width="18"> in the above figure. However, we provide descriptions and examples of each Dark Pattern in this [document](provide the pdf link here).

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
**NOTE**: Our provided instructions for installing AidUI are based on Ubuntu 20.04.2 LTS. Similar steps can be performed for other operating systems from UNIX family (i.e., Linux, MacOS and so on).

To setup and run AidUI, following steps need to be done.
1. #### Clone AidUI
Clone this repositry by using the ```git clone``` command. If git is not already installed, please follow the installation instructions provided [here](https://git-scm.com/downloads).

2. #### Install Anaconda
To install Anaconda, please follow the instructions at this [link](https://www.anaconda.com/).

3. #### Setup the conda environments
Installed Anaconda comes with a default conda envirionment _"base"_. We can check the available environments using the following command:
```bash
conda info --envs
```
For AidUI, two conda environments need to be setup: _**"dl_dp_obj_det_env"**_ and _**"dp_uied3"**_

We provide the specification files to build identical conda environments as ours:
- _**"dl_dp_obj_det_env"**_: [env_specification_files/dl_dp_obj_det_env.txt](env_specification_files/dl_dp_obj_det_env.txt)
- _**"dp_uied3"**_: [env_specification_files/dp_uied3.txt](env_specification_files/dp_uied3.txt)

Following commands can be used to create the required enviroinments from the root of the cloned repository:
```bash
conda create --name dl_dp_obj_det_env --file env_specification_files/dl_dp_obj_det_env.txt
```
```bash
conda create --name dp_uied3 --file env_specification_files/dp_uied3.txt
```

4. #### Download and setup Visual Cue Detection model
- Download the pretrained Visual Cue Detection model from [here](provide the zenodo link)

- Then, copy the downloaded model into the destination dir: ```AidUI/object_detection/object_detection_frcnn_mscoco_boilerplate/```

5. #### Run AidUI
- Move to the root directory of AidUI

- Execute the following command to run AidUI
```bash
./run_dp_detection.sh
```

## Part3: Datasets for AidUI
_CONTEXTDP_, the evaluation dataset for AidUI, contains 162 web and 339 mobile screenshots depicting 301 DP and 243 Non-DP instances. We make this dataset fully open source to encourage future work on automated DP detection and localization.

_CONTEXTDP_ is provided along with this repository in the directory location: ```AidUI/evaluation/evaluation_dataset/```. It is also available [here](provide zenodo link).

We also provide the dataset for training visual cue detection model. The dataset is available [here](provide zenodo link).


## References
1. C. M. Gray, Y. Kou, B. Battles, J. Hoggatt, and A. L. Toombs. The dark (patterns) side of ux design. In Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems, pages 1–14, 2018.
2. A. Mathur, G. Acar, M. J. Friedman, E. Lucherini, J. Mayer, M. Chetty, and A. Narayanan. Dark patterns at scale: Findings from a crawl of 11k shopping websites. Proceedings of the ACM on Human-Computer Interaction, 3(CSCW):1–32, 2019.
3. H. Brignull, M. Miquel, J. Rosenberg, and J. Offer. Dark patterns - user interfaces designed to trick people. 2010.




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
