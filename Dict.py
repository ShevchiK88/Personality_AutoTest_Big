Type_dict={"INFP" : "Mediator",
           "INFJ" : "Advocate",
           "ENFJ" : "Protagonist",
           "ENFP" : "Campaigner",
           "INTJ" : "Architect",
           "ENTJ" : "Commander",
           "ENTP" : "Debater",
           "INTP" : "Logician",
           "ESFJ" : "Consul",
           "ESFP" : "Entertainer",
           "ISFJ" : "Defender",
           "ISFP" : "Adventurer",
           "ESTJ" : "Executive",
           "ESTP" : "Entrepreneur",
           "ISTJ" : "Logistician",
           "ISTP" : "Virtuoso"}

Type_list_abbreviation = [
    "INFP" ,
    "INFJ" ,
    "ENFJ" ,
    "ENFP" ,
    "INTJ" ,
    "ENTJ" ,
    "ENTP" ,
    "INTP" ,
    "ESFJ" ,
    "ESFP" ,
    "ISFJ" ,
    "ISFP" ,
    "ESTJ" ,
    "ESTP" ,
    "ISTJ" ,
    "ISTP" ]

Type_list_transcript = [
    "Mediator",
    "Advocate",
    "Protagonist",
    "Campaigner",
    "Architect",
    "Commander",
    "Debater",
    "Logician",
    "Consul",
    "Entertainer",
    "Defender",
    "Adventurer",
    "Executive",
    "Entrepreneur",
    "Logistician",
    "Virtuoso"]

for i in range(0,len(Type_list_abbreviation),1):
    type_A = Type_list_abbreviation[i]
    type_T = Type_list_transcript[i]
    print(type_A,type_T)