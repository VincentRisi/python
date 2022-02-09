from SYS_FUNCTIONS import *
from INTRINSICS import *
import sys
import types
import time
import traceback
import xml.sax

def isList(l):
  return type(l) is list

def isDict(l):
  return type(l) is dict

def msgname(d):
  keys = list(d.keys())
  key = keys[0]
  n = key.find('.')
  if n == -1:
      n = key.find('/')
  if n > 0:
      name = key[:n]
  else:
      name = key
  return name

def printDict(d):
  for key in list(d.keys()):
    value = d[key]
    if isList(value):
      for i in range(len(value)):
        print(key+'['+str(i)+']', "'"+value[i]+"'")
    else:
      print(key, '"'+value+'"')

# -- This printClass has no eval -- but uses standard attr routines
def printClass(c, name='top'):
    if hasattr(c, '__slots__'):
        items = c.__slots__
    else:
        items = vars(c)
    for item in items:
        try:
            attr = getattr(c, item)
            if hasattr(attr, '__dict__') or hasattr(attr, '__slots__'):
                printClass(attr, '%s.%s' % (name, item))
            else:
                print ('%s.%s=%s' % (name, item, repr(attr)))
        except Exception as ex:
            print (name, item, ex)

def Catch(ModuleName, xType, xValue, xTraceback):
   if type(xValue) is tuple:
      RaiseMsg = str(xValue)
      Jotter = "\nException caught in Module: " + ModuleName + \
                  " at line=" + str( xTraceback.tb_lineno) + ", " +\
                  str(xType) + " = " + str(xType) + ": " + RaiseMsg
   else:
      RaiseMsg = str(xValue.args)

      Jotter = "\nException caught in Module: " + ModuleName + \
                  " at line=" + str( xTraceback.tb_lineno) + ", " +\
                  str(xType) + " = " + str(xType.__doc__) + ": " + RaiseMsg

   Jotter += "\n"

   for i in list(traceback.format_tb(xTraceback,50)):
     Jotter += i

   print("\n"+"-"*60)
   print(Jotter)

#   traceback.print_exception(xType, xValue, xTraceback,50)
   return Jotter

# Take the InclusiveAmount and VatPerc and calculate
# the VatAmount and CleanAmount
def CalcInclusiveVatValue(InclusiveAmount, VatPerc, Decimals, type=int):
   try:
      ExclusiveAmount = (InclusiveAmount * 100)
      ExclusiveAmount = ExclusiveAmount / (100.0+VatPerc)
      ExclusiveAmount = round(ExclusiveAmount, Decimals)

      if type == int:
         return (int(ExclusiveAmount), int(InclusiveAmount)-int(ExclusiveAmount) )

   except Exception as strMsg:
      (xType, xValue, xTraceback) = sys.exc_info ()
      Catch(__name__, xType, xValue, xTraceback)
      raise xType(xValue)

def CalcRate(oldRate):
   floatRate = float(oldRate)
   newRate = round(floatRate * 1000000)
   strRate = str(int(newRate))

   return strRate
class QueuereplyExp(BaseException):
   def __init__(self, aQueue, aReply):
      self.Queue = aQueue
      self.Reply = aReply
      self.Message = 'Route To ('+aQueue+') Reply (' + aReply + ')'
      print (self.Message)
   def __str__(self):
      return self.Message

def ExcErrorMsg(QueueName, ErrorMessage):
   raise QueuereplyExp(str(QueueName), str(ErrorMessage))
#   route(str(ExcID))
#   reply(str(ExcMsg))
#   commit()
#   raise Exception, ExcMsg

def WasteReport(Waste):

   d = {}
   d['Waste.TransDate'] = Waste.TransDate
   value = float(Waste.AmountInCents)
   Amount = round(value/100.0, 2)
   Amt = "%.2f" %(Amount)
   d['Waste.AmountInCents'] = Amt
   d['Waste.AccNo'] = Waste.AccNo
   d['Waste.TransCode'] = Waste.TransCode
   x = xmlbuild(d)

   print(x)
   saveSummary(xmlbuild(d))
   n = xmlparse(x)
   printDict(n)

