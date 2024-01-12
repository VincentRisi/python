unit BoardUnit;

{$mode delphi}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, ExtCtrls,
  AHTypes, AHGamePieces;

type

  { TBoardForm }

  TBoardForm = class(TForm)
    GameImages: TImageList;
    TownMap: TImage;
    procedure TownMapPaint(Sender: TObject);
  private
    { private declarations }
  public
    { public declarations }
  end;

var
  BoardForm: TBoardForm;

implementation

{$R *.lfm}

{ TBoardForm }

procedure TBoardForm.TownMapPaint(Sender: TObject);
var
  i, j, x, y  : integer;
  GatePlace : TGatePlace;
  MapPlace  : TMapPlace;
begin
  for i := 0 to high(GatePlacesArray) do begin
    GatePlace := GatePlacesArray[i];
    MapPlace := MapPlacesArray[GatePlace.mapPlaceId];
    x := MapPlace.rcol + (MapPlace.lcol - MapPlace.rcol) div 2;
    y := MapPlace.trow - 18;
    for j := 1 to GatePlace.clues do
      GameImages.Draw(TownMap.Canvas, x+(j*2), y, 0);
  end;
end;

end.

