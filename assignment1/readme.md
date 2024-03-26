Install tessreact for OCR
```
https://github.com/UB-Mannheim/tesseract/wiki
```
Then install requirements using 
```
pip install -r requirements.txt
```
modify path of tessreact
```
pytesseract.pytesseract.tesseract_cmd = r'D:/testreact_folder/tesseract.exe'
```
To train new model 
```
python ./main.py
```
To infer for new data using web UI
```
streamlit run .\streamlit_app.py
```

Preprocessing
```
- Since text consists of noise, entities provided in train.csv or test.csv are not exist as it is in the files, so by reading text and labels, annotations are created in mod_train.csv and test.csv files.
- One extra file removed from train folder (24158401)
- One file doesn't consist information due to image of older agreement, so it is removed from train data (44737744)
- Two models trained based on text splitted with new line (\n) delimeter (models/split_lines_main) and fixed span length of 500 characters (models/split_fixedlen_main)
```

Performance measure f1 score on test data with 500 characters
```
{'ents_p': 0.5, 'ents_r': 0.3157894736842105, 'ents_f': 0.3870967741935484, 'ents_per_type': {'Party Two': {'p': 0.0, 'r': 0.0, 'f': 0.0}, 'Aggrement End Date': {'p': 0.25, 'r': 0.25, 'f': 0.25}, 'Aggrement Start Date': {'p': 0.0, 'r': 0.0, 'f': 0.0}, 'Renewal Notice (Days)': {'p': 0.6666666666666666, 'r': 1.0, 'f': 0.8}, 'Party One': {'p': 0.5, 'r': 0.3333333333333333, 'f': 0.4}, 'Aggrement Value': {'p': 0.0, 'r': 0.0, 'f': 0.0}}}
```
on train data with 500 characters
```
{'ents_p': 0.9333333333333333, 'ents_r': 0.9545454545454546, 'ents_f': 0.9438202247191012, 'ents_per_type': {'Party One': {'p': 1.0, 'r': 1.0, 'f': 1.0}, 'Aggrement End Date': {'p': 0.8181818181818182, 'r': 1.0, 'f': 0.9}, 'Aggrement Start Date': {'p': 1.0, 'r': 0.7142857142857143, 'f': 0.8333333333333333}, 'Aggrement Value': {'p': 0.8, 'r': 1.0, 'f': 0.888888888888889}, 'Renewal Notice (Days)': {'p': 1.0, 'r': 1.0, 'f': 1.0}, 'Party Two': {'p': 1.0, 'r': 1.0, 'f': 1.0}}}
```

Performance measure on test data with line split

```
{'ents_p': 0.42857142857142855, 'ents_r': 0.42857142857142855, 'ents_f': 0.42857142857142855, 'ents_per_type': {'Party One': {'p': 0.0, 'r': 0.0, 'f': 0.0}, 'Party Two': {'p': 0.0, 'r': 0.0, 'f': 0.0}, 'Aggrement End Date': {'p': 0.42857142857142855, 'r': 0.75, 'f': 0.5454545454545454}, 'Aggrement Start Date': {'p': 0.3333333333333333, 'r': 0.5, 'f': 0.4}, 'Renewal Notice (Days)': {'p': 0.8, 'r': 0.8, 'f': 0.8000000000000002}, 'Aggrement Value': {'p': 0.0, 'r': 0.0, 'f': 0.0}}}
```

train data
```
{'ents_p': 0.8958333333333334, 'ents_r': 0.9555555555555556, 'ents_f': 0.924731182795699, 'ents_per_type': {'Party One': {'p': 0.8333333333333334, 'r': 1.0, 'f': 0.9090909090909091}, 'Aggrement Start Date': {'p': 0.8888888888888888, 'r': 1.0, 'f': 0.9411764705882353}, 'Aggrement End Date': {'p': 0.9, 'r': 1.0, 'f': 0.9473684210526316}, 'Aggrement Value': {'p': 1.0, 'r': 0.75, 'f': 0.8571428571428571}, 'Renewal Notice (Days)': {'p': 1.0, 'r': 1.0, 'f': 1.0}, 'Party Two': {'p': 0.8, 'r': 0.8, 'f': 0.8000000000000002}}}
```