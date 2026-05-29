export module splits;
import <cstdio>;
import <cstdlib>;
import <string.h>;
import <malloc.h>;

import xcstring;

export typedef struct Splits
{
  char* readbuff;
  char* writebuff;
  char* workbuff;
  char** flds;
  char* next;
  size_t left;
  int fldc;
  int no_flds;
  int error_no;
  int last_no;
} Splits;

export char* splits(const char *readbuff, char delim, int fldc, const char** flds, int *no_flds)
{
  int i,j,n,m,q,s,d;
  char* result = strdup(readbuff); // "a|b|c0" 0 is the null
  n = strlen(result);              // n=5
  while (result[n - 1] == '\n' || result[n - 1] == '\r')
    result[--n] = 0;
  strtrim(result);
  s = d = q = 0;
  for (i=0; i<n; i++)
  {
    q++;
    // if first char is single quote s == 1
    if (q == 1 && result[i] == '\'')
    {
      s = 1;
      continue;
    }
    // if first char is double quote d == 1
    if (q == 1 && result[i] == '"')
    {
      d = 1;
      continue;
    }
    // if looking for and find single quote s == 0
    if (s == 1 && result[i] == '\'')
    {
      s = 0;
      continue;
    }
    // if looking for and find double quote d == 0
    if (d == 1 && result[i] == '"')
    {
      d = 0;
      continue;
    }
    // if in looking for single or double quote
    if (s == 1 || d == 1)
      continue;
    // not looking for quotes check if delimiter
    if (result[i] == delim)
    {
      result[i] = 0;           // "a0b0c0"
      s = d = q = 0;
    }
  }
  for (i=0; i<fldc; i++)
    flds[i] = &result[n];      // assuming arg=3 all three point to last null terminator 
  flds[0] = result;            // "a0"
  for (i=1,j=0; i<fldc; i++,j++)  
  {
    m = strlen(flds[j])+1;     // m=2:m=2:m=2
    n -= m;                    // n=3:n=1:n=-1
    if (n < 1) 
      break;
    flds[i]=flds[j]+m;          // "b0":"c0" 
  }
  *no_flds = j+1;
  return result;
}

export enum 
{
  _split_ok
, _no_split_ctx
, _split_no_out_of_range
};

export const char* _split_errors[] =
{
  "No error"
  , "No split context available"
  , "Split no out of range"
};

export int splits_init(Splits** ctxp, int fldc)
{
  Splits* ctx = (Splits*) malloc(sizeof(Splits));
  *ctxp = ctx;
  ctx->readbuff = 0;
  ctx->writebuff = 0;
  ctx->next = 0;
  ctx->left = 0;
  ctx->no_flds = fldc;
  ctx->fldc = fldc;
  ctx->flds = (char**)calloc(fldc, sizeof(char*));
  ctx->error_no = 0;
  ctx->last_no = 0;
  return _split_ok;
}

export int splits_done(Splits** ctxp)
{
  Splits* ctx = *ctxp;
  free(ctx->flds);
  if (ctx->readbuff != 0)
    free(ctx->readbuff);
  if (ctx->writebuff != 0)
    free(ctx->writebuff);
  free(ctx);
  ctx = 0;
  return _split_ok;
}


export int splits_read(Splits* ctx, const char* data, char delim)
{
  if (ctx == 0)
    return _no_split_ctx;
  if (ctx->readbuff != 0)
    free(ctx->readbuff);
  if (ctx->writebuff != 0)
  {
    free(ctx->writebuff);
    ctx->writebuff = 0;
  }
  ctx->last_no = 0;
  ctx->no_flds = 0;
  ctx->readbuff = splits(data, delim, ctx->fldc, (const char**)ctx->flds, &ctx->no_flds);
  return ctx->error_no = _split_ok;
}

export struct auto_splits_make
{
  int len;
  char* data;
  auto_splits_make(size_t len) { data = new char[len]; this->len = len; }
  ~auto_splits_make() 
  { 
    delete [] data;
  }
  char* check(char* value, char* del)
  {
    if (value == 0)
      return (char*) "";
    if (value[0] == '"' || value[0] == '\'')
      return value;
    if (strchr(value, del[0]) == 0)
    {
      if (value[0] != '0')
        return value;
      int cnt = strspn(value, "0123456789");
      if (cnt != strlen(value))
        return value;
    }
    snprintf(data, len, "\"%s\"", value);
    return data;
  }
};

