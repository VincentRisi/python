unit MainUnit;
(***
This code uses materials which are the intellectual property of
the Arkham Horror Board Game and expansions.
As such this code cannot be put into the public domain or even
as open source.
***)

{$mode delphi}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics,
  Dialogs, StdCtrls, ExtCtrls, Buttons, ComCtrls,
  AHGame, AHTypes, AHGamePieces, AHLogger,
  ChooseExpansionsUnit, ChooseInvestigatorsUnit, RevealAncientOneUnit;

type
  { TMainForm }

  TMainForm = class(TForm)
    AncientsMemo: TMemo;
    DoneButton: TBitBtn;
    GameMemo: TMemo;
    GateImages: TImageList;
    MonsterImages: TImageList;
    InvImages: TImageList;
    GameImages: TImageList;
    DoomTrackImages: TImageList;
    DoomTrack: TImage;
    MythosMemo: TMemo;
    MythosMemo1: TMemo;
    MythosMemo2: TMemo;
    MemoPages: TPageControl;
    ScreenPages: TPageControl;
    AncientMemoTab: TTabSheet;
    HeadlineMemoTab: TTabSheet;
    EnvironmentMemoTab: TTabSheet;
    RumourMemoTab: TTabSheet;
    GameMemoTab: TTabSheet;
    TownMap: TImage;
    procedure DoneButtonClick(Sender: TObject);
    procedure FormActivate(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure TownMapPaint(Sender: TObject);
  private
    JustCreated : boolean;
  public
    chooseExpansionsForm : TChooseExpansionsForm;
    chooseInvestigatorsForm : TChooseInvestigatorsForm;
    chooseRevealAncientOneForm : TRevealAncientOneForm;
    function GetPlace(row, col : integer) : string;
    procedure ChooseExpansions;
    procedure ChooseExpansionsOk(Sender: TObject);
    procedure ChooseInvestigators;
    procedure ChooseInvestigatorsOk(Sender: TObject);
    procedure RevealAncientOne;
    procedure RevealAncientOneOk(Sender: TObject);
    procedure Log(message : string);
  end;

var
  MainForm: TMainForm;

implementation

{$R *.lfm}

{ TMainForm }

procedure TMainForm.FormCreate(Sender: TObject);
begin
  StartLog('ahgame.log');
  JustCreated := true;
end;

procedure TMainForm.FormActivate(Sender: TObject);
begin
  if JustCreated = false then exit;
  try
    JustCreated := false;
    AHGame.ParentForm      := self;
    AHGame.AncientsMemo    := AncientsMemo;
    AHGame.MythosMemo      := MythosMemo;
    AHGame.GameMemo        := GameMemo;
    AHGame.TownMap         := TownMap;
    AHGame.GameImages      := GameImages;
    AHGame.DoomTrack       := DoomTrack;
    AHGame.DoomTrackImages := DoomTrackImages;
    AHGame.ScreenPages     := ScreenPages;
    Log('Setup common controls in games unit.');
    ChooseExpansions;
  except
    on ex: Exception do
      log(format('exception: %s',[ex.Message]));
  end;
end;

procedure TMainForm.DoneButtonClick(Sender: TObject);
begin
  Log('Exiting game on Done Button.');
  Close;
end;

procedure TMainForm.ChooseExpansions;
var
  sheet   : TTabSheet;
begin
  Log('Setting up choose expansions and running.');
  chooseExpansionsForm := TChooseExpansionsForm.Create(self);
  sheet := TTabSheet.Create(ScreenPages);
  sheet.PageControl := ScreenPages;
  chooseExpansionsForm.BorderStyle := bsNone;
  chooseExpansionsForm.Align := alClient;
  chooseExpansionsForm.Parent := sheet;
  chooseExpansionsForm.Visible := True;
  chooseExpansionsForm.OkButton.OnClick := ChooseExpansionsOk;
  ScreenPages.ActivePage := sheet;
  sheet.Caption := chooseExpansionsForm.Caption;
  chooseExpansionsForm.FormCreate(sheet);
  chooseExpansionsForm.FormActivate(sheet);
end;

procedure TMainForm.ChooseExpansionsOk(Sender: TObject);
var
  sheet      : TTabSheet;
  expansions : SExpansion;
begin
  try
    Log('Choose expansions done.');
    sheet := ScreenPages.ActivePage;
    sheet.PageControl := nil;
    sheet.Destroy;
    expansions := [EXP_AH];
    if chooseExpansionsForm.COTDPCheckBox.Checked  = true then expansions := expansions + [EXP_COTDP];
    if chooseExpansionsForm.TBGOTWCheckBox.Checked = true then expansions := expansions + [EXP_TBGOTW];
    if chooseExpansionsForm.TKIYCheckBox.Checked   = true then expansions := expansions + [EXP_TKIY];
    if chooseExpansionsForm.TLATTCheckBox.Checked  = true then expansions := expansions + [EXP_TLATT];
    Log('Loading Game Pieces.');
    LoadGamePieces('materials.ark', expansions, GameMemo);
    Log('Load Card Decks from Game Pieces.');
    LoadCards(GameMemo);
    Log('Place Clues.');
    PlaceClues;
    TownMap.Refresh;
    chooseInvestigators;
  except
    on ex: Exception do
      log(format('exception: %s',[ex.Message]));
  end;
end;

procedure TMainForm.ChooseInvestigators;
var
  sheet   : TTabSheet;
begin
  Log('Setting up choose investigators and running.');
  chooseInvestigatorsForm := TChooseInvestigatorsForm.Create(self);
  sheet := TTabSheet.Create(ScreenPages);
  sheet.PageControl := ScreenPages;
  chooseInvestigatorsForm.BorderStyle := bsNone;
  chooseInvestigatorsForm.Align := alClient;
  chooseInvestigatorsForm.Parent := sheet;
  chooseInvestigatorsForm.Visible := True;
  chooseInvestigatorsForm.OkButton.OnClick := ChooseInvestigatorsOk;
  ScreenPages.ActivePage := sheet;
  sheet.Caption := chooseInvestigatorsForm.Caption;
  chooseInvestigatorsForm.FormCreate(sheet);
  chooseInvestigatorsForm.FormActivate(sheet);
end;

procedure TMainForm.ChooseInvestigatorsOk(Sender: TObject);
var
  sheet   : TTabSheet;
begin
  try
    Log('Choose investigators done.');
    sheet := ScreenPages.ActivePage;
    sheet.PageControl := nil;
    sheet.Destroy;
    RevealAncientOne;
  except
    on ex: Exception do
      log(format('exception: %s',[ex.Message]));
  end;
end;

procedure TMainForm.RevealAncientOne;
var
  sheet   : TTabSheet;
begin
  Log('Setting up Revealing Ancient One and run.');
  chooseRevealAncientOneForm := TRevealAncientOneForm.Create(self);
  sheet := TTabSheet.Create(ScreenPages);
  sheet.PageControl := ScreenPages;
  chooseRevealAncientOneForm.BorderStyle := bsNone;
  chooseRevealAncientOneForm.Align := alClient;
  chooseRevealAncientOneForm.Parent := sheet;
  chooseRevealAncientOneForm.Visible := True;
  chooseRevealAncientOneForm.OkButton.OnClick := RevealAncientOneOk;
  ScreenPages.ActivePage := sheet;
  sheet.Caption := chooseRevealAncientOneForm.Caption;
  chooseRevealAncientOneForm.FormCreate(sheet);
  chooseRevealAncientOneForm.FormActivate(sheet);
end;

procedure TMainForm.RevealAncientOneOk(Sender: TObject);
var
  chosen  : TListBox;
  name    : string;
  index  : integer;
  sheet   : TTabSheet;
begin
  try
    Log('Revealing Ancient One done.');
    sheet := ScreenPages.ActivePage;
    sheet.PageControl := nil;
    sheet.Destroy;
    chosen := chooseInvestigatorsForm.ChosenListBox;
    GameVars.first := 0;
    GameVars.gamephase := PHASE_SETUP;
    setLength(GameVars.investigatorsStats, chosen.Count);
    Log('Make Investigator forms.');
    GameVars.MakeInvestigatorForms(ScreenPages, chosen);
    Log('Display Ancient One and Terror Track.');
    name := chooseRevealAncientOneForm.AncientOneEdit.Text;
    GameVars.SetupAncient(AncientIndexOf(name));
    for index := 0 to pred(chosen.Count) do begin
      name := chosen.Items[index];
      Log(format('Complete setup for %s.',[name]));
      GameVars.SetupInvestigator(index, InvestigatorIndexOf(name));
    end;
    ScreenPages.ActivePageIndex := 0;
  except
    on ex: Exception do
      log(format('exception: %s',[ex.Message]));
  end;
end;

procedure TMainForm.Log(message: string);
begin
  AHLogger.Log(format('mainform: %s',[message]));
end;

procedure TMainForm.TownMapPaint(Sender: TObject);
var
  i, j, x, y, x2, y2, n, m : integer;
  GamePlace   : TGamePlace;
  MapPlace    : TMapPlace;
  Gate        : TGate;
  Monster     : TMonster;
begin
  for i := 0 to high(GamePlaceRecs) do begin
    GamePlace := GamePlaceRecs[i];
    if GamePlace.mapPlaceId = -1 then begin
      log(format('Game place %s does not have a map place', [gamePlace.name]));
      continue;
    end;
    for j := 0 to high(GamePlace.pending) do begin
      n := length(gamePlace.monsterIds);
      setLength(gamePlace.monsterIds, n+1);
      gamePlace.monsterIds[n] := GamePlace.pending[j];
    end;
    setLength(GamePlace.pending, 0);
    MapPlace := MapPlaceRecs[GamePlace.mapPlaceId];
    x := MapPlace.lcol - 6;
    y := MapPlace.trow - 12;
    if (GamePlace.gateId <> -1) and (GamePlace.gateState = GATE_OPEN) then begin
      Gate := GateRecs[GamePlace.gateId];
      TownMap.Canvas.TextOut(x+8, y+36, Gate.name);
    end;
    for j := 1 to GamePlace.clues do begin
      GameImages.Draw(TownMap.Canvas, x, y, CLUE_IMAGE);
      inc(x, 15);
    end;
    for j := 0 to high(GamePlace.playerNos) do begin
      n := GamePlace.playerNos[j];
      GameImages.Draw(TownMap.Canvas, x, y, n+INVESTIGATORS_IMAGE);
      inc(x, 15);
    end;
    for j := 0 to high(GamePlace.monsterIds) do begin
      n := GamePlace.monsterIds[j];
      Monster := MonsterRecs[n];
      m := integer(Monster.monsterType);
      GameImages.Draw(TownMap.Canvas, x, y, m+MONSTERS_IMAGE);
      inc(x, 15);
    end;
    for j := 0 to pred(length(GameVars.investigatorsStats)) do begin
      n := GameVars.investigatorsStats[j].investigatorId;
      if n = -1 then continue;
      x2 := 225+((j mod 4)*41);
      y2 := 705+((j div 4)*55);
      InvImages.Draw(TownMap.Canvas, x2, y2, n);
    end;
  end;
end;

function TMainForm.GetPlace(row, col: integer): string;
var
  i : integer;
  function between(no, lo, hi : integer) : boolean;
  begin
    result := true;
    if (no < lo) or (no > hi) then result := false;
  end;
begin
  result := '';
  for i := 0 to high(MapPlaceRecs) do begin
    with MapPlaceRecs[i] do begin
      if between(row, trow, brow) and between(col, lcol, rcol) then begin
        result := name;
        exit;
      end;
    end;
  end;
end;

end.
