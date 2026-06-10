export module xmlmake;
import machine;
import addlist;
import <exception>;
import <iostream>;
import <format>;
import <print>;

using namespace std;
export enum EXMLMake
{
   errxmlEROK,
   errxmlAttr,
   errxmlName,
   errxmlNull,
   errxmlTopNotSame,
   errxmlAlreadyLoaded
};

const char* XMLError[] =
{ "OK"
, "Null Pointer passed"
, "Tag Name not specified"
, "Attr Name not specified"
, "The Top Element is not the same"
, "Load has already been done"
};


export struct XXMLMake : public exception
{
  static const char* getText(int err)
  {
    return XMLError[err];
  }
  XXMLMake(const char* file, const int line, int error)
  {
    println("XMLMake {} {} : {}", file, line, error, getText(error));
  }
  XXMLMake(const XXMLMake& aX)
  {
  }
};

export struct ArrayPair
{
  int no;
  int of;
  ArrayPair(int n=0, int o=1)
  {
    no = n;
    of = o;
  }
  ArrayPair(ArrayPair &x)
  {
    no = x.no;
    of = x.of;
  }
};

export struct XMLBase
{
  char *Name;
  XMLBase(const char *AName)
  {
    if (!strlen(AName))
      throw XXMLMake(__FILE__, __LINE__, errxmlAttr);
    Name = new char[strlen(AName)+1];
    strcpy(Name, AName);
  }
  virtual ~XMLBase()
  {
    delete [] Name;
  }
};

export struct XMLAttribute : public XMLBase
{
  char *Value;
  XMLAttribute(const char *AName, const char *AValue)
  : XMLBase(AName)
  {
    Value = new char[strlen(AValue)+1];
    strcpy(Value, AValue);
  }
  virtual ~XMLAttribute()
  {
    delete[] Value;
  }
  void AddValue(const char *AValue)
  {
    char* oldValue = Value;
    Value = new char[strlen(oldValue)+strlen(AValue)+2];
    strcpy(Value, oldValue);
    strcat(Value, ";");
    strcat(Value, AValue);
    delete [] oldValue;
  }
};

export struct XMLElement : public XMLBase
{
  TAddList<char*, int> Values;
  TAddList<XMLAttribute*, int> Attributes;
  TAddList<XMLElement*, int> Elements;
  XMLElement *Parent;
  long ElementIndex, AttrIndex, ValueIndex;
  ArrayPair arrayPair;  // zero based
  XMLElement(const char *AName, const char *AValue=0)
  : XMLBase(AName)
  , Values(4)
  , Attributes(4)
  , Elements(8)
  , Parent(0)
  {
    if (AValue)
      AddValue(AValue);
  }
  virtual ~XMLElement()
  {
    int n;
    if ((n = Values.getCount()) > 0)
    {
      for (int i=0; i < n; i++)
        delete [] Values[i];
      Values.clear();
    }
    if ((n = Attributes.getCount()) > 0)
    {
      for (int i=0; i < n; i++)
        delete Attributes[i];
      Attributes.clear();
    }
    if ((n = Elements.getCount()) > 0)
    {
      for (int i=0; i < n; i++)
        if (Elements[i])
          delete Elements[i];
      Elements.clear();
    }
  }
  void AddValue(const char *AValue)
  {
    int nlCount=0;
    AddValue(AValue, nlCount);
  }
  void AddValue(const char *AValue, int &nlCount)
  {
    char *Value;
    int n=strlen(AValue);
    int last = Values.getCount()-1;
    if (last == -1)
    {
      Value = new char[n+1];
      strcpy(Value, AValue);
      Values.add(Value);
      return;
    }
    if (n == 1 && strchr("\n", *AValue) != 0)
    {
      Value = new char[1];
      Value[0] = 0;
      Values.add(Value);
      return;
    }
    int m = strlen(Values[last]);
    Value = new char[m+n+nlCount+1];
    strcpy(Value, Values[last]);
    for (int i=0; i<nlCount; i++)
      strcat(Value, "\n");
    nlCount = 0;
    strcat(Value, AValue);
    delete [] Values[last];
    Values[last] = Value;
  }
  void AddAttribute(XMLAttribute *AAttribute)
  {
    Attributes.add(AAttribute);
  }
  void AddElement(XMLElement *AElement)
  {
    for (int i=0; i<Elements.getCount(); i++)
    {
      if (stricmp(Elements[i]->Name, AElement->Name) == 0)
      {
        Elements[i]->arrayPair.of++;
        AElement->arrayPair.no++;
        AElement->arrayPair.of = Elements[i]->arrayPair.of;
      }
    }
    Elements.add(AElement);
    AElement->Parent = this;
  }
  XMLElement *FindElement(char *AName, ArrayPair &arrayPair)
  {
    for (int i=0; i < Elements.getCount(); i++)
    {
      if (stricmp(AName, Elements[i]->Name) == 0)
      {
        arrayPair.of = Elements[i]->arrayPair.of;
        if (arrayPair.no == Elements[i]->arrayPair.no)
          return Elements[i];
      }
    }
    return 0;
  }
  XMLAttribute *FindAttribute(char *AName)
  {
    for (int i=0; i < Attributes.getCount(); i++)
      if (stricmp(AName, Attributes[i]->Name) == 0)
        return Attributes[i];
    return 0;
  }
};
