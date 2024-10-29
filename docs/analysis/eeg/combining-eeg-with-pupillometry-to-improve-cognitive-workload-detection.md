# Combining EEG with Pupillometry to Improve Cognitive Workload Detection

## Combining EEG with Pupillometry to Improve Cognitive Workload Detection

### Citation Information

* Authors: David Rozado (Otago Polytechnic), Andreas Duenser (Commonwealth Scientific and Industrial Research Organisation - CSIRO)
* Title: “Combining EEG with Pupillometry to Improve Cognitive Workload Detection”
* Journal/Source: Computer
* Publication Year: October 2015
* DOI: 10.1109/MC.2015.314&#x20;
* Affiliations: Otago Polytechnic (David Rozado), CSIRO (Andreas Duenser)

### Key Details

#### Summary

**Abstract Summary**

The article investigates the integration of EEG (electroencephalography) with pupillometry to improve the detection of cognitive workload in real-time. Traditional neuroimaging tools like EEG and fMRI face limitations in accuracy and latency when measuring cognitive workload. This study combines EEG signals with data from pupil dilation, which has been correlated with cognitive processes, aiming to refine cognitive workload monitoring. The authors conducted an experiment where EEG and pupillometry data were collected from participants performing cognitive tasks (e.g., mental arithmetic) and relaxed states to assess the combined effectiveness of these signals.

**Keywords**

• Cognitive workload detection • EEG (Electroencephalography) • Pupillometry • Human-computer interaction (HCI) • Multimodal brain-computer interface (BCI)

### Comprehensive Analysis

#### Audience

• Target Audience: The article is primarily intended for researchers, practitioners, and professionals in the fields of cognitive neuroscience, human-computer interaction, and physiological computing. Specifically, those focused on improving BCI technology through multimodal signal processing would find this work valuable. • Application: This research has direct applications in real-time monitoring systems for high-stress environments (e.g., aviation, military), user-adaptive interfaces, and fields needing real-time feedback on cognitive states. • Outcome: If applied, these findings could enhance the development of adaptive systems that modify their responses based on the user’s cognitive workload, leading to safer and more efficient interfaces.

### Relevance

• Significance: Integrating EEG with pupillometry aligns with current trends in HCI and BCI technology, where multi-signal approaches are being explored for improved accuracy and reliability. • Real-World Implications: Enhanced cognitive workload detection could be used in creating adaptive user interfaces that reduce cognitive load in high-stakes or information-heavy environments, promoting greater safety and efficiency.

### Conclusions

• Key Findings: Combining EEG with pupillometry significantly improves cognitive workload detection accuracy compared to using either signal in isolation. • Takeaways: The combination of EEG and pupil dilation data enhances the detection accuracy of cognitive workload over using either signal alone. The experiment found that the multimodal approach reduced error rates in distinguishing between workload and no-task conditions. • Practical Implications: The study supports the use of multimodal physiological data to develop BCI systems that are more accurate and less intrusive, potentially improving performance in real-world applications. • Potential Impact: Expanding on this research could lead to robust real-time monitoring solutions that could be applied in industries requiring rapid, accurate assessment of mental workload, such as healthcare and critical transportation sectors.

### Contextual Insight

• Abstract in a Nutshell: The study proposes a combined EEG-pupillometry approach to improve cognitive workload detection, offering potential benefits in real-time HCI and BCI applications. • Abstract Keywords: Cognitive workload detection, EEG, Pupillometry, BCI, HCI. • Gap/Need: There is a need for higher accuracy, reliability, and response times in workload monitoring systems, which are often limited by single-modality approaches. • Innovation: By combining EEG with pupil-dilation tracking, this work improves classification accuracy and reduces error rates, providing a feasible pathway toward real-time cognitive workload monitoring.

### Key Quotes

1. “Our results show that combining a pupil-diameter feature with EEG-derived features can predict cognitive workload \[…] with an error rate of 17 percent.”
2. “One issue when using physiological data is that it can be sensitive \[…] to external stimuli.”
3. “This multimodal approach has great potential for real-time BCI systems because it achieves relatively high accuracy under suboptimal data-quality conditions.”
4. “The classification error rate was significantly lower with the combination of EEG and pupillometry than with either EEG or pupillometry alone.”
5. “Although pupillometry alone requires less complex infrastructure, it may not have the granularity required for detecting finer changes in cognitive workload levels.”

### Questions and Answers

