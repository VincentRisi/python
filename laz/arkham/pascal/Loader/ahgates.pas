unit AHGates;
(***
This code uses materials which are the intellectual property of
the Arkham Horror Board Game and expansions.
As such this code cannot be put into the public domain or even
as open source.
***)

{$mode delphi}{$H+}

interface

uses
  Classes, SysUtils, AHTypes;

var
  Gates     : TStringList;

implementation

procedure Add(const aName          : string;
              const aExpansion     : EExpansion;
              const aDescription   : string;
              const aStrength      : integer;
              const aFaction       : eFactionType);
var
  Gate : TGate;
begin
  Gate := TGate.Create;
  with Gate do begin
    name          := aName;
    expansion     := aExpansion;
    description   := aDescription;
    strength      := aStrength;
    faction       := aFaction;
  end;
  Gates.AddObject(aName, Gate);
end;

procedure LoadGates;
begin
  Add('ANOTHER',   EXP_AH, 'Another Dimension',           0, SQUARE);
  Add('CELEANO',   EXP_AH, 'Great Hall of Celeano',      -1, STAR);
  Add('PLATLENG',  EXP_AH, 'Plateau of Leng',            -1, DIAMOND);
  Add('RLYEH',     EXP_AH, 'R''Lyeh',                    -3, CROSS);
  Add('ABYSS',     EXP_AH, 'The Abyss',                  -2, HEX);
  Add('GREATRACE', EXP_AH, 'The City of the Great Race',  0, TRIANGLE);
  Add('DREAMLAND', EXP_AH, 'The Dream Lands',             1, SLASH);
  Add('YUGGOTH',   EXP_AH, 'Yuggoth',                     1, ROUNDEL);
end;

initialization
  Gates := TStringList.Create;
  LoadGates;
  Gates.Sort;
end.

