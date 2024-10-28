Do LLMs Have Distinct and Consistent Personality? TRAIT: Personality Testset designed for LLMs with Psychometrics

Citation Information

	•	Authors: Seungbeen Lee, Seungwon Lim, Seungju Han, Giyeong Oh, Hyungjoo Chae, Jiwan Chung, Minju Kim, Beong-woo Kwak, Yeonsoo Lee, Dongha Lee, Jinyoung Yeo, Youngjae Yu
	•	Affiliations: Yonsei University, Seoul National University, Allen Institute for AI, NCSOFT
	•	Publication Date: June 2024
	•	DOI: Not provided, but available on arXiv as 2406.14703v1

Abstract

This paper explores whether Large Language Models (LLMs) possess personality traits akin to humans, a question extending traditional descriptive psychology to artificial intelligence. The authors present “TRAIT,” a tool with 8,000 context-specific multiple-choice questions to assess LLM personality in a validated manner. TRAIT is based on the Big Five Inventory (BFI) and Short Dark Triad (SD-3) psychometric scales, augmented with the ATOMIC10x commonsense knowledge graph to simulate real-world scenarios. Findings reveal that LLMs demonstrate consistent and distinct personality traits, which are influenced by their alignment training data, showing differences across models like GPT-3.5 and GPT-4. Additionally, while simple prompts can induce certain personality traits, traits such as high psychopathy and low conscientiousness remain resistant, indicating potential areas for further research.

Keywords

	•	Personality in LLMs
	•	Psychometric assessments
	•	Big Five Inventory (BFI)
	•	Short Dark Triad (SD-3)
	•	ATOMIC10x knowledge graph
	•	TRAIT tool
	•	Prompt sensitivity

Comprehensive Analysis and Detailed Breakdown

Purpose/Objective

	•	Goal: This study aims to determine if LLMs can consistently demonstrate human-like personality traits, and if these traits can be systematically measured with psychometric rigor.
	•	Research Questions:
	•	Can LLMs exhibit personality traits similar to those observed in humans?
	•	How reliable and valid are self-assessment tests like the Big Five and Dark Triad for analyzing LLM personality?
	•	Can context-specific questioning yield more accurate personality insights from LLMs?
	•	Significance: Understanding personality in LLMs could enhance their reliability and alignment with human values, especially as they become increasingly embedded in social and professional settings.

Background Knowledge

	•	Core Concepts:
	•	Big Five Inventory (BFI): A prominent psychometric model assessing human personality across openness, conscientiousness, extraversion, agreeableness, and neuroticism.
	•	Short Dark Triad (SD-3): Assesses three adverse personality traits—Machiavellianism, narcissism, and psychopathy.
	•	ATOMIC10x: A large commonsense knowledge graph providing detailed situational prompts, enabling nuanced testing for personality assessment.
	•	Prior Research: LLMs have been evaluated using personality assessments adapted from human psychometrics, but previous tests lacked validity in assessing LLMs due to prompt sensitivity and refusal rates.

Methodology

	•	Research Design: The authors developed TRAIT as an expanded personality test, incorporating validated human personality scales (BFI and SD-3) with 8,000 scenario-specific questions.
	•	Instruments:
	•	TRAIT Test: This tool extends 71 validated human assessment items into multiple contexts, creating a set of 8,000 questions covering a range of scenarios.
	•	T-EVALUATOR: A classifier fine-tuned to analyze responses and assess personality traits across models.
	•	Reliability Metrics: Refusal rate, prompt sensitivity, option order sensitivity, and paraphrase sensitivity, which were measured to ensure reliability.

Main Findings

	•	Distinct Personality Patterns: LLMs show distinct and stable personality traits, which vary significantly between models (e.g., GPT-4 and GPT-3.5) and depend heavily on alignment tuning.
	•	Alignment Impact: Alignment training, especially preference tuning, enhances traits like agreeableness and conscientiousness while reducing dark triad traits (e.g., psychopathy).
	•	Limitations of Prompting: Prompts effectively induce personality traits in LLMs but face challenges with certain characteristics, such as high psychopathy, indicating alignment tuning’s limitations.

Conclusions

	•	Takeaways: LLMs can exhibit personality-like traits, but these are influenced by context and training data, especially alignment tuning. TRAIT successfully captures these traits more reliably than standard self-assessment tools.
	•	Practical Implications: TRAIT’s design provides a foundation for reliably assessing LLM personalities, which could improve human-LLM interactions by aligning personality responses with human values.
	•	Potential Impact: TRAIT’s findings could influence future tuning approaches, potentially allowing models to emulate desired traits while filtering out socially adverse traits.

Limitations and Future Work

	•	Cultural Bias: TRAIT’s reliance on ATOMIC10x and GPT-4 data may limit cultural inclusivity, as many responses reflect Western-centric perspectives.
	•	Generative Settings: TRAIT does not account for personality expressions in multi-turn dialogues, limiting insights into conversational personality.

References

	•	Notable Citations:
	•	John et al., 1999, on BFI in personality assessment.
	•	Jones and Paulhus, 2014, on Dark Triad.
	•	West et al., 2022, on ATOMIC10x knowledge graph in psychological assessments.
