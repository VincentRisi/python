unit RevealAncientOneUnit;
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
  ExtCtrls, AHGamePieces, AHGame, AHTypes;

type

  { TRevealAncientOneForm }

  TRevealAncientOneForm = class(TForm)
    AncientOneEdit: TEdit;
    ChooseCheckBox: TCheckBox;
    ChooseListBox: TListBox;
    AncientOneLabel: TLabel;
    BGImage: TImage;
    Label1: TLabel;
    OkButton: TButton;
    procedure FormActivate(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure RandomOnOff(Sender: TObject);
    procedure TakeClick(Sender: TObject);
  private
    { private declarations }
    justCreated : boolean;
    deck        : array of integer;
  public
    { public declarations }
  end;

var
  RevealAncientOneForm: TRevealAncientOneForm;

implementation

{$R *.lfm}

{ TRevealAncientOneForm }

procedure TRevealAncientOneForm.FormCreate(Sender: TObject);
begin
  justCreated := true;
end;

procedure TRevealAncientOneForm.RandomOnOff(Sender: TObject);
var
  i, deckcard : integer;
  ancient  : TAncient;
begin
  if ChooseCheckBox.Checked then begin
    ChooseListBox.Visible := true;
    ChooseListBox.Clear;
    ChooseListBox.Sorted := true;
    for i := 0 to high(deck) do begin
      deckcard := deck[i];
      ancient := AncientRecs[deckcard];
      ChooseListBox.items.Add(ancient.name);
    end;
    ChooseListBox.ItemIndex := 0;
  end
  else begin
    ChooseListBox.Visible := false;
    deckcard := deck[0];
    ancient := AncientRecs[deckcard];
    AncientOneEdit.Text := ancient.name;
  end;
end;

procedure TRevealAncientOneForm.FormActivate(Sender: TObject);
begin
  if justCreated = false then exit;
  justCreated := false;
  deck := AncientCards.deck;
  RandomOnOff(Sender);
end;

procedure TRevealAncientOneForm.TakeClick(Sender: TObject);
var
  chooseIndex : integer;
begin
  if ChooseListBox.Visible = false then exit;
  if ChooseListBox.ItemIndex <> -1 then begin
    chooseIndex := ChooseListBox.ItemIndex;
    AncientOneEdit.Text := ChooseListBox.Items[chooseIndex];
  end;
end;

end.

