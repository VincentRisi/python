#pragma once

struct Book
{
    const char* filename;
    const char* atppi;
    const char* atpst;
    const char* atpti;
    const char* sti;
    const char* aacr;
    const char* aart;
    const char* atnu;
    const char* cdek;
    const char* cdet;
    const char* cprt;
    const char* guid;
    const char* prid;
    const char* released;
    const char* vers;
    const char* album;
    const char* author;
    const char* comment;
    const char* atday;
    const char* genre;
    const char* name;
    const char* narrator;
    const char* publisher;
    const char* trkn;
};
const char* book_fields = "filename|atppi|atpst|atpti|sti|aacr|aart|atnu|cdek|cdet|cprt|guid|prid|released|vers|album|author|comment|atday|genre|name|narrator|publisher|trkn";
enum BookFields
{
    filename,
    atppi,
    atpst,
    atpti,
    sti,
    aacr,
    aart,
    atnu,
    cdek,
    cdet,
    cprt,
    guid,
    prid,
    released,
    vers,
    album,
    author,
    comment,
    atday,
    genre,
    name,
    narrator,
    publisher,
    trkn,
    BookFieldsCount
};
