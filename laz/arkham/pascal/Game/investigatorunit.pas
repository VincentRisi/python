unit InvestigatorUnit;
(***
This code uses materials which are the intellectual property of
the Arkham Horror Board Game and expansions.
As such this code cannot be put into the public domain or even
as open source.
***)

{$mode delphi}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls,
  Buttons, ExtCtrls, Grids, ActnList, ComCtrls, AHGamePieces, AHTypes, Types,
  AHLogger;

type

  { TInvestigatorForm }

  TInvestigatorForm = class(TForm)
    ActionImages: TImageList;
    ActionsList: TActionList;
    MoveToCombo: TComboBox;
    Label24: TLabel;
    NorthWestBB: TBitBtn;
    NorthBB: TBitBtn;
    NorthEastBB: TBitBtn;
    WestBB: TBitBtn;
    EastBB: TBitBtn;
    SouthWestBB: TBitBtn;
    SouthBB: TBitBtn;
    SouthEastBB: TBitBtn;
    CardListUp: TSpeedButton;
    CardListDown: TSpeedButton;
    EastLabel: TLabel;
    NorthEastLabel: TLabel;
    SouthEastLabel: TLabel;
    WestLabel: TLabel;
    NorthLabel: TLabel;
    SouthLabel: TLabel;
    TopButton: TButton;
    CardListCombo: TComboBox;
    DiscardButton: TButton;
    BottomButton: TButton;
    CardListMemo: TMemo;
    CardNameEdit: TEdit;
    BoxButton: TButton;
    ReshuffleButton: TButton;
    TakeButton: TButton;
    ViewButton: TButton;
    EncounterButton1: TSpeedButton;
    DrawCardButton: TButton;
    Label9: TLabel;
    OutworldDeckCombo: TComboBox;
    CombatButton: TButton;
    CardDeckCombo: TComboBox;
    MonsterBacksList: TImageList;
    MonsterFrontsList: TImageList;
    InvestigatorImage1: TImage;
    InvestigatorImage2: TImage;
    LoreButton: TButton;
    EvadeButton: TButton;
    PlaceCombo: TComboBox;
    SpeedButton: TButton;
    DiscardCardAction: TAction;
    DoneButton: TBitBtn;
    EncounterButton: TSpeedButton;
    EncounterMemo: TMemo;
    FightDNButton: TSpeedButton;
    FightText: TLabel;
    FightUPButton: TSpeedButton;
    FocusText: TLabel;
    InvNotesMemo: TMemo;
    ActionPages: TPageControl;
    PhaseText: TLabel;
    Label23: TLabel;
    LocAbilityMemo: TMemo;
    InvestigatorImage: TImage;
    InvestigatorPics: TImageList;
    InvHomeText: TLabel;
    InvLocationText: TLabel;
    InvProfessionText: TLabel;
    InvAbilityMemo: TMemo;
    InvNameText: TLabel;
    Label1: TLabel;
    Label10: TLabel;
    Label11: TLabel;
    Label12: TLabel;
    Label13: TLabel;
    Label14: TLabel;
    Label15: TLabel;
    Label16: TLabel;
    Label17: TLabel;
    Label18: TLabel;
    Label19: TLabel;
    Label20: TLabel;
    Label21: TLabel;
    Label22: TLabel;
    Label2: TLabel;
    CluesText: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    Label7: TLabel;
    Label8: TLabel;
    CashText: TLabel;
    LoreDNButton: TSpeedButton;
    LoreText: TLabel;
    LoreUPButton: TSpeedButton;
    LuckText: TLabel;
    MaxFocusText: TLabel;
    maxLuckText: TLabel;
    MaxSanityText: TLabel;
    maxSneakText: TLabel;
    MaxStaminaText: TLabel;
    maxWillText: TLabel;
    minFightText: TLabel;
    minLoreText: TLabel;
    minSpeedText: TLabel;
    SanityDNButton: TSpeedButton;
    CashDNButton: TSpeedButton;
    CluesDNButton: TSpeedButton;
    SanityText: TLabel;
    SanityUPButton: TSpeedButton;
    CashUPButton: TSpeedButton;
    CluesUPButton: TSpeedButton;
    SneakText: TLabel;
    SneakButton: TButton;
    FightButton: TButton;
    NorthWestLabel: TLabel;
    SouthWestLabel: TLabel;
    WillButton: TButton;
    SpeedDNButton: TSpeedButton;
    SpeedText: TLabel;
    SpeedUPButton: TSpeedButton;
    StaminaDNButton: TSpeedButton;
    StaminaText: TLabel;
    StaminaUPButton: TSpeedButton;
    ItemsStringGrid: TStringGrid;
    DrawCardAction: TAction;
    EncountersTab: TTabSheet;
    CardsTab: TTabSheet;
    CombatTab: TTabSheet;
    ChecksTab: TTabSheet;
    MovementsTab: TTabSheet;
    LuckButton: TButton;
    HorrorlButton: TButton;
    WillText: TLabel;
    procedure BottomCardClick(Sender: TObject);
    procedure BoxCardClick(Sender: TObject);
    procedure CardListChange(Sender: TObject);
    procedure CardListDownClick(Sender: TObject);
    procedure CardListUpClick(Sender: TObject);
    procedure CardTypeChange(Sender: TObject);
    procedure DiscardCardClick(Sender: TObject);
    procedure DrawCardClick(Sender: TObject);
    procedure ItemsOnClick(Sender: TObject);
    procedure MoveBBClick(Sender: TObject);
    procedure MoveToDirectly(Sender: TObject);
    procedure ShuffleDeck(Sender: TObject);
    procedure TakeCardClick(Sender: TObject);
    procedure TopCardClick(Sender: TObject);
    procedure ViewCards(Sender: TObject);
    procedure CashDNButtonClick(Sender: TObject);
    procedure CashUPButtonClick(Sender: TObject);
    procedure CluesDNButtonClick(Sender: TObject);
    procedure FightDNButtonClick(Sender: TObject);
    procedure FightUPButtonClick(Sender: TObject);
    procedure FormActivate(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure LoreDNButtonClick(Sender: TObject);
    procedure LoreUPButtonClick(Sender: TObject);
    procedure SanityDNButtonClick(Sender: TObject);
    procedure CluesUPButtonClick(Sender: TObject);
    procedure SanityUPButtonClick(Sender: TObject);
    procedure EncounterButtonClick(Sender: TObject);
    procedure SpeedDNButtonClick(Sender: TObject);
    procedure SpeedUPButtonClick(Sender: TObject);
    procedure StaminaDNButtonClick(Sender: TObject);
    procedure StaminaUPButtonClick(Sender: TObject);
  private
    procedure setAbilityMemo(const value : string);
    function getCashText : integer;
    procedure setCashText(const value : integer);
    function getCluesText : integer;
    procedure setCluesText(const value : integer);
    function getInvFocusText : integer;
    procedure setInvFocusText(const value : integer);
    function getFightText : integer;
    procedure setFightText(const value : integer);
    function getInvNameText : string;
    procedure setInvNameText(const value : string);
    function getInvHomeId : string;
    procedure setInvHomeId(const value : string);
    function getInvLocationId : string;
    procedure setInvLocationId(const value : string);
    function getInvProfessionText : string;
    procedure setInvProfessionText(const value : string);
    function getLoreText : integer;
    procedure setLoreText(const value : integer);
    function getLuckText : integer;
    procedure setLuckText(const value : integer);
    function getMaxFocusText : integer;
    procedure setMaxFocusText(const value : integer);
    function getMaxSanityText : integer;
    procedure setMaxSanityText(const value : integer);
    function getMaxStaminaText : integer;
    procedure setMaxStaminaText(const value : integer);
    function getSanityText : integer;
    procedure setSanityText(const value : integer);
    function getSetLuckText : integer;
    procedure setSetLuckText(const value : integer);
    function getSneakText : integer;
    procedure setSneakText(const value : integer);
    function getSpeedText : integer;
    procedure setSpeedText(const value : integer);
    function getStaminaText : integer;
    procedure setStaminaText(const value : integer);
    function getWillText : integer;
    procedure setWillText(const value : integer);
    function getMaxSneakText : integer;
    procedure setMaxSneakText(const value : integer);
    function getMaxWillText : integer;
    procedure setMaxWillText(const value : integer);
    function getMinFightText : integer;
    procedure setMinFightText(const value : integer);
    function getMinLoreText : integer;
    procedure setMinLoreText(const value : integer);
    function getMinSpeedText : integer;
    procedure setMinSpeedText(const value : integer);
    function getPicId : integer;
    procedure setPicture(const value : integer);
    procedure setPlayerNo(const value : integer);
    procedure setPhase(const value : EPhase);
    procedure setInvNote(const value : string);
  public
    gameImages : TImageList;
    townMap    : TImage;
    procedure AddICard(cardId : integer);
    procedure DisplayICard(icard : TICard);
    function  RemoveICard(Name : string): integer;
    property Ability       : string                            write setAbilityMemo;
    property Cash          : integer read getCashText          write setCashText;
    property Clues         : integer read getCluesText         write setCluesText;
    property Fight         : integer read getFightText         write setFightText;
    property InvFocus      : integer read getInvFocusText      write setInvFocusText;
    property InvHome       : string  read getInvHomeId         write setInvHomeId;
    property InvLocation   : string  read getInvLocationId     write setInvLocationId;
    property InvName       : string  read getInvNameText       write setInvNameText;
    property InvNote       : string                            write setInvNote;
    property InvProfession : string  read getInvProfessionText write setInvProfessionText;
    property Lore          : integer read getLoreText          write setLoreText;
    property Luck          : integer read getLuckText          write setLuckText;
    property MaxFocus      : integer read getMaxFocusText      write setMaxFocusText;
    property MaxLuck       : integer read getSetLuckText       write setSetLuckText;
    property MaxSanity     : integer read getMaxSanityText     write setMaxSanityText;
    property MaxSneak      : integer read getMaxSneakText      write setMaxSneakText;
    property MaxStamina    : integer read getMaxStaminaText    write setMaxStaminaText;
    property MaxWill       : integer read getMaxWillText       write setMaxWillText;
    property MinFight      : integer read getMinFightText      write setMinFightText;
    property MinLore       : integer read getMinLoreText       write setMinLoreText;
    property MinSpeed      : integer read getMinSpeedText      write setMinSpeedText;
    property Phase         : EPhase                            write setPhase;
    property PicId         : integer                           write setPicture;
    property PlayerNo      : integer                           write setPlayerNo;
    property Sanity        : integer read getSanityText        write setSanityText;
    property Sneak         : integer read getSneakText         write setSneakText;
    property Speed         : integer read getSpeedText         write setSpeedText;
    property Stamina       : integer read getStaminaText       write setStaminaText;
    property Will          : integer read getWillText          write setWillText;
  private
    justCreated    : boolean;
    investigatorId : integer;
    invPlayerNo    : integer;
    gameImageId    : integer;
    invHomeId      : string;
    invLocationId  : string;
    gamePhase      : EPhase;
    icards         : array of integer;
    MoveBitBtn     : array [EDirection] of TBitBtn;
    MoveLabel      : array [EDirection] of TLabel;
    procedure SetCardTabDefaults;
    procedure SetMovementTab;
  end;

var
  InvestigatorForm: TInvestigatorForm;

type
  TInvestigatorStats = class
    investigatorId : integer;
    backStoryId    : integer;
    phase          : EPhase;
    form           : TInvestigatorForm;
  end;

procedure Log(message: string);

implementation

{$R *.lfm}

{ TInvestigatorForm }

procedure Log(message: string);
begin
  AHLogger.Log(format('InvestigatorUnit: %s', [message]));
end;

procedure handle_other(routine : string);
begin
  log(format('%s',[routine]));
end;

procedure handle_exception(routine: string; ex : exception);
begin
  log(format('%s: %s: %s',[routine, ex.ClassName, ex.Message]));
end;

function toInt(value :string) : integer;
begin
  try
    result := strtoint(value);
  except
    result := 0;
  end;
end;

function toMMInt(value :string) : integer;
begin
  try
    result := strtoint(value[1]);
  except
    result := 0;
  end;
end;

function toStr(value :integer) : string;
begin
  result := format('%d', [value]);
end;

function toMinStr(value :integer) : string;
begin
  result := format('%d %d %d %d', [value, value+1, value+2, value+3]);
end;

function toMaxStr(value :integer) : string;
begin
  result := format('%d %d %d %d', [value, value-1, value-2, value-3]);
end;

procedure SetCell(var grid : TStringGrid; row, col : integer; value : string);
var
  n : integer;
  function getExtent(value : string): integer;
  begin
    try
      result := grid.Canvas.TextExtent(value).cx + 8;
    except
      result := 0;
    end;
  end;
begin
  n := getExtent(value);
  if grid.ColWidths[col] < n then
    grid.ColWidths[col] := n;
  grid.Cells[col, row] := value;
end;

procedure TInvestigatorForm.FormCreate(Sender: TObject);
begin
  try
    justCreated   := true;
    invHomeId     := '';
    invLocationId := '';
    gameImageId   := -1;
    investigatorId := -1;
    setLength(icards, 0);
  except on x : exception do handle_exception('FormCreate', x)
    else handle_other('FormCreate')
  end;
end;

procedure TInvestigatorForm.FormActivate(Sender: TObject);
var
  i, j : integer;
  ei : EICardType;
  eo : EOWorldPlace;
begin
  try
    if justCreated = false then exit;
    justCreated := false;
    Top := 248;
    Left := 714;
    ItemsStringGrid.ColCount := 4;
    SetCell(ItemsStringGrid, 0, 0, 'Item');
    SetCell(ItemsStringGrid, 0, 1, 'Type');
    ItemsStringGrid.ColWidths[2] := 8;
    SetCell(ItemsStringGrid, 0, 2, 'H');
    SetCell(ItemsStringGrid, 0, 3, 'Rules -- (H is for hands, you only have two)');
    for ei := low(EICardType) to high(EICardType) do begin
      if length(ICardDecks[ei].deck) > 0 then
        CardDeckCombo.AddItem(ICardTypeNames[ei], ICardDecks[ei]);
    end;
    CardDeckCombo.ItemIndex := 0;
    for eo := low(EOWorldPlace) to high(EOWorldPlace) do
      OutworldDeckCombo.AddItem(OWorldPlaceNames[eo], OWorldDecks[eo]);
    OutworldDeckCombo.ItemIndex := 0;
    for i := 0 to high(PlaceRecs) do begin
      with PlaceRecs[i] do
        PlaceCombo.AddItem(description, PlaceRecs[i]);
    end;
    PlaceCombo.ItemIndex := 0;
    MoveBitBtn[EAST]          := EASTBB;
    MoveLabel[EAST]           := EASTLabel;
    MoveBitBtn[NORTH]         := NORTHBB;
    MoveLabel[NORTH]          := NORTHLabel;
    MoveBitBtn[NORTHEAST]     := NORTHEASTBB;
    MoveLabel[NORTHEAST]      := NORTHEASTLabel;
    MoveBitBtn[NORTHWEST]     := NORTHWESTBB;
    MoveLabel[NORTHWEST]      := NORTHWESTLabel;
    MoveBitBtn[SOUTH]         := SOUTHBB;
    MoveLabel[SOUTH]          := SOUTHLabel;
    MoveBitBtn[SOUTHEAST]     := SOUTHEASTBB;
    MoveLabel[SOUTHEAST]      := SOUTHEASTLabel;
    MoveBitBtn[SOUTHWEST]     := SOUTHWESTBB;
    MoveLabel[SOUTHWEST]      := SOUTHWESTLabel;
    MoveBitBtn[DEADEND]       := nil;
    MoveLabel[DEADEND]        := nil;
    MoveBitBtn[WEST]          := WESTBB;
    MoveLabel[WEST]           := WESTLabel;
    MoveBitBtn[EAST].Tag      := LongInt(EAST);
    MoveBitBtn[NORTH].Tag     := LongInt(NORTH);
    MoveBitBtn[NORTHEAST].Tag := LongInt(NORTHEAST);
    MoveBitBtn[NORTHWEST].Tag := LongInt(NORTHWEST);
    MoveBitBtn[SOUTH].Tag     := LongInt(SOUTH);
    MoveBitBtn[SOUTHEAST].Tag := LongInt(SOUTHEAST);
    MoveBitBtn[SOUTHWEST].Tag := LongInt(SOUTHWEST);
    MoveBitBtn[WEST].Tag      := LongInt(WEST);
    for i := 0 to high(LocationRecs) do begin
      case LocationRecs[i].placeType of
        PLACE: begin
          j := PlaceIndexOf(LocationRecs[i].name);
          if j <> -1 then MoveToCombo.AddItem(PlaceRecs[j].description, LocationRecs[i]);
        end;
        DISTRICT: begin
          j := DistrictIndexOf(LocationRecs[i].name);
          if j <> -1 then MoveToCombo.AddItem(DistrictRecs[j].description, LocationRecs[i]);
        end;
        GATE: begin
          j := GateIndexOf(LocationRecs[i].name);
          if j <> -1 then MoveToCombo.AddItem(GateRecs[j].description, LocationRecs[i]);
        end;
        OUTTOWN: begin
          if LocationRecs[i].name = 'SPACETIME' then
            MoveToCombo.AddItem('Lost in Time and Space', LocationRecs[i]);
        end;
      end;
    end;
  except on x : exception do handle_exception('FormActivate', x)
    else handle_other('FormActivate')
  end;
end;

procedure TInvestigatorForm.SpeedDNButtonClick(Sender: TObject);
var
  no : integer;
begin
  try
    no := Speed - MinSpeed;
    if no > 0 then begin
      Speed := Speed - 1;
      Sneak := Sneak + 1;
    end;
  except on x : exception do handle_exception('SpeedDNButtonClick', x)
    else handle_other('SpeedDNButtonClick')
  end;
end;

procedure TInvestigatorForm.FightDNButtonClick(Sender: TObject);
var
  no : integer;
begin
  try
    no := Fight - MinFight;
    if no > 0 then begin
      Fight := Fight - 1;
      Will  := Will + 1;
    end;
  except on x : exception do handle_exception('FightDNButtonClick', x)
    else handle_other('FightDNButtonClick')
  end;
end;

procedure TInvestigatorForm.CashDNButtonClick(Sender: TObject);
begin
  try
    if Cash > 0 then
      Cash := Cash - 1;
  except on x : exception do handle_exception('CashDNButtonClick', x)
    else handle_other('CashDNButtonClick')
  end;
end;

procedure TInvestigatorForm.SetCardTabDefaults;
begin
  try
    if CardListCombo.Visible = true then begin
      CardListCombo.Visible := false;
      ShuffleDeck(ReshuffleButton);
    end;
    CardListDown.Visible := false;
    CardListUp.Visible := false;
    CardListMemo.Visible := false;
    CardNameEdit.Visible := false;
    DiscardButton.Enabled := false;
    TopButton.Enabled := false;
    BoxButton.Enabled := false;
    TakeButton.Enabled := false;
    DrawCardButton.Enabled := true;
    BottomButton.Enabled := true;
    ReshuffleButton.Enabled := true;
  except on x : exception do handle_exception('SetCardTabDefaults', x)
    else handle_other('SetCardTabDefaults')
  end;
end;

procedure TInvestigatorForm.SetMovementTab;
var
  i, index : Integer;
  location  : TLocation;
  road      : TRoad;
  ed        : EDirection;
begin
  for ed := low(MoveBitBtn) to high(MoveBitBtn) do begin
    if ed = DEADEND then continue;
    MoveBitBtn[ed].Enabled := false;
    MoveLabel[ed].Visible := false;
    MoveLabel[ed].Caption := '';
  end;
  index := LocationIndexOf(InvLocation);
  if index <> -1 then begin
    location := LocationRecs[index];
    for i := 0 to high(RoadRecs) do begin
      road := RoadRecs[i];
      if road.location1 = location.name then begin
        if road.direction <> DEADEND then begin
          MoveBitBtn[road.direction].Enabled := true;
          MoveLabel[road.direction].Visible := true;
          MoveLabel[road.direction].Caption := road.location2;
        end;
      end;
    end;
  end;
end;

procedure TInvestigatorForm.MoveBBClick(Sender: TObject);
var
  ed : EDirection;
begin
  try
    with Sender as TBitBtn do begin
      ed := EDirection(Tag);
      InvLocation := MoveLabel[ed].Caption;
      townMap.Refresh;
    end;
  except on x : exception do handle_exception('MoveBBClick', x)
    else handle_other('MoveBBClick')
  end;
end;

procedure TInvestigatorForm.MoveToDirectly(Sender: TObject);
var
  no : integer;
  rec : TLocation;
begin
  no := MoveToCombo.ItemIndex;
  if no <> -1 then begin
    rec := MoveToCombo.Items.Objects[no] as TLocation;
    if rec <> nil then begin
      InvLocation := rec.name;
      townMap.Refresh;
    end;
  end;
end;


procedure TInvestigatorForm.ShuffleDeck(Sender: TObject);
var
  cardDeck : TCardDeck;
begin
  try
    SetCardTabDefaults;
    if CardDeckCombo.ItemIndex <> -1 then begin
      cardDeck := CardDeckCombo.Items.Objects[CardDeckCombo.ItemIndex] as TCardDeck;
      cardDeck.Shuffle;
    end;
  except on x : exception do handle_exception('ShuffleDeck', x)
    else handle_other('ShuffleDeck')
  end;
end;

procedure TInvestigatorForm.ViewCards(Sender: TObject);
var
  cardDeck : TCardDeck;
  i, no : integer;
begin
  try
    SetCardTabDefaults;
    if CardDeckCombo.ItemIndex <> -1 then begin
      cardDeck := CardDeckCombo.Items.Objects[CardDeckCombo.ItemIndex] as TCardDeck;
      CardListCombo.Clear;
      CardListCombo.Visible := true;
      CardListMemo.Visible := true;
      CardListDown.Visible := true;
      CardListUp.Visible := true;
      TakeButton.Enabled := true;
      DrawCardButton.Enabled := false;
      BottomButton.Enabled := false;
      ReshuffleButton.Enabled := false;
      for i := 0 to high(cardDeck.deck) do begin
        no := cardDeck.deck[i];
        CardListCombo.AddItem(ICardRecs[no].fullname, ICardRecs[no]);
      end;
      CardListCombo.ItemIndex := 0;
      CardListChange(Sender);
      CardListCombo.SetFocus;
    end;
  except on x : exception do handle_exception('ViewCards', x)
    else handle_other('ViewCards')
  end;
end;

procedure TInvestigatorForm.TakeCardClick(Sender: TObject);
var
  no, id   : integer;
  cardDeck : TCardDeck;
  ICard    : TICard;
begin
  try
    no := CardListCombo.ItemIndex;
    if no <> -1 then begin
      ICard := CardListCombo.Items.Objects[no] as TICard;
      id := ICardIndexOf(ICard.name);
      if CardDeckCombo.ItemIndex <> -1 then begin
        cardDeck := CardDeckCombo.Items.Objects[CardDeckCombo.ItemIndex] as TCardDeck;
        AddICard(cardDeck.Find(id));
        SetCardTabDefaults;
      end;
    end;
  except on x : exception do handle_exception('TakeCardClick', x)
    else handle_other('TakeCardClick')
  end;
end;

procedure TInvestigatorForm.CardTypeChange(Sender: TObject);
begin
  try
    SetCardTabDefaults;
    CardListCombo.Clear;
    CardListMemo.Clear;
  except on x : exception do handle_exception('CardTypeChange', x)
    else handle_other('CardTypeChange')
  end;
end;

procedure TInvestigatorForm.BottomCardClick(Sender: TObject);
var
  cardDeck : TCardDeck;
  no    : integer;
begin
  try
    SetCardTabDefaults;
    no := CardDeckCombo.ItemIndex;
    if no <> -1 then begin
      cardDeck := CardDeckCombo.Items.Objects[no] as TCardDeck;
      AddICard(cardDeck.Bottom);
    end;
  except on x : exception do handle_exception('BottomCardClick', x)
    else handle_other('BottomCardClick')
  end;
end;

procedure TInvestigatorForm.DrawCardClick(Sender: TObject);
var
  cardDeck : TCardDeck;
  no    : integer;
begin
  try
    SetCardTabDefaults;
    no := CardDeckCombo.ItemIndex;
    if no <> -1 then begin
      cardDeck := CardDeckCombo.Items.Objects[no] as TCardDeck;
      AddICard(cardDeck.Draw);
    end;
  except on x : exception do handle_exception('DrawCardClick', x)
    else handle_other('DrawCardClick')
  end;
end;

procedure TInvestigatorForm.DiscardCardClick(Sender: TObject);
var
  cardDeck : TCardDeck;
  no, id   : integer;
begin
  try
    if CardNameEdit.Visible = true then begin
      no := CardDeckCombo.ItemIndex;
      if no <> -1 then begin
        cardDeck := CardDeckCombo.Items.Objects[no] as TCardDeck;
        id := RemoveICard(CardNameEdit.Text);
        cardDeck.Discard(id);
        SetCardTabDefaults;
      end;
    end;
  except on x : exception do handle_exception('DiscardCardClick', x)
    else handle_other('DiscardCardClick')
  end;
end;

procedure TInvestigatorForm.TopCardClick(Sender: TObject);
var
  cardDeck : TCardDeck;
  no, id   : integer;
begin
  try
    if CardNameEdit.Visible = true then begin
      no := CardDeckCombo.ItemIndex;
      if no <> -1 then begin
        cardDeck := CardDeckCombo.Items.Objects[no] as TCardDeck;
        id := RemoveICard(CardNameEdit.Text);
        cardDeck.Top(id);
        SetCardTabDefaults;
      end;
    end;
  except on x : exception do handle_exception('TopCardClick', x)
    else handle_other('TopCardClick')
  end;
end;

procedure TInvestigatorForm.BoxCardClick(Sender: TObject);
var
  id   : integer;
begin
  try
    if CardNameEdit.Visible = true then begin
      id := RemoveICard(CardNameEdit.Text);
      SetCardTabDefaults;
    end;
  except on x : exception do handle_exception('BoxCardClick', x)
    else handle_other('BoxCardClick')
  end;
end;

procedure TInvestigatorForm.ItemsOnClick(Sender: TObject);
var
  r, c : integer;
begin
  try
    with ItemsStringGrid do begin
      r := Selection.Top;
      while (r > 1) and (Cells[0, r] = '') do dec(r);
      if ActionPages.ActivePage = CardsTab then begin
        SetCardTabDefaults;
        CardNameEdit.Visible := true;
        CardNameEdit.Text := Cells[0, r];
        CardDeckCombo.Text := Cells[1, r];
        DiscardButton.Enabled := true;
        TopButton.Enabled := true;
        BoxButton.Enabled := true;
      end
      else if ActionPages.ActivePage = CombatTab then begin
      end;
    end;
  except on x : exception do handle_exception('ItemsOnClick', x)
    else handle_other('ItemsOnClick')
  end;
end;

procedure TInvestigatorForm.CardListChange(Sender: TObject);
var
  no    : integer;
  ICard : TICard;
begin
  try
    no := CardListCombo.ItemIndex;
    if no <> -1 then begin
      ICard := CardListCombo.Items.Objects[no] as TICard;
      if ICard <> nil then begin
        CardListMemo.Clear;
        CardListMemo.Lines.Append(ICard.description);
      end;
    end;
  except on x : exception do handle_exception('CardListChange', x)
    else handle_other('CardListChange')
  end;
end;

procedure TInvestigatorForm.CardListDownClick(Sender: TObject);
begin
  try
    if CardListCombo.ItemIndex > 0 then begin
      CardListCombo.ItemIndex := CardListCombo.ItemIndex - 1;
      CardListChange(Sender);
    end;
  except on x : exception do handle_exception('CardListDownClick', x)
    else handle_other('CardListDownClick')
  end;
end;

procedure TInvestigatorForm.CardListUpClick(Sender: TObject);
begin
  try
    if CardListCombo.ItemIndex < CardListCombo.Items.Count then begin
      CardListCombo.ItemIndex := CardListCombo.ItemIndex + 1;
      CardListChange(Sender);
    end;
  except on x : exception do handle_exception('CardListUpClick', x)
    else handle_other('CardListUpClick')
  end;
end;

procedure TInvestigatorForm.CashUPButtonClick(Sender: TObject);
begin
  try
    Cash := Cash + 1;
  except on x : exception do handle_exception('CashUPButtonClick', x)
    else handle_other('CashUPButtonClick')
  end;
end;

procedure TInvestigatorForm.CluesDNButtonClick(Sender: TObject);
begin
  try
    if Clues > 0 then
      Clues := Clues - 1;
  except on x : exception do handle_exception('CluesDNButtonClick', x)
    else handle_other('CluesDNButtonClick')
  end;
end;

procedure TInvestigatorForm.FightUPButtonClick(Sender: TObject);
var
  no : integer;
begin
  try
    no := Fight - minFight;
    if no < 3 then begin
      Fight := Fight + 1;
      Will  := Will - 1;
    end;
  except on x : exception do handle_exception('FightUPButtonClick', x)
    else handle_other('FightUPButtonClick')
  end;
end;

procedure TInvestigatorForm.LoreDNButtonClick(Sender: TObject);
var
  no : integer;
begin
  try
    no := Lore - MinLore;
    if no > 0 then begin
      Lore := Lore - 1;
      Luck := Luck + 1;
    end;
  except on x : exception do handle_exception('LoreDNButtonClick', x)
    else handle_other('LoreDNButtonClick')
  end;
end;

procedure TInvestigatorForm.LoreUPButtonClick(Sender: TObject);
var
  no : integer;
begin
  try
    no := Lore - MinLore;
    if no < 3 then begin
      Lore := Lore + 1;
      Luck := Luck - 1;
    end;
  except on x : exception do handle_exception('LoreUPButtonClick', x)
    else handle_other('LoreUPButtonClick')
  end;
end;

procedure TInvestigatorForm.SanityDNButtonClick(Sender: TObject);
begin
  try
    if Sanity > 0 then
      Sanity := Sanity - 1;
  except on x : exception do handle_exception('SanityDNButtonClick', x)
    else handle_other('SanityDNButtonClick')
  end;
end;

procedure TInvestigatorForm.CluesUPButtonClick(Sender: TObject);
begin
  try
    Clues := Clues + 1;
  except on x : exception do handle_exception('CluesUPButtonClick', x)
    else handle_other('CluesUPButtonClick')
  end;
end;

procedure TInvestigatorForm.SanityUPButtonClick(Sender: TObject);
begin
  try
    if Sanity < MaxSanity then
      Sanity := Sanity + 1;
  except on x : exception do handle_exception('SanityUPButtonClick', x)
    else handle_other('SanityUPButtonClick')
  end;
end;

procedure TInvestigatorForm.EncounterButtonClick(Sender: TObject);
var
  p : integer;
  encounter, work : string;
begin
  try
    work := GetPlaceEncounter(invLocationId);
    EncounterMemo.Clear;
    while true do begin
      p := pos('] [', work);
      if p > 0 then begin
        encounter := copy(work, 1, p-1);
        work := copy(work, p+3, length(work));
        EncounterMemo.Lines.Add(encounter);
        continue;
      end;
      p := pos('[', work);
      if p > 0 then begin
        encounter := copy(work, 1, p);
        work := copy(work, p+2, length(work));
        EncounterMemo.Lines.Add(encounter);
        continue;
      end;
      p := pos(']', work);
      if p > 0 then begin
        encounter := copy(work, 1, p-1);
        work := copy(work, p+1, length(work));
        EncounterMemo.Lines.Add(encounter);
        continue;
      end;
      encounter := work;
      EncounterMemo.Lines.Add(encounter);
      break;
    end
  except on x : exception do handle_exception('EncounterButtonClick', x)
    else handle_other('EncounterButtonClick')
  end;
end;

procedure TInvestigatorForm.SpeedUPButtonClick(Sender: TObject);
var
  no : integer;
begin
  try
    no := Speed - minSpeed;
    if no < 3 then begin
      Speed := Speed + 1;
      Sneak := Sneak - 1;
    end;
  except on x : exception do handle_exception('SpeedUPButtonClick', x)
    else handle_other('SpeedUPButtonClick')
  end;
end;

procedure TInvestigatorForm.StaminaDNButtonClick(Sender: TObject);
begin
  try
    if Stamina > 0 then
      Stamina := Stamina - 1;
  except on x : exception do handle_exception('StaminaDNButtonClick', x)
    else handle_other('StaminaDNButtonClick')
  end;
end;

procedure TInvestigatorForm.StaminaUPButtonClick(Sender: TObject);
begin
  try
    if Stamina < MaxStamina then
      Stamina := Stamina + 1;
  except on x : exception do handle_exception('StaminaUPButtonClick', x)
    else handle_other('StaminaUPButtonClick')
  end;
end;

procedure TInvestigatorForm.setAbilityMemo(const value: string);
begin
  InvAbilityMemo.Lines.Add(value);
end;

function TInvestigatorForm.getCashText: integer;
begin
  result := toInt(CashText.Caption);
end;

procedure TInvestigatorForm.setCashText(const value: integer);
begin
  CashText.Caption := toStr(value);
end;

function TInvestigatorForm.getCluesText: integer;
begin
  result := toInt(CluesText.Caption);
end;

procedure TInvestigatorForm.setCluesText(const value: integer);
begin
  CluesText.Caption := toStr(value);
end;

function TInvestigatorForm.getInvFocusText: integer;
begin
  result := toInt(FocusText.Caption);
end;

procedure TInvestigatorForm.setInvFocusText(const value: integer);
begin
  FocusText.Caption := toStr(value);
end;

function TInvestigatorForm.getFightText: integer;
begin
  result := toInt(FightText.Caption);
end;

procedure TInvestigatorForm.setFightText(const value: integer);
begin
  FightText.Caption := toStr(value);
end;

procedure TInvestigatorForm.setInvHomeId(const value: string);
var
  special : string;
begin
  InvHomeId := value;
  InvHomeText.Caption := GetLocationDescription(value, special);
end;

function TInvestigatorForm.getInvLocationId: string;
begin
  result := InvLocationId;
end;

procedure TInvestigatorForm.setInvLocationId(const value: string);
var
  special          : string;
  gateFrom, gateTo : integer;
  GamePlace        : TGamePlace;
  procedure remove(var iArray : TIntegerDynArray; const id : integer);
  var
    i, no : integer;
    found : boolean;
  begin
    found := false;
    no    := pred(length(iArray));
    for i := 0 to no do begin
      if iArray[i] = id then found := true;
      if found = true then begin
        if i < no then
          iArray[i] := iArray[i+1];
      end;
    end;
    if found = true then
      setLength(iArray, no);
  end;
  procedure add(var iArray : TIntegerDynArray; const id : integer);
  var
    i, no : integer;
  begin
    no := pred(length(iArray));
    for i := 0 to no do
      if iArray[i] = id then exit;
    no := length(iArray) + 1;
    setLength(iArray, no);
    iArray[no-1] := id;
  end;
begin
  try
    gateFrom := GamePlaceIndexOf(InvLocationId);
    gateTo   := GamePlaceIndexOf(value);
    InvLocationId := value;
    InvLocationText.Caption := GetLocationDescription(value, special);
    LocAbilityMemo.Lines.Clear;
    LocAbilityMemo.Lines.Add(special);
    if gateFrom >= 0 then begin
      GamePlace := GamePlaceRecs[gateFrom];
      remove(GamePlace.playerNos, invPlayerNo);
    end;
    if gateTo >= 0 then begin
      GamePlace := GamePlaceRecs[gateTo];
      if GamePlace.clues > 0 then begin
        Clues := Clues + GamePlace.clues;
        GamePlace.clues := 0;
      end;
      add(GamePlace.playerNos, invPlayerNo);
    end;
    SetMovementTab;
  except on x : exception do handle_exception('setInvLocationId', x)
    else handle_other('setInvLocationId')
  end;
end;

function TInvestigatorForm.getInvProfessionText: string;
begin
  result := InvProfessionText.Caption;
end;

procedure TInvestigatorForm.setInvProfessionText(const value: string);
begin
  InvProfessionText.Caption := value;
end;

function TInvestigatorForm.getInvHomeId: string;
begin
  result := InvHomeId;
end;

function TInvestigatorForm.getInvNameText: string;
begin
  result := InvNameText.Caption;
end;

procedure TInvestigatorForm.setInvNameText(const value: string);
begin
  InvNameText.Caption := value;
end;

function TInvestigatorForm.getLoreText: integer;
begin
  result := toInt(LoreText.Caption);
end;

procedure TInvestigatorForm.setLoreText(const value: integer);
begin
  LoreText.Caption := toStr(value);
end;

function TInvestigatorForm.getLuckText: integer;
begin
  result := toInt(LuckText.Caption);
end;

procedure TInvestigatorForm.setLuckText(const value: integer);
begin
  LuckText.Caption := toStr(value);
end;

function TInvestigatorForm.getMaxFocusText: integer;
begin
  result := toInt(MaxFocusText.Caption);
end;

procedure TInvestigatorForm.setMaxFocusText(const value: integer);
begin
  MaxFocusText.Caption := toStr(value);
end;

function TInvestigatorForm.getMaxSanityText: integer;
begin
  result := toInt(MaxSanityText.Caption);
end;

procedure TInvestigatorForm.setMaxSanityText(const value: integer);
begin
  MaxSanityText.Caption := toStr(value);
end;

function TInvestigatorForm.getMaxStaminaText: integer;
begin
  result := toInt(MaxStaminaText.Caption);
end;

procedure TInvestigatorForm.setMaxStaminaText(const value: integer);
begin
  MaxStaminaText.Caption := toStr(value);
end;

function TInvestigatorForm.getSanityText: integer;
begin
  result := toInt(SanityText.Caption);
end;

procedure TInvestigatorForm.setSanityText(const value: integer);
begin
  SanityText.Caption := toStr(value);
end;

function TInvestigatorForm.getSetLuckText: integer;
begin
  result := toMMInt(maxLuckText.Caption);
end;

procedure TInvestigatorForm.setSetLuckText(const value: integer);
begin
  maxLuckText.Caption := toMaxStr(value);
end;

function TInvestigatorForm.getSneakText: integer;
begin
  result := toInt(SneakText.Caption);
end;

procedure TInvestigatorForm.setSneakText(const value: integer);
begin
  SneakText.Caption := toStr(value);
end;

function TInvestigatorForm.getSpeedText: integer;
begin
  result := toInt(SpeedText.Caption);
end;

procedure TInvestigatorForm.setSpeedText(const value: integer);
begin
  SpeedText.Caption := toStr(value);
end;

function TInvestigatorForm.getStaminaText: integer;
begin
  result := toInt(StaminaText.Caption);
end;

procedure TInvestigatorForm.setStaminaText(const value: integer);
begin
  StaminaText.Caption := toStr(value);
end;

function TInvestigatorForm.getWillText: integer;
begin
  result := toInt(WillText.Caption);
end;

procedure TInvestigatorForm.setWillText(const value: integer);
begin
  WillText.Caption := toStr(value);
end;

function TInvestigatorForm.getMaxSneakText: integer;
begin
  result := toMMInt(MaxSneakText.Caption);
end;

procedure TInvestigatorForm.setMaxSneakText(const value: integer);
begin
  MaxSneakText.Caption := toMaxStr(value);
end;

function TInvestigatorForm.getMaxWillText: integer;
begin
  result := toMMInt(MaxWillText.Caption);
end;

procedure TInvestigatorForm.setMaxWillText(const value: integer);
begin
  MaxWillText.Caption := toMaxStr(value);
end;

function TInvestigatorForm.getMinFightText: integer;
begin
  result := toMMInt(MinFightText.Caption);
end;

procedure TInvestigatorForm.setMinFightText(const value: integer);
begin
  MinFightText.Caption := toMinStr(value);
end;

function TInvestigatorForm.getMinLoreText: integer;
begin
  result := toMMInt(MinLoreText.Caption);
end;

procedure TInvestigatorForm.setMinLoreText(const value: integer);
begin
  MinLoreText.Caption := toMinStr(value);
end;

function TInvestigatorForm.getMinSpeedText: integer;
begin
  result := toMMInt(MinSpeedText.Caption);
end;

procedure TInvestigatorForm.setMinSpeedText(const value: integer);
begin
  MinSpeedText.Caption := toMinStr(value);
end;

function TInvestigatorForm.getPicId: integer;
begin
  result := investigatorId;
end;

procedure TInvestigatorForm.setPicture(const value: integer);
begin
  investigatorId := value;
  InvestigatorImage.Stretch := true;
  InvestigatorImage.Proportional := true;
  InvestigatorPics.GetBitmap(investigatorId, InvestigatorImage.Picture.Bitmap);
end;

procedure TInvestigatorForm.setPlayerNo(const value: integer);
begin
  invPlayerNo := value;
  gameImageId := INVESTIGATORS_IMAGE + value;
  GameImages.Draw(InvestigatorImage.Canvas, 0, 0, gameImageId);
end;


procedure TInvestigatorForm.setPhase(const value: EPhase);
begin
  gamePhase := value;
  case gamePhase of
    PHASE_SETUP: begin
      PhaseText.Caption := 'Setup';
      Color := $00FEFCD8;
    end;
    PHASE_UPKEEP: begin
      PhaseText.Caption := 'Upkeep';
      Color := $00DEFED8;
    end;
    PHASE_MOVEMENT: begin
      PhaseText.Caption := 'Movement';
      Color := $00D8FEE7;
    end;
    PHASE_ARHAM_ENCOUNTER: begin
      PhaseText.Caption := 'Arkham Encounter';
      Color := $00ECFFFF;
    end;
    PHASE_OTHER_WORLD_ENCOUNTER: begin
      PhaseText.Caption := 'Other World Encounter';
      Color := $00FFE1F3;
    end;
    PHASE_MYTHOS: begin
      PhaseText.Caption := 'Mythos';
      Color := $00DFD8FE;
    end;
    PHASE_END_GAME: begin
      PhaseText.Caption := 'End Game';
      Color := $00FBFAFD;
    end;
  end;
end;

procedure TInvestigatorForm.setInvNote(const value: string);
begin
  InvNotesMemo.Lines.Add(value);
end;

procedure TInvestigatorForm.AddICard(cardId: integer);
var
  icard   : TIcard;
  i       : integer;
begin
  try
    if cardId = -1 then
      exit;
    i := length(icards);
    setLength(icards, i+1);
    icards[i] := cardId;
    icard := ICardRecs[cardId];
    DisplayICard(icard);
  except on x : exception do handle_exception('AddICard', x)
    else handle_other('AddICard')
  end;
end;

procedure TInvestigatorForm.DisplayICard(icard: TICard);
var
  row, i     : integer;
  work, cost : string;
  lines      : TStringDynArray;
begin
  try
    work := icard.description;
    if icard.cost > 0 then
      cost := format('$%d', [icard.cost])
    else
      cost := '';
    lines := SplitWrap(work, 72);
    row  := ItemsStringGrid.RowCount;
    ItemsStringGrid.RowCount := ItemsStringGrid.RowCount + 1;
    SetCell(ItemsStringGrid, row, 0, icard.fullname);
    SetCell(ItemsStringGrid, row, 1, icardtypenames[icard.icardtype]);
    if icard.handed > 0 then
      SetCell(ItemsStringGrid, row, 2, inttostr(icard.handed)+' '+cost)
    else
      SetCell(ItemsStringGrid, row, 2, cost);
    SetCell(ItemsStringGrid, row, 3, lines[0]);
    for i := 1 to pred(length(lines)) do begin
      row  := ItemsStringGrid.RowCount;
      ItemsStringGrid.RowCount := ItemsStringGrid.RowCount + 1;
      SetCell(ItemsStringGrid, row, 3, lines[i]);
    end;
    setLength(lines, 0);
  except on x : exception do handle_exception('DisplayICard', x)
    else handle_other('DisplayICard')
  end;
end;

function TInvestigatorForm.RemoveICard(Name: string): integer;
var
  icard   : TIcard;
  row, i  : integer;
  cardId  : integer;
  work    : string;
  lines   : TStringDynArray;
  drop    : boolean;
begin
  try
    drop := false;
    result := -1;
    ItemsStringGrid.RowCount := 1;
    for i := 0 to high(icards) do begin
      cardid := icards[i];
      icard := ICardRecs[cardid];
      if (drop = false) and (icard.fullname = name) then begin
        result := cardid;
        drop := true;
      end
      else begin
        DisplayICard(icard);
        if drop = true then
          icards[i-1] := icards[i];
      end;
    end;
    if drop = true then
      setLength(icards, length(icards)-1);
  except on x : exception do handle_exception('RemoveICard', x)
    else handle_other('RemoveICard')
  end;
end;

end.