export int splits_make(Splits* ctx, char* line, size_t line_len, char delim)
{
  int i, n;
  char del[2];
  del[0]=delim;
  del[1]=0;
  if (ctx == 0)
    return _no_split_ctx;
  n = line_len;
  auto_splits_make work(n);
  strncpy(line, work.check(ctx->flds[0], del), n);
  for (i=1; i<ctx->no_flds; i++)
  {
    strcat(line, del);
    n = line_len - strlen(line);
    strncat(line, work.check(ctx->flds[i], del), n);
  }
  return _split_ok;
}

static const size_t _writebuff_size_ = 4096;

static char* _get_writeBuff_(Splits *ctx)
{
  if (ctx->writebuff == 0)
  {
    ctx->writebuff = (char*) calloc(_writebuff_size_, 1);
    ctx->next = ctx->writebuff;
  }
  else
    ctx->next += strlen(ctx->next) + 1;
  ctx->left = _writebuff_size_ - (ctx->next - ctx->writebuff);
  return ctx->next;
}

export int splits_to_short(Splits* ctx, short* tgt, int no)
{
  if (ctx == 0)
    return _no_split_ctx;
  ctx->last_no = no;
  if (no >= ctx->no_flds)
    return ctx->error_no = _split_no_out_of_range;
  *tgt = (short) atoi(ctx->flds[no]);
  return ctx->error_no = _split_ok;
}

export int splits_as_short(Splits* ctx, short src, int no)
{
  char* tgt;
  if (ctx == 0)
    return _no_split_ctx;
  if (no >= ctx->no_flds)
    return ctx->error_no = _split_no_out_of_range;
  tgt = _get_writeBuff_(ctx);
  snprintf(tgt, ctx->left, "%d", (int)src);
  ctx->flds[no] = tgt;
  return _split_ok;
}

export int splits_to_int(Splits* ctx, int* tgt, int no)
{
  if (ctx == 0)
    return _no_split_ctx;
  ctx->last_no = no;
  if (no >= ctx->no_flds)
    return ctx->error_no = _split_no_out_of_range;
  *tgt = atoi(ctx->flds[no]);
  return ctx->error_no = _split_ok;
}

export int splits_as_int(Splits* ctx, int src, int no)
{
  char* tgt;
  if (ctx == 0)
    return _no_split_ctx;
  if (no >= ctx->no_flds)
    return ctx->error_no = _split_no_out_of_range;
  tgt = _get_writeBuff_(ctx);
  snprintf(tgt, ctx->left, "%d", src);
  ctx->flds[no] = tgt;
  return _split_ok;
}

export int splits_to_long(Splits* ctx, long long* tgt, int no)
{
  if (ctx == 0)
    return _no_split_ctx;
  ctx->last_no = no;
  if (no >= ctx->no_flds)
    return ctx->error_no = _split_no_out_of_range;
  *tgt = atoll(ctx->flds[no]);
  return ctx->error_no = _split_ok;
}

export int splits_as_long(Splits* ctx, long long src, int no)
{
  char* tgt;
  if (ctx == 0)
    return _no_split_ctx;
  if (no >= ctx->no_flds)
    return ctx->error_no = _split_no_out_of_range;
  tgt = _get_writeBuff_(ctx);
  snprintf(tgt, ctx->left, "%lld", src);
  ctx->flds[no] = tgt;
  return _split_ok;
}

export int splits_to_double(Splits* ctx, double* tgt, int no)
{
  if (ctx == 0)
    return _no_split_ctx;
  ctx->last_no = no;
  if (no >= ctx->no_flds)
    return ctx->error_no = _split_no_out_of_range;
  *tgt = atof(ctx->flds[no]);
  return ctx->error_no = _split_ok;
}

