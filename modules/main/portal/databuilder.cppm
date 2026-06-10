export module databuilder;
import machine;

export class DataBuilder
{
public:
    virtual void name(const char *inName) = 0;

    virtual void add(const char *name, const int8    value) = 0;
    virtual void addByte(const char *name, const int8 value) = 0;
    virtual void addByte(const char *name, const int8 *value, const size_t size) = 0;
    virtual void add(const char *name, const int16   value) = 0;
    virtual void add(const char *name, const int32   value) = 0;
    virtual void add(const char *name, const int64   value) = 0;
    virtual void add(const char *name, const char   *value) = 0;
    virtual void add(const char *name, const size_t len, const unsigned char *value) = 0;
    virtual void add(const char *name, const double  value) = 0;

    virtual void add(const char *name, const int8    value, const int16 isNull) = 0;
    virtual void addByte(const char *name, const int8 value, const int16 isNull) = 0;
    virtual void addByte(const char *name, const int8 *value, const size_t size, const int16 isNull) = 0;
    virtual void add(const char *name, const int16   value, const int16 isNull) = 0;
    virtual void add(const char *name, const int32   value, const int16 isNull) = 0;
    virtual void add(const char *name, const int64   value, const int16 isNull) = 0;
    virtual void add(const char *name, const char   *value, const int16 isNull) = 0;
    virtual void add(const char *name, const size_t len, const unsigned char *value, const int16 isNull) = 0;
    virtual void add(const char *name, const double  value, const int16 isNull) = 0;

    virtual void set(const char *name, int8   &value, const size_t size) = 0;
    virtual void setByte(const char *name, int8 &value, const size_t size) = 0;
    virtual void setByte(const char *name, int8 *value, const size_t size) = 0;
    virtual void set(const char *name, int16  &value, const size_t size) = 0;
    virtual void set(const char *name, int32  &value, const size_t size) = 0;
    virtual void set(const char *name, int64  &value, const size_t size) = 0;
    virtual void set(const char *name, char   *value, const size_t size) = 0;
    virtual void set(const char *name, int &len, unsigned char *value, const size_t size) = 0;
    virtual void set(const char *name, double &value, const size_t size) = 0;

    virtual void set(const char *name, int8   &value, const size_t size, int16 &null) = 0;
    virtual void setByte(const char *name, int8 &value, const size_t size, int16 &null) = 0;
    virtual void setByte(const char *name, int8 *value, const size_t size, int16 &null) = 0;
    virtual void set(const char *name, int16  &value, const size_t size, int16 &null) = 0;
    virtual void set(const char *name, int32  &value, const size_t size, int16 &null) = 0;
    virtual void set(const char *name, int64  &value, const size_t size, int16 &null) = 0;
    virtual void set(const char *name, char   *value, const size_t size, int16 &null) = 0;
    virtual void set(const char *name, int &len, unsigned char *value, const size_t size, int16 &null) = 0;
    virtual void set(const char *name, double &value, const size_t size, int16 &null) = 0;

};
