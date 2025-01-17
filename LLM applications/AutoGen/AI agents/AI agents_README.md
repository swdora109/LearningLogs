# Autogen Practice: Analyzing Temperature Changes with Chat GPT Models 📈

This project utilizes Autogen to analyze changes in Korea's average January temperature from 2014 to 2024 using two different Chat GPT models. Results are presented and compared in both Korean and English.

## Table of Contents 📑
- [Introduction](#introduction)
- [Models Used](#models-used)
- [Prompt](#prompt)
- [Results](#results)
- [Learning Points](#learning-points)
- [Conclusion](#conclusion)
- [Acknowledgments](#acknowledgments)

## Introduction 📋
This project demonstrates how to use Autogen with Chat GPT models for climate analysis. The primary objective is to compare the outputs of two models and analyze the differences between Korean and English results. This exercise highlights the impact of language and model variations on the generated content.

## Models Used 🧠
- Model A: gpt-4-turbo-preview
- Model B: gpt-4o
- Model C: dall-e-3 (for image generations)

## Prompt 📝
The same prompt was provided.

Korean: "2014년부터 2024년까지 한국 1월의 평균 기온 그래프를 그려서 winter_temperature_KOR.png 파일로 저장해줘. X축에는 매 연도를, Y축은 -5도부터 5도까지 0.5도 간격으로 설정해줘. 기온은 x축에 정수 형태로 표기해줘. 평균 기온의 차이가 잘 드러나도록 그래프를 그려줘.
그림은 ggplot 스타일로 그려줘. 크기는 가로 10, 세로 6으로 해줘. 제목은 Changes in Average January Temperature in Korea (2014-2024)로 해줘."

English: "Create a graph showing the average temperature of January in Korea for each year from 2014 to 2024, and save it as winter_temperature_ENG.png. Set the x-axis to represent each year and the y-axis to range from -5°C to 5°C with 0.5°C intervals. Display the values of each temperature in integer on the x-axis. Ensure that the differences in average temperatures are clearly visible. Use the ggplot style for the graph, and set the size to 10 (width) by 6 (height). Changes in Average January Temperature in Korea (2014-2024)"

## Results 📊

**Korean Output:**  
![winter_temperature_KOR](https://github.com/user-attachments/assets/cc3235eb-e59f-4f32-acb3-0a1d709db164)


**English Output:**  
![winter_temperature_ENG](https://github.com/user-attachments/assets/430d0754-c276-456c-a780-1bfcc7d77e2a)


## Learning Points 💡
Observing how outputs can vary significantly depending on the language used, even with identical prompts, I recognized the need for a more systematic approach to ensure data accuracy and reliability. This involves adopting a strategy that combines diverse models and languages in various ways to achieve the most precise analysis. Furthermore, I realized the importance of validating information through additional research to reinforce the overall process. Ultimately, I believe this multi-layered approach not only enhances data reliability but also fosters the discovery of diverse perspectives and insights.


## Conclusion 🏁
This project successfully demonstrated how to use Autogen and Chat GPT models for temperature trend analysis. The exercise provided insights into the variability of outputs across models and languages. A key takeaway is the necessity of rigorous validation and reliability checks to ensure consistency and accuracy, particularly in multilingual scenarios. Such comparative studies are essential for evaluating model performance and building trust in AI-generated results.