1. How does combining EEG with pupillometry improve cognitive workload detection? The combination reduces error rates and increases classification accuracy, providing a more robust detection mechanism than either EEG or pupillometry alone.
2. What are the main challenges in using pupillometry for cognitive workload detection? External stimuli, such as lighting changes, can affect pupil size, complicating workload detection based solely on pupil dilation.
3. Why is cognitive workload monitoring important in HCI and BCI applications? Monitoring workload enables the design of adaptive systems that adjust based on user state, potentially improving safety and user experience in critical applications.
4. What advantages does the multimodal approach provide over single-modality systems? It offers improved reliability in real-world scenarios, better error rates, and potential applications in a wider range of environments.
5. What future improvements did the authors suggest? They recommended exploring control for external stimuli effects on pupil size and testing the approach with more complex cognitive tasks.

### Paper Details

Purpose/Objective

• Goal: To determine if combining EEG with pupillometry can improve the accuracy of cognitive workload detection. • Research Questions/Hypotheses: The authors hypothesized that multimodal physiological data could outperform single-modality approaches in real-time cognitive workload monitoring. • Significance: This research addresses the limitations of single-modality workload monitoring systems, potentially paving the way for enhanced BCI and HCI interfaces.

Background Knowledge

• Core Concepts: Cognitive workload, multimodal physiological signals, EEG, pupillometry, brain-computer interface (BCI). • Preliminary Theories: The study builds upon previous EEG-based workload monitoring systems and research linking pupil dilation to cognitive states. • Contextual Timeline: The paper references evolving research from single-modality EEG studies to modern multimodal approaches. • Prior Research: The authors acknowledge earlier studies combining physiological metrics like heart rate and EEG, which laid the groundwork for multimodal workload detection. • Terminology: Cognitive workload - the mental effort needed to process information; BCI - systems that interpret brain activity for user control interfaces. • Essential Context: Advances in real-time HCI have shown a need for systems capable of accurately monitoring user state, a gap this paper addresses.

### Methodology

• Research Design & Rationale: • Type: Experimental design with cognitive workload and no-task control conditions. • Implications: The design tests the combined effects of EEG and pupillometry, offering insights for BCI development. • Participants/Subjects: • Sample Size: 23 participants. • Demographics: Age range 15-48, including males and females. • Instruments/Tools: Tobii X2-30 eye tracker for pupillometry, Biosemi ActiveTwo EEG for brain activity, and EEG analysis software (EEGLab, BCILAB). • Data Collection: Data was gathered in controlled blocks of mental arithmetic tasks versus relaxed states, with ambient light controlled to reduce external noise. • Data Analysis Techniques: • Techniques: Common spatial patterns (CSPs) for EEG, linear discriminant analysis (LDA) for classification. • Comparison to Standard: The methodology adheres to standard EEG and cognitive workload detection protocols, incorporating innovative multimodal techniques. • Replicability Score: 8/10, due to detailed methodology, equipment availability, and reliance on standard analysis tools.

Main Results/Findings

• Metrics: • Classification Error Rate: Reduced to 17% with multimodal signals compared to 26.1% (pupillometry alone) and 24.1% (EEG alone). • Information Transfer Rate: Improved by combining both modalities. • Outcomes: Multimodal approach achieves significantly better accuracy. • Data & Code Availability: Data sources are cited, though the code is not specified. • Statistical Significance: The error rate improvement with combined EEG and pupillometry was statistically significant.

### Authors' Perspective

• Authors’ Views: The authors emphasize the potential of multimodal workload detection for BCI, citing enhanced accuracy and usability benefits over single-modality methods. • Comparative Analysis: This study builds on prior EEG and pupillometry research by testing their combined efficacy in real-world applicable conditions.

#### Limitations

• List: Sensitivity of pupil dilation to lighting changes, limited complexity in task variety. • Mitigations: Ambient light controlled, stimulus brightness constant; suggestions for future work on more diverse tasks.

#### Proposed Future Work

• Authors’ Proposals: Testing other cognitive tasks, refining stimulus brightness control, and exploring the technique in various BCI applications.

### Conclusion

This study demonstrates the potential of combining EEG and pupillometry for more accurate cognitive workload detection, offering a promising approach for real-time BCI applications. The multimodal approach not only enhances accuracy but also reduces error rates, suggesting its practical applicability in various HCI and BCI scenarios. Future research could further refine stimulus control and explore the technique in more complex cognitive tasks to validate its broader utility.

### **Brain Waves-Based Index for Workload Estimation and Mental Effort Engagement Recognition**

#### Citation Information