def TibosReport(msg, Type):

   d = {}

   d['Tibos.BrnNo'] = msg.BrnNo
   d['Tibos.TranCde'] = msg.TranCde
   d['Tibos.TranDate'] = msg.TranDate

   if Type == 'BJ' or Type == 'AS':
      d['Tibos.AccNo'] = msg.AccNo

   if Type != 'DR':
      d['Tibos.CcyCode'] = msg.CcyCde

   if Type == 'DR':
      d['Tibos.ContrNo'] = msg.ContrNo
      d['Tibos.PurchCcyCde'] = msg.PurchCcyCde
      d['Tibos.SaleCcyCde'] = msg.SaleCcyCde

   if Type == 'AS':
      d['Tibos.DueDate'] = msg.DueDate

   if Type != 'AJ':
      d['Tibos.ExchRte'] = msg.ExchRte
      value = float(msg.ZARAmt)
      Amount = round(value/100.0, 2)
      Amt = "%.2f" %(Amount)
      d['Tibos.ZARAmt'] = Amt

   if Type == 'BJ' or Type == 'AS':
      value = float(msg.ForeignAmt)
      Amount = round(value/100.0, 2)
      Amt = "%.2f" %(Amount)
      d['Tibos.ForeignAmt'] = Amt

   if Type == 'DR' or Type == 'AJ':
      d['Tibos.PurchAccNo'] = msg.PurchAccNo
      value = float(msg.PurchAmt)
      Amount = round(value/100.0, 2)
      Amt = "%.2f" %(Amount)
      d['Tibos.PurchAmt'] = Amt
      d['Tibos.SaleAccNo'] = msg.SaleAccNo
      value = float(msg.SaleAmt)
      Amount = round(value/100.0, 2)
      Amt = "%.2f" %(Amount)
      d['Tibos.SaleAmt'] = Amt

   if Type == 'DR' or Type == 'BJ':
      d['Tibos.TranValDate'] = msg.TranValDate

   x = xmlbuild(d)

   print(x)
   saveSummary(xmlbuild(d))
   n = xmlparse(x)
   printDict(n)

def BuildReply(Type, Swift):
  try:
    r = {}
    r['REPLY.TYPE'] = Type
    r['REPLY.SWIFT'] = Swift
    s = xmlbuild(r)
    reply(s)

  except Exception as strMsg:
    (xType, xValue, xTraceback) = sys.exc_info ()
    Catch(__name__, xType, xValue, xTraceback)
    raise xType(xValue)

def BuildReplyBop(RecBank, CorrBank):
  try:
    r = {}
    r['BOP.RECBANK'] = RecBank
    r['BOP.CORRBANK'] = CorrBank
    s = xmlbuild(r)
    reply(s)

  except Exception as strMsg:
    (xType, xValue, xTraceback) = sys.exc_info ()
    Catch(__name__, xType, xValue, xTraceback)
    raise xType(xValue)

def CheckSwiftUsingEnv(Swift):

   if env == 0:
      TestSwift = Swift[:7] + '0'
      print("Changing Swift Address from ", Swift, " to ", TestSwift)
      return TestSwift
   else:
      return Swift

class DiaryTranExp:
   def __init__(self, aQueue):
      self.Queue = aQueue
      self.args =  'Route '+aQueue
   def __str__(self):
      return self.args

class DictHandler(xml.sax.ContentHandler):
    def __init__(self, mem_char='.', att_char='/', list_char='%', use_lists=False):
        self.tags = []
        self.dnames = []
        self.tags_kv = {}
        self.tags_value = {}
        self.result = {}
        self.mem_char = mem_char;
        self.att_char = att_char;
        self.list_char = list_char;
        self.use_lists = use_lists
    def startElement(self, name, attrs):
        self.tags.append(name)
        self.last_started = name
        self.tags_kv[name] = []
        self.tags_value[name] = []
        for attr in attrs.getNames():
            self.tags_kv[name].append((attr, attrs.getValue(attr)))
    def endElement(self, name):
        if self.last_started != name and self.tags_value[name] == [] and self.tags_kv[name] == []:
            self.tags.pop()
            return
        def _make_key(name, no):
            n = name.rfind('.')
            if n < 1:
                pname = '%s%s%d' % (name, self.list_char, no)
            else:
                pname = '%s%s%d%s' % (name[:n], self.list_char, no, name[n:])
            return pname
        def _add_value(result, name, no, value):
            if no > 0 or name in result:
                if self.use_lists:
                    if not isinstance(result[name], list):
                        prev_value = result[name]
                        result[name] = [prev_value]
                    result[name].append(value)
                elif no > 0:
                    if no == 1:
                        result[_make_key(name, 0)]=result.pop(name)
                    result[_make_key(name, no)]=value
                else:
                    result[name]=value 
            else:
                result[name]=value 
        dname = self.tags[0]
        for tag in self.tags[1:]:
            dname += self.mem_char + tag
        no = self.dnames.count(dname)
        self.dnames.append(dname)
        self.tags.pop()
        value = ''
        nl = ''
        for line in self.tags_value[name]:
            value += nl + line
            nl = '\n'
        _add_value(self.result, dname, no, value)
        if name in self.tags_kv:
            for k, v in self.tags_kv[name]:
                aname = dname+self.att_char+k
                _add_value(self.result, aname, no, v)
    def characters(self, content):
        store = content.strip()
        if len(store) > 0:
            name = self.tags[-1]
            self.tags_value[name].append(store)

