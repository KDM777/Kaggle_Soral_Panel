# Overview
- 프로젝트의 목표 : kaggle의 Image Classifciation Task 중 하나로, 기존의 EfficientNet에 block을 추가하여 성능을 높이는 것
  - https://www.kaggle.com/datasets/pythonafroz/solar-panel-images/data

- Dataset
  - 아래의 표 참조
<img width="507" height="255" alt="image" src="https://github.com/user-attachments/assets/ff54ce62-54e6-4d1d-a140-9e93fe4cd1b8" />

# Network Architecture Design
- Image Classifcation에서 SOTA 성능을 가진 두 가지 특징 추출기 (EfficientNet + VGG19) 를 결합하면 좋은 성능이 나올 것으로 기대
- 과적합 방지를 위해 프리징(Freezing) 전략 채용
- 특징 보존과 학습 안정성을 위해 Residual Block 적용
- 다중 스케일 정보를 활용하기 위해 ASPP 적용하는 것으로 고안
<img width="835" height="252" alt="image" src="https://github.com/user-attachments/assets/2a08eaee-34b2-4c33-8aa4-38489c0bb499" />

# Experimental Setup and Results
- 학습 방법 및 하이퍼 파라미터
  - Optimizer : AdamW
  - Loss function : CrossEntropyLoss
  - Label smoothing 적용 (값 = 0.1)
  - Learning rate : 1e-3
  - Batch size : 32
  - Epoch : 50

- 실험 진행 및 결과
  - 기존 Efficientnet 모델보다 성능이 2.9% 상승
- 모델별 ROC 곡선
  - (a) : EfficientNet, AUC 평균 값 : 0.961
  - (b) : VGG19, AUC 평균 값 : 0.892
  - (c) : EfficientNet+VGG19, AUC 평균 값 : 0.973
  - (d) : Ours, AUC 평균 값 : 0.974

- Accuracy와 AUC평균 값을 고려하였을 때 Ours(EfficientNet +VGG19 + Residual Block + ASPP)의 성능이 가장 좋음
<img width="1150" height="891" alt="image" src="https://github.com/user-attachments/assets/b34b2053-9f6e-48a7-afc1-6457abdff44e" />

# Paper
