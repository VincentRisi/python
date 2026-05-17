export module date;
import machine;
import <cstdio>;
import <corecrt.h>;
import <time.h>;

//using uchar = unsigned char;
//using pchar = char*;

// The leapYear function determines whether a given year is a leap year according to 
// the rules of the Gregorian calendar.

export bool leapYear(int year)
{
  if ((year % 400) == 0)
    return (true);
  if ((year % 100) == 0)
    return (false);
  if ((year % 4) == 0)
    return (true);
  return (false);
}

// The following functions are based on the algorithm described in "Calendrical Calculations" by Reingold and Dershowitz.
// originally published in "Communications of the ACM" in 1992. 
// The algorithm is designed to be efficient and accurate for a wide range of dates, including those in the distant past and future.
// The gregDateToDays function converts a given Gregorian date (day, month, year) into the number of days 
// since a fixed reference point (January 1, 4713 BC). In error called this function "Julian Day Number", but it is not the same 
// as the Julian Day Number used in astronomy, which counts days from a different reference point (January 1, 4713 BC at noon). 
// The algorithm accounts for leap years and the varying number of days in each month to ensure accurate conversion.

export int gregDateToDays(int day, int month, int year)
{
  int lYear, lMonth, lDay, lCentury, lCy;

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

// The gregDaysToDate function performs the inverse operation, converting a given number of days since the reference point 
// back into a Gregorian date (day, month, year).

export void gregDaysToDate(int gregDays, int& day, int& month, int& year)
{
  int lTemp = gregDays - 1721119;
  int lYear, lMonth, lDay;
  lYear = (4 * lTemp - 1) / 146097;
  lTemp = 4 * lTemp - 1 - 146097 * lYear;
  lDay = lTemp / 4;
  lTemp = (4 * lDay + 3) / 1461;
  lDay = 4 * lDay + 3 - 1461 * lTemp;
  lDay = (lDay + 4) / 4;
  lMonth = (5 * lDay - 3) / 153;
  lDay = 5 * lDay - 3 - 153 * lMonth;
  lDay = (lDay + 5) / 5;
  lYear = 100 * lYear + lTemp;

  if (lMonth < 10)
    lMonth += 3;
  else
  {
    lMonth -= 9;
    lYear++;
  }
  day = (int)lDay;
  month = (int)lMonth;
  year = (int)lYear;
}

// The currentDate function retrieves the current date from the system 
// and formats it as an integer in the format YYYYMMDD.

export int currentDate()
{
  time_t tt;
  struct tm* lt;

  time(&tt);
  lt = localtime(&tt);
  return (19000000L + 10000L * (int)lt->tm_year + 100L * ((int)lt->tm_mon + 1) + (int)lt->tm_mday);
}

// The currentTime function retrieves the current time from the system
// and formats it as an integer in the format HHMMSS.

export int currentTime()
{
  time_t tt;
  struct tm* lt;

  time(&tt);
  lt = localtime(&tt);
  return (10000L * (int)lt->tm_hour + 100L * ((int)lt->tm_min) + (int)lt->tm_sec);
}

// The fromOracleDate function converts an Oracle date, 
// represented as a 7-byte array, into an integer in the format YYYYMMDD.

export int fromOracleDate(uchar* oradate)
{
  int date;
  date = (int)(oradate[0] - 100) * 1000000L + (int)(oradate[1] - 100) * 10000L;
  if (date >= 0)
    date += ((int)oradate[2] * 100L + (int)oradate[3]);
  else
    date -= ((int)oradate[2] * 100L + (int)oradate[3]);
  return date;
}

// The toOracleDate function converts a date represented as an integer in the format YYYYMMDD 
// and an optional time in the format HHMMSS

export void toOracleDate(uchar* oradate, int yyyymmdd, int hhmmss)
{
  int BC = yyyymmdd < 0;
  if (hhmmss)
  {
    oradate[6] = (uchar)(hhmmss % 100);
    hhmmss /= 100;
    oradate[5] = (uchar)(hhmmss % 100);
    hhmmss /= 100;
    oradate[4] = (uchar)(hhmmss % 100);
  }
  else
    oradate[6] = oradate[5] = oradate[4] = 1;
  if (BC)
    yyyymmdd = -yyyymmdd;
  oradate[3] = (uchar)(hhmmss % 100);
  yyyymmdd /= 100;
  oradate[2] = (uchar)(hhmmss % 100);
  yyyymmdd /= 100;
  oradate[1] = (uchar)(hhmmss % 100);
  yyyymmdd /= 100;
  oradate[0] = (uchar)(hhmmss % 100);
  if (BC)
  {
    oradate[1] = 100 - oradate[1];
    oradate[0] = 100 - oradate[0];
  }
  else
  {
    oradate[1] += 100;
    oradate[0] += 100;
  }
}

// The gregDaysToOracle function converts a given number of days since the reference point
// into an Oracle date string in the format YYYYMMDD.

export pchar gregDaysToOracle(int aGregDays, pchar aOracleDate)
{
  int day, month, year;
  gregDaysToDate(aGregDays, day, month, year);
  snprintf(aOracleDate, 8, "%04d%02d%02d", year, month, day);
  return aOracleDate;
}