def xml_to_dict(xml_data, lists=False):
    '''
    Similar to xmlparse, but if use_lists is True (default is False)
    it returns duplicate tags as arrays
    but be aware that duplicate tag groups should have the same named
    sub tags to keep the array elements consistant.
    '''
    try:
        handler = DictHandler()
        handler.use_lists = lists
        xml.sax.parseString(xml_data, handler)
        return handler.result
    except:
        return None

def _build_yaml_attrib(attribs_dict, key_name, pad):
    attrib = []
    attrib.append('%sAttributes:' % (pad))
    for key, value in attribs_dict[key_name]:
        attrib.append("%s%s: '%s'" % (pad+'  ', key, value))
    return attrib

def _build_yaml(classes_dict, attribs_dict, key_name, done, pad=''):
    entry = []
    if key_name in attribs_dict:
        attribs = _build_yaml_attrib(attribs_dict, key_name, pad)
        entry.extend(attribs)
    for field_name, field_value in classes_dict[key_name]:
        sub_key_name = key_name + '.' + field_name
        if sub_key_name in classes_dict: 
            if not sub_key_name in done:
                sub_entry = _build_yaml(classes_dict, attribs_dict, sub_key_name, done, pad+'    ')
                entry.append('%s%s:' % (pad, field_name.replace('%', '_')))
                entry.extend(sub_entry)
                done.append(sub_key_name)
        else:
            entry.append('%s%s: %s' % (pad, field_name.replace('%', '_'), field_value))
    return entry

def _build_json_attrib(attribs_dict, group_name):
    attrib = {}
    for field, value in attribs_dict[group_name]:
        attrib[field]=value
    return attrib

def _build_json(classes_dict, attribs_dict, group_name, done):
    group = {}
    if group_name in attribs_dict:
        attribs = _build_json_attrib(attribs_dict, group_name)
        group['Attributes'] = attribs
    for field_name, field_value in classes_dict[group_name]:
        sub_group_name = group_name + '.' + field_name
        if sub_group_name in classes_dict: 
            if not sub_group_name in done:
                sub_group = _build_json(classes_dict, attribs_dict, sub_group_name, done)
                group[field_name.replace('%', '_')] = sub_group
                done.append(sub_group_name)
        else:
            group[field_name.replace('%', '_')] = field_value
    return group

def _class_slots(classes_dict, attribs_dict, module_name):
    slots = []
    for field,_ in classes_dict[module_name]:
        dfield = field.replace('%','_')
        if not dfield in slots:
            slots.append(dfield)
    return slots

def _attrib_slots(attribs_dict, module_name):
    slots = []
    for name, value in attribs_dict[module_name]:
        if not name in slots:
            slots.append(name)
    return slots

class Class: pass

def _build_rec_attrib(attribs_dict, module_name):
    attrib = Class()
    attrib.__slots__ = _attrib_slots(attribs_dict, module_name)
    for field, value in attribs_dict[module_name]:
        setattr(attrib, field, value)
    return attrib

def _build_rec(classes_dict, attribs_dict, module_name, done):
    module = Class()
    module.__slots__ = _class_slots(classes_dict, attribs_dict, module_name)
    if module_name in attribs_dict:
        attrib = _build_rec_attrib(attribs_dict, module_name)
        module.__slots__.append('Attributes')
        setattr(module, 'Attributes', attrib)
    for field_name, field_value in classes_dict[module_name]:
        sub_module_name = module_name + '.' + field_name
        if sub_module_name in classes_dict: 
            if not sub_module_name in done:
                sub_module = _build_rec(classes_dict, attribs_dict, sub_module_name, done)
                setattr(module, field_name.replace('%','_'), sub_module)
                done.append(sub_module_name)
        else:
            setattr(module, field_name.replace('%','_'), field_value)
    return module

