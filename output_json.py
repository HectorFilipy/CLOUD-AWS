import json

# Arquivo para converter
arquivo = 'output_certs.txt'
  
# Dicit 1
dict1 = {}
  
# Campos 
fields =['Dominio', 'Metodo', 'Status', 'Validade', 'Tempo']
  
with open(arquivo) as fh:
      
    # variável de contagem para criação de id.
    id = 1
      
    for line in fh:
          
        # lendo linha por linha do arquivo de texto
        desc = list(line.strip().split(None, 5))
          
        # para ver a saída
        print(desc) 
          
        # criação automática de id para certificado
        sno ='cert'+str(id)
      
        # variável de loop
        i = 0
        # Dict 2
        dict2 = {}
        while i < len(fields):
              
                # criando dicionário para cada certificado
                dict2[fields[i]] = desc[i]
                i = i + 1 
        # anexando o registro de cada certificado a o dicionário principal
        dict1[sno]= dict2
        id = id + 1

# criando o json file        
out_file = open("certificados.json", "w")
json.dump(dict1, out_file, indent = 4)
out_file.close()