
export module xdir;
import machine;
import <cstdio>;
import <cstdlib>;
import <cstring>;
import xcstring;

export const int DIRMAX_PATH = _MAX_PATH;
export const int DIRMAX_DIR  = _MAX_DRIVE + _MAX_DIR;
export const int DIRMAX_NAME = _MAX_FNAME;
export const int DIRMAX_EXT  = _MAX_EXT;

//  splits path into user supplied memory for dir, name and ext 
export void FNameSplit(const char *path, char *dir, char *name, char *ext)
{
#if defined (__GNUC__)
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
#if defined (__GNUC__)
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

//  returns strdup of name part of path (user must free) 
//export char *FNameName(char *Path)
//{
//  char Dir[DIRMAX_DIR];
//  char Name[DIRMAX_NAME];
//  char Ext[DIRMAX_EXT];
//
//  FNameSplit(Path, Dir, Name, Ext);
//  return strdup(Name);
//}

//  returns strdup of dir part of path (user must free)
//export char *FNameDir(char *Path)
//{
//  char Dir[DIRMAX_DIR];
//  char Name[DIRMAX_NAME];
//  char Ext[DIRMAX_EXT];
//
//  FNameSplit(Path, Dir, Name, Ext);
//  return strdup(Dir);
//}

//  returns strdup of ext part of path (user must free)
//export char *FNameExt(char *Path)
//{
//  char Dir[DIRMAX_DIR];
//  char Name[DIRMAX_NAME];
//  char Ext[DIRMAX_EXT];
//
//  FNameSplit(Path, Dir, Name, Ext);
//  return strdup(Ext);
//}

//  returns static area containing path if found else empty string
//  is kept between calls to FNameFind.
//export char *FNameFind(char *File, char *Env)
//{
//  static char Path[DIRMAX_PATH];
//  char Dir[DIRMAX_DIR];
//  char Name[DIRMAX_NAME];
//  char Ext[DIRMAX_EXT];
//  char *EnvData, *p1, *p2;
//  int size;
//
//  // if File exists as is, return it
//  if (access(File, 0) == 0)
//  {
//    strcpy(Path, File);
//    return Path;
//  }
//
//  FNameSplit(File, Dir, Name, Ext);
//  if (strlen(Dir))
//  {
//    strcpy(Path,"");
//    return Path;
//  }
//
//  EnvData = getenv(Env);
//  p1 = EnvData;
//  while (p1)
//  {
//    p2 = strchr(p1, PATH_DELIM);
//    if (p2)
//    {
//      size = p2 - p1;
//      strncpy(Dir, p1, size);
//      Dir[size]=0;
//      p2++;
//    }
//    else
//      strcpy(Dir, p1);
//    p1 = p2;
//    FNameMerge(Path, Dir, Name, Ext);
//
//    // if file exists on path for environment variable Env, return it
//    if (access(Path, 0) == 0)
//      return Path;
//  }
//  strcpy(Path, "");
//  return Path;
//}
