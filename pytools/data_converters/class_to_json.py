from finreq_usage import finreq as main_class

def expand_vars(class_var_dict):
    if '_renames' in class_var_dict:
        renames = class_var_dict['_renames']
        del class_var_dict['_renames']
        for key in renames:
            new_name = renames[key]
            if key in class_var_dict:
                value = class_var_dict[key]
                del class_var_dict[key]
                class_var_dict[new_name] = value
    for item in class_var_dict:
        item_type = repr(type(class_var_dict[item]))
        if 'list' in item_type:
            no = len(class_var_dict[item])
            for i in range(no):
                class_var_dict[item][i] = vars(class_var_dict[item][i])
                expand_vars(class_var_dict[item][i])
        elif '.' in item_type:
            class_var_dict[item] = vars(class_var_dict[item])
            expand_vars(class_var_dict[item])

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



