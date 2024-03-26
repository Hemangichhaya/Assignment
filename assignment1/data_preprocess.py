import pytesseract
from PIL import Image
import pandas as pd
import docx2txt
import os, re
import json
from unicodedata import normalize
pytesseract.pytesseract.tesseract_cmd = r'D:/testreact_folder/tesseract.exe'



def preprocess(filename, file_location):
  if filename.endswith('.docx'):
      content = docx2txt.process(os.path.join(file_location, filename))
  else:
      content = pytesseract.image_to_string(Image.open(os.path.join(file_location, filename)))
  content = normalize('NFKD',content).encode('ascii', 'ignore').decode('ascii')
  lines = content.replace('\n\n', '\n ')
  lines = re.sub(' +',' ', lines)
  # lines = lines.split('\n')
  line = []
  # # for 500 characters
  # for i in range(len(lines)//500):
  #     line.append(lines[i*500:(i+1)*500])
  #for \n line split
  for line_ in lines:
     line.append(line_)
  return line

def convert_spacy_json(input_file_name, output_file_name, file_location, entities_val):
  lines = preprocess(input_file_name, file_location)
  data = []
  for line in lines:
    entities_list = []
    for key_ in entities_val.keys():
        # print(key_)
        if str(key_) in line:
            strt = line.index(str(key_))
            entities_list.append(tuple((strt, strt+len(str(key_)), entities_val[key_])))
    data.append(tuple((line, {'entities':entities_list})))
  return {'data':data}
  # with open(output_file_name, 'w') as file:
  #   json.dump({'data':data}, file)

def convert_llm_data(input_file_name, output_file_name, file_location, entities_val):
  lines = preprocess(input_file_name, file_location)
  inp_data, output_data = [], []
  for line in lines:
    entities_list = []
    # print(line)
    for key_ in entities_val.keys():
        if str(key_) in line:
            entities_list.append(tuple((str(key_), entities_val[str(key_)])))
    inp_data.append(line)
    output_data.append(entities_list)
  # with open(output_file_name, 'w') as file:
  #   json.dump({'input':inp_data, 'output':output_data}, file)
  return {'input':inp_data, 'output':output_data}

def data(df_location, output_file_name, file_location):
  df = pd.read_csv(df_location)
  
  filename_map = {}
  for files in os.listdir(file_location):
    filename_map[files.split('.')[0]] = files
  llm_data_json, spacy_data_json = {'input':[], 'output':[]}, {'data':[]}
  for idx, val in df.iterrows():
    
    if val['File Name'] not in filename_map or '44737744-Maddireddy-Bhargava-Reddy-Rental-Agreement' == val['File Name']:
      continue
    entities_val = {val['Aggrement Value']:'Aggrement Value', val['Aggrement Start Date']:'Aggrement Start Date',
                val['Aggrement End Date']:'Aggrement End Date', val['Renewal Notice (Days)']:'Renewal Notice (Days)', 
                val['Party One']:'Party One', val['Party Two']:'Party Two'}
    # print(filename_map[val['File Name']])
    # if filename_map[val['File Name']].endswith('.docx'):
    tmp_llm_json = convert_llm_data(filename_map[val['File Name']], val['File Name']+'.json', file_location, entities_val)
    llm_data_json['input'].extend(tmp_llm_json['input'])
    llm_data_json['output'].extend(tmp_llm_json['output'])
    tmp_spacy_json = convert_spacy_json(filename_map[val['File Name']], val['File Name']+'.json', file_location, entities_val)
    spacy_data_json['data'].extend(tmp_spacy_json['data'])
  with open('./data/'+output_file_name+'_llm.json', 'w') as file:
    json.dump(llm_data_json, file)
  with open('./data/'+output_file_name+'_spacy.json', 'w') as file:
    json.dump(spacy_data_json, file)