* **Authors**: A. Zammouri, S. Chraa-Mesbahi, A. Ait Moussa, S. Zerouali, M. Sahnoun, H. Tairi, and A. M. Mahraz
* **Title**: _Brain Waves-Based Index for Workload Estimation and Mental Effort Engagement Recognition_
* **Journal**: _Journal of Physics: Conference Series_
* **Publisher**: IOP Publishing
* **Conference**: 7th International Conference on New Computational Methods for Inverse Problems
* **Volume and Article**: 904, 012008
* **Publication Date**: 2017
* **DOI**: [10.1088/1742-6596/904/1/012008](https://doi.org/10.1088/1742-6596/904/1/012008)
* **Affiliations**: Various institutions in Morocco and France, including Mohammed First University, University of Sidi Mohammed Ben Abdellah, and CESI-Centre Nord-Ouest.

#### Abstract

The study develops an EEG-based index for estimating mental workload and effort during cognitive tasks of varying difficulty. By using a classifier based on Power Spectral Density (PSD) of EEG signals, the authors identify brain regions engaged under different cognitive loads. Results indicate that increased task difficulty correlates with decreased Theta and Alpha power in the parietal and temporal lobes. A new EEG index introduced here, validated against existing indices, shows strong agreement and high sensitivity to cognitive workload changes, demonstrating its efficacy in distinguishing workload levels.

#### Keywords

* [Electroencephalography (EEG)](https://scholar.google.com/scholar?q=Electroencephalography+EEG)
* [Cognitive Workload](https://scholar.google.com/scholar?q=Cognitive+Workload)
* [Brain-Computer Interface (BCI)](https://scholar.google.com/scholar?q=Brain-Computer+Interface)
* [Power Spectral Density (PSD)](https://scholar.google.com/scholar?q=Power+Spectral+Density+PSD)
* [Theta and Alpha Bands](https://scholar.google.com/scholar?q=Theta+and+Alpha+Bands)
* [Mental Effort](https://scholar.google.com/scholar?q=Mental+Effort)

***

### Study Overview and Key Components

#### Introduction

The study addresses the need for communication systems that can adapt to the mental workload of users, especially within assistive technologies. By incorporating artificial intelligence into systems that can interact with humans, particularly through Brain-Computer Interfaces (BCIs), it becomes possible to support individuals with disabilities or high-dependence needs. EEG-based indices are identified as effective tools for estimating mental workload, primarily because they offer precise insights into an individual's cognitive state through biological signals, including brain wave patterns.

**Objective**

The primary aim is to create a workload estimation tool that can distinguish mental states based on task difficulty levels, particularly using EEG signals. The paper introduces a classifier for analyzing cognitive load by examining the power spectral density of EEG signals in relation to specific frequency bands.

#### Methodology

The study uses EEG data from four male participants engaged in a cognitive task involving matrix product calculations at varying difficulty levels. EEG signals are analyzed across seven electrodes, processed through a variances comparison-based classifier (VCC) and Power Spectral Density (PSD) analyses, focusing on the Alpha (8-12 Hz) and Theta (4-7 Hz) bands. The researchers employ a Welch periodogram approach for signal analysis and a VCC to compare EEG signal variations across task difficulties.

**Key Steps in EEG Analysis**

1. **Artifact Reduction**: Blind Source Separation (BSS) technique is applied to remove unwanted noise from EEG signals.
2. **Spectral Power Calculation**: EEG signals are converted to the frequency domain using the Short Time Fourier Transform (STFT) and analyzed for Alpha and Theta power variations.
3. **Classifier Design**: VCC is used to test the variance between two sessions (low and high difficulty), determining whether cognitive load affects signal power in these specific bands.

**Cognitive Workload Index Development**

A new cognitive workload index is developed by calculating the ratio of Alpha and Theta powers in the parietal and frontal regions. This index is specifically sensitive to task difficulty, as shown by decreased power in the higher-difficulty tasks, indicating increased cognitive load.

#### Experimental Results

* **Behavior of Alpha and Theta Waves**: Findings indicate that as task difficulty increases, there is a decrease in Alpha and Theta band power in parietal and temporal areas, reflecting higher cognitive load.
* **Cognitive Workload Index Sensitivity**: The introduced index correlates with difficulty, as evidenced by distinct Alpha and Theta power reductions during more challenging tasks.
* **Kappa Coefficient Analysis**: Agreement between the introduced index and an existing index (Holm’s index) is tested using the Kappa coefficient, revealing high consistency, which underscores the index’s robustness in differentiating workload levels.

#### Discussion

The study provides insights into how EEG signals can be utilized to estimate mental effort engagement. Variations in the Alpha and Theta bands directly correlate with cognitive workload, particularly as tasks become more demanding. The index’s reliance on Alpha and Theta band power is shown to be effective, and the method proves useful in real-time applications for adaptive systems in healthcare and other fields requiring user-state monitoring.

**Practical Implications**

For practical applications, this index could enhance adaptive technologies like assistive devices for individuals with limited mobility or alertness-monitoring systems in environments requiring sustained attention (e.g., driving or air traffic control).

#### Conclusion

This study proposes a novel EEG-based index that is sensitive to cognitive load variations, demonstrating potential applications in BCIs for workload estimation and adaptive user support systems. Future research should involve larger datasets to refine threshold values for various cognitive states and investigate further applications in different environments and user groups.

***
