unit ChooseInvestigatorsUnit;
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
  ComCtrls, ExtCtrls, AHGamePieces, AHGame, AHTypes;

type

  { TChooseInvestigatorsForm }

  TChooseInvestigatorsForm = class(TForm)
    BackStoryMemo: TMemo;
    BGImage: TImage;
    Label2: TLabel;
    OkButton: TButton;
    ChooseCheckBox: TCheckBox;
    NoOfEdit: TEdit;
    Label1: TLabel;
    ChooseListBox: TListBox;
    ChosenListBox: TListBox;
    UpDown1: TUpDown;
    procedure Choose(Sender: TObject);
    procedure ListBoxSelectionChange(Sender: TObject; User: boolean);
    procedure TakeClick(Sender: TObject);
    procedure DropClick(Sender: TObject);
    procedure FormActivate(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure UpDown1Click(Sender: TObject; Button: TUDBtnType);
  private
    { private declarations }
    justCreated : boolean;
  public
    { public declarations }
  end;

var
  ChooseInvestigatorsForm: TChooseInvestigatorsForm;

implementation

{$R *.lfm}

{ TChooseInvestigatorsForm }

procedure TChooseInvestigatorsForm.FormCreate(Sender: TObject);
begin
  justCreated := true;
end;

procedure TChooseInvestigatorsForm.UpDown1Click(Sender: TObject;
  Button: TUDBtnType);
begin

end;

procedure TChooseInvestigatorsForm.FormActivate(Sender: TObject);
begin
  if justCreated = false then exit;
  justCreated := false;
  Choose(Sender);
end;

procedure TChooseInvestigatorsForm.Choose(Sender: TObject);
var
  i, noOf : integer;
  deckCard : integer;
  investigator : TInvestigator;
begin
  ChooseListBox.Visible := ChooseCheckBox.Checked;
  if ChooseListBox.Visible then begin
    ChooseListBox.Clear;
    ChosenListBox.Clear;
    for i := 0 to high(InvestigatorCards.deck) do begin
      deckCard := InvestigatorCards.deck[i];
      investigator := InvestigatorRecs[deckCard];
      ChooseListBox.items.Add(investigator.name);
    end;
  end
  else begin
    ChosenListBox.Clear;
    try
      noOf := StrToInt(NoOfEdit.Text);
    except
      noOf := 1;
    end;
    for i := 0 to pred(noOf) do begin
      deckCard := InvestigatorCards.deck[i];
      investigator := InvestigatorRecs[deckCard];
      ChosenListBox.items.Add(investigator.name);
    end;
  end;
end;

procedure TChooseInvestigatorsForm.ListBoxSelectionChange(
  Sender: TObject; User: boolean);
var
  xname : string;
  id    : integer;
  backStory : TBackStory;
begin
  with Sender as TListBox do begin
    if ItemIndex <> -1 then begin
      xname := Items[ItemIndex];
      id := BackStoryIndexOf(xname);
      if id <> -1 then begin
        backStory := BackStoryRecs[id];
        BackStoryMemo.Clear;
        BackStoryMemo.Lines.Add(backStory.description);
      end;
    end;
  end;
end;

procedure TChooseInvestigatorsForm.TakeClick(Sender: TObject);
var
  chooseIndex, noOf : integer;
  xname : string;
begin
  try
    noOf := StrToInt(NoOfEdit.Text);
  except
    noOf := 1;
  end;
  if ChosenListBox.Count < noOf then begin
    if ChooseListBox.ItemIndex <> -1 then begin
      chooseIndex := ChooseListBox.ItemIndex;
      xname := ChooseListBox.Items[chooseIndex];
      ChosenListBox.items.Add(xname);
      ChooseListBox.Items.Delete(chooseIndex);
    end;
  end;
end;

procedure TChooseInvestigatorsForm.DropClick(Sender: TObject);
var
  chosenIndex : integer;
  xname : string;
begin
  if ChooseListBox.Visible = false then exit;
  if ChosenListBox.ItemIndex <> -1 then begin
    chosenIndex := ChosenListBox.ItemIndex;
    xname := ChosenListBox.Items[chosenIndex];
    ChooseListBox.items.Add(xname);
    ChosenListBox.Items.Delete(chosenIndex);
  end;
end;

end.

