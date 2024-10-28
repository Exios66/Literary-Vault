# **Brain Waves-Based Index for Workload Estimation and Mental Effort Engagement Recognition**

## Citation Information

- **Authors**: A. Zammouri, S. Chraa-Mesbahi, A. Ait Moussa, S. Zerouali, M. Sahnoun, H. Tairi, and A. M. Mahraz
- **Title**: *Brain Waves-Based Index for Workload Estimation and Mental Effort Engagement Recognition*
- **Journal**: *Journal of Physics: Conference Series*
- **Publisher**: IOP Publishing
- **Conference**: 7th International Conference on New Computational Methods for Inverse Problems
- **Volume and Article**: 904, 012008
- **Publication Date**: 2017
- **DOI**: [10.1088/1742-6596/904/1/012008](https://doi.org/10.1088/1742-6596/904/1/012008)
- **Affiliations**: Various institutions in Morocco and France, including Mohammed First University, University of Sidi Mohammed Ben Abdellah, and CESI-Centre Nord-Ouest.

## Abstract

The study develops an EEG-based index for estimating mental workload and effort during cognitive tasks of varying difficulty. By using a classifier based on Power Spectral Density (PSD) of EEG signals, the authors identify brain regions engaged under different cognitive loads. Results indicate that increased task difficulty correlates with decreased Theta and Alpha power in the parietal and temporal lobes. A new EEG index introduced here, validated against existing indices, shows strong agreement and high sensitivity to cognitive workload changes, demonstrating its efficacy in distinguishing workload levels.

## Keywords

- [Electroencephalography (EEG)](https://scholar.google.com/scholar?q=Electroencephalography+EEG)
- [Cognitive Workload](https://scholar.google.com/scholar?q=Cognitive+Workload)
- [Brain-Computer Interface (BCI)](https://scholar.google.com/scholar?q=Brain-Computer+Interface)
- [Power Spectral Density (PSD)](https://scholar.google.com/scholar?q=Power+Spectral+Density+PSD)
- [Theta and Alpha Bands](https://scholar.google.com/scholar?q=Theta+and+Alpha+Bands)
- [Mental Effort](https://scholar.google.com/scholar?q=Mental+Effort)

---

# Comprehensive Content Breakdown

## Introduction

The study addresses the need for communication systems that can adapt to the mental workload of users, especially within assistive technologies. By incorporating artificial intelligence into systems that can interact with humans, particularly through Brain-Computer Interfaces (BCIs), it becomes possible to support individuals with disabilities or high-dependence needs. EEG-based indices are identified as effective tools for estimating mental workload, primarily because they offer precise insights into an individual's cognitive state through biological signals, including brain wave patterns.

### Objective

The primary aim is to create a workload estimation tool that can distinguish mental states based on task difficulty levels, particularly using EEG signals. The paper introduces a classifier for analyzing cognitive load by examining the power spectral density of EEG signals in relation to specific frequency bands.

## Methodology

The study uses EEG data from four male participants engaged in a cognitive task involving matrix product calculations at varying difficulty levels. EEG signals are analyzed across seven electrodes, processed through a variances comparison-based classifier (VCC) and Power Spectral Density (PSD) analyses, focusing on the Alpha (8-12 Hz) and Theta (4-7 Hz) bands. The researchers employ a Welch periodogram approach for signal analysis and a VCC to compare EEG signal variations across task difficulties.

### Key Steps in EEG Analysis

1. **Artifact Reduction**: Blind Source Separation (BSS) technique is applied to remove unwanted noise from EEG signals.
2. **Spectral Power Calculation**: EEG signals are converted to the frequency domain using the Short Time Fourier Transform (STFT) and analyzed for Alpha and Theta power variations.
3. **Classifier Design**: VCC is used to test the variance between two sessions (low and high difficulty), determining whether cognitive load affects signal power in these specific bands.

### Cognitive Workload Index Development

A new cognitive workload index is developed by calculating the ratio of Alpha and Theta powers in the parietal and frontal regions. This index is specifically sensitive to task difficulty, as shown by decreased power in the higher-difficulty tasks, indicating increased cognitive load.

## Experimental Results

- **Behavior of Alpha and Theta Waves**: Findings indicate that as task difficulty increases, there is a decrease in Alpha and Theta band power in parietal and temporal areas, reflecting higher cognitive load.
- **Cognitive Workload Index Sensitivity**: The introduced index correlates with difficulty, as evidenced by distinct Alpha and Theta power reductions during more challenging tasks.
- **Kappa Coefficient Analysis**: Agreement between the introduced index and an existing index (Holm’s index) is tested using the Kappa coefficient, revealing high consistency, which underscores the index’s robustness in differentiating workload levels.

## Discussion

The study provides insights into how EEG signals can be utilized to estimate mental effort engagement. Variations in the Alpha and Theta bands directly correlate with cognitive workload, particularly as tasks become more demanding. The index’s reliance on Alpha and Theta band power is shown to be effective, and the method proves useful in real-time applications for adaptive systems in healthcare and other fields requiring user-state monitoring.

### Practical Implications

For practical applications, this index could enhance adaptive technologies like assistive devices for individuals with limited mobility or alertness-monitoring systems in environments requiring sustained attention (e.g., driving or air traffic control).

## Conclusion

This study proposes a novel EEG-based index that is sensitive to cognitive load variations, demonstrating potential applications in BCIs for workload estimation and adaptive user support systems. Future research should involve larger datasets to refine threshold values for various cognitive states and investigate further applications in different environments and user groups.

---
