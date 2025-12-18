from finreq_usage import finreq as main_class

def expand_vars(class_var_dict):
    for name in class_var_dict:
        if type(class_var_dict[name]) is list:
            no = len(class_var_dict[name])
            for i in range(no):
                class_var_dict[name][i] = vars(class_var_dict[name][i])
                expand_vars(class_var_dict[name][i])
        x = repr(type(class_var_dict[name]))
        if '__main__.' in x:
            class_var_dict[name] = vars(class_var_dict[name])
            expand_vars(class_var_dict[name])

def class_as_dict(cls):
    cls_var_dict = vars(cls)
    expand_vars(cls_var_dict)
    return cls_var_dict

import yaml, json

def main():
    cls_dict = class_as_dict(main_class)
    json_string = json.dumps(cls_dict, indent=2)
    yaml_string = yaml.dump(cls_dict, sort_keys=False)
    print (json_string)
    print ('----------------- yaml ---------- ')
    print (yaml_string)
 
if __name__ == '__main__':
    main()



