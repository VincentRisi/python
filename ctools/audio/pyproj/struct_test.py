'''
int32 JulDate(int16 day, int16 month, int16 year)
{
  int32 lYear, lMonth, lDay, lCentury, lCy;

  lDay = day;
  if (year < 1)
    year = 1;
  lYear = year;

  if (month > 2)
    lMonth = month - 3;
  else
  {
    lMonth = month + 9;
    lYear = year - 1;
  }
  lCentury = lYear / 100;
  lCy = lYear - 100 * lCentury;
  return (146097 * lCentury) / 4 + (1461 * lCy) / 4 + (153 * lMonth + 2) / 5 + lDay + 1721119;
}
'''

def juldate(day, month, year):
    if year < 1:
        year = 1
    if month > 2:
        month -= 3
    else:
        month += 9
        year -= 1
    century = year / 100
    cy = year - 100 * century
    return (146097 * century) / 4 + (1461 * cy) / 4 + (153 * month + 2) / 5 + day + 1721119


lyn = int(juldate(17, 6, 1953))
vince = int(juldate(7, 6, 1949))
now = int(juldate(8, 3, 2023))
print ((now - vince) / 29.5)
print ((now - lyn) / 29.5)

