# ML-AI_CS-2022

|  | school | sex | age | address | famsize | Pstatus | Medu | Fedu | Mjob | Fjob | reason | guardian | traveltime | studytime | failures | activities | nursery | higher | internet | romantic | famrel | freetime | goout | Dalc | Walc | health | absences | G1 | G2 | G3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |---| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| 0 | GP | F | 18 | U | GT3 | A | 4 | 4 | at_home | teacher | course | mother | 2 | 2 | 0 | no | yes | yes | no | no | 4 | 3 | 4 | 1 | 1 | 3 | 6 | 5 | 6 | 6 |
| 1 | GP | F | 17 | U | GT3 | T | 1 | 1 | at_home | other | course | father | 1 | 2 | 0 | no | no | yes | yes | no | 5 | 3 | 3 | 1 | 1 | 3 | 4 | 5 | 5 | 6 |
| 2 | GP | F | 15 | U | LE3 | T | 1 | 1 | at_home | other | other | mother | 1 | 2 | 3 | no | yes | yes | yes | no | 4 | 3 | 2 | 2 | 3 | 3 | 10 | 7 | 8 | 10 |
| 3 | GP | F | 15 | U | GT3 | T | 4 | 2 | health | services | home | mother | 1 | 3 | 0 | yes | yes | yes | yes | yes | 3 | 2 | 2 | 1 | 1 | 5 | 2 | 15 | 14 | 15 |
| 4 | GP | F | 16 | U | GT3 | T | 3 | 3 | other | other | home | father | 1 | 2 | 0 | no | yes | yes | no | no | 4 | 3 | 2 | 1 | 2 | 5 | 4 | 6 | 10 | 10 |

Task: classification
--

### tree

#### Label: health

- **Train score**: 1.0
- **Train precision**: 1.0
- **Train recall**: 1.0
- **Train f1**: 1.0
- **Test score**: 0.2435
- **Test precision**: 0.1917
- **Test recall**: 0.1924
- **Test f1**: 0.181

#### Label: Dalc

- **Train score**: 1.0
- **Train precision**: 1.0
- **Train recall**: 1.0
- **Train f1**: 1.0
- **Test score**: 0.6603
- **Test precision**: 0.293
- **Test recall**: 0.3255
- **Test f1**: 0.2971

#### Label: Walc

- **Train score**: 1.0
- **Train precision**: 1.0
- **Train recall**: 1.0
- **Train f1**: 1.0
- **Test score**: 0.3262
- **Test precision**: 0.3147
- **Test recall**: 0.2858
- **Test f1**: 0.2729

### rand forest

#### Label: health

- **Train score**: 1.0
- **Train precision**: 1.0
- **Train recall**: 1.0
- **Train f1**: 1.0
- **Test score**: 0.3287
- **Test precision**: 0.2046
- **Test recall**: 0.1595
- **Test f1**: 0.1622

#### Label: Dalc

- **Train score**: 1.0
- **Train precision**: 1.0
- **Train recall**: 1.0
- **Train f1**: 1.0
- **Test score**: 0.6935
- **Test precision**: 0.2638
- **Test recall**: 0.2182
- **Test f1**: 0.234

#### Label: Walc

- **Train score**: 1.0
- **Train precision**: 1.0
- **Train recall**: 1.0
- **Train f1**: 1.0
- **Test score**: 0.5159
- **Test precision**: 0.4058
- **Test recall**: 0.4289
- **Test f1**: 0.3697

### xgboost

#### Label: health

- **Train score**: 1.0
- **Train precision**: 1.0
- **Train recall**: 1.0
- **Train f1**: 1.0
- **Test score**: 0.2835
- **Test precision**: 0.2036
- **Test recall**: 0.2077
- **Test f1**: 0.1959

#### Label: Dalc

- **Train score**: 1.0
- **Train precision**: 1.0
- **Train recall**: 1.0
- **Train f1**: 1.0
- **Test score**: 0.6856
- **Test precision**: 0.3907
- **Test recall**: 0.3869
- **Test f1**: 0.3721

#### Label: Walc

- **Train score**: 1.0
- **Train precision**: 1.0
- **Train recall**: 1.0
- **Train f1**: 1.0
- **Test score**: 0.4651
- **Test precision**: 0.4548
- **Test recall**: 0.3981
- **Test f1**: 0.3875

### catboost

#### Label: health

- **Train score**: 1.0
- **Train precision**: 1.0
- **Train recall**: 1.0
- **Train f1**: 1.0
- **Test score**: 0.2907
- **Test precision**: 0.1877
- **Test recall**: 0.1415
- **Test f1**: 0.1509

#### Label: Dalc

- **Train score**: 1.0
- **Train precision**: 1.0
- **Train recall**: 1.0
- **Train f1**: 1.0
- **Test score**: 0.6756
- **Test precision**: 0.3289
- **Test recall**: 0.3205
- **Test f1**: 0.3072

#### Label: Walc

- **Train score**: 1.0
- **Train precision**: 1.0
- **Train recall**: 1.0
- **Train f1**: 1.0
- **Test score**: 0.4622
- **Test precision**: 0.3982
- **Test recall**: 0.4124
- **Test f1**: 0.3677

Task: regression
--

### lin reg

#### Label: G1

- **Train score**: 0.778
- **Train MSE**: 2.44
- **Test score**: 0.6713
- **Test MSE**: 3.56

#### Label: G2

- **Train score**: 0.9044
- **Train MSE**: 1.173
- **Test score**: 0.8547
- **Test MSE**: 1.619

#### Label: G3

- **Train score**: 0.8871
- **Train MSE**: 1.771
- **Test score**: 0.8499
- **Test MSE**: 2.25

### tree

#### Label: G1

- **Train score**: 1.0
- **Train MSE**: 0.0
- **Test score**: 0.6367
- **Test MSE**: 3.705

#### Label: G2

- **Train score**: 1.0
- **Train MSE**: 0.0
- **Test score**: 0.8032
- **Test MSE**: 2.302

#### Label: G3

- **Train score**: 1.0
- **Train MSE**: 0.0
- **Test score**: 0.8075
- **Test MSE**: 2.919

### rand forest

#### Label: G1

- **Train score**: 0.9757
- **Train MSE**: 0.267
- **Test score**: 0.7943
- **Test MSE**: 2.11

#### Label: G2

- **Train score**: 0.9882
- **Train MSE**: 0.1444
- **Test score**: 0.8879
- **Test MSE**: 1.34

#### Label: G3

- **Train score**: 0.9868
- **Train MSE**: 0.2068
- **Test score**: 0.8925
- **Test MSE**: 1.589

### xgboost

#### Label: G1

- **Train score**: 1.0
- **Train MSE**: 4.408e-06
- **Test score**: 0.7461
- **Test MSE**: 2.603

#### Label: G2

- **Train score**: 1.0
- **Train MSE**: 1.7e-06
- **Test score**: 0.8779
- **Test MSE**: 1.447

#### Label: G3

- **Train score**: 1.0
- **Train MSE**: 2.383e-06
- **Test score**: 0.8751
- **Test MSE**: 1.863

### catboost

#### Label: G1

- **Train score**: 0.9979
- **Train MSE**: 0.02271
- **Test score**: 0.7773
- **Test MSE**: 2.307

#### Label: G2

- **Train score**: 0.9993
- **Train MSE**: 0.009097
- **Test score**: 0.8871
- **Test MSE**: 1.369

#### Label: G3

- **Train score**: 0.999
- **Train MSE**: 0.01497
- **Test score**: 0.8835
- **Test MSE**: 1.766