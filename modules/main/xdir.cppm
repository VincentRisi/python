
export module xdir;
import machine;
import <cstdio>;
import <cstdlib>;
import <cstring>;
import xcstring;

export constexpr int DIRMAX_PATH = _MAX_PATH;
export constexpr int DIRMAX_DIR  = _MAX_DRIVE + _MAX_DIR;
export constexpr int DIRMAX_NAME = _MAX_FNAME;
export constexpr int DIRMAX_EXT  = _MAX_EXT;

//  splits path into user supplied memory for dir, name and ext 
export void FNameSplit(const char *path, char *dir, char *name, char *ext)
{
#if defined (__GNUC__) || defined (__clang__)
  char *p = strrchr((char*)path, '/');
  char *p2;

  if (p)
  {
    strncpyz(dir, path, (p-path)+1);
    p++;
  }
  else
  {
    dir[0] = 0;
    p = (char*)path;
  }
  p2 = strrchr(p+1, '.');
  if (p2)
  {
    strncpyz(name, p, p2-p);
    strcpy(ext, p2);
  }
  else
  {
    strcpy(name, p);
    ext[0] = 0;
  }
#else 
  char drive[_MAX_DRIVE], dir2[_MAX_DIR];
  _splitpath(path, drive, dir2, name, ext);
  strcpy(dir, drive);
  strcat(dir, dir2);
#endif  
}

//  merges dir, name and ext into user supplied memory for path
export void FNameMerge(char* path, const char* dir, const char* name, const char* ext)
{
#if defined (__GNUC__) || defined (__clang__)
  int i;
  if (dir)
  {
    strcpy(path, dir);
    if ((i=strlen(dir)) && (dir[i-1] != '/'))
      strcat(path, "/");
  }
  if (name)
    strcat(path, name);
  if (ext)
  {
    if (strlen(ext) && *ext != '.')
      strcat(path, ".");
    strcat(path, ext);
  }
#else
  _makepath(path, "", dir, name, ext);
  for (size_t i=0; i<strlen(path); i++)
    if (path[i] == '/') path[i] = '\\';
#endif
}