def _clear_sub_marker(field):
    n = field.find('%')
    if n > 0:
        return field[:n]
    return field

def _build_xml(classes_dict, attribs_dict, tag_name, done, pad=''):
    lines = []
    attribs = ''
    if tag_name in attribs_dict:
        for field, value in attribs_dict[tag_name]:
            attribs += ' %s=%s' % (field, repr(value))
    tags = tag_name.split('.')
    start_tag = '%s<%s%s>' % (pad, _clear_sub_marker(tags[-1]), attribs)
    end_tag = '%s</%s>' % (pad, _clear_sub_marker(tags[-1])) 
    lines.append(start_tag)
    for field_name, field_value in classes_dict[tag_name]:
        sub_tag_name = tag_name + '.' + field_name
        if sub_tag_name in classes_dict:
            if not sub_tag_name in done:
                sub_lines = _build_xml(classes_dict, attribs_dict, sub_tag_name, done, pad + '    ')
                lines.extend(sub_lines)
                done.append(sub_tag_name)
        else:
            lines.append('{0}<{1}>{2}</{1}>'.format(pad + '    ', field_name, field_value))
    lines.append(end_tag)
    return lines

def _check_attribs(key, name, value, attribs_dict):
    if len(name) > 0:
        if not key in attribs_dict:
            attribs_dict[key] = []
        attribs_dict[key].append((name, value))

def load_in_dicts(input):
    classes_dict = {}
    start_module = ''
    done = []
    attribs_dict = {}
    for input_key in input:
        input_value = input[input_key]
        attrib_name = ''
        n = input_key.find('/')
        if n != -1:
            attrib_name = input_key[n + 1:]
            input_key = input_key[:n]
        parts = input_key.split('.')
        if len(parts) == 1:
            _check_attribs(input_key, attrib_name, input_value, attribs_dict)
            continue
        if parts[0] != start_module:
            start_module = parts[0]
        class_key = ''
        attrib_key = ''
        for i in range(len(parts) - 1):
            class_key += parts[i]
            class_field = parts[i + 1]
            attrib_key = class_key + '.' + class_field
            if class_key not in classes_dict:
                classes_dict[class_key] = []
            if class_field not in classes_dict[class_key]:
                classes_dict[class_key].append((class_field, input_value))
            class_key += '.'
        _check_attribs(attrib_key, attrib_name, input_value, attribs_dict)
    return start_module, classes_dict, attribs_dict

def dict_to_rec(input_dict):
    '''
    Returns a dynamic class rec instance of the dictionary.
	d['Aaa.Bbb']=12 translates to Aaa.Bbb with a value of 12
	(getattr, setattr and hasattr -- could be useful)
    '''
    done = []
    start_name, classes_dict, attribs_dict = load_in_dicts(input_dict)
    return _build_rec(classes_dict, attribs_dict, start_name, done)

def dict_to_xml(input_dict):
    '''
	Returns a string representing the xml. Drops %[0-9]+
	for duplicate tags. Does not use xmlrecord - pure python.
    '''
    done = []
    start_name, classes_dict, attribs_dict = load_in_dicts(input_dict)
    lines = _build_xml(classes_dict, attribs_dict, start_name, done)
    return '\n'.join(lines)

def dict_to_json(input_dict):
    '''
	Returns a string in json format translates %[0-9] to _[0-9]
	for duplicate tags.
    '''
    done = []
    start_name, classes_dict, attribs_dict = load_in_dicts(input_dict)
    return repr(_build_json(classes_dict, attribs_dict, start_name, done)).replace("'", '"')

def dict_to_yaml(input_dict):
    '''
	Returns a string in json format translates %[0-9] to _[0-9]
	for duplicate tags.
    '''
    done = []
    start_name, classes_dict, attribs_dict = load_in_dicts(input_dict)
    lines = _build_yaml(classes_dict, attribs_dict, start_name, done)
    result = '%YAML 1.2\n---\n'
    for line in lines:
        result += line + '\n'
    return result
