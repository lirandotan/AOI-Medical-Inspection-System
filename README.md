# Automated Optical Inspection (AOI) System for Medical Components

## Overview
This repository contains the software and hardware control logic for a Final B.Sc. Engineering Project developed at Philips Medical. The project replaces a manual microscope inspection process with a fully automated, Machine Vision-based system. 

The system is designed to detect micro-chipping defects in the Photodiode Array (PDA) layer of CT scanner Tile components. By utilizing a motorized 3D-printed Jig, a controlled optical environment (Darkroom + Ring Light), and classical computer vision algorithms, the system provides consistent, objective, and rapid quality control.

## Hardware Architecture
The system operates as a Standalone inspection station managed by a **Raspberry Pi 5**.
* **Vision:** RPi HQ Camera (12.3MP) with an Arducam 8-50mm Manual Zoom Lens for precise macro focusing.
* **Motion:** Stepper Motor (NEMA 17) driven by a TB6600 industrial driver, rotating the component to inspect all 4 corners.
* **Safety & Power:** A dedicated Relay module separates the logic voltage (5V) from the motor power (12V) to prevent overheating during standby.
* **HMI:** Active buzzer (via ULN2003 driver) for audio alerts and a dedicated GUI.

## Algorithmic Approach (Classical Computer Vision)
Instead of relying on heavy Machine Learning models or generic edge detection (like Canny), this system utilizes a highly efficient **Color Segmentation and Morphological Analysis** pipeline to identify the exposed yellow Scintillator layer beneath the black PDA layer.

The 5-step image processing pipeline:
1. **ROI Extraction & Color Space Conversion:** Cropping the relevant corner area and converting the image from BGR to HSV.
2. **Color Thresholding:** Isolating the specific yellow hue of the defect (Parameters: `Hue 10-37`, `Sat 60-200`, `Val 90-200`).
3. **Morphological Filtering:** Applying Opening/Closing operations on the binary mask to remove isolated noise and reflections.
4. **Geometric Inspection:** Filtering remaining contours based on Aspect Ratio and Area to ensure only true defect structures are counted.
5. **Pixel Summation & Classification:** Counting the total defect pixels and applying a multi-level grading logic:
   * **Class A (PASS):** < 1200 pixels.
   * **Class B (WARNING):** 1200 - 2500 pixels (Flags a boundary case).
   * **FAIL:** > 2500 pixels (Triggers the Fail-Fast mechanism).

<img width="939" height="454" alt="image" src="https://github.com/user-attachments/assets/27ce3777-2e15-4a4e-a682-3111742ba89a" />

## System Features
* **Fail-Fast Mechanism:** If a critical defect (`FAIL`) is detected in one corner, the scanning sequence halts immediately to save cycle time.
* **Custom GUI:** A user-friendly interface built with `CustomTkinter` displaying real-time tracking, dual-screen validation (Original vs. Mask), and clear PASS/WARNING/FAIL indications.
* **Standalone Operation:** Includes modes for both Live Inspection (motor synchronization) and static File Analysis for debugging.

## Repository Structure
Below is the organizational map of the project files and directories:

```text
AOI-Medical-Inspection-System/
│
├── gui_app.py              # Main GUI application and primary execution logic (Run this file)
├── main.py                 # Secondary/Backend execution script
├── requirements.txt        # Required external Python libraries
├── README.md               # Project documentation and overview
│
├── vision/                 # Computer vision and image processing modules
│   ├── morphology.py       # Morphological filtering and noise reduction operations
│   ├── yellow_check.py     # Color segmentation and defect identification logic
│   └── infoo.txt
│
├── hardware/               # Hardware control and interface modules
│   ├── motor.py            # Stepper motor and TB6600 driver control logic
│   ├── camera.py           # RPi HQ Camera interface and capture settings
│   ├── buzzer.py           # ULN2003 buzzer control for audio alerts
│   └── info.txt
│
├── dev_tools/              # Standalone utility scripts and development tools
│   ├── New_Take_a_pic_for_HQ_Camera_for_Checking.py # Independent camera testing script
│   ├── YELLOW_CHECK_with_color_find.py              # Color threshold calibration tool
│   ├── test_skeleton.py                             # Skeleton analysis testing (topology)
│   └── ...                                          # Additional ROI and debugging scripts
│
└── assets/                 # Visual and technical reference materials
    └── Diagrams/           
        ├── Block_Diagram.png        # System architecture and data flow
        ├── Electronic_schema.png    # Hardware wiring and power distribution
        ├── CV_flowchart.png         # Computer Vision algorithmic pipeline
        └── system_flowchart.png     # General system logic and Fail-Fast mechanism

## How to Run
1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the main system (GUI):
   Launch the user interface to start a Live Inspection with hardware synchronization, or perform static File Analysis:
   ```bash
   python gui_app.py