export int splits_as_double(Splits* ctx, double src, int no)
{
  char* tgt;
  if (ctx == 0)
    return _no_split_ctx;
  if (no >= ctx->no_flds)
    return ctx->error_no = _split_no_out_of_range;
  tgt = _get_writeBuff_(ctx);
  snprintf(tgt, ctx->left, "%lf", src);
  ctx->flds[no] = tgt;
  return _split_ok;
}

export int splits_as_money(Splits* ctx, double src, int no)
{
  char* tgt;
  if (ctx == 0)
    return _no_split_ctx;
  if (no >= ctx->no_flds)
    return ctx->error_no = _split_no_out_of_range;
  tgt = _get_writeBuff_(ctx);
  snprintf(tgt, ctx->left, "%0.2f", src);
  ctx->flds[no] = tgt;
  return _split_ok;
}

export int splits_to_char(Splits* ctx, char* work, int worklen, int no)
{
  if (ctx == 0)
    return _no_split_ctx;
  ctx->last_no = no;
  if (no >= ctx->no_flds)
    return ctx->error_no = _split_no_out_of_range;
  strncpy(work, ctx->flds[no], worklen-1);
  work[worklen-1] = 0;
  return ctx->error_no = _split_ok;
}

export int splits_as_char(Splits* ctx, char* src, int no)
{
  char* tgt;
  char work[512];
  int n;
  if (ctx == 0)
    return _no_split_ctx;
  if (no >= ctx->no_flds)
    return ctx->error_no = _split_no_out_of_range;
  strncpy(work, src, sizeof(work)-1);
  work[sizeof(work)-1]=0;
  tgt = _get_writeBuff_(ctx);
  n = strlen(src)-1;
  while(work[n] == ' ' || work[n] == '\r' || work[n] == '\t')
  {
    work[n] = 0;
    n--;
  }
  snprintf(tgt, ctx->left, "%s", work);
  ctx->flds[no] = tgt;
  return _split_ok;
}

export const char* splits_error(Splits* ctx)
{
  if (ctx == 0)
    return _split_errors[_no_split_ctx];
  return _split_errors[ctx->last_no];
}

export int splits_last_no(Splits* ctx)
{
  if (ctx == 0)
    return -1;
  return ctx->last_no;
}

export int splits_used(Splits* ctx)
{
  if (ctx == 0)
    return -1;
  return ctx->no_flds;
}

export class Splitter
{
  Splits* ctx;
  int rc;
public:
  /* constructor uses count for max fields to use */
  Splitter(int noFields) { rc = splits_init(&ctx, noFields); }
  virtual ~Splitter() { rc = splits_done(&ctx); }
  const char* error() { return splits_error(ctx); }
  int get_rc() { return rc; }
	char** flds() { return ctx->flds; }
  int no_flds() { return ctx->no_flds; }
  int error_no() { return ctx->error_no; }
  int read(const char* data, char delim) { return rc = splits_read(ctx, data, delim); }
  int make(char* line, size_t line_len, char delim) { return rc = splits_make(ctx, line, line_len, delim); }
  int used() { return rc = splits_used(ctx); }
  int last_no() { return rc = splits_last_no(ctx); }
  int to_short(short* tgt, int no) { return rc = splits_to_short(ctx, tgt, no); }
  int as_short(short src, int no) { return rc = splits_as_short(ctx, src, no); }
  int to_int(int* tgt, int no) { return rc = splits_to_int(ctx, tgt, no); }
  int as_int(int src, int no) { return rc = splits_as_int(ctx, src, no); }
  int to_long(long long* tgt, int no) { return rc = splits_to_long(ctx, tgt, no); }
  int as_long(long long src, int no) { return rc = splits_as_long(ctx, src, no); }
  int to_double(double* tgt, int no) { return rc = splits_to_double(ctx, tgt, no); }
  int as_money(double src, int no) { return rc = splits_as_money(ctx, src, no); }
  int as_double(double src, int no) { return rc = splits_as_double(ctx, src, no); }
  int to_char(char* tgt, int maxlen, int no) { return rc = splits_to_char(ctx, tgt, maxlen, no); }
  int as_char(char* src, int no) { return rc = splits_as_char(ctx, src, no); }
};